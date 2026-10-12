"""Index a journal's overflow directory: write <JOURNAL>/INDEX.md.

python journal_index.py <path to the overflow directory, e.g. NOTEBOOK/>

One section per rolled file (its date span and size), one line per entry (its title as
written; a dated sub-heading indented under its entry). The rolled files never change, so
regenerating the index at each rollover leaves every existing line as it was. Entry forms
recognized: a `## YYYY-MM-DD ...` heading, or a top-level `- YYYY-MM-DD ...` /
`- **YYYY-MM-DD** ...` bullet (the same detection as rollover.py); and, under a bare date
heading (`## 2026-10-04`, nothing after the date) until the next heading, each top-level
bullet that opens with a bold run (`- **E24: the P6 addition closed.** ...`) is an entry
titled by that run, indented under its day. A journal that writes a bare date heading over
bold-lead bullets is thus indexed by its titles, not by its dates alone; under a titled
heading (`## 2026-10-04 the P6 addition`) a bold-lead bullet is body, not an entry.
"""
import os
import re
import sys

DATE = r'\d{4}-\d{2}-\d{2}'
HEAD = re.compile(r'^(#{2,3}) (' + DATE + r'.*)$')
ANY_HEAD = re.compile(r'^#{1,6} ')
BULLET = re.compile(r'^- \**(' + DATE + r')\**:?\s*(.*)$')
BOLD_LEAD = re.compile(r'^- \*\*(.+?)\*\*')
TITLE_MAX = 110


def trim(title):
    if len(title) > TITLE_MAX:
        title = title[:TITLE_MAX].rsplit(' ', 1)[0] + ' ...'
    return title


def entry_lines(text):
    """Yield (level, date or None, title) for every entry line of a rolled file."""
    under = None  # the level of the bare date heading the bold-lead bullets fall under
    for line in text.splitlines():
        m = HEAD.match(line)
        if m:
            title = m.group(2)
            under = len(m.group(1)) if title.strip() == title[:10] else None
            yield (len(m.group(1)), title[:10], title)
            continue
        if ANY_HEAD.match(line):
            under = None
            continue
        m = BULLET.match(line)
        if m:
            yield (2, m.group(1), m.group(1) + ' ' + trim(m.group(2).strip()))
            continue
        m = BOLD_LEAD.match(line)
        if m and under:
            yield (under + 1, None, trim(m.group(1).strip()))


def write_index(odir):
    odir = odir.rstrip('/\\')
    stem = os.path.basename(odir)
    files = sorted(f for f in os.listdir(odir) if re.fullmatch(DATE + r'\.md', f))
    if not files:
        sys.exit(f'{odir}: no rolled files')
    out = [f"# {stem} index (the rolled-over periods)\n\n",
           f"> Every entry rolled out of `../{stem}.md`, by file: its date span, then one\n",
           f"> line per entry, its date and title as written. The rolled files never\n",
           f"> change, so this index is regenerated at each rollover and its existing\n",
           f"> lines stay as they are. The live entries are in `../{stem}.md`. To read one\n",
           f"> entry: `grep -n \"<date>\" {stem}/*.md`, then read from that line to the\n",
           f"> next entry.\n\n"]
    for f in files:
        text = open(os.path.join(odir, f), encoding='utf-8', newline='').read()
        entries = list(entry_lines(text))
        dates = [d for _, d, _ in entries if d]
        if not dates:
            sys.exit(f'{odir}/{f}: no dated entries recognized')
        kb = len(text.encode('utf-8')) / 1024
        out.append(f"## `{f}`: {min(dates)} to {max(dates)} ({kb:.1f} KB)\n\n")
        for level, _, title in entries:
            title = title.replace(' — ', ': ').replace('—', ':').replace('–', '-')
            out.append('  ' * (level - 2) + '- ' + title + '\n')
        out.append('\n')
    text = ''.join(out).rstrip('\n') + '\n'
    open(os.path.join(odir, 'INDEX.md'), 'w', encoding='utf-8', newline='').write(text)
    print(f'{odir}/INDEX.md: {len(text.encode())} bytes, {len(files)} files')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    write_index(sys.argv[1])
