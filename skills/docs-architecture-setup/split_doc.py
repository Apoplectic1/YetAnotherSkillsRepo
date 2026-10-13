"""Split a reference doc past its budget by topic: each `## ` section becomes one file in a
directory named for the doc, and the doc itself becomes the index.

python split_doc.py <repo>/<DOC>.md [--apply] [--budget-kb 40] [--today YYYY-MM-DD]
python split_doc.py <repo>/<DOC>.md --reindex      (after a part is edited: the Parts list rewritten)

The doc's title line and preamble (its charter, everything before the first `## `) stay in
the index, followed by a split note and one line per part: the heading as written, the part's
file and size, its first sentence. Each part file carries a one-line title naming its parent,
a note, then the section byte for byte, its `## ` heading included, so a section citation
("ARCHITECTURE § Build chain", or an unambiguous short form of the heading) resolves by grep
over the file and the directory. The router keeps naming the parent only. A section is never
split below `## `: a single topic past the budget stays one part, reported as such.

Refused: a doc under budget; a doc with no `## ` sections; a journal (dated `## ` headings or
dated top-level bullets: a journal rolls over by date with rollover.py, it never splits by
topic); an existing directory (a split is never rewritten). The dry run lists the parts, every
section citation it finds in the repository's own Markdown (child repositories and
sub-projects with their own router are skipped), the lines inside each part that a move one
directory down leaves stale (relative paths, "this file"), and any heading carrying a date (the
part's filename follows the heading, and a dated heading is edited in place); `--apply`
writes the parts, rewrites the index, and checks that the preamble and the parts reconstruct
the original byte for byte. `--today` fixes the date in the notes, for a byte-exact check.
"""
import datetime
import os
import re
import sys

HEAD = re.compile(r'(?m)^## (.+?)\r?$')  # the heading's text without a CRLF doc's carriage return
DATE = r'\d{4}-\d{2}-\d{2}'
DATED_HEAD = re.compile(r'(?m)^## ' + DATE)
DATED_BULLET = re.compile(r'(?m)^- \**' + DATE)
STALE = re.compile(r'\.\./|\bthis file\b|\bbeside this file\b|\]\(\./|\]\((?!https?://|#|/)[^)]*\.md')


def slug(heading, taken):
    s = re.sub(r'`[^`]*`', lambda m: m.group(0).strip('`'), heading)
    s = re.sub(r'\(.*?\)', '', s)
    s = re.sub(r'[^A-Za-z0-9]+', '-', s).strip('-').lower()
    s = re.sub(r'-{2,}', '-', s) or 'part'
    base, n = s, 2
    while s in taken:
        s = f'{base}-{n}'
        n += 1
    taken.add(s)
    return s


def first_sentence(body):
    """The part's first prose sentence: skips headings, fences and their contents, tables, images."""
    fenced = False
    for line in body.split('\n')[1:]:
        t = line.strip()
        if t.startswith('```'):
            fenced = not fenced
            continue
        if fenced or not t or t.startswith(('#', '|', '![', '>')):
            continue
        t = re.sub(r'^[-*]\s+', '', t)
        m = re.search(r'\. ', t)
        t = t[:m.end() - 1] if m else t
        return t[:160].rstrip() + (' ...' if len(t) > 160 else '')
    return ''


def parse(text):
    """Return (preamble, [(heading, section_text)]) with sections byte-exact, headings included."""
    starts = [m.start() for m in HEAD.finditer(text)]
    if not starts:
        sys.exit('no `## ` sections: nothing to split by topic')
    preamble = text[:starts[0]]
    sections = []
    for i, s in enumerate(starts):
        e = starts[i + 1] if i + 1 < len(starts) else len(text)
        sec = text[s:e]
        sections.append((HEAD.match(sec).group(1), sec))
    assert preamble + ''.join(s for _, s in sections) == text
    return preamble, sections


def is_journal(text, sections):
    dated_heads = len(DATED_HEAD.findall(text))
    dated_bullets = len(DATED_BULLET.findall(text))
    return (dated_heads and dated_heads * 2 >= len(sections)) or dated_bullets >= 3


def citations(repo, stem, exclude_dir, headings=()):
    """Lines in the repository's own Markdown that cite the doc by section: the `§` form, and the
    prose form (the doc's name, then within a few words a quoted heading or a short form of one);
    child repositories and sub-projects (a directory with its own CLAUDE.md or .git) are skipped."""
    pat = re.compile(r'\b' + re.escape(stem) + r'(?:\.md)?(?:\'s)?\s*(?:§|section|§)', re.I)
    own = re.compile(r'§|§')  # inside the doc itself, a bare "see § Topic" crosses parts after the split
    quoted = re.compile(r'\b' + re.escape(stem) + r'(?:\.md)?[^\n"“]{0,40}["“]([^"”\n]{1,80})["”]', re.I)
    lows = [h.lower() for h in headings]

    def prose(line):
        return any(q.lower() in h for q in quoted.findall(line) for h in lows)
    out = []
    for dirpath, dirs, files in os.walk(repo):
        dirs[:] = [d for d in dirs
                   if d not in ('.git', 'node_modules', '_gsdata_')
                   and os.path.join(dirpath, d) != exclude_dir
                   and not os.path.exists(os.path.join(dirpath, d, 'CLAUDE.md'))
                   and not os.path.exists(os.path.join(dirpath, d, '.git'))]
        for f in files:
            if not f.endswith('.md'):
                continue
            p = os.path.join(dirpath, f)
            here = (f == stem + '.md' and dirpath == repo)
            try:
                for i, line in enumerate(open(p, encoding='utf-8', newline='').read().split('\n'), 1):
                    if pat.search(line) or (here and own.search(line)) or (not here and prose(line)):
                        out.append((os.path.relpath(p, repo).replace(os.sep, '/'), i, line.strip()))
            except (OSError, UnicodeDecodeError):
                continue
    return out


def stale_lines(section):
    return [(i, l.strip()) for i, l in enumerate(section.split('\n'), 1) if STALE.search(l)]


def mixed(t):
    """A text whose line endings are not one form: a lone carriage return, or CRLF beside a bare LF."""
    crlf = t.count('\r\n')
    return t.count('\r') > crlf or 0 < crlf < t.count('\n')


def part_head(stem, fname, h, today):
    """The lines a part opens with before its section text; a stale line's number in the part counts them."""
    return (f"# {stem}: {h} (part of ../{fname})\n\n"
            f"> One topic of `../{fname}`, split out on {today} when the file passed its\n"
            f"> budget; the heading keeps its text, so \"{stem} § {h}\" resolves by grep over\n"
            f"> the file and `{stem}/`. The index is `../{fname}`.\n\n")


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    sys.stdout.reconfigure(encoding='utf-8', errors='replace', newline='\n')  # the citation list carries the section mark
    path = os.path.abspath(argv[1])
    apply = '--apply' in argv
    budget = 40 * 1024
    if '--budget-kb' in argv:
        budget = int(argv[argv.index('--budget-kb') + 1]) * 1024
    repo, fname = os.path.split(path)
    stem = fname[:-3]
    odir = os.path.join(repo, stem)
    today = datetime.date.today().isoformat()
    if '--today' in argv:  # for a byte-exact fixture check
        today = argv[argv.index('--today') + 1]

    text = open(path, encoding='utf-8', newline='').read()
    nl = '\r\n' if '\r\n' in text else '\n'  # the doc's own line ending: the parts and the index keep it
    if '--reindex' in argv:  # a part was edited: rewrite the index's Parts list from the directory, bodies untouched
        if not os.path.isdir(odir):
            sys.exit(f'{stem}/ does not exist: nothing to reindex')
        i = text.find(nl + '## Parts' + nl)
        if i < 0:
            sys.exit(f'{fname} carries no "## Parts" list: not a split index')
        listed = re.findall(r'\(`' + re.escape(stem) + r'/([^`]+)`', text[i:])  # the index's own order
        present = [f for f in os.listdir(odir) if f.endswith('.md')]
        order = [f for f in listed if f in present] + sorted(f for f in present if f not in listed)
        index = text[:i + len(nl)] + '## Parts' + nl + nl
        for f in order:
            part = open(os.path.join(odir, f), encoding='utf-8', newline='').read()
            m = HEAD.search(part)
            body = part[m.start():] if m else part
            kb = len(body.encode('utf-8')) / 1024
            fs = first_sentence(body)
            index += f"- **{m.group(1) if m else f}** (`{stem}/{f}`, {kb:.1f} KB)" + (f": {fs}" if fs else '') + nl
        assert mixed(text) or not mixed(index), 'the index would mix line endings'
        open(path, 'w', encoding='utf-8', newline='').write(index)
        gone = [f for f in listed if f not in present]
        print(f'  reindexed: {fname} lists {len(order)} parts in the index\'s order'
              + (f'; dropped from the list, no longer in {stem}/: {", ".join(gone)}' if gone else ''))
        return
    size = len(text.encode('utf-8'))
    if size <= budget:
        sys.exit(f'{fname}: under budget ({size // 1024} KB of {budget // 1024}), nothing to split')
    if os.path.exists(odir):
        sys.exit(f'{stem}/ exists: a split is never rewritten')
    preamble, sections = parse(text)
    if is_journal(text, sections):
        sys.exit(f'{fname} is a journal (dated entries): a journal rolls over by date with rollover.py, it never splits by topic')
    taken = set()
    parts = [(h, s, slug(h, taken)) for h, s in sections]

    print(f'{fname}: {size / 1024:.1f} KB, {len(parts)} topics (budget {budget // 1024} KB)')
    for h, s, sl in parts:
        kb = len(s.encode('utf-8')) / 1024
        flags = ''
        if kb * 1024 > budget:
            flags += '  [this part alone is past the budget: it stays one part; the author\'s `###` headings are the lever]'
        if re.search(DATE, h):
            flags += '  [dated heading: the part\'s filename follows it, and an edit in place renames the part]'
        print(f'  {kb:5.1f} KB  {stem}/{sl}.md  "{h}"{flags}')
    print(f'  {len(preamble.encode()) / 1024:5.1f} KB  preamble kept in the index')
    cites = citations(repo, stem, odir, [h for h, _, _ in parts])
    print(f'section citations in this repository\'s Markdown: {len(cites)} (each resolves by grep after the split; check they name a heading as written or an unambiguous short form)')
    for p, i, line in cites[:40]:
        print(f'  {p}:{i}: {line[:110]}')
    if len(cites) > 40:
        print(f'  ... {len(cites) - 40} more')
    stale = [(sl, i + part_head(stem, fname, h, today).count('\n'), l) for h, s, sl in parts for i, l in stale_lines(s)]
    print(f'lines a move one directory down leaves stale (relative paths, "this file"): {len(stale)} (fix after the apply; the numbers are the parts\' lines)')
    for sl, i, l in stale[:40]:
        print(f'  {stem}/{sl}.md:{i}: {l[:110]}')
    if len(stale) > 40:
        print(f'  ... {len(stale) - 40} more')
    if not apply:
        print('  dry run: --apply writes the parts and the index')
        return

    os.makedirs(odir)
    for h, s, sl in parts:
        open(os.path.join(odir, sl + '.md'), 'w', encoding='utf-8', newline='').write(part_head(stem, fname, h, today).replace('\n', nl) + s)
    note = (f"Split (since {today}): past {budget // 1024} KB this doc's `##` topics live in `{stem}/`, one\n"
            f"file per topic named by its heading, and this file is the index. A section citation\n"
            f"(\"{stem} § <heading>\", or an unambiguous short form of the heading) resolves by\n"
            f"`grep -n \"<heading>\" {fname} {stem}/*.md`.\n\n"
            f"## Parts\n\n").replace('\n', nl)
    index = preamble.rstrip('\r\n') + nl + nl + note
    for h, s, sl in parts:
        kb = len(s.encode('utf-8')) / 1024
        fs = first_sentence(s)
        index += f"- **{h}** (`{stem}/{sl}.md`, {kb:.1f} KB)" + (f": {fs}" if fs else '') + nl
    written = [open(os.path.join(odir, sl + '.md'), encoding='utf-8', newline='').read() for _, _, sl in parts]
    rebuilt = preamble + ''.join(w.split(nl + nl, 2)[2] for w in written)
    assert rebuilt == text, 'the parts would not reconstruct the original byte for byte'
    assert mixed(text) or not any(mixed(w) for w in written + [index]), \
        'a part or the index would mix line endings (the doc itself is one form)'
    open(path, 'w', encoding='utf-8', newline='').write(index)
    print(f'  applied: {len(parts)} parts in {stem}/, index {len(index.encode()) / 1024:.1f} KB')


if __name__ == '__main__':
    main(sys.argv)
