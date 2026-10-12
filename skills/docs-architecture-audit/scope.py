#!/usr/bin/env python3
"""Print what a docs-architecture audit of <dir> covers, one line per item with the rule it keys.

python scope.py [<launch dir>] [--lens release] [--root <dir>] [--global <file>|none] [--memory <file>|none]

The scope (R12 to R16), the chain row (R30, through chain_budget.py beside this script), the
structural findings a count can make (R25; a split index that no longer lists its parts), and
the seed of the cross-reference pass (R19): every path and section citation in the router and
the reference docs that does not resolve. With --lens release, the lines in the in-scope docs
that carry the phrases a release leaves behind (R29). Detection only: a claim's modality, what a
block of the router is, and whether a mismatch is drift or a contract are the workers' judgments.
Paths are relative to <dir>. A report, never a change.
"""
import os
import re
import subprocess
import sys

CANON = ['ARCHITECTURE.md', 'ROADMAP.md', 'DOMAIN.md', 'VERIFICATION.md']
JOURNAL = ['NOTEBOOK.md', 'CHANGELOG.md']
EXCLUDED = ['vendor', 'third_party', 'node_modules', 'bin', 'obj', 'dist', 'target', 'out', '.claude', 'openspec']
ARCHIVES = ['docs/archive', 'openspec/changes/archive', 'archive']
LENS = ['waits for', 'wait for', 'waiting for', 'not yet', 'until', 'today', 'currently', 'pending',
        'in progress', 'for now']
EXT = ('.md', '.py', '.cs', '.json', '.toml', '.yaml', '.yml', '.txt', '.ps1', '.sh', '.csv', '.html',
       '.js', '.ts', '.c', '.h', '.cpp', '.vhd', '.v', '.sv', '.ini', '.cfg', '.xml', '.bat')
NUMBER = r'(?:\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)'
DATED_HEAD = re.compile(r'^##+ +\**(\d{4}-\d{2}-\d{2})', re.M)
DATED_BULLET = re.compile(r'^- +\**(\d{4}-\d{2}-\d{2})', re.M)
TOKEN = re.compile(r'`([^`\n]+)`')
SECTION = re.compile(r'(root )?(?:`([^`]+\.md)`|\b([A-Z][A-Za-z_-]{2,})(?:\.md)?) § ([^,.;:)\n`]+)')
VERSION = re.compile(r'\bv\d+\.\d+|\b\d+\.\d+\.\d+\b|\b(?:release|version)\b', re.I)
COUNT = re.compile(r'\b' + NUMBER + r'\s+(?:[a-z-]{3,}\s+){0,2}[a-z]{3,}s\b', re.I)


def read(p):
    return open(p, encoding='utf-8', errors='replace', newline='').read()


def kb(n):
    return f'{n / 1024:.1f} KB'


def rel(p, d):
    return os.path.relpath(p, d).replace(os.sep, '/')


def is_pathlike(tok):
    dated = re.match(r'(?:[\w./-]+/)?\d{4}-\d{2}-\d{2} - [^/]+\.\w+$', tok)  # the spaced dated form, `docs/YYYY-MM-DD - name.md`
    if (' ' in tok and not dated) or any(c in tok for c in '<>*{}|$?…') or '...' in tok \
            or tok.startswith(('http://', 'https://', '--', '-')) or re.match(r'[\w.-]+\.(com|org|net|io|dev)/', tok) \
            or (tok.startswith('.') and tok.count('.') == 1 and '/' not in tok):  # a bare extension, `.cs`
        return False
    return '/' in tok or tok.lower().endswith(EXT)


def ancestors(d, root_):
    """Parent directories carrying a CLAUDE.md, nearest first, up to --root (inclusive) or the drive root."""
    found, cur = [], os.path.dirname(d)
    stop = os.path.abspath(root_) if root_ else None
    while True:
        if os.path.isfile(os.path.join(cur, 'CLAUDE.md')):
            found.append(cur)
        if (stop and os.path.normcase(cur) == os.path.normcase(stop)) or os.path.dirname(cur) == cur:
            break
        cur = os.path.dirname(cur)
    return found


def subprojects(d):
    found = []
    for cur, dirs, files in os.walk(d):
        dirs[:] = sorted(x for x in dirs if not x.startswith('.') and x not in EXCLUDED)
        if cur != d and ('CLAUDE.md' in files or os.path.isdir(os.path.join(cur, '.git'))):
            found.append(cur)
            dirs[:] = []
            continue
        if cur != d and rel(cur, d).count('/') >= 1:
            dirs[:] = []
    return found


def tree_index(d, depth=None):
    """Basename -> relative paths (files, and directories as 'name/'), for the rename-orphan check; .git and
    generated trees skipped, sub-projects included (a router may name a sub-project's file)."""
    index = {}
    for cur, dirs, files in os.walk(d):
        if depth is not None and cur != d and rel(cur, d).count('/') + 1 >= depth:
            dirs[:] = []
        dirs[:] = [x for x in dirs if not x.startswith('.') and x not in EXCLUDED]
        for x in dirs:
            index.setdefault(x + '/', []).append(rel(os.path.join(cur, x), d) + '/')
        for f in files:
            index.setdefault(f, []).append(rel(os.path.join(cur, f), d))
    return index


def line_of(text, tok):
    for i, line in enumerate(text.split('\n'), 1):
        if tok in line:
            return i, line.strip()
    return 0, ''


def heading_in(text, heading):
    return bool(re.search(r'^#+\s.*' + re.escape(heading.strip()), text, re.M | re.I))


def main(argv):
    args = argv[1:]
    if '-h' in args or '--help' in args:
        sys.exit(__doc__)

    def opt(name, default=None):
        if name in args:
            i = args.index(name)
            v = args[i + 1]
            del args[i:i + 2]
            return v
        return default

    lens = opt('--lens')
    glob_, memory, root_ = opt('--global'), opt('--memory'), opt('--root')
    d = os.path.abspath(args[0]) if args else os.getcwd()
    if not os.path.isdir(d):
        sys.exit(f'{d}: not a directory')
    out = []
    say = out.append
    say('docs-architecture-audit scope (a line ending in -> <rule> names the rule that governs it)')

    # The router and its ancestors
    say('')
    say('the router')
    rp = os.path.join(d, 'CLAUDE.md')
    router = read(rp) if os.path.isfile(rp) else ''
    if router:
        say(f'  CLAUDE.md {router.count(chr(10))} lines, {kb(len(router.encode("utf-8")))} (placement-audited itself: R26, R30)')
    else:
        say('  no CLAUDE.md: nothing routes this directory; the canonical set is the scope -> R12')
    for a in ancestors(d, root_):
        say(f'  ancestor router {rel(os.path.join(a, "CLAUDE.md"), d)} ({kb(os.path.getsize(os.path.join(a, "CLAUDE.md")))}): '
            'loads in every session here; its weight is its own audit\'s (R30)')
    subs = subprojects(d)
    index = tree_index(d)

    # What the router names
    tokens = [t for t in TOKEN.findall(router) if is_pathlike(t) or re.fullmatch(r'[a-z0-9][a-z0-9-]*', t)]
    named_files, named_specs = [], []
    for t in tokens:
        p = os.path.normpath(os.path.join(d, t))
        if os.path.isfile(p):
            r = rel(p, d)
            if r not in named_files:
                named_files.append(r)
        elif os.path.isdir(p):
            continue
        elif re.fullmatch(r'[a-z0-9][a-z0-9-]*', t) and os.path.isfile(os.path.join(d, 'openspec', 'specs', t, 'spec.md')):
            s = f'openspec/specs/{t}/spec.md'
            if s not in named_specs:
                named_specs.append(s)
    for f in list(named_files):
        if f.startswith('openspec/specs/') and f.endswith('spec.md'):
            named_files.remove(f)
            if f not in named_specs:
                named_specs.append(f)

    say('')
    say('in scope (R12)')
    reference = []
    for f in CANON + ['RELEASING.md']:
        if os.path.isfile(os.path.join(d, f)):
            reference.append(f)
            how = 'named by the router' if f in named_files else 'present, not named by the router'
            say(f'  {f:16} {kb(os.path.getsize(os.path.join(d, f))):>9}   {how}')
    routed_dated, routed_leaves = [], []
    for f in named_files:
        if f in reference or os.path.basename(f) == f and f in JOURNAL + ['CLAUDE.md', 'README.md']:
            continue
        top = f.split('/')[0]
        n, line = line_of(router, f)
        if not n:
            n, line = line_of(router, os.path.basename(f))
        quote = line[:100] + ('...' if len(line) > 100 else '')
        if f.startswith('docs/'):
            routed_dated.append(f)
            kind = 'a dated doc' if re.match(r'docs/\d{4}-\d{2}-\d{2}', f) else 'an undated doc under docs/'
            say(f'  {f}: {kind} the router names (line {n}: "{quote}") -> R12 (named: in scope; its role is the line\'s)')
        elif top in EXCLUDED:
            routed_leaves.append(f)
            say(f'  {f}: a router-named leaf inside an excluded tree (line {n}: "{quote}") -> R13 (in scope)')
        elif f.endswith('.md'):
            reference.append(f)
            say(f'  {f}: named by the router outside the canonical set (line {n}: "{quote}") -> R12')
    for s in named_specs:
        say(f'  {s}: a router-named spec: currency-audited, never edited -> R13 (a wrong SHALL is spec-change)')
    parts = {}
    for f in reference:
        stem = f[:-3]
        sd = os.path.join(d, stem)
        if os.path.isdir(sd):
            ps = sorted(x for x in os.listdir(sd) if x.endswith('.md'))
            listed = re.findall(r'\(`' + re.escape(stem) + r'/([^`]+)`', read(os.path.join(d, f)))
            parts[f] = [f'{stem}/{x}' for x in ps]
            say(f'  {stem}/: {len(ps)} parts of the split {f}, each the index\'s tier and charter -> R12'
                + ('' if sorted(listed) == ps else f' (the index lists {len(listed)}: stale, split_doc.py --reindex)'))

    say('')
    say('out of scope')
    journal = [j for j in JOURNAL if os.path.isfile(os.path.join(d, j))]
    docs = os.path.join(d, 'docs')
    records = []
    if os.path.isdir(docs):
        records = [f'docs/{x}' for x in sorted(os.listdir(docs)) if x.endswith('.md') and os.path.isfile(os.path.join(docs, x))
                   and f'docs/{x}' not in routed_dated]
    rolled = [j[:-3] + '/' for j in JOURNAL if os.path.isdir(os.path.join(d, j[:-3]))]
    if journal or records or rolled:
        say(f'  journal, never currency-audited: {", ".join(journal + rolled)}'
            + (f'{"; " if journal or rolled else ""}docs/ ({len(records)} unrouted dated records)' if os.path.isdir(docs) else '')
            + ' -> R14')
    arch = [a + '/' for a in ARCHIVES if os.path.isdir(os.path.join(d, a))]
    if arch:
        say(f'  archives: {", ".join(arch)} -> R14')
    excl = [x + '/' for x in EXCLUDED if os.path.isdir(os.path.join(d, x))]
    if excl:
        say(f'  excluded trees present: {", ".join(excl)} (unrouted content; a router-named leaf is in) -> R13')
    specs_dir = os.path.join(d, 'openspec', 'specs')
    if os.path.isdir(specs_dir):
        unnamed = [f'openspec/specs/{x}/spec.md' for x in sorted(os.listdir(specs_dir))
                   if os.path.isfile(os.path.join(specs_dir, x, 'spec.md')) and f'openspec/specs/{x}/spec.md' not in named_specs]
        if unnamed:
            say(f'  specs the router does not name: {", ".join(unnamed)} -> R13 (out)')
    for s in subs:
        why = 'own CLAUDE.md' if os.path.isfile(os.path.join(s, 'CLAUDE.md')) else 'own .git'
        say(f'  sub-project {rel(s, d)}/ ({why}): flag-and-skip, its own audit -> R16')
    if len(out) and out[-1] == 'out of scope':
        say('  nothing beyond the defaults')

    # Cold docs cited from the reference tier
    scope_docs = (['CLAUDE.md'] if router else []) + reference + routed_dated + routed_leaves + [p for ps in parts.values() for p in ps]
    cold = []
    for f in scope_docs:
        text = read(os.path.join(d, f))
        for t in TOKEN.findall(text):
            if not is_pathlike(t):
                continue
            p = os.path.normpath(os.path.join(d, t))
            r = rel(p, d) if os.path.isfile(p) else None
            if r and (r.startswith('docs/') and r not in routed_dated or re.match(r'openspec/changes/archive/.*/design\.md$', r)):
                n, _ = line_of(text, t)
                cold.append((r, f'{f}:{n}'))
    if cold:
        say('')
        say('cold docs cited from the reference tier (consistency check only) -> R15')
        seen = set()
        for r, where in cold:
            if r in seen:
                continue
            seen.add(r)
            kind = 'an archived design: its values are design-time, never a tier violation' if 'openspec/changes/archive' in r \
                else 'a dated record: a code-coupled fact inside it is a tier violation'
            say(f'  {r}, cited by {where} ({kind})')

    # Structure
    say('')
    say('structure')
    rm = os.path.join(d, 'ROADMAP.md')
    if os.path.isfile(rm):
        t = read(rm)
        for m in re.finditer(r'^## +(.*?)\s*$', t, re.M):
            if 'shipped' in m.group(1).lower() or 'history' in m.group(1).lower():
                nxt = re.search(r'^## ', t[m.end():], re.M)
                sec = t[m.end(): m.end() + nxt.start()] if nxt else t[m.end():]
                n = len(DATED_HEAD.findall(sec)) + len(DATED_BULLET.findall(sec))
                say(f'  ROADMAP.md "{m.group(1)}": {n} dated entries'
                    + (' -> R25 (one structural flag, move-to CHANGELOG.md; the entries are journal-tier)' if n > 5 else ''))
    for f in reference:
        b = os.path.getsize(os.path.join(d, f))
        if b > 40 * 1024 and f not in parts:
            say(f'  {f} {kb(b)}: past the budget and unsplit (a SETUP T5 job, reported here)')
    out.extend(chain_lines(d, glob_, memory, root_))

    # The cross-reference seed
    say('')
    say('cross-references that do not resolve (the seed of the R19 pass; code identifiers are the workers\')')
    n0 = len(out)
    resolved = 0
    anc = ancestors(d, root_)
    sibling_index = None
    for f in scope_docs:
        text = read(os.path.join(d, f))
        base = os.path.dirname(os.path.join(d, f))
        seen = {}
        for t in TOKEN.findall(text):
            if not is_pathlike(t) or t.startswith(('~', '/')):
                continue
            if t in seen:
                seen[t] += 1
                continue
            seen[t] = 1
            cands = [os.path.normpath(os.path.join(base, t)), os.path.normpath(os.path.join(d, t))]
            name = os.path.basename(t.rstrip('/')) + ('/' if t.endswith('/') else '')
            if any(os.path.exists(c) for c in cands) or ('/' not in t.rstrip('/') and name in index):
                resolved += 1
                seen[t] = 0
                continue
            n, _ = line_of(text, t)
            elsewhere = [p for p in index.get(name, []) if p != t]
            if elsewhere:
                say(f'  {f}:{n} `{t}`: not at that path; {name} is at {", ".join(elsewhere[:2])} -> R19 (a rename-orphan?)')
                continue
            if anc:
                if sibling_index is None:
                    sibling_index = tree_index(anc[0], depth=3)
                near = [rel(os.path.join(anc[0], p), d) for p in sibling_index.get(name, [])]
                if near:
                    say(f'  {f}:{n} `{t}`: not in this tree; under the ancestor at {", ".join(near[:2])} -> R19 (a sibling\'s file)')
                    continue
            say(f'  {f}:{n} `{t}`: not in the tree -> R19')
        for i in range(len(out) - 1, n0 - 1, -1):  # the first occurrence is listed; the count rides on it
            m = re.match(r'  ' + re.escape(f) + r':\d+ `([^`]+)`', out[i])
            if m and seen.get(m.group(1), 0) > 1 and 'more occurrence' not in out[i]:
                out[i] += f' ({seen[m.group(1)] - 1} more occurrence{"s" if seen[m.group(1)] > 2 else ""})'
        for m in SECTION.finditer(text):
            is_root, doc, heading = bool(m.group(1)), m.group(2) or (m.group(3) + '.md'), m.group(4).strip()
            targets = []
            if doc == 'CLAUDE.md' and (is_root or f != 'CLAUDE.md' and not router):
                targets = [os.path.join(a, 'CLAUDE.md') for a in anc]
            if not targets:
                targets = [os.path.join(d, doc)] + [os.path.join(d, p) for p in parts.get(doc, [])]
                if doc == 'CLAUDE.md':
                    targets += [os.path.join(a, 'CLAUDE.md') for a in anc]
            hit = next((tg for tg in targets if os.path.isfile(tg) and heading_in(read(tg), heading)), None)
            if hit:
                resolved += 1
                continue
            n, _ = line_of(text, m.group(0))
            where = ', '.join(rel(tg, d) for tg in targets if os.path.isfile(tg)) or f'{doc} (absent)'
            say(f'  {f}:{n} "{doc} § {heading}": no such heading in {where} -> R19')
    if len(out) == n0:
        say('  none')
    say(f'  ({resolved} paths and section citations resolve)')

    # The lens
    if lens:
        say('')
        say(f'the {lens}-close lens: lines the phrases a release leaves behind are on (R29; the workers judge each)')
        n0 = len(out)
        for f in scope_docs:
            for i, line in enumerate(read(os.path.join(d, f)).split('\n'), 1):
                low = line.lower()
                hits = [p for p in LENS if p in low]
                if VERSION.search(line):
                    hits.append('a version')
                if COUNT.search(low):
                    hits.append('a count')
                if hits:
                    s = line.strip()
                    say(f'  {f}:{i} [{", ".join(hits)}] {s[:110]}{"..." if len(s) > 110 else ""}')
        if len(out) == n0:
            say('  none')
    print('\n'.join(out))


def chain_lines(d, glob_, memory, root_):
    cb = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chain_budget.py')
    if not os.path.isfile(cb):
        return [f'  the chain: chain_budget.py not found beside this script ({cb})']
    cmd = [sys.executable, cb, d]
    for flag, val in (('--global', glob_), ('--memory', memory), ('--root', root_)):
        if val:
            cmd += [flag, val]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    rows, keep = [], []
    for l in r.stdout.split('\n'):
        m = re.match(r'\s*([\d.]+)\s+(\d+)\s+(\d+)\s+(\S.*)$', l)
        if m and 'total' not in l:
            rows.append((int(m.group(3)), m.group(1), m.group(2), m.group(4).strip()))
        elif 'total:' in l or "this project's part" in l or 'files over their own line' in l:
            keep.append(l.split())
    if not keep:
        return ['  the chain: chain_budget.py printed nothing' + (f' ({r.stderr.strip()})' if r.stderr.strip() else '')]
    first = keep[0]
    head = (f'total {first[0]} KB, {first[1]} tokens: ' + ' '.join(first[3:]) if len(first) > 3 and first[2] == 'total:'
            else ' '.join(first))
    lines = ['  the chain (chain_budget.py) -> R30 (the row goes in the coverage note): ' + head]
    lines += ['    ' + ' '.join(k) for k in keep[1:]]
    for tok, k, ln, rest in sorted(rows, reverse=True)[:3]:
        lines.append(f'    largest: {rest} ({k} KB, {ln} lines, {tok} tokens)')
    return lines


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace', newline='\n')
    main(sys.argv)
