"""Every script-level case of the setup skill's split_doc.py, and of the --check that survey.py and
the audit skill's scope.py run, on scratch copies of the TidePool `fat-topics` ARCHITECTURE.

python check_split.py [<scratch dir>] [--write]

One PASS or FAIL line per case; exit 1 on any FAIL. --write regenerates dryrun.expected.txt and
index.expected.md beside this script from the current split_doc.py and lines.md first (then the
run checks them like any other). The scratch dir defaults to a new temporary directory; it is
never this repository.
"""
import difflib
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
SPLIT = os.path.join(REPO, 'skills', 'docs-architecture-setup', 'split_doc.py')
SURVEY = os.path.join(REPO, 'skills', 'docs-architecture-setup', 'survey.py')
SCOPE = os.path.join(REPO, 'skills', 'docs-architecture-audit', 'scope.py')
FIXTURE = os.path.join(REPO, 'harness', 'tidepool-fixture')
VARIANT = os.path.join(REPO, 'harness', 'tidepool-fixture-variants', 'fat-topics')
DOC = os.path.join(VARIANT, 'ARCHITECTURE.md')
LINES = os.path.join(HERE, 'lines.md')
GIT = ['git', '-c', 'user.name=t', '-c', 'user.email=t@t', '-c', 'core.autocrlf=false']
args = [a for a in sys.argv[1:] if not a.startswith('--')]
ROOT = os.path.abspath(args[0]) if args else tempfile.mkdtemp(prefix='check_split-')
WRITE = '--write' in sys.argv
assert not ROOT.startswith(REPO), 'the scratch dir must lie outside this repository'
failed = 0


def rm(d):
    if os.path.exists(d):  # git's objects are read-only on Windows
        shutil.rmtree(d, onexc=lambda fn, p, e: (os.chmod(p, 0o666), fn(p)))


def scratch(name, crlf=False):
    d = os.path.join(ROOT, name)
    rm(d)
    os.makedirs(d)
    t = open(DOC, 'rb').read()
    if crlf:
        t = t.replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')
    open(os.path.join(d, 'ARCHITECTURE.md'), 'wb').write(t)
    return d


def split(d, *args):
    r = subprocess.run([sys.executable, SPLIT, 'ARCHITECTURE.md', *args], cwd=d, capture_output=True)
    return r.returncode, r.stdout.decode('utf-8'), r.stderr.decode('utf-8', 'replace')


def applied(name):
    d = scratch(name)
    c, o, e = split(d, '--apply', '--today', '2026-10-12', '--lines', LINES)
    assert c == 0, o + e
    return d


def rd(d, p='ARCHITECTURE.md'):
    return open(os.path.join(d, p), encoding='utf-8', newline='').read()


def wr(d, p, t, mode='w'):
    with open(os.path.join(d, p), mode, encoding='utf-8', newline='') as f:
        f.write(t)


def case(label, good, detail=''):
    global failed
    failed += not good
    print(f"{'PASS' if good else 'FAIL'} {label}")
    if not good and detail:
        print('   ' + detail.replace('\n', '\n   ')[:2000])


def git_baseline(d):
    for cmd in (['init', '-q'], ['add', '-A'], ['commit', '-qm', '=== SKILLS-TEST BASELINE ===']):
        subprocess.run(GIT + cmd, cwd=d, capture_output=True)


# the expected outputs: the dry run, the apply's index, the reconstruction, the CRLF run
d = scratch('dry')
c, out, err = split(d)
if WRITE:
    wr(HERE, 'dryrun.expected.txt', out)
exp = rd(HERE, 'dryrun.expected.txt')
case('dry run prints dryrun.expected.txt', c == 0 and out == exp,
     ''.join(difflib.unified_diff(exp.splitlines(True), out.splitlines(True), n=1)) or err)
lf = scratch('lf')
c, out, err = split(lf, '--apply', '--today', '2026-10-12', '--lines', LINES)
if WRITE and c == 0:
    wr(HERE, 'index.expected.md', rd(lf))
case('apply leaves index.expected.md as the index', c == 0 and rd(lf) == rd(HERE, 'index.expected.md'), err)
orig = rd(VARIANT)
parts = re.findall(r'\(`ARCHITECTURE/([^`]+)`', rd(lf))
body = ''.join(rd(lf, f'ARCHITECTURE/{p}').split('\n\n', 2)[2] for p in parts)
case("the preamble and the parts' sections reconstruct the doc byte for byte",
     orig[:orig.index('\n## ') + 1] + body == orig)
cr = scratch('crlf', crlf=True)
c1 = split(cr, '--apply', '--today', '2026-10-12', '--lines', LINES)[0]
c2 = split(cr, '--reindex')[0]
e = subprocess.run([sys.executable, os.path.join(HERE, 'eol_check.py'), cr, 'ARCHITECTURE.md'], capture_output=True, text=True)
case('the CRLF apply and reindex pass eol_check.py', c1 == 0 and c2 == 0 and e.returncode == 0, e.stdout[-600:])
sizes = re.compile(r', \d+\.\d KB\)')
case("the CRLF run converted back equals the LF run's but for the sizes",
     all(sizes.sub('', rd(lf, p)) == sizes.sub('', rd(cr, p).replace('\r\n', '\n'))
         for p in ['ARCHITECTURE.md'] + [f'ARCHITECTURE/{x}' for x in parts]))

# the apply's refusals: each exits non-zero, names its cause, writes nothing
good = open(LINES, encoding='utf-8').read()
refusals = [
    ('no lines file', None, '--apply needs --lines'),
    ('a heading with no line', re.sub(r'(## Errors and exit paths\n)[^\n]+\n', r'\1', good),
     'errors-and-exit-paths.md "Errors and exit paths": no line'),
    ('a heading absent from the lines file', re.sub(r'## Errors and exit paths\n[^\n]+\n\n', '', good),
     '"Errors and exit paths": no line in the lines file'),
    ('a heading the doc lacks', good + '\n## Caching policy\nA heading the doc does not have.\n',
     '"Caching policy": not a `## ` heading of the doc'),
    ('a backticked term its part lacks', good.replace('`fetch_predictions` and its fixed', '`fetch_tides()` and its fixed'),
     '`fetch_tides()` does not occur in the part'),
    ('a line of 321 characters', re.sub(r'(## State \(2026-07-10\)\n)[^\n]+', lambda m: m.group(1) + 'x' * 321, good),
     'the line is 321 characters, past the cap of 320'),
]
for label, text, must in refusals:
    d = scratch('refuse')
    a = ['--apply']
    if text is not None:
        wr(ROOT, 'lines-variant.md', text)
        a += ['--lines', os.path.join(ROOT, 'lines-variant.md')]
    c, o, e = split(d, *a)
    case(f'apply refuses {label}, writing nothing',
         c != 0 and must in o + e and rd(d) == orig and not os.path.exists(os.path.join(d, 'ARCHITECTURE')), o + e)
d = scratch('journal')
wr(d, 'ARCHITECTURE.md', '# A journal\n\n' + ''.join(f'## 2026-{m:02d}-{k:02d}\n\n' + 'An entry.\n' * 120
                                                       for m in range(1, 4) for k in range(1, 15)))
c, o, e = split(d, '--apply', '--lines', LINES)
case('a doc whose `##` headings are dates is refused, naming the rollover, nothing written',
     c != 0 and 'rolls over by date with rollover.py' in o + e and not os.path.exists(os.path.join(d, 'ARCHITECTURE')), o + e)
d = scratch('cap')
wr(ROOT, 'lines-variant.md', re.sub(r'(## State \(2026-07-10\)\n)[^\n]+', lambda m: m.group(1) + 'y' * 320, good))
case('a line of 320 characters passes', split(d, '--lines', os.path.join(ROOT, 'lines-variant.md'))[0] == 0)
d = scratch('dry-lines')
c, o, e = split(d, '--lines', LINES)
case('the dry run checks lines.md without writing', c == 0 and 'a line for each of the 19 parts, every check passed' in o
     and not os.path.exists(os.path.join(d, 'ARCHITECTURE')), o[-800:] + e)

# --reindex
d = applied('reindex')
before = rd(d)
c, o, e = split(d, '--reindex')
case('reindex on an untouched split leaves the index byte-identical, no review', c == 0 and rd(d) == before and 'review' not in o, o + e)
wr(d, 'ARCHITECTURE/window-scoring.md', '\nA paragraph added after the split, about the scorer.\n' * 20, 'a')
c, o, e = split(d, '--reindex')
eb = next(l for l in before.split('\n') if 'window-scoring.md' in l)
ea = next(l for l in rd(d).split('\n') if 'window-scoring.md' in l)
case('a grown part: its size refreshed, its line kept byte for byte',
     c == 0 and '3.4 KB' in eb and '3.4 KB' not in ea and eb.split('KB): ', 1)[1] == ea.split('KB): ', 1)[1], o + e)
case('a grown part is listed for review with both sizes and its line',
     'review: 1 part(s)' in o and 'ARCHITECTURE/window-scoring.md: 3.4 KB -> ' in o and eb.split('KB): ', 1)[1] in o, o)
case('the other entries are unchanged', all(l in rd(d) for l in before.split('\n') if l.startswith('- **') and 'window-scoring' not in l))
d = applied('new-part')
before = rd(d)
wr(d, 'ARCHITECTURE/tide-datums.md', '# ARCHITECTURE: Tide datums\n\n> Added after the split.\n\n## Tide datums\n\nWhy `MLLW` and not `MSL`.\n')
c, o, e = split(d, '--reindex')
case('a new part with no line is refused, the index unchanged',
     c != 0 and 'ARCHITECTURE/tide-datums.md: no line (a new part: give its line with --lines)' in o + e and rd(d) == before, o + e)
wr(ROOT, 'new-lines.md', '## Tide datums\nWhy every height is `MLLW` rather than `MSL`.\n')
c, o, e = split(d, '--reindex', '--lines', os.path.join(ROOT, 'new-lines.md'))
case('a new part is entered after the listed parts from a lines file, the others kept',
     c == 0 and [l for l in rd(d).split('\n') if l.startswith('- **')][-1]
     == '- **Tide datums** (`ARCHITECTURE/tide-datums.md`, 0.0 KB): Why every height is `MLLW` rather than `MSL`.'
     and all(l in rd(d) for l in before.split('\n') if l.startswith('- **')), o + e)
d = applied('renamed')
wr(d, 'ARCHITECTURE/the-co-ops-client.md', rd(d, 'ARCHITECTURE/the-co-ops-client.md').replace('fetch_predictions', 'get_predictions'))
before = rd(d)
c, o, e = split(d, '--reindex')
case('a renamed identifier is refused naming the part and the term, the index unchanged',
     c != 0 and 'ARCHITECTURE/the-co-ops-client.md: `fetch_predictions` does not occur in the part' in o + e and rd(d) == before, o + e)

# --check
d = applied('check')
git_baseline(d)
c, o, e = split(d, '--check')
case('--check on a fresh split: nothing stale, exit 0', c == 0 and 'the index matches its 19 parts' in o, o + e)
os.remove(os.path.join(d, 'ARCHITECTURE', 'state.md'))
wr(d, 'ARCHITECTURE/extra.md', '## Extra\n\nx\n')
wr(d, 'ARCHITECTURE/csv-export.md', 'More about the exporter.\n' * 30, 'a')
idx = rd(d)
cli = next(l for l in idx.split('\n') if '`ARCHITECTURE/the-cli.md`' in l)
idx = idx.replace(cli, cli.split('): ')[0] + ')').replace('`low_tides` (no height cut)', '`low_tide_filter` (no height cut)')
wr(d, 'ARCHITECTURE.md', idx)
git_baseline(d)
c, o, e = split(d, '--check')
case('--check names each of five planted findings, exit 1', c == 1 and 'the index is stale, 5 finding(s)' in o and all(w in o for w in [
    'ARCHITECTURE/state.md: listed in the index, not in ARCHITECTURE/',
    'ARCHITECTURE/extra.md: in ARCHITECTURE/, not listed in the index',
    'ARCHITECTURE/csv-export.md: the index records 1.5 KB, the part is',
    'ARCHITECTURE/the-cli.md: no line',
    'ARCHITECTURE/the-co-ops-client.md: `low_tide_filter` does not occur in the part']), o + e)
st = subprocess.run(['git', 'status', '--porcelain'], cwd=d, capture_output=True, text=True).stdout
case('--check writes nothing (git status clean)', st == '', st)

# survey.py and scope.py run --check on a project holding the split
sp = os.path.join(ROOT, 'project')
rm(sp)
shutil.copytree(FIXTURE, sp)
shutil.copytree(VARIANT, sp, dirs_exist_ok=True)
assert subprocess.run([sys.executable, SPLIT, os.path.join(sp, 'ARCHITECTURE.md'), '--apply', '--today', '2026-10-12',
                       '--lines', LINES], capture_output=True).returncode == 0
git_baseline(sp)


def report_lines(script, starts):
    r = subprocess.run([sys.executable, script, sp, '--root', sp, '--global', 'none', '--memory', 'none'], capture_output=True)
    out = r.stdout.decode('utf-8').split('\n')
    i = next(k for k, l in enumerate(out) if l.startswith(starts))
    return out[i:i + 2]


AL = '  ARCHITECTURE/:'
s = report_lines(SURVEY, '  ARCHITECTURE.md 7')
a = report_lines(SCOPE, AL)
case('survey and scope: a current split draws no stale remark', 'stale' not in s[0] and 'stale' not in a[0], '\n'.join(s + a))
wr(sp, 'ARCHITECTURE/window-scoring.md', '\nAn edit after the split.\n' * 20, 'a')
s = report_lines(SURVEY, '  ARCHITECTURE.md 7')
a = report_lines(SCOPE, AL)
case("survey: an edited part makes the doc's line stale, ending -> T5 (--reindex), the part named below",
     s[0].endswith('the index is stale, 1 finding(s) -> T5 (--reindex)') and 'ARCHITECTURE/window-scoring.md: the index records 3.4 KB' in s[1], '\n'.join(s))
case('scope: an edited part makes the split line stale with --reindex, the part named below',
     'the index is stale, 1 finding(s): split_doc.py --reindex' in a[0] and 'ARCHITECTURE/window-scoring.md: the index records 3.4 KB' in a[1], '\n'.join(a))
print(f'{failed} failed; scratch: {ROOT}')
sys.exit(1 if failed else 0)
