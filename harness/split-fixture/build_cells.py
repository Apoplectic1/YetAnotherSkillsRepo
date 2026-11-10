"""Build the scratch projects for the split-index cells SD6, SD8 and SD9 (catalog-tidepool.md).

python build_cells.py <out dir>

Each is the TidePool fixture with the `fat-topics` ARCHITECTURE overlaid, baselined in git:
  <out>/sd6-authoring  unsplit: the authoring rep splits it and writes the lines
  <out>/sd8-review     split with lines.md, then a paragraph on reading the `tides` listing
                       against NOAA's own tide table appended to that part (a topic its line
                       does not name; the part's size moves, so --check reports it)
  <out>/sd9-audit      split with lines.md, then the CSV export part's line in the index
                       rewritten to describe the terminal table, a topic the part does not
                       hold; its terms occur in the part and no size moves, so --check passes
SD7 needs no project: its inputs are four index texts (the catalog names them).
"""
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
FIXTURE = os.path.join(REPO, 'harness', 'tidepool-fixture')
VARIANT = os.path.join(REPO, 'harness', 'tidepool-fixture-variants', 'fat-topics')
SPLIT = os.path.join(REPO, 'skills', 'docs-architecture-setup', 'split_doc.py')
GIT = ['git', '-c', 'user.name=t', '-c', 'user.email=t@t', '-c', 'core.autocrlf=false']

TIDES_PARAGRAPH = """
Reading the listing against NOAA's own tide table: the station page on tidesandcurrents.noaa.gov
shows the same hi/lo predictions, by default in the three settings the client pins (MLLW datum,
local standard or daylight time, feet), so a `tides` line and the website's row for the same
date agree to the minute and the hundredth of a foot. A mismatch is diagnostic: a height off by
a constant means the page was switched to another datum (MHHW and STND are the usual ones), a
time off by an hour means the page shows LST without the daylight shift, and a missing row
means the page shows a subordinate station's offsets, which the hi/lo product does not apply.
Checking one day this way is the quickest proof that a candidate station's predictions are what
a tidepooler will find on the beach.
"""
CSV_LINE_WRITTEN = ('`CSV_COLUMNS` (the nine names in order), `export_csv` writing with `newline=""` and '
                    '`DictWriter` (missing keys empty, extra keys dropped), the row values taken unformatted from '
                    '`_windows()`, and the `--out` path: relative to the working directory, overwritten without asking.')
CSV_LINE_PLANTED = ('How the terminal table is laid out: the column widths, the header row and the order of the '
                    'printed keys, with `CSV_COLUMNS` as the shared list of names and `_windows()` as the source of '
                    'the rounding.')


def project(out, name, split):
    d = os.path.join(out, name)
    if os.path.exists(d):
        sys.exit(f'{d} exists: build into an empty directory')
    shutil.copytree(FIXTURE, d)
    shutil.copytree(VARIANT, d, dirs_exist_ok=True)
    if split:
        r = subprocess.run([sys.executable, SPLIT, os.path.join(d, 'ARCHITECTURE.md'), '--apply', '--today',
                            '2026-10-12', '--lines', os.path.join(HERE, 'lines.md')], capture_output=True, text=True)
        if r.returncode:
            sys.exit(r.stdout + r.stderr)
    return d


def baseline(d):
    for cmd in (['init', '-q'], ['add', '-A'], ['commit', '-qm', '=== SKILLS-TEST BASELINE ===']):
        subprocess.run(GIT + cmd, cwd=d, check=True, capture_output=True)


def main(out):
    os.makedirs(out, exist_ok=True)
    baseline(project(out, 'sd6-authoring', split=False))
    d = project(out, 'sd8-review', split=True)
    with open(os.path.join(d, 'ARCHITECTURE', 'the-tides-subcommand-and-the-raw-listing.md'), 'a',
              encoding='utf-8', newline='') as f:
        f.write(TIDES_PARAGRAPH)
    baseline(d)
    d = project(out, 'sd9-audit', split=True)
    p = os.path.join(d, 'ARCHITECTURE.md')
    t = open(p, encoding='utf-8', newline='').read()
    assert t.count(CSV_LINE_WRITTEN) == 1
    open(p, 'w', encoding='utf-8', newline='').write(t.replace(CSV_LINE_WRITTEN, CSV_LINE_PLANTED))
    baseline(d)
    print(f'built sd6-authoring, sd8-review, sd9-audit in {out}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(os.path.abspath(sys.argv[1]))
