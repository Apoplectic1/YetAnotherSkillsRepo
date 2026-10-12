"""Split a reference doc past its budget by topic: each `## ` section becomes one file in a
directory named for the doc, and the doc itself becomes the index.

python split_doc.py <repo>/<DOC>.md [--apply] [--budget-kb 40]

The doc's title line and preamble (its charter, everything before the first `## `) stay in
the index, followed by a split note and one line per part: the heading as written, the part's
file and size, its first sentence. Each part file carries a one-line title naming its parent,
a note, then the section byte for byte, its `## ` heading included, so a section citation
("ARCHITECTURE § Build chain") resolves by grep over the file and the directory. The router
keeps naming the parent only. A section is never split below `## `: a single topic past the
budget stays one part. Refused: a doc under budget, a doc with no `## ` sections, an existing
directory (a split is never rewritten). The dry run lists the parts and every section
citation it can find in the repo's Markdown, for the operator to check; `--apply` writes the
parts, rewrites the index, and checks that the parts and the preamble reconstruct the
original byte for byte.
"""
import datetime
import os
import re
import sys

HEAD = re.compile(r'(?m)^## (.+)$')


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


def citations(repo, stem, exclude_dir):
    """Lines in the repo's Markdown that cite the doc by section ("STEM § ...", "STEM.md § ...")."""
    pat = re.compile(r'\b' + re.escape(stem) + r'(?:\.md)?(?:\'s)?\s*(?:§|section|§)', re.I)
    own = re.compile(r'§|§')  # inside the doc itself, a bare "see § Topic" crosses parts after the split
    out = []
    for dirpath, dirs, files in os.walk(repo):
        dirs[:] = [d for d in dirs if d not in ('.git', 'node_modules', '_gsdata_') and os.path.join(dirpath, d) != exclude_dir]
        for f in files:
            if not f.endswith('.md'):
                continue
            p = os.path.join(dirpath, f)
            here = (f == stem + '.md' and dirpath == repo)
            try:
                for i, line in enumerate(open(p, encoding='utf-8', newline='').read().split('\n'), 1):
                    if pat.search(line) or (here and own.search(line)):
                        out.append((os.path.relpath(p, repo), i, line.strip()))
            except (OSError, UnicodeDecodeError):
                continue
    return out


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    sys.stdout.reconfigure(errors='replace', newline='\n')
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
    size = len(text.encode('utf-8'))
    if size <= budget:
        sys.exit(f'{fname}: under budget ({size // 1024} KB of {budget // 1024}), nothing to split')
    if os.path.exists(odir):
        sys.exit(f'{stem}/ exists: a split is never rewritten')
    preamble, sections = parse(text)
    taken = set()
    parts = [(h, s, slug(h, taken)) for h, s in sections]

    print(f'{fname}: {size / 1024:.1f} KB, {len(parts)} topics (budget {budget // 1024} KB)')
    for h, s, sl in parts:
        kb = len(s.encode('utf-8')) / 1024
        flag = '  [this part alone is past the budget: it stays one part]' if kb * 1024 > budget else ''
        print(f'  {kb:5.1f} KB  {stem}/{sl}.md  "{h}"{flag}')
    print(f'  {len(preamble.encode()) / 1024:5.1f} KB  preamble kept in the index')
    cites = citations(repo, stem, odir)
    print(f'section citations in the repo\'s Markdown: {len(cites)} (each resolves by grep after the split; check they name a heading as written)')
    for p, i, line in cites[:40]:
        print(f'  {p}:{i}: {line[:110]}')
    if len(cites) > 40:
        print(f'  ... {len(cites) - 40} more')
    if not apply:
        print('  dry run: --apply writes the parts and the index')
        return

    os.makedirs(odir)
    for h, s, sl in parts:
        head = (f"# {stem}: {h} (part of ../{fname})\n\n"
                f"> One topic of `../{fname}`, split out on {today} when the file passed its\n"
                f"> budget; the heading keeps its text, so \"{stem} § {h}\" resolves by grep over\n"
                f"> the file and `{stem}/`. The index is `../{fname}`.\n\n")
        open(os.path.join(odir, sl + '.md'), 'w', encoding='utf-8', newline='').write(head + s)
    note = (f"Split (since {today}): past {budget // 1024} KB this doc's `##` topics live in `{stem}/`, one\n"
            f"file per topic named by its heading, and this file is the index. A section citation\n"
            f"(\"{stem} § <heading>\") resolves by `grep -n \"<heading>\" {fname} {stem}/*.md`.\n\n"
            f"## Parts\n\n")
    index = preamble.rstrip('\n') + '\n\n' + note
    for h, s, sl in parts:
        kb = len(s.encode('utf-8')) / 1024
        fs = first_sentence(s)
        index += f"- **{h}** (`{stem}/{sl}.md`, {kb:.1f} KB)" + (f": {fs}" if fs else '') + '\n'
    rebuilt = preamble + ''.join(open(os.path.join(odir, sl + '.md'), encoding='utf-8', newline='').read().split('\n\n', 2)[2] for _, _, sl in parts)
    assert rebuilt == text, 'the parts would not reconstruct the original byte for byte'
    open(path, 'w', encoding='utf-8', newline='').write(index)
    print(f'  applied: {len(parts)} parts in {stem}/, index {len(index.encode()) / 1024:.1f} KB')


if __name__ == '__main__':
    main(sys.argv)
