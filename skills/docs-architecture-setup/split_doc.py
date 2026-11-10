"""Split a reference doc past its budget by topic: each `## ` section becomes one file in a
directory named for the doc, and the doc itself becomes the index.

python split_doc.py <repo>/<DOC>.md [--lines <file>] [--apply] [--budget-kb 40] [--today YYYY-MM-DD]
python split_doc.py <repo>/<DOC>.md --reindex [--lines <file>]   (after a part is edited)
python split_doc.py <repo>/<DOC>.md --check                      (read-only: is the index current?)

The doc's title line and preamble (its charter, everything before the first `## `) stay in
the index, followed by a split note and one entry per part, on one line: the heading as
written, the part's file and size, and a line the splitting run writes saying what the part
holds. The lines come in a lines file: each part's `## ` heading as written, its line on the
lines below (a wrapped line is joined); the dry run prints the headings to fill in. A line is
at most 320 characters, and every `backticked` term in it occurs verbatim in its part. A part
with no line, or a line failing either check, is refused and nothing is written. Each part
file carries a one-line title naming its parent, a note, then the section byte for byte, its
`## ` heading included, so a section citation ("ARCHITECTURE § Build chain", or an
unambiguous short form of the heading) resolves by grep over the file and the directory. The
router keeps naming the parent only. A section is never split below `## `: a single topic
past the budget stays one part, reported as such.

--reindex keeps every line byte for byte and refreshes each entry's heading, file and size
from the directory; a part whose size moved is listed with its line for review (does the line
still say what the part holds?); a lines file sets the line of each heading it names (a new
part's, or one the review rewrote). The checks run again, so --reindex is also the check for
a line edited in the index by hand. --check writes nothing and reports an index whose files,
sizes or lines no longer match its parts, exiting 1 when it is stale.

Refused: a doc under budget; a doc with no `## ` sections; a journal (dated `## ` headings or
dated top-level bullets: a journal rolls over by date with rollover.py, it never splits by
topic); an existing directory (a split is never rewritten). The dry run lists the parts, every
section citation it finds in the repository's own Markdown (child repositories and
sub-projects with their own router are skipped), the lines inside each part that a move one
directory down leaves stale (relative paths, "this file"), and any heading carrying a date (the
part's filename follows the heading, and a dated heading is edited in place); with --lines it
checks the lines without writing. `--apply` writes the parts, rewrites the index, and checks
that the preamble and the parts reconstruct the original byte for byte. `--today` fixes the
date in the notes, for a byte-exact check.
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
LINE_CAP = 320
TERM = re.compile(r'(?<!`)`([^`\n]+)`(?!`)')  # a code-formatted term: a search term the line promises
ENTRY = re.compile(r'^- \*\*(?P<h>.*?)\*\* \(`(?P<f>[^`]+)`, (?P<kb>\d+\.\d) KB\)(?:: (?P<line>.*))?$')
WHAT_A_LINE_SAYS = (
    "the index's line per part (--apply refuses a part without one) says what the part holds, in\n"
    "its own terms: the things, names and rules a reader would search for there, not its opening\n"
    "restated, its history or a judgment of it. At most 320 characters; every `backticked` term\n"
    "must occur verbatim in its part.")


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


def line_faults(line, section):
    """The two mechanical checks on a written line; whether it describes the part is the run's judgment."""
    if not line or not line.strip():
        return ['no line']
    out = []
    if len(line) > LINE_CAP:
        out.append(f'the line is {len(line)} characters, past the cap of {LINE_CAP}')
    for t in TERM.findall(line):
        if t not in section:
            out.append(f'`{t}` does not occur in the part')
    return out


def read_lines(path):
    """The lines file: [(heading, line)], each `## ` heading with the non-empty lines below it joined."""
    if not os.path.isfile(path):
        sys.exit(f'lines file {path}: not found')
    out = []
    for raw in open(path, encoding='utf-8').read().splitlines():
        m = re.match(r'## (.+?)\s*$', raw)
        if m:
            out.append((m.group(1), []))
        elif out and raw.strip():
            out[-1][1].append(raw.strip())
    return [(h, ' '.join(ls)) for h, ls in out]


def match_lines(pairs, headings):
    """Pair the lines file's headings with the doc's, by text and order: (lines, faults)."""
    want = [h.rstrip() for h in headings]
    got = [h for h, _ in pairs]
    if got == want:
        return [l for _, l in pairs], []
    faults = []
    for h in dict.fromkeys(want):
        if want.count(h) > got.count(h):
            faults.append(f'"{h}": no line in the lines file')
    for h in dict.fromkeys(got):
        if got.count(h) > want.count(h):
            faults.append(f'"{h}": not a `## ` heading of the doc')
    return None, faults or ["the lines file's headings are out of the doc's order"]


def parse_index(text, nl, stem, fname):
    """The Parts list: (its offset, [(heading, file, size text, line or None)]) in the index's order."""
    i = text.find(nl + '## Parts' + nl)
    if i < 0:
        sys.exit(f'{fname} carries no "## Parts" list: not a split index')
    entries = []
    for raw in text[i:].split(nl):
        m = ENTRY.match(raw)
        if m and m.group('f').startswith(stem + '/'):
            entries.append((m.group('h'), m.group('f')[len(stem) + 1:], m.group('kb'), m.group('line')))
    return i, entries


def read_part(odir, f):
    """A part file's heading, its section (heading included), and that section's size as the index writes it."""
    part = open(os.path.join(odir, f), encoding='utf-8', newline='').read()
    m = HEAD.search(part)
    body = part[m.start():] if m else part
    return (m.group(1) if m else f), body, f'{len(body.encode("utf-8")) / 1024:.1f}'


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


def check(fname, stem, odir, entries):
    """--check: one finding per line for an index that no longer matches its parts; nothing written."""
    present = sorted(f for f in os.listdir(odir) if f.endswith('.md'))
    byfile = {e[1]: e for e in entries}
    findings = [f'{stem}/{f}: listed in the index, not in {stem}/' for f in byfile if f not in present]
    for f in [e[1] for e in entries if e[1] in present] + [f for f in present if f not in byfile]:
        h, body, kb = read_part(odir, f)
        if f not in byfile:
            findings.append(f'{stem}/{f}: in {stem}/, not listed in the index')
            continue
        e = byfile[f]
        if e[2] != kb:
            findings.append(f'{stem}/{f}: the index records {e[2]} KB, the part is {kb} KB')
        findings += [f'{stem}/{f}: {x}' for x in line_faults(e[3], body)]
    if not findings:
        print(f'{fname}: the index matches its {len(present)} parts')
        return 0
    print(f'{fname}: the index is stale, {len(findings)} finding(s) (split_doc.py --reindex)')
    for x in findings:
        print(f'  {x}')
    return 1


def reindex(path, text, nl, fname, stem, odir, entries, i, lines_path):
    """--reindex: the lines kept, the heading, file and size refreshed, a changed part put to review."""
    present = [f for f in os.listdir(odir) if f.endswith('.md')]
    byfile = {e[1]: e for e in entries}
    order = [e[1] for e in entries if e[1] in present] + sorted(f for f in present if f not in byfile)
    parts = {f: read_part(odir, f) for f in order}
    given, faults = {}, []
    if lines_path:
        heads = {}
        for f in order:
            heads.setdefault(parts[f][0].rstrip(), []).append(f)
        for h, l in read_lines(lines_path):
            fs = heads.get(h, [])
            if not fs:
                faults.append(f'"{h}" (lines file): not the heading of any part in {stem}/')
            elif len(fs) > 1:
                faults.append(f'"{h}" (lines file): the heading of {len(fs)} parts; set their lines in the index itself')
            else:
                given[fs[0]] = l
    out, review = [], []
    for f in order:
        h, body, kb = parts[f]
        e = byfile.get(f)
        line = given[f] if f in given else (e[3] if e else None)
        faults += [f'{stem}/{f}: {x}' + ('' if e or f in given else ' (a new part: give its line with --lines)')
                   for x in line_faults(line, body)]
        if e and f not in given and e[2] != kb:
            review.append(f'    {stem}/{f}: {e[2]} KB -> {kb} KB: {line}')
        out.append(f"- **{h}** (`{stem}/{f}`, {kb} KB): {line}")
    if faults:
        sys.exit(f'{fname}: not reindexed, the index is unchanged:\n' + '\n'.join(f'  {x}' for x in faults))
    index = text[:i + len(nl)] + '## Parts' + nl + nl + nl.join(out) + nl
    assert mixed(text) or not mixed(index), 'the index would mix line endings'
    open(path, 'w', encoding='utf-8', newline='').write(index)
    gone = [e[1] for e in entries if e[1] not in present]
    print(f'  reindexed: {fname} lists {len(order)} parts in the index\'s order'
          + (f'; dropped from the list, no longer in {stem}/: {", ".join(gone)}' if gone else '')
          + (f'; {len(given)} line(s) set from the lines file' if given else ''))
    if review:
        print(f'  review: {len(review)} part(s) changed size since the index recorded them; does each line'
              f' still say what its part holds? (edit the line in the index, or pass --lines, then --reindex)')
        print('\n'.join(review))


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    sys.stdout.reconfigure(encoding='utf-8', errors='replace', newline='\n')  # the citation list carries the section mark

    def opt(name):
        if name not in argv:
            return None
        k = argv.index(name) + 1
        if k >= len(argv) or argv[k].startswith('--'):
            sys.exit(f'{name} needs a value')
        return argv[k]
    path = os.path.abspath(argv[1])
    apply = '--apply' in argv
    lines_path = opt('--lines')
    budget = int(opt('--budget-kb') or 40) * 1024
    repo, fname = os.path.split(path)
    stem = fname[:-3]
    odir = os.path.join(repo, stem)
    today = opt('--today') or datetime.date.today().isoformat()  # --today: for a byte-exact fixture check

    text = open(path, encoding='utf-8', newline='').read()
    nl = '\r\n' if '\r\n' in text else '\n'  # the doc's own line ending: the parts and the index keep it
    if '--reindex' in argv or '--check' in argv:
        if not os.path.isdir(odir):
            sys.exit(f'{stem}/ does not exist: not a split doc')
        i, entries = parse_index(text, nl, stem, fname)
        if '--check' in argv:
            sys.exit(check(fname, stem, odir, entries))
        reindex(path, text, nl, fname, stem, odir, entries, i, lines_path)
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
    lines, faults = None, []
    if lines_path:
        lines, faults = match_lines(read_lines(lines_path), [h for h, _, _ in parts])
        if lines is not None:
            faults = [f'{stem}/{sl}.md "{h}": {x}' for (h, s, sl), l in zip(parts, lines) for x in line_faults(l, s)]
    elif apply:
        faults = ['--apply needs --lines <file>: every part takes a written line (the dry run prints the headings)']
    if apply and faults:
        sys.exit(f'{fname}: refused, nothing written:\n' + '\n'.join(f'  {x}' for x in faults))

    if not apply:
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
        print(WHAT_A_LINE_SAYS)
        if lines_path:
            if faults:
                print(f'lines file {lines_path}: {len(faults)} fault(s); --apply refuses until they are fixed')
                print('\n'.join(f'  {x}' for x in faults))
                sys.exit(1)
            print(f'lines file {lines_path}: a line for each of the {len(parts)} parts, every check passed')
            print('  dry run: --apply --lines <file> writes the parts and the index')
            return
        print('the lines file (--lines <file>): each heading below, its line on the lines after it')
        for h, _, _ in parts:
            print(f'## {h}')
        print('  dry run: --apply --lines <file> writes the parts and the index')
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
    for (h, s, sl), l in zip(parts, lines):
        kb = len(s.encode('utf-8')) / 1024
        index += f"- **{h}** (`{stem}/{sl}.md`, {kb:.1f} KB): {l}" + nl
    written = [open(os.path.join(odir, sl + '.md'), encoding='utf-8', newline='').read() for _, _, sl in parts]
    rebuilt = preamble + ''.join(w.split(nl + nl, 2)[2] for w in written)
    assert rebuilt == text, 'the parts would not reconstruct the original byte for byte'
    assert mixed(text) or not any(mixed(w) for w in written + [index]), \
        'a part or the index would mix line endings (the doc itself is one form)'
    open(path, 'w', encoding='utf-8', newline='').write(index)
    print(f'  applied: {len(parts)} parts in {stem}/, index {len(index.encode()) / 1024:.1f} KB')


if __name__ == '__main__':
    main(sys.argv)
