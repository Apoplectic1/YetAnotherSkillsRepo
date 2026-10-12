# harness/ — RED/GREEN fixture sources

**Charter:** version-controlled sources for the skill-testing harness (`VERIFICATION.md`
holds the method contract). Everything under here is **test content, not project docs** —
the fixture's CLAUDE.md/ARCHITECTURE/ROADMAP describe a fictional project (TidePool) and
must never be audited, graduated, or edited as if they were this repo's docs.

## Contents
- `tidepool-fixture/` — the round-3 synthetic fixture: a fictional NOAA tide-window planner
  CLI, docs-conformant, with **cataloged planted defects** (embedded ROADMAP shipped-history
  D1–D3 per-entry drift, D4 live-section control, D5 clean control) plus **verified genuine
  drift** that accrued by accident and was kept deliberately (dead cache subsystem, DOMAIN
  daylight-contract violation, Gulf-coast plan contradiction, Atlantic-pilot cross-record
  conflict, CLI-smoke install gap). Provenance + scoring expectations:
  `docs/2026-07-13-round3-red-green-results.md`. Extended 2026-07-26 with a planted
  `openspec/changes/archive/` (O1–O4 in the catalog) for the archive-awareness runs, and
  again 2026-07-26 with the code-bug plants (CB1–CB4: journal-contract-vs-code regression,
  no-contract drift control, persistence/dedup cells) for the code-bug-persistence runs.
  Since 2026-09-24 it also carries the generated OpenSpec tooling (`.claude/` opsx set,
  `openspec/config.yaml`), kept current by the machine-wide opsx sync; not a plant (catalog:
  OpenSpec tooling baseline).
- `tidepool-fixture-variants/big-journal/` (2026-09-26, `journal-rollover`): a 57 KB
  newest-first bullet NOTEBOOK (the base's entries verbatim above 168 generated ones) and an
  ARCHITECTURE citation into an old entry; overlay it on a fixture copy, then baseline. Cells
  RO1 to RO5 in the catalog; `fat-arch/` is the earlier variant (`m9-hold-on-bloat`).
- `tidepool-fixture-variants/fat-topics/` (2026-10-12, `reference-doc-split`): a 40 KB
  ARCHITECTURE of eighteen true-to-code mechanics topics, the split's target; `fat-arch/`
  (rationale bloat) is its control, which must extract, never split. Cells SD1 to SD5 in the
  catalog. `split-fixture/index.expected.md` is what the setup skill's `split_doc.py` must
  leave as the index when applied to that doc with `--today 2026-10-12` (the parts are the
  doc's own sections and reconstruct it byte for byte).
- `tidepool-fixture-variants/fat-gotchas/` (2026-10-12, `always-on-budget`): the router with a
  6.6 KB pack of true, `tides.py`-only gotchas beside its three load-bearing ones: content
  passes, breadth fails. Cells ST1 to ST3 in the catalog. Its container twin is
  `reefstack-fixture-variants/fat-chain/` (a root router carrying one sub-project's gotcha
  pack and a glossary; cells CH1, CH2, SC1 to SC3 in `catalog-reefstack.md`).
- `chain-fixture/` (2026-10-12, `always-on-budget`): `gen_chain_fixture.py` writes a
  three-level tree of instruction files with exact sizes into a scratch directory, and
  `chain.expected.txt` is what the audit skill's `chain_budget.py` must print for its leaf
  (`--root . --global global.md --memory none`), byte for byte. A script-level check.
- `tidepool-fixture-variants/release-lens/` (2026-10-12, `audit-scoped-modes`): the four
  reference docs with post-release phrasings the code has moved past ("waits for", "not
  yet", "until", "today", a version, a count) beside three where the wait is real; overlay
  on a fixture copy, then baseline. Cells RL1 to RL6, RC1 to RC3, SM1, SM2 in the catalog.
- `journal-index-fixture/` (2026-10-12, `rolled-index-titled-entries`): one rolled TidePool
  NOTEBOOK file in the bare-date form (`## 2026-10-01` over bold-lead bullets) and the
  `INDEX.expected.md` the maintain skill's `journal_index.py` must reproduce byte for byte
  from a copy of its `NOTEBOOK/`. A script-level check, no subagent run.
- `catalog-tidepool.md` — the ground-truth catalog (planted items, expected RED/GREEN
  dispositions, must-nots). **Never place a copy inside the fixture tree** and never hand
  its path to a test agent — poisoned-fixture rule.
- `reefstack-fixture/` + `catalog-reefstack.md` — portfolio *container* fixture (added
  2026-07-26 for `b4-portfolio-domain`): fictional reef-tank automation portfolio — root
  router with planted cross-repo contract prose, three routered sub-projects, an owned
  contract (`PulseMonitor/SCHEMA.md`), a planted mutual-pointer glossary loop, and a
  portfolio-level journal truth. Same copy/baseline/reset recipe.
- `reefstack-fixture-variants/audit-scope/` (2026-10-12, `audit-scope-from-routers`): an
  overlay on the reefstack copy for AUDIT scope cells: root conventions for every repo
  beneath (cited by ReefDash's router, uncited by DoseKeeper's), violated in code; a dangling
  upward pointer; a restated rule; a router-routed dated `docs/` reference doc with drift
  beside an unrouted dated record; a router-named spec with a false SHALL beside an unnamed
  one. Cells AR1 to AR6, SP1, SP2, SS1, SS2 in `catalog-reefstack.md`.

## Using the fixture (per test run)
1. Copy `tidepool-fixture/` to a scratch location (session scratchpad), one copy per rep.
2. In each copy: `git init && git add -A && git commit -m "=== SKILLS-TEST BASELINE ==="`.
3. Run the test agent against the copy (candidate SKILL text injected in the prompt — the
   live Skill tool only ever sees the deployed copy; see `VERIFICATION.md`).
4. Score against the catalog, **disk-verifying every claim**; after any mutating run apply
   the reset contract: `git reset --hard <baseline> && git clean -fd` (inside the copy only).

## Caveats
- **Derivation status:** TidePool validated the round-3 CHANGELOG deltas (R25/A2′). It stays
  a fair fixture for *other* rule changes, but any future rule **derived from TidePool
  findings** poisons it for validating that rule — build a fresh fixture then (the
  non-derived rule, `VERIFICATION.md`).
- `pytest` must be importable in the test environment (fixture suite: 5 tests, pure math,
  no network/astral needed). `.gitignore` here covers `__pycache__` — the round-3 lesson.
- FermCtl (AUDIT-general) and TrailKit (SETUP-general) fixtures from arms 1–2 died with the
  Cowork container; recreate from the arm-1/arm-2 results docs' Method sections if needed.
- `tidepool-fixture-variants/near-budget/` (2026-10-12, `split-doc-field-fixes`): a 38 KB
  ARCHITECTURE and a router carrying a 4 KB mechanics block S7 moves into it, so the run's
  own move pushes the doc past the budget. Cells NB1 to NB4 in the catalog;
  `split-fixture/dryrun.expected.txt` is the dry run's output on the fat-topics doc (its
  dated heading flagged, its stale lines listed).
- `tidepool-fixture-variants/s8-field/` (2026-10-12, `s8-field-fixes`): `build_variant.py`
  composes a router past 200 lines with the four shapes the HDL pilot found S8 silent on
  (a command-keyed block, sibling-repository gotchas, a duplicated module map, a State
  block), a ROADMAP halt and a halted graduate. Cells SF1 to SF6, SM1, CR1 in the catalog.
