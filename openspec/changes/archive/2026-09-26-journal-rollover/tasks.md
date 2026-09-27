# Tasks

## 1. The scripts and the fixture
- [x] 1.1 `skills/docs-architecture-maintain/rollover.py` and `journal_index.py`: both entry forms (D6), the contract (D3 to D5), refusals; replay against the pilot's inputs reproduces the pilot's committed output byte for byte
- [x] 1.2 `harness/tidepool-fixture-variants/big-journal/`: the 80 KB newest-first bullet NOTEBOOK with RO1 to RO3; the ARCHITECTURE citation; the catalog cells (RO1 to RO5) in `harness/catalog-tidepool.md`; `harness/README.md` names the variant

## 2. RED
- [x] 2.1 MAINTAIN, two on-disk reps on TidePool + big-journal with the current SKILL text: record what happens to the 80 KB journal (left whole, judged into archive/, trimmed) and to RO1 to RO3
- [x] 2.2 Prompt-only probes: SETUP on a container root carrying a `/*/` ignore file (D8); SETUP on a router stating the spaced dated-record pattern (D9); AUDIT on a rolled file with stale values (R14); whats-next on a rolled file with a closed open item

## 3. The skill text
- [x] 3.1 MAINTAIN: the rollover step before the fan-out (the script, the dry run, the open-thread carry), slicing by rolled file, D5 (frozen rolled files, M3 narrowed, the watermark in the report), the scripts named by relative position
- [x] 3.2 SETUP: the enforced-set rows and T1 (the overflow directory, the index), the router line (citation by grep), B2 (the stated dated-record pattern), B4 (a container root's ignore file by name; a wildcard flagged)
- [x] 3.3 AUDIT: R14's set includes `<JOURNAL>/` and its `INDEX.md`; the cross-reference pass resolves a dated citation in the file or the directory
- [x] 3.4 whats-next: the journal row reads the live file (carried threads first); rolled files not swept

## 4. GREEN
- [x] 4.1 MAINTAIN, two on-disk reps with the candidate text and the scripts' path: rolled files under budget and byte-exact, `INDEX.md` present, the live file about half the budget, RO1 carried, RO2 not carried, RO3 resolving by grep, no reference doc edited by a rolled-file disposition, the report naming the watermark
- [x] 4.2 The probes of 2.2 with the candidate text; no-failure halves status-noted, not shipped

## 5. The reference tier and the record
- [x] 5.1 The design doc: three journal members (the stale "TWO members"); the rollover paragraph in the tier section; the frozen-file property under anti-staleness
- [x] 5.2 `ARCHITECTURE.md` (the scripts beside the maintain skill), `README.md` (one storefront sentence: a journal that outgrows one file rolls into a directory beside it), `VERIFICATION.md` if the variant changes the fixture recipe
- [x] 5.3 The dated results record `docs/2026-09-26 - journal-rollover-red-green.md`; ROADMAP: the item to Recently shipped; the NOTEBOOK entry of the day extended if the runs teach something new
- [x] 5.4 The maintain and whats-next specs' Purposes written (they read TBD)
- [x] 5.5 `openspec validate journal-rollover --strict`; archive with `--yes`, judged by its output text; `main` fast-forwarded; `deploy.sh`
