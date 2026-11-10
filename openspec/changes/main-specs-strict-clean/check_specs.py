"""The main specs lost nothing in main-specs-strict-clean (design D5).

python check_specs.py [<capability>]

For each main spec (or the one named): every clause of every old requirement description
(the spec at BASE) occurs in the new spec on disk or in ledger.md beside this script; every
old requirement name and scenario name occurs in the new spec; every new requirement has a
scenario. Then `openspec validate --specs --strict`. One line per fault; exit 1 on any fault
or a strict failure.
"""
import os
import re
import subprocess
import sys

BASE = '6edbf67'  # the commit the apply starts from (the planning commit; the specs as of 9b5bc5b)
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
SPECS = os.path.join(ROOT, 'openspec', 'specs')


def norm(t):
    return re.sub(r'\s+', ' ', t.replace('“', '"').replace('”', '"')).strip()


def requirements(text):
    """[(name, description, [scenario names], [scenario bodies])] in order; a body is its
    WHEN/THEN/AND bullets, without any paragraph that follows them."""
    out = []
    for block in re.split(r'(?m)^### Requirement: ', text)[1:]:
        name, _, rest = block.partition('\n')
        parts = re.split(r'(?m)^#### Scenario: ', rest)
        desc = re.split(r'(?m)^## ', parts[0])[0]
        scen = [p.split('\n', 1)[0].strip() for p in parts[1:]]
        bodies = [re.split(r'\n\s*\n', re.split(r'(?m)^## ', p.split('\n', 1)[1] if '\n' in p else '')[0])[0]
                  for p in parts[1:]]
        out.append((name.strip(), desc.strip(), scen, bodies))
    return out


def clauses(desc):
    """A description's clauses: split at sentence ends and semicolons, line wraps joined."""
    t = norm(desc)
    bits = re.split(r'(?<=[.;])\s+(?=[A-Z*`(\[])|;\s+', t)
    return [b.strip() for b in bits if len(b.strip()) >= 12]


def main(argv):
    only = argv[1] if len(argv) > 1 else None
    ledger = norm(open(os.path.join(HERE, 'ledger.md'), encoding='utf-8').read())
    caps = sorted(d for d in os.listdir(SPECS) if os.path.isfile(os.path.join(SPECS, d, 'spec.md')))
    faults = 0
    for cap in caps:
        if only and cap != only:
            continue
        old = subprocess.run(['git', 'show', f'{BASE}:openspec/specs/{cap}/spec.md'], cwd=ROOT,
                             capture_output=True, text=True, encoding='utf-8').stdout
        new = open(os.path.join(SPECS, cap, 'spec.md'), encoding='utf-8').read()
        nnew = norm(new)
        new_reqs = requirements(new)
        new_names = {r[0] for r in new_reqs}
        new_scen = {s for r in new_reqs for s in r[2]}
        found = []
        for name, desc, scen, bodies in requirements(old):
            if name not in new_names and f'Renamed: "{name}"' not in ledger:
                found.append(f'requirement gone (and no "Renamed:" ledger entry): "{name}"')
            for s, b in zip(scen, bodies):
                if s not in new_scen:
                    found.append(f'scenario gone: "{s}" (was under "{name}")')
                elif norm(b) not in nnew and norm(b) not in ledger:
                    found.append(f'scenario body changed: "{s}" (under "{name}")')
            for c in clauses(desc):
                if c not in nnew and c not in ledger:
                    found.append(f'clause neither kept nor in the ledger, from "{name}": {c[:140]}')
        for name, _, scen, _ in new_reqs:
            if not scen:
                found.append(f'requirement without a scenario: "{name}"')
        found += [f'a status note is left (line {i})' for i, l in enumerate(new.split('\n'), 1)
                  if re.match(r'\**Status note', l.strip())]
        old_n, new_n = len(requirements(old)), len(new_reqs)
        print(f'{cap}: {old_n} -> {new_n} requirements, {len(found)} fault(s)')
        for f in found:
            print(f'  {f}')
        faults += len(found)
    r = subprocess.run('openspec validate --specs --strict', cwd=ROOT, shell=True, capture_output=True,
                       text=True, encoding='utf-8', errors='replace')
    tot = re.search(r'Totals: (\d+) passed, (\d+) failed', r.stdout + r.stderr)
    print(f'strict validation: {tot.group(1)} passed, {tot.group(2)} failed' if tot else 'strict validation: no totals line')
    return 1 if faults or not tot or tot.group(2) != '0' else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
