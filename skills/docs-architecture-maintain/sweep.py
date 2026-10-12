#!/usr/bin/env python3
"""Print a maintain sweep's sources and budgets, or read its report back, one line per item with the rule.

python sweep.py [<dir>] [--budget-kb 40]            the sources: the live journals against their budget
                                                    (M17), the rolled files newer than the last watermark
                                                    (M19), the dated records, the archived designs (M11),
                                                    the targets past their budget (M9, M14), the last report
python sweep.py [<dir>] --check [<report>]          the run's report read back: the accounting slot (M16),
                                                    the ROADMAP lines a code-bug flag (M13), a held
                                                    promotion (M14) and a portfolio-level graduate (M15)
                                                    require; the newest docs/*maintain-report*.md by default

Detection only: what graduates, where, and with which disposition is the sweep's judgment. Paths are
relative to <dir>. A report, never a change.
"""
import os
import re
import sys

JOURNALS = ['NOTEBOOK.md', 'CHANGELOG.md']
TARGETS = ['ARCHITECTURE.md', 'ROADMAP.md', 'DOMAIN.md', 'VERIFICATION.md']
DATED_HEAD = re.compile(r'^##+ +\**(\d{4}-\d{2}-\d{2})', re.M)
DATED_BULLET = re.compile(r'^- +\**(\d{4}-\d{2}-\d{2})', re.M)
DATED_NAME = re.compile(r'^(\d{4}-\d{2}-\d{2})')


def read(p):
    return open(p, encoding='utf-8', errors='replace', newline='').read()


def kb(n):
    return f'{n / 1024:.1f} KB'


def rel(p, d):
    return os.path.relpath(p, d).replace(os.sep, '/')


def dated(text):
    heads, bullets = DATED_HEAD.findall(text), DATED_BULLET.findall(text)
    dates, form = (heads, 'dated headings') if len(heads) >= len(bullets) else (bullets, 'dated bullets')
    order = ''
    if len(dates) >= 2:
        order = ', newest first' if dates[0] >= dates[-1] else ', oldest first'
    return len(dates), form, order


def reports(d):
    """Maintain reports under docs/, newest name last."""
    docs = os.path.join(d, 'docs')
    if not os.path.isdir(docs):
        return []
    return sorted(f'docs/{x}' for x in os.listdir(docs) if 'maintain-report' in x and x.endswith('.md'))


def field(text, *keys):
    """The first line carrying every key (case-insensitive), stripped, or ''."""
    for line in text.split('\n'):
        low = line.lower()
        if all(k in low for k in keys):
            return line.strip()
    return ''


NEGATED = re.compile(r'\bnone\b|: no\b|\bnothing\b|\bno [a-z-]+ (?:is|are|was|were)\b', re.I)


def count(text, pattern):
    """Lines carrying the pattern; a heading (it names a section, not an item) and a line that says none,
    no or nothing beside the word are not counted."""
    return len([l for l in text.split('\n')
                if re.search(pattern, l, re.I) and not l.lstrip().startswith('#') and not NEGATED.search(l)])


def sources(d, budget, say):
    say(f'docs-architecture-maintain sweep (budget {budget // 1024} KB per journal; a line ending in -> <rule> names the rule)')
    last = reports(d)
    watermark = ''
    if last:
        wm = field(read(os.path.join(d, last[-1])), 'watermark')
        m = re.search(r'(?:NOTEBOOK|CHANGELOG)/[\w.-]+\.md', wm)
        watermark = m.group(0) if m else ''
    say('')
    say('the journal (the live files)')
    n0 = len(say.out)
    slices = []
    for j in JOURNALS:
        p = os.path.join(d, j)
        if not os.path.isfile(p):
            continue
        t = read(p)
        b = len(t.encode('utf-8'))
        n, form, order = dated(t)
        line = f'  {j} {kb(b)}, {n} {form}{order}'
        if b > budget:
            line += f'; past {budget // 1024} KB -> M17 (rollover.py, a dry run first; carry the open threads, M18)'
        elif n == 0 and b > 4096:
            line += '; no dated entries -> M17 (rollover.py refuses it: a SETUP finding)'
        say(line)
        slices.append(j)
        rolled = os.path.join(d, j[:-3])
        if os.path.isdir(rolled):
            files = sorted(f for f in os.listdir(rolled) if f.endswith('.md') and f != 'INDEX.md')
            stem = j[:-3]
            newer = [f for f in files if not watermark or f'{stem}/{f}' > watermark]
            line = f'  {stem}/ (rolled, frozen): {len(files)} files' \
                   + ('' if os.path.isfile(os.path.join(rolled, 'INDEX.md')) else ', no INDEX.md -> M17 (journal_index.py)')
            if files:
                line += (f'; newer than the watermark: {", ".join(newer)}' if watermark and newer
                         else '; none newer than the watermark' if watermark
                         else '; every file is a slice (no watermark yet)') + ' -> M19'
            say(line)
            slices += [f'{stem}/{f}' for f in newer]
    docs = os.path.join(d, 'docs')
    if os.path.isdir(docs):
        recs = [x for x in sorted(os.listdir(docs)) if x.endswith('.md') and DATED_NAME.match(x)
                and os.path.isfile(os.path.join(docs, x)) and 'maintain-report' not in x and 'audit-report' not in x]
        say(f'  docs/: {len(recs)} dated records (a spent one archives, M3 and M7; the reports are not sources)')
        if recs:
            slices.append(f'docs/ ({len(recs)} records)')
    arch = os.path.join(d, 'openspec', 'changes', 'archive')
    if os.path.isdir(arch):
        designs = sorted(f'openspec/changes/archive/{x}/design.md' for x in os.listdir(arch)
                         if os.path.isfile(os.path.join(arch, x, 'design.md')))
        say(f'  openspec/changes/archive/: {len(designs)} design docs -> M11 (a first-class source; cross-ref only, never edited)')
        if designs:
            slices.append(f'openspec/changes/archive/ ({len(designs)} designs)')
    if len(say.out) == n0:
        say('  no journal: nothing to sweep (a SETUP finding)')
    say('')
    say('the last report')
    if last:
        t = read(os.path.join(d, last[-1]))
        say(f'  {last[-1]}: watermark {watermark or "not stated -> M16"}; '
            f'{count(t, r"\bheld\b")} lines saying held; {count(t, r"flag-code-bug")} lines naming flag-code-bug'
            + (f'; {len(last) - 1} earlier' if len(last) > 1 else ''))
    else:
        say('  none under docs/: the first sweep (every rolled file is a slice; the report starts the watermark, M16)')
    say('')
    say('the targets (where a graduate lands)')
    for r in TARGETS:
        p = os.path.join(d, r)
        if not os.path.isfile(p):
            say(f'  {r:16}  missing (a SETUP finding; a graduate aimed here has no home)')
            continue
        t = read(p)
        b = len(t.encode('utf-8'))
        topics = len(re.findall(r'^## ', t, re.M))
        line = f'  {r:16} {kb(b):>9}   {topics} `##` topics'
        sd = os.path.join(d, r[:-3])
        if os.path.isdir(sd):
            parts = [x for x in os.listdir(sd) if x.endswith('.md')]
            line += f'; split: {r[:-3]}/ holds {len(parts)} parts (a promotion lands in the part whose heading it belongs under, M14)'
        elif b > budget:
            line += f'; past {budget // 1024} KB -> M14 (a graduate aimed here is held; the split is SETUP\'s T5)'
        elif b > budget // 2:
            line += f'; past half the budget: the M9 content test decides (held if dominated by content a split would relocate)'
        say(line)
    up = os.path.dirname(d)
    pd = os.path.join(up, 'DOMAIN.md')
    if os.path.isfile(os.path.join(up, 'CLAUDE.md')):
        say(f'  portfolio DOMAIN: ' + (f'../DOMAIN.md present ({kb(os.path.getsize(pd))}) -> M15 (the portfolio-level target)'
                                       if os.path.isfile(pd) else 'none beside the ancestor router -> M15 (a portfolio-level graduate is flag-and-ask)'))
    say('')
    say('the slices (M10): ' + ', '.join(slices))


def check(d, report, say):
    if report is None:
        rs = reports(d)
        if not rs:
            sys.exit('no docs/*maintain-report*.md to check: the run has not persisted its report (M13, M16)')
        report = rs[-1]
    p = os.path.join(d, report)
    if not os.path.isfile(p):
        sys.exit(f'{report}: not found')
    t = read(p)
    rm = os.path.join(d, 'ROADMAP.md')
    roadmap = read(rm) if os.path.isfile(rm) else ''
    say(f'docs-architecture-maintain check of {report} (a line ending in -> <rule> names what is missing)')
    say('')
    name = os.path.basename(report)
    say('  the name: ' + ('dated' if DATED_NAME.match(name) else 'not dated -> M13 (a dated report)'))
    prune = field(t, 'prune', 'candidate')
    say('  prune/archive candidates: ' + (f'"{prune[:90]}"' if prune else 'no line -> M16'))
    delta = field(t, 'net', 'delta') or field(t, 'reference-tier delta')
    say('  net reference-tier delta: ' + (f'"{delta[:90]}"' if delta else 'no line -> M16'))
    wm = field(t, 'watermark')
    say('  watermark: ' + (f'"{wm[:90]}"' if wm else 'no line -> M16'))
    bugs = count(t, r'flag-code-bug')
    if bugs:
        lines = [l for l in roadmap.split('\n') if re.search(r'code bug|flag-code-bug|' + re.escape(name), l, re.I)]
        say(f'  flag-code-bug in the report: {bugs} mention(s); ROADMAP lines carrying a code bug or naming the report: {len(lines)}'
            + ('' if lines else ' -> M13 (one line per surviving bug, or one line pointing at the report)'))
    else:
        say('  flag-code-bug in the report: none')
    held = count(t, r'\bheld\b')
    if held:
        lines = [l for l in roadmap.split('\n') if re.search(r'split', l, re.I) and re.search(r'T5|split_doc|by `##`|topic', l, re.I)]
        say(f'  held promotions: {held} line(s) saying held; ROADMAP lines naming a split job (T5, split_doc.py): {len(lines)}'
            + ('' if lines else ' -> M14 (one open line naming the pending split job and its shape)'))
    else:
        say('  held promotions: none mentioned')
    port = count(t, r'flag-and-ask|portfolio-level')
    if port:
        lines = [l for l in roadmap.split('\n') if re.search(r'portfolio', l, re.I) and re.search(r'DOMAIN|placement|home', l, re.I)]
        say(f'  portfolio-level graduates: {port} mention(s); ROADMAP lines asking for the placement: {len(lines)}'
            + ('' if lines else ' -> M15 (one open line for the placement decision)'))
    else:
        say('  portfolio-level graduates: none mentioned')


def main(argv):
    args = argv[1:]
    if '-h' in args or '--help' in args:
        sys.exit(__doc__)
    budget = 40 * 1024
    if '--budget-kb' in args:
        i = args.index('--budget-kb')
        budget = int(args[i + 1]) * 1024
        del args[i:i + 2]
    report = None
    checking = '--check' in args
    if checking:
        i = args.index('--check')
        if i + 1 < len(args) and not args[i + 1].startswith('--'):
            report = args[i + 1]
            del args[i:i + 2]
        else:
            del args[i]
    d = os.path.abspath(args[0]) if args else os.getcwd()
    if not os.path.isdir(d):
        sys.exit(f'{d}: not a directory')
    out = []

    def say(line):
        out.append(line)
    say.out = out
    if checking:
        check(d, report, say)
    else:
        sources(d, budget, say)
    print('\n'.join(out))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace', newline='\n')
    main(sys.argv)
