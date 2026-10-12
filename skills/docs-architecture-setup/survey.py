#!/usr/bin/env python3
"""Survey a project's tree against the docs-architecture-setup rules, one line per finding.

python survey.py [<dir>] [--budget-kb 40] [--root <dir>] [--global <file>|none] [--memory <file>|none]

Each line states what a rule keys on and ends with the rule (-> S5, -> T5, ...) when it is a
finding; an inventory line carries no arrow. Detection only: the content tests (S7's reference
content, S8's breadth and stability, a charter's honesty) are the reader's. The chain row comes
from chain_budget.py beside the audit skill when it is found; --root, --global and --memory pass
through to it. Paths are relative to <dir>. A report, never a change.
"""
import os
import re
import subprocess
import sys

SET = ['CLAUDE.md', 'ARCHITECTURE.md', 'ROADMAP.md', 'NOTEBOOK.md', 'VERIFICATION.md', 'DOMAIN.md']
CONDITIONAL = ['CHANGELOG.md', 'README.md', 'RELEASING.md']
REFERENCE = ['ARCHITECTURE.md', 'ROADMAP.md', 'DOMAIN.md', 'VERIFICATION.md']
JOURNALS = ['NOTEBOOK.md', 'CHANGELOG.md']
NOT_AT_A_CONTAINER = ['ARCHITECTURE.md', 'NOTEBOOK.md', 'VERIFICATION.md', 'CHANGELOG.md']
EXCLUDED = ['vendor', 'third_party', 'node_modules', 'bin', 'obj', 'dist', 'target', 'out', '.claude', 'openspec']
TOOLING = ['scripts', 'tools', 'ci']
CODE_EXT = {'.py', '.cs', '.c', '.h', '.cpp', '.hpp', '.cc', '.js', '.ts', '.tsx', '.rs', '.go', '.java', '.kt',
            '.swift', '.vhd', '.vhdl', '.v', '.sv', '.cu', '.m', '.jl', '.r', '.csproj', '.sln', '.vcxproj', '.fsproj'}
MANIFESTS = ['pyproject.toml', 'setup.py', 'setup.cfg', 'package.json', 'Cargo.toml', 'go.mod', 'CMakeLists.txt',
             'Makefile', 'build.gradle', 'pom.xml', 'Directory.Build.props']
MANIFEST_EXT = {'.sln', '.csproj', '.vcxproj', '.fsproj', '.xpr'}
LINE_GUIDANCE = 200
DATED_HEAD = re.compile(r'^##+ +\**(\d{4}-\d{2}-\d{2})', re.M)
DATED_BULLET = re.compile(r'^- +\**(\d{4}-\d{2}-\d{2})', re.M)


def read(p):
    return open(p, encoding='utf-8', errors='replace', newline='').read()


def kb(n):
    return f'{n / 1024:.1f} KB'


def rel(p, d):
    return os.path.relpath(p, d).replace(os.sep, '/')


def charter_line(text):
    """The first non-heading line of the file, bold stripped, and whether it calls itself a charter."""
    for line in text.split('\n')[:12]:
        s = line.strip()
        if s and not s.startswith('#'):
            s = s.replace('**', '')
            return s[:80] + ('...' if len(s) > 80 else ''), 'charter' in s.lower()
    return '', False


def topics(text):
    return re.findall(r'^## +(.+?)\s*$', text, re.M)


def dated(text):
    heads, bullets = DATED_HEAD.findall(text), DATED_BULLET.findall(text)
    dates, form = (heads, 'dated headings') if len(heads) >= len(bullets) else (bullets, 'dated bullets')
    order = ''
    if len(dates) >= 2:
        order = ', newest first' if dates[0] >= dates[-1] else ', oldest first'
    return len(dates), form, order


def subprojects(d):
    """Directories up to two levels down with their own router or repository; not descended into."""
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


def code_files(d, subs, depth):
    """Source files within `depth` directory levels, outside the sub-projects, exclusions and tooling; capped."""
    n, first, skip = 0, '', set(subs)
    for cur, dirs, files in os.walk(d):
        if cur != d and rel(cur, d).count('/') + 1 >= depth:
            dirs[:] = []
        dirs[:] = [x for x in dirs if not x.startswith('.') and x not in EXCLUDED and x not in TOOLING
                   and os.path.join(cur, x) not in skip]
        for f in sorted(files):
            if os.path.splitext(f)[1].lower() in CODE_EXT:
                n += 1
                first = first or rel(os.path.join(cur, f), d)
                if n >= 200:
                    return n, first
    return n, first


def shape_report(d, say):
    """'project', 'container' or 'either': a manifest or reference docs at the root make a project; nothing
    first-party within two levels outside the sub-projects makes a container root; the rest is the router's call."""
    subs = subprojects(d)
    manifest = sorted(f for f in os.listdir(d)
                      if f in MANIFESTS or os.path.splitext(f)[1].lower() in MANIFEST_EXT)
    docs = [f for f in ('ARCHITECTURE.md', 'NOTEBOOK.md', 'VERIFICATION.md') if os.path.isfile(os.path.join(d, f))]
    if os.path.isdir(os.path.join(d, 'docs')):
        docs.append('docs/')
    n, first = code_files(d, subs, 2)
    count = '200+' if n >= 200 else str(n)
    if not subs:
        shape = 'project'
        say(f'  a project: {count} source files within two levels'
            + (f', manifest {", ".join(manifest)}' if manifest else ''))
    elif manifest or docs:
        shape = 'project'
        say(f'  a project with {len(subs)} sub-projects beneath: '
            + (f'manifest {", ".join(manifest)}' if manifest else f'{", ".join(docs)} at the root'))
    elif n == 0:
        shape = 'container'
        say(f'  container root: no manifest, no reference docs and no source within two levels outside its '
            f'{len(subs)} sub-projects -> B4 (the router plus at most a portfolio DOMAIN and a thin ROADMAP)')
    else:
        shape = 'either'
        say(f'  a container root or a project: no manifest and no reference docs at the root, {count} source files '
            f'within two levels outside its {len(subs)} sub-projects (first: {first}); the router says which -> B4 or B3')
    for s in subs:
        why = ('own CLAUDE.md' if os.path.isfile(os.path.join(s, 'CLAUDE.md')) else '')
        if os.path.isdir(os.path.join(s, '.git')):
            why = (why + ' and .git') if why else 'own .git'
        say(f'  sub-project {rel(s, d)}/ ({why}) -> B3 flag-and-skip')
    return subs, shape


def set_report(d, shape, say):
    present = []
    container, either = shape == 'container', shape == 'either'
    absent_set = ('absent (B4: not at a container root)' if container
                  else 'absent (S5 for a project; B4 keeps a container root to the router, a DOMAIN and a ROADMAP)'
                  if either else 'missing -> S5 (create it charter\'d-thin)')
    for f in SET + CONDITIONAL:
        p = os.path.join(d, f)
        if os.path.isfile(p):
            present.append(f)
            t = read(p)
            if f == 'README.md':
                say(f'  {f:16} {kb(len(t.encode("utf-8"))):>9}   present (the public entry point)')
                continue
            c, ok = charter_line(t)
            state = (f'charter: "{c}"' if ok else f'no charter line ("{c}") -> S5' if c
                     else 'empty -> S5 (charter it, never blank)')
            if container and f in NOT_AT_A_CONTAINER:
                state += ' -> B4 (a container root does not carry it; its content is a project\'s)'
            say(f'  {f:16} {kb(len(t.encode("utf-8"))):>9}   {state}')
        elif f in SET:
            say(f'  {f:16} {"":>9}   ' + (absent_set if f != 'CLAUDE.md' else 'missing -> S5 (create it charter\'d-thin)'))
        else:
            say(f'  {f:16} {"":>9}   absent (conditional)')
    docs = os.path.join(d, 'docs')
    if os.path.isdir(docs):
        say(f'  {"docs/":16} {"":>9}   present' + (' -> B4 (a container root keeps no journal)' if container else ''))
    else:
        say(f'  {"docs/":16} {"":>9}   ' + (absent_set if shape != 'project' else 'missing -> S5 (the journal\'s dated records)'))
    for f in sorted(x for x in os.listdir(d) if x.endswith('.md') and x not in SET + CONDITIONAL
                    and os.path.isfile(os.path.join(d, x))):
        b = os.path.getsize(os.path.join(d, f))
        say(f'  {f:16} {kb(b):>9}   outside the set'
            + (' -> B5 if the project is code-light (a design slot), else its charter home' if b >= 20 * 1024
               else ' (S6 if it is the domain doc under another name; else its charter home or a dated record)'))
    return present


def router_report(d, text, present, say):
    lines = text.count('\n') + (0 if text.endswith('\n') else 1)
    say(f'  CLAUDE.md {lines} lines, {kb(len(text.encode("utf-8")))}'
        + (f' [over {LINE_GUIDANCE} lines] -> S8' if lines > LINE_GUIDANCE else ''))
    others = [f for f in present if f != 'CLAUDE.md']
    named = [f for f in others if f in text]
    unnamed = [f for f in others if f not in text]
    say(f'  names: {", ".join(named) or "none of the set"}'
        + (f'; does not name: {", ".join(unnamed)} -> T4' if unnamed else ''))
    m = re.search(r'YYYY-MM-DD[^`\s)]*', text)
    say(f'  dated-record pattern stated: `{m.group(0)}`' if m else '  dated-record pattern not stated -> T4')
    excl = [x for x in EXCLUDED if os.path.isdir(os.path.join(d, x))]
    if excl:
        noted = [x for x in excl if x in text]
        unnoted = [x for x in excl if x not in text]
        say(f'  exclusions present: {", ".join(x + "/" for x in excl)}; noted in the router: {", ".join(noted) or "none"}'
            + (f'; not noted: {", ".join(unnoted)} -> B1' if unnoted else ''))
    rules_dir = os.path.join(d, '.claude', 'rules')
    if os.path.isdir(rules_dir):
        for f in sorted(x for x in os.listdir(rules_dir) if x.endswith('.md')):
            t = read(os.path.join(rules_dir, f))
            scoped = t.startswith('---') and bool(re.search(r'^paths:', t, re.M))
            say(f'  rule file .claude/rules/{f}: '
                + ('path-scoped' if scoped else 'always-on (no paths:, loads at launch) -> S8')
                + (', named in the router' if f in text else ', not named in the router -> S8'))
    skills_dir = os.path.join(d, '.claude', 'skills')
    if os.path.isdir(skills_dir):
        names = sorted(x for x in os.listdir(skills_dir) if os.path.isfile(os.path.join(skills_dir, x, 'SKILL.md')))
        if names:
            say(f'  skills under .claude/skills/: {len(names)} ({", ".join(names[:6])}{", ..." if len(names) > 6 else ""})')


def chain_lines(d, glob_, memory, root_):
    cb = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..',
                                       'docs-architecture-audit', 'chain_budget.py'))
    if not os.path.isfile(cb):
        return [f'  the chain: run python chain_budget.py (beside the audit skill; not found at {cb})']
    cmd = [sys.executable, cb, d]
    for flag, val in (('--global', glob_), ('--memory', memory), ('--root', root_)):
        if val:
            cmd += [flag, val]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    keep = [l.split() for l in r.stdout.split('\n')
            if 'total:' in l or "this project's part" in l or 'files over their own line' in l]
    if not keep:
        return ['  the chain: chain_budget.py printed nothing' + (f' ({r.stderr.strip()})' if r.stderr.strip() else '')]
    first = keep[0]
    head = (f'total {first[0]} KB, {first[1]} tokens: ' + ' '.join(first[3:]) if len(first) > 3 and first[2] == 'total:'
            else ' '.join(first))
    return ['  the chain (chain_budget.py): ' + head] + ['    ' + ' '.join(k) for k in keep[1:]]


def journal_report(d, budget, say):
    for j in JOURNALS:
        p = os.path.join(d, j)
        if not os.path.isfile(p):
            continue
        t = read(p)
        b = len(t.encode('utf-8'))
        n, form, order = dated(t)
        line = f'  {j} {kb(b)}, {n} {form}{order}'
        if b > budget:
            line += f'; past {budget // 1024} KB -> T1 (rollover.py)'
        elif n == 0 and b > 4096:
            line += '; no dated entries -> T1 (a journal rolls by date)'
        say(line)
        rolled = os.path.join(d, j[:-3])
        if os.path.isdir(rolled):
            files = [f for f in os.listdir(rolled) if f.endswith('.md') and f != 'INDEX.md']
            say(f'  {j[:-3]}/ (rolled): {len(files)} files'
                + ('' if os.path.isfile(os.path.join(rolled, 'INDEX.md')) else ', no INDEX.md -> T1 (journal_index.py)'))
    docs = os.path.join(d, 'docs')
    if os.path.isdir(docs):
        entries = sorted(os.listdir(docs))
        files = [f for f in entries if f.endswith('.md') and os.path.isfile(os.path.join(docs, f))]
        spaced = [f for f in files if re.match(r'\d{4}-\d{2}-\d{2} - ', f)]
        slug = [f for f in files if re.match(r'\d{4}-\d{2}-\d{2}-', f)]
        undated = [f for f in files if f not in spaced and f not in slug]
        dirs = [f for f in entries if os.path.isdir(os.path.join(docs, f))]
        say(f'  docs/: {len(files)} records: `YYYY-MM-DD - <name>.md` {len(spaced)}, `YYYY-MM-DD-<slug>.md` {len(slug)}, '
            f'undated {len(undated)}'
            + (f' ({", ".join(undated[:4])}{", ..." if len(undated) > 4 else ""}) -> B2 (the stated pattern, '
               'unless the router routes them as reference)' if undated else '')
            + (f'; subdirectories: {", ".join(x + "/" for x in dirs[:5])}' if dirs else ''))
        if spaced and slug:
            say('  docs/: two dated forms in use (the router\'s journal line decides which stands: B2)')


def reference_report(d, budget, say):
    for r in REFERENCE:
        p = os.path.join(d, r)
        if not os.path.isfile(p):
            continue
        t = read(p)
        b = len(t.encode('utf-8'))
        tp = topics(t)
        line = f'  {r} {kb(b)}, {len(tp)} `##` topics'
        stem = r[:-3]
        sd = os.path.join(d, stem)
        if os.path.isdir(sd):
            parts = sorted(f for f in os.listdir(sd) if f.endswith('.md'))
            listed = re.findall(r'\(`' + re.escape(stem) + r'/([^`]+)`', t)
            line += f'; split: {stem}/ holds {len(parts)} parts, the index lists {len(listed)}'
            if sorted(listed) != parts:
                line += ' -> T5 (--reindex)'
        elif b > budget:
            line += f'; past {budget // 1024} KB -> ' + ('T5 (split_doc.py)' if len(tp) >= 2
                                                          else 'T5 cannot split one topic: its headings are the lever')
        say(line)
    p = os.path.join(d, 'ROADMAP.md')
    if os.path.isfile(p):
        t = read(p)
        for m in re.finditer(r'^## +(.*?)\s*$', t, re.M):
            if 'shipped' in m.group(1).lower() or 'history' in m.group(1).lower():
                nxt = re.search(r'^## ', t[m.end():], re.M)
                sec = t[m.end(): m.end() + nxt.start()] if nxt else t[m.end():]
                n = len(DATED_HEAD.findall(sec)) + len(DATED_BULLET.findall(sec))
                say(f'  ROADMAP.md "{m.group(1)}": {n} dated entries'
                    + (' -> A2 (CHANGELOG.md; a five-line digest stays)' if n > 5 else ''))


def ignore_report(d, subs, shape, say):
    """B6 is a container root's rule; a project with a nested repository gets the fact without the arrow."""
    repos = [s for s in subs if os.path.isdir(os.path.join(s, '.git'))]
    p = os.path.join(d, '.gitignore')
    if not repos:
        return
    b6 = ' -> B6 (name each one)' if shape != 'project' else ''
    if not os.path.isfile(p):
        say(f'  no .gitignore over {len(repos)} nested repositories{b6}')
        return
    lines = [l.strip() for l in read(p).split('\n')]
    wild = [l for l in lines if l in ('/*/', '*/', '/*', '*')]

    def named_by(s):
        r = rel(s, d)
        for l in lines:
            pat = l.strip('/')
            pat = pat[:-2] if pat.endswith('/*') else pat
            if pat and not any(ch in pat for ch in '*?[') and (r == pat or r.startswith(pat + '/')):
                return True
        return False

    named = [s for s in repos if named_by(s)]
    unnamed = [rel(s, d) + '/' for s in repos if s not in named]
    if wild:
        say(f'  .gitignore: wildcard `{wild[0]}` over {len(repos)} nested repositories{b6}')
    else:
        say(f'  .gitignore: names {len(named)} of {len(repos)} nested repositories'
            + (f' (unnamed: {", ".join(unnamed[:3])}{", ..." if len(unnamed) > 3 else ""}){b6}' if unnamed else ''))


def git_report(d, say):
    try:
        r = subprocess.run(['git', '-C', d, 'rev-parse', '--show-toplevel'], capture_output=True, text=True,
                           encoding='utf-8', errors='replace')
    except OSError:
        say('  git: not available')
        return
    top = r.stdout.strip()
    if r.returncode != 0 or not top:
        say('  not a git repository -> S3 (create the net first)')
        return
    if os.path.normcase(os.path.abspath(top)) != os.path.normcase(os.path.abspath(d)):
        say(f'  git: inside the repository at {top} (not its own)')
    s = subprocess.run(['git', '-C', d, 'status', '--porcelain', '.'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    n = len([l for l in s.stdout.split('\n') if l.strip()])
    say('  git: clean tree' if n == 0 else f'  git: {n} changed or untracked paths -> S2 (commit first)')


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

    budget = int(opt('--budget-kb', '40')) * 1024
    glob_, memory, root_ = opt('--global'), opt('--memory'), opt('--root')
    d = os.path.abspath(args[0]) if args else os.getcwd()
    if not os.path.isdir(d):
        sys.exit(f'{d}: not a directory')
    out = []
    say = out.append
    say(f'docs-architecture-setup survey (budget {budget // 1024} KB per doc, {LINE_GUIDANCE} lines per always-on file; '
        'a line ending in -> <rule> is a finding)')
    say('')
    say('shape')
    subs, shape = shape_report(d, say)
    say('')
    say('the set')
    present = set_report(d, shape, say)
    say('')
    say('the router')
    rp = os.path.join(d, 'CLAUDE.md')
    if os.path.isfile(rp):
        router_report(d, read(rp), present, say)
    else:
        say('  no CLAUDE.md -> T4 (write the router)')
    out.extend(chain_lines(d, glob_, memory, root_))
    say('')
    say('the journal')
    n0 = len(out)
    journal_report(d, budget, say)
    if len(out) == n0:
        say('  none')
    say('')
    say('reference docs')
    n0 = len(out)
    reference_report(d, budget, say)
    if len(out) == n0:
        say('  none')
    say('')
    say('the tree')
    ignore_report(d, subs, shape, say)
    git_report(d, say)
    print('\n'.join(out))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace', newline='\n')
    main(sys.argv)
