"""Generate the chain fixture: a three-level tree of instruction files with known sizes, for
the script-level check of the audit skill's chain_budget.py.

python gen_chain_fixture.py <out dir>

Writes, under <out dir>: global.md (a stand-in for the owner's global file, 27 KB), CLAUDE.md
(4.5 KB), mid/CLAUDE.md (12 KB), mid/leaf/CLAUDE.md (40 KB, over the 200-line guidance),
mid/leaf/.claude/rules/always.md (1 KB, no paths: line, so always-on) and
mid/leaf/.claude/rules/scoped.md (2 KB, with paths:, so on demand and out of the chain). The
text is deterministic filler of fixed-width lines, so byte counts, line counts and the
expected output (chain.expected.txt) are exact. The check:

    python gen_chain_fixture.py <scratch>/chain
    cd <scratch>/chain && python <skill dir>/chain_budget.py mid/leaf --root . --global global.md --memory none > out.txt
    diff out.txt <repo>/harness/chain-fixture/chain.expected.txt
"""
import os
import sys

LINE = 'x' * 99 + '\n'  # 100 bytes per line


def filler(title, total_bytes):
    head = f'# {title}\n\n'
    body_bytes = total_bytes - len(head.encode())
    n, rem = divmod(body_bytes, len(LINE))
    return head + LINE * n + ('y' * (rem - 1) + '\n' if rem else '')


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8', newline='').write(text)


def main(out):
    write(os.path.join(out, 'global.md'), filler('global stand-in', 27 * 1024))
    write(os.path.join(out, 'CLAUDE.md'), filler('root router', 4608))
    write(os.path.join(out, 'mid', 'CLAUDE.md'), filler('mid router', 12 * 1024))
    write(os.path.join(out, 'mid', 'leaf', 'CLAUDE.md'), filler('leaf router', 40 * 1024))
    write(os.path.join(out, 'mid', 'leaf', '.claude', 'rules', 'always.md'),
          filler('always-on rule', 1024))
    write(os.path.join(out, 'mid', 'leaf', '.claude', 'rules', 'scoped.md'),
          '---\npaths: ["src/**/*.py"]\n---\n' + filler('scoped rule', 2048 - 30))
    print(f'{out}: written')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
