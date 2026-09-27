"""Journal rollover: a journal past its budget rolls its oldest whole days into an overflow
directory named for the file, one file per period, each under the budget.

python rollover.py <repo>/<JOURNAL>.md [--apply] [--budget-kb 40] [--keep-kb 20]

Works on NOTEBOOK.md (newest last) and CHANGELOG.md (newest first): the order is read from the
dates. Entry forms recognized: `## YYYY-MM-DD ...` headings (a `##` journal; column-0 bullets
inside an entry belong to it), or top-level `- YYYY-MM-DD ...` / `- **YYYY-MM-DD** ...` bullets
(a bullet journal; a bullet's indented lines belong to it). Undated units (an "Open threads"
section, an undated bullet) stay in the live file right after its header.

Rules: whole days stay together; a rolled file is named by the first (earliest) date it holds;
about KEEP bytes of dated entries stay live, so the file does not roll again the next day;
entries move byte for byte (checked); a rolled file is never rewritten. With --apply it writes
the files, adds the rollover note to the live header once, and regenerates <JOURNAL>/INDEX.md.
Carrying an open thread out of an entry about to roll is the operator's step before --apply:
the dry run lists what will roll.
"""
import datetime
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from journal_index import write_index  # noqa: E402

DATE = r'\d{4}-\d{2}-\d{2}'
HEAD_DATED = re.compile(r'^## (' + DATE + ')')
BULLET_DATED = re.compile(r'^- \**(' + DATE + ')')


def parse(text):
    """Split a journal into (header, units); a unit is (date or None, text)."""
    lines = text.split('\n')
    heads = sum(1 for l in lines if HEAD_DATED.match(l))
    bullets = sum(1 for l in lines if BULLET_DATED.match(l))
    if heads == 0 and bullets == 0:
        sys.exit('no dated entries recognized (## YYYY-MM-DD headings or - YYYY-MM-DD bullets)')
    form = 'heading' if heads >= bullets else 'bullet'
    if form == 'heading':
        starts = [i for i, l in enumerate(lines) if l.startswith('## ')]
        dated = HEAD_DATED
    else:
        starts = [i for i, l in enumerate(lines) if l.startswith('- ') or l.startswith('#')]
        dated = BULLET_DATED
    if not starts:
        sys.exit('no entry boundaries found')
    # the top title line (# ...) and the charter before the first unit are the header
    first = starts[0]
    if form == 'bullet':
        # a '# title' line above the first bullet is header, not a unit
        while first < len(lines) and lines[first].startswith('#') and not lines[first].startswith('## '):
            starts.pop(0)
            if not starts:
                sys.exit('no entry boundaries found')
            first = starts[0]
    header = '\n'.join(lines[:first]) + '\n' if first else ''
    units = []
    for k, s in enumerate(starts):
        e = starts[k + 1] if k + 1 < len(starts) else len(lines)
        body = '\n'.join(lines[s:e])
        if k + 1 < len(starts):
            body += '\n'
        m = dated.match(lines[s])
        units.append((m.group(1) if m else None, body))
    assert header + ''.join(b for _, b in units) == text
    return header, units


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    path = argv[1]
    apply = '--apply' in argv
    budget = 40 * 1024
    keep = 20 * 1024
    if '--budget-kb' in argv:
        budget = int(argv[argv.index('--budget-kb') + 1]) * 1024
    if '--keep-kb' in argv:
        keep = int(argv[argv.index('--keep-kb') + 1]) * 1024
    repo, fname = os.path.split(os.path.abspath(path))
    stem = fname[:-3]
    odir = os.path.join(repo, stem)
    today = datetime.date.today().isoformat()

    src = open(path, encoding='utf-8', newline='').read()
    if len(src.encode('utf-8')) <= budget:
        sys.exit(f'{path}: under budget ({len(src.encode()) // 1024} KB of {budget // 1024}), nothing to roll')
    header, units = parse(src)
    dated = [(d, b) for d, b in units if d]
    undated = [b for d, b in units if not d]
    size = lambda bs: sum(len(b.encode('utf-8')) for b in bs)
    newest_first = len(dated) > 1 and dated[0][0] > dated[-1][0]
    chrono = list(reversed(dated)) if newest_first else dated

    days = []
    for d, b in chrono:
        if days and days[-1][0] == d:
            days[-1][1].append(b)
        else:
            days.append((d, [b]))
    live, acc = [], 0
    for d, bs in reversed(days):
        if acc + size(bs) > keep and live:
            break
        live.insert(0, (d, bs))
        acc += size(bs)
    roll = days[:len(days) - len(live)]
    if not roll:
        sys.exit(f'{path}: the newest day alone fills the live share; nothing to roll')
    groups, cur = [], []
    for d, bs in roll:
        if cur and size([b for _, xs in cur for b in xs]) + size(bs) > budget:
            groups.append(cur)
            cur = []
        cur.append((d, bs))
    groups.append(cur)

    def body(group):
        g = list(reversed(group)) if newest_first else group
        return ''.join(b for _, xs in g for b in (list(reversed(xs)) if newest_first else xs))

    where = 'top' if newest_first else 'bottom'
    out = {}
    for g in groups:
        first, last = g[0][0], g[-1][0]
        if os.path.exists(os.path.join(odir, f'{first}.md')):
            sys.exit(f'{stem}/{first}.md exists: a rolled file is never rewritten')
        head = (f"# {stem}, {first} to {last} (rolled over)\n\n"
                f"> Entries of `../{fname}` from {first} to {last}, rolled out on {today}\n"
                f"> when the live file passed its budget. Each entry is a record: its text\n"
                f"> is unchanged. Newest at the {where}. A dated citation resolves by\n"
                f"> `grep -n \"<date>\" {fname} {stem}/*.md`; `{stem}/INDEX.md` lists every\n"
                f"> rolled entry.\n\n")
        out[f'{first}.md'] = (head, body(g))
    live_body = body(live)

    orig = ''.join(b for _, b in dated)
    rolled = [out[k][1] for k in sorted(out)]
    joined = (live_body + ''.join(reversed(rolled))) if newest_first else (''.join(rolled) + live_body)
    assert joined == orig, 'the rollover would not preserve the entries byte for byte'

    note = (f"Rollover (since {today}): when this file passes {budget // 1024} KB, its oldest\n"
            f"whole days move to `{stem}/`, one file per period named by its first date and\n"
            f"each under {budget // 1024} KB, until about {keep // 1024} KB stays here. Entries\n"
            f"move byte for byte and keep their text; a dated citation resolves by\n"
            f"`grep -n \"<date>\" {fname} {stem}/*.md`, and `{stem}/INDEX.md` lists every\n"
            f"rolled entry. An open thread in a rolled entry is carried into this file's\n"
            f"open list first.\n\n")
    has_note = f'`{stem}/INDEX.md`' in header
    if os.path.isdir(odir) and not has_note:
        sys.exit(f'{stem}/ exists but the live header carries no rollover note: check by hand')

    print(f'form: {"newest first" if newest_first else "newest last"}; '
          f'{len(dated)} dated entries, {len(undated)} undated units kept live')
    for k, (h, b) in out.items():
        g = [x for x in groups if x[0][0] == k[:-3]][0]
        print(f'  {stem}/{k}: {len((h + b).encode())} bytes, {sum(len(xs) for _, xs in g)} entries, '
              f'{g[0][0]} to {g[-1][0]}')
    print(f'  live: {len(live_body.encode())} bytes of entries from {live[0][0]}')
    if not apply:
        print('  dry run: scan the entries above for open threads to carry, then --apply')
        return
    os.makedirs(odir, exist_ok=True)
    for k, (h, b) in out.items():
        open(os.path.join(odir, k), 'w', encoding='utf-8', newline='').write(h + b)
    new_header = header if has_note else header + note
    open(path, 'w', encoding='utf-8', newline='').write(new_header + ''.join(undated) + live_body)
    write_index(odir)
    print('  applied')


if __name__ == '__main__':
    main(sys.argv)
