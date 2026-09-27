# Proposal: journal-rollover

## Why

A journal is one file that grows forever. On the HDL tree a NOTEBOOK reached 311 KB in 33
days and another 138 KB in 20; a maintain sweep spent three workers on one file, and
`docs-architecture-maintain`'s only relief, M3's archive disposition, moves entries by
judgment into `archive/`, which breaks every dated citation the reference tier makes into the
journal and needs adjudication per entry. The owner decided (2026-09-26): a journal rolls over
chronologically, and its closed periods live in a directory named for the file, beside it.
Piloted the same day across seven journals in six repositories (ROADMAP, "Journal rollover and
the overflow directory"; the findings there). The family's four skills each touch the journal
and none knows the directory; this change teaches them, and ships the scripts the pilot
proved.

## What Changes

- **SETUP**, modified: the journal tier gains the overflow directory (`NOTEBOOK/`,
  `CHANGELOG/`, each rolled file named by its first date, `INDEX.md` inside); the enforced-set
  rows and T1 name it; the router line teaches that a dated citation resolves by grep over the
  file and its directory; B2's filename normalization targets the project's stated dated-record
  pattern (default `YYYY-MM-DD-<slug>.md`, stated in the router's journal line) instead of one
  fixed spelling; a container root's ignore file names its nested repositories and never
  wildcards the root's directories (a wildcard silently drops a new directory, the overflow
  directory first).
- **MAINTAIN**, modified: a step before the fan-out rolls any journal past its budget with
  the bundled script (`rollover.py` and `journal_index.py`, beside the SKILL.md); the sweep
  slices by rolled file; rolled files are frozen like the openspec archive (a graduate from one
  takes `cross-ref` in the reference doc or `stub`, never an edit, never M7); M3's archive
  disposition applies to dated `docs/` records only; the report records the newest rolled file
  it covered as the next sweep's watermark. The rollover also runs on its own, whenever a
  journal passes the budget, no sweep needed.
- **AUDIT**, modified: R14's never-currency-audited set includes the overflow directories and
  their `INDEX.md`; the cross-reference pass resolves a dated citation in the live file or the
  directory.
- **whats-next**, modified: the journal row reads the live file, its carried open threads
  first; rolled files are frozen history, not swept.
- **The design doc**: the tier section names three journal members (it still says two, from
  before the 2026-07-12 CHANGELOG decision) and the rollover; the scripts' contract.
- **Specs**: the maintain and whats-next specs get the Purposes they never had.

## Capabilities

### Modified Capabilities
- `docs-architecture-setup`: the journal tier's overflow directory; the dated-record pattern
  as a stated convention; a container root's ignore file by name.
- `docs-architecture-maintain`: the rollover step, frozen rolled files, M3 narrowed, the
  watermark.
- `docs-architecture-audit`: the overflow directory is journal-tier; citation resolution.
- `whats-next`: open items from the live file only.

## Impact

Every consumer project keeps its `NOTEBOOK.md` and `CHANGELOG.md` where they are; a
directory appears beside a journal only when it passes the budget (40 KB by default, about
10k tokens, the harness's per-file warning). No pointer in any project changes: a dated
citation names a date, and the date is found by grep in the file or the directory. A
manifest that enumerates a project's files (a kit list) is a consumer the rollover names.
Gated on RED/GREEN on non-derived fixtures: TidePool with a big-journal variant (a
newest-first bullet journal, the second entry form the scripts accept) and the reefstack
container for the ignore rule; the HDL tree is the deriving evidence and is poisoned for this
rule. No back-compat: the pilot's copies of the scripts under `docs/2026-09-26 -
journal-rollover/` stay as the record of what ran; the skill's copies are the product.
