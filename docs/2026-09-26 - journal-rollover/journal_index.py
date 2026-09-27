"""Write <dir>/INDEX.md for a journal's overflow directory (2026-09-26).

python journal_index.py <repo>/<STEM>/   (e.g. NOTEBOOK/ or CHANGELOG/)
One section per rolled file (its date span and size), one line per dated entry (its date and
title as written; a dated '###' sub-entry indented under it). The rolled files are frozen, so
regenerating the index at each rollover leaves every existing line as it was.
"""
import os, re, sys

d = sys.argv[1].rstrip('/\\')
stem = os.path.basename(d)
files = sorted(f for f in os.listdir(d) if re.fullmatch(r'\d{4}-\d{2}-\d{2}\.md', f))
if not files:
    sys.exit(f'{d}: no rolled files')
lines = [f"# {stem} index (the rolled-over periods)\n\n",
         f"> Every entry rolled out of `../{stem}.md`, by file: its date span, then one\n",
         f"> line per entry, its date and title as written (an em dash in an old title\n",
         f"> shown as a colon). The rolled files never change, so this index is\n",
         f"> regenerated at each rollover and its existing lines stay as they are. The\n",
         f"> live entries are in `../{stem}.md`. To read one entry:\n",
         f"> `grep -n \"^## <date>\" {stem}/*.md`, then read from that line to the next\n",
         f"> `## `.\n\n"]
for f in files:
    text = open(os.path.join(d, f), encoding='utf-8', newline='').read()
    heads = re.findall(r'(?m)^(##|###) (\d{4}-\d{2}-\d{2}.*)$', text)
    dates = [re.match(r'\d{4}-\d{2}-\d{2}', h).group(0) for _, h in heads]
    first, last = min(dates), max(dates)
    kb = len(text.encode('utf-8')) / 1024
    lines.append(f"## `{f}`: {first} to {last} ({kb:.1f} KB)\n\n")
    for lvl, h in heads:
        h = h.replace(' — ', ': ').replace('—', ':').replace('–', '-')
        lines.append(('  - ' if lvl == '###' else '- ') + h + '\n')
    lines.append('\n')
out = ''.join(lines).rstrip('\n') + '\n'
open(os.path.join(d, 'INDEX.md'), 'w', encoding='utf-8', newline='').write(out)
print(f'{d}/INDEX.md: {len(out.encode())} bytes, {len(files)} files')
