"""Measure the always-on chain: what a session launched in a directory loads before its first
question, against a budget.

python chain_budget.py [<launch dir>] [--root <dir>] [--global <file>|none] [--memory <file>|none]
                       [--window 200000] [--share 0.05] [--chars-per-token 4]

The chain, in the order the harness loads it: the owner's global instructions
(`~/.claude/CLAUDE.md`, and the files under `~/.claude/rules/` that carry no `paths:` line, since
those load at launch too); every `CLAUDE.md` and `CLAUDE.local.md` from the filesystem root
(or --root) down to the launch directory; the launch directory's `.claude/rules/` files without
`paths:`; and the project's memory index (`~/.claude/projects/<dir>/memory/MEMORY.md`). A rule
file with `paths:` loads only when a matching file is touched, so it is not in the chain. Each
file is reported in bytes, lines and estimated tokens (bytes / 4, the rule of thumb; change it
with --chars-per-token), with the harness's own per-file guidance (200 lines) marked, then the
total against the budget: --share of --window, 5 percent of 200k by default, about 10k tokens.
The part the project controls (its own router and rules) is subtotaled apart from the ancestors
and the owner's global file, since each of those is leaned from its own place. A report, never
a gate: exit 0 whatever the verdict; a missing launch directory exits 1. With --root, paths are
printed relative to it (forward slashes), so a fixture's output is the same on every machine.
"""
import os
import re
import sys

LINE_GUIDANCE = 200


def scoped(path):
    """True when a rules file carries a `paths:` line in its frontmatter (loads on demand)."""
    try:
        text = open(path, encoding='utf-8', newline='').read()
    except OSError:
        return False
    if not text.startswith('---'):
        return False
    end = text.find('\n---', 3)
    front = text[3:end] if end > 0 else text[3:]
    return re.search(r'(?m)^paths:', front) is not None


def always_on_rules(rules_dir):
    out = []
    if os.path.isdir(rules_dir):
        for dirpath, _, files in os.walk(rules_dir):
            for f in sorted(files):
                p = os.path.join(dirpath, f)
                if f.endswith('.md') and not scoped(p):
                    out.append(p)
    return out


def memory_index(launch):
    mangled = re.sub(r'[:\\/ ]', '-', os.path.abspath(launch))
    return os.path.join(os.path.expanduser('~'), '.claude', 'projects', mangled, 'memory', 'MEMORY.md')


def measure(path, cpt):
    data = open(path, 'rb').read()
    return len(data), data.count(b'\n'), round(len(data) / cpt)


def main(argv):
    args = argv[1:]

    def opt(name, default):
        if name in args:
            i = args.index(name)
            v = args[i + 1]
            del args[i:i + 2]
            return v
        return default

    root = opt('--root', None)
    glob_ = opt('--global', os.path.join(os.path.expanduser('~'), '.claude', 'CLAUDE.md'))
    memory = opt('--memory', None)
    window = int(opt('--window', '200000'))
    share = float(opt('--share', '0.05'))
    cpt = float(opt('--chars-per-token', '4'))
    launch = os.path.abspath(args[0] if args else '.')
    if not os.path.isdir(launch):
        sys.exit(f'{launch}: not a directory')
    root = os.path.abspath(root) if root else None
    if root and not (launch == root or launch.startswith(root + os.sep)):
        sys.exit(f'{launch} is not under --root {root}')

    def show(p):
        if root:
            return os.path.relpath(p, root).replace(os.sep, '/')
        return p

    # (path, role) in load order
    chain = []
    if glob_ != 'none':
        if os.path.isfile(glob_):
            chain.append((glob_, "the owner's global file"))
        for p in always_on_rules(os.path.join(os.path.dirname(glob_), 'rules')):
            chain.append((p, "the owner's global rule"))
    ancestors = []
    d = launch
    while True:
        ancestors.append(d)
        if root and d == root:
            break
        parent = os.path.dirname(d)
        if parent == d:
            break
        d = parent
    for d in reversed(ancestors):
        role = 'this project' if d == launch else 'ancestor'
        for name in ('CLAUDE.md', 'CLAUDE.local.md'):
            p = os.path.join(d, name)
            if os.path.isfile(p):
                chain.append((p, role))
    for p in always_on_rules(os.path.join(launch, '.claude', 'rules')):
        chain.append((p, "this project's rule"))
    mem = None if memory == 'none' else (memory or memory_index(launch))
    if mem and os.path.isfile(mem):
        chain.append((mem, 'memory index'))

    budget = round(window * share)
    print(f"Always-on chain for {show(launch)} (window {window} tokens, budget {share * 100:g}% = "
          f"{budget} tokens; tokens = bytes/{cpt:g})")
    print()
    print(f"{'KB':>7} {'lines':>6} {'tokens':>7}  file")
    totals = {'bytes': 0, 'tokens': 0, 'own': 0, 'ancestors': 0, 'global': 0, 'memory': 0}
    sizes = []
    for p, role in chain:
        b, lines, t = measure(p, cpt)
        mark = f'  [over {LINE_GUIDANCE} lines]' if lines > LINE_GUIDANCE else ''
        print(f"{b / 1024:7.1f} {lines:6d} {t:7d}  {show(p)}  ({role}){mark}")
        totals['bytes'] += b
        totals['tokens'] += t
        key = {'this project': 'own', "this project's rule": 'own', 'ancestor': 'ancestors',
               "the owner's global file": 'global', "the owner's global rule": 'global',
               'memory index': 'memory'}[role]
        totals[key] += t
        sizes.append((b, show(p), role))
    if not chain:
        print('   (nothing: no instruction file loads here)')
    print()
    verdict = ('within budget' if totals['tokens'] <= budget
               else f"over budget by {totals['tokens'] - budget} tokens ({totals['tokens'] / budget:.1f}x)")
    print(f"{totals['bytes'] / 1024:7.1f} {'':6} {totals['tokens']:7d}  total: {verdict}")
    print(f"{'':22}this project's part {totals['own']}; ancestors {totals['ancestors']}; "
          f"the owner's global {totals['global']}; memory index {totals['memory']}")
    if sizes:
        top = sorted(sizes, reverse=True)[:3]
        print(f"{'':22}largest: " + '; '.join(f'{s} {b / 1024:.1f} KB ({r})' for b, s, r in top))


if __name__ == '__main__':
    main(sys.argv)
