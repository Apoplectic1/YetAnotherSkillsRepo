"""Journal rollover, as piloted on the HDL tree 2026-09-26 (ROADMAP: "Journal rollover and the
overflow directory"). The skill change decides where this lives when it ships.

python rollover.py <repo>/<JOURNAL>.md [--apply]

A journal (a NOTEBOOK, newest last; a CHANGELOG, newest first, detected from its dates) past
BUDGET rolls its oldest whole days into <JOURNAL>/<first-date>.md, the first date being the
earliest the file holds; each file stays under BUDGET, and about KEEP bytes of dated entries stay
live so the file does not roll again the next day. Undated '## ' sections (an Open threads list)
stay live right after the header. Entries move byte for byte (checked). With --apply it writes
the files, adds the rollover note to the live file's header on the first rollover, and
regenerates <JOURNAL>/INDEX.md. It refuses if the overflow directory exists and the note is
missing, or if the journal is under budget. Carrying an open thread out of a rolled entry is the
operator's step, before --apply.
"""
import datetime, os, re, subprocess, sys

BUDGET, KEEP = 40 * 1024, 20 * 1024
path = sys.argv[1]; apply = '--apply' in sys.argv
repo, fname = os.path.split(os.path.abspath(path)); stem = fname[:-3]
odir = os.path.join(repo, stem)
today = datetime.date.today().isoformat()

src = open(path, encoding='utf-8', newline='').read()
parts = re.split(r'(?m)^(?=## )', src)
header, secs = parts[0], parts[1:]
dated, undated = [], []
for e in secs:
    m = re.match(r'## (\d{4}-\d{2}-\d{2})', e)
    (dated.append((m.group(1), e)) if m else undated.append(e))
newest_first = len(dated) > 1 and dated[0][0] > dated[-1][0]
chrono = list(reversed(dated)) if newest_first else dated          # oldest first

size = lambda es: sum(len(x.encode('utf-8')) for x in es)
if len(src.encode('utf-8')) <= BUDGET:
    sys.exit(f'{path}: under budget, nothing to roll')

days = []                                                           # [(date, [entries])], oldest first
for d, e in chrono:
    if days and days[-1][0] == d: days[-1][1].append(e)
    else: days.append((d, [e]))
live, acc = [], 0
for d, es in reversed(days):
    if acc + size(es) > KEEP and live: break
    live.insert(0, (d, es)); acc += size(es)
roll = days[:len(days) - len(live)]
if not roll:
    sys.exit(f'{path}: the newest day alone exceeds the live share; nothing to roll')
groups, cur = [], []
for d, es in roll:
    if cur and size([x for _, xs in cur for x in xs]) + size(es) > BUDGET:
        groups.append(cur); cur = []
    cur.append((d, es))
groups.append(cur)

def body(group):                                                    # in the journal's own order
    g = list(reversed(group)) if newest_first else group
    return ''.join(x for _, xs in g for x in (list(reversed(xs)) if newest_first else xs))

where = 'top' if newest_first else 'bottom'
out = {}
for g in groups:
    first, last = g[0][0], g[-1][0]
    if os.path.exists(os.path.join(odir, f'{first}.md')):
        sys.exit(f'{stem}/{first}.md exists: a rolled file is never rewritten')
    h = (f"# {stem}, {first} to {last} (rolled over)\n\n"
         f"> Entries of `../{fname}` from {first} to {last}, rolled out on {today}\n"
         f"> when the live file passed 40 KB. Each entry is a record: its text is\n"
         f"> unchanged. Newest at the {where}. A dated citation resolves by\n"
         f"> `grep -n \"^## <date>\" {fname} {stem}/*.md`.\n\n")
    out[f'{first}.md'] = (h, body(g))
live_body = body(live)

# check: every dated entry lands exactly once, in its original order
orig = ''.join(e for _, e in dated)
rolled_in_order = [out[k][1] for k in sorted(out)]
joined = (live_body + ''.join(reversed(rolled_in_order))) if newest_first else (''.join(rolled_in_order) + live_body)
assert joined == orig, 'rollover would not preserve the entries byte for byte'

note = (f"Rollover (since {today}): when this file passes 40 KB, its oldest whole\n"
        f"days move to `{stem}/`, one file per period named by its first date and each\n"
        f"under 40 KB, until about 20 KB stays here. Entries move byte for byte and\n"
        f"keep their text; a dated citation resolves by\n"
        f"`grep -n \"^## <date>\" {fname} {stem}/*.md`. An open thread in a rolled\n"
        f"entry is carried into this file's open list first. `{stem}/INDEX.md` lists\n"
        f"every rolled entry by date and title, file by file.\n\n")
has_note = f'`{stem}/INDEX.md`' in header
if os.path.isdir(odir) and not has_note:
    sys.exit(f'{stem}/ exists but the live header has no rollover note: check by hand')

for k, (h, b) in out.items():
    print(f'  {stem}/{k}: {len((h + b).encode())} bytes')
print(f'  live: {len(live_body.encode())} bytes of entries from {live[0][0]}; undated kept: {len(undated)}')
if apply:
    os.makedirs(odir, exist_ok=True)
    for k, (h, b) in out.items():
        open(os.path.join(odir, k), 'w', encoding='utf-8', newline='').write(h + b)
    new_header = header if has_note else header + note
    open(path, 'w', encoding='utf-8', newline='').write(new_header + ''.join(undated) + live_body)
    subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    'journal_index.py'), odir], check=True)
    print('  applied')
