# setup-tools-first: regression record (2026-10-12)

**Charter:** the dated record of the regression that gated the SETUP trim: what ran, what
each family's cells showed with the trimmed text, what did not fire, and what the reps
named. The design is `openspec/changes/archive/2026-10-12-setup-tools-first/design.md`; the
standing truth is the design doc's "Tools over prose" part and SETUP's text.

## The gate

A trim claims nothing new, so it earns no RED. It ships when the representative cells still
pass with the trimmed text: one plan-only rep per fixture family, Sonnet at high, through
one Workflow (five reps, 355k tokens, 113 s). The text under test: SETUP at 10.4 KB and 143
lines (from 14.6 KB and 188), each rule its action plus one boundary, the procedure opening
with `survey.py` beside it (the survey's own check: byte-exact output on three baselined
fixture copies, `harness/survey-fixture/`). The orchestrator-context leak is disclosed as
always: the owner's global rules reached the reps (one named "A2's em dashes conflict with
the user's no-em-dash rule").

## The families

| Rep | Fixture | Cells | Result |
|---|---|---|---|
| tp | the base TidePool | t2 | PASS. `CHANGELOG.md` created, charter'd, the nine entries verbatim and newest first; ROADMAP keeps a five-line digest and a pointer; the router's journal line teaches the three-way split; nothing clobbered (`openspec/`, `.claude/` untouched); the diff shown before the commit (S2). Beyond the cells: B1 (`.claude/` noted, the archived design docs marked), the three gotchas to one rule file `src-invariants.md` with a trigger line (breadth judged failing on a five-file project; the datum guard went too, which the morning's reps kept). |
| rs | the reefstack root | PC1 to PC3, L1 | PASS. A portfolio `DOMAIN.md` chartered cross-repo truth only (the cross-store disambiguation, the shared terms with the salinity event copied exactly from the ReefDash entry, `readings.db` by pointer to `PulseMonitor/SCHEMA.md`); the schema prose dropped as the owner's, a one-line single-writer guard kept; no set scaffolded at the root, the thin ROADMAP kept with one status line; the mutual DOMAIN pointers noticed and reported for each sub-project's own run (credit). |
| nb | `near-budget` | NB1, NB2 | NB1 PASS: the 3.8 KB mechanics block leaves the router for ARCHITECTURE's sections (S7). NB2 not exercised: the rep checked the block fact by fact against the 37 KB doc, found one fact missing, merged that (0.3 KB) and stayed under the budget, applying T5's same-run clause to its own smaller move ("37.4 KB, so T5 is not triggered"). The earlier RED reps on this variant moved the block as text and split. The variant's block restates the doc's own topics, so a fact-level merge is an S1 merge the fixture permits; a block the doc does not already cover would make the cell bite. |
| sf | `s8-field` | SF1 to SF6, ST | PASS. The owner's share reported as the owner's, this project's 3,498 the only part chased; the build-and-bench block and the bench network to one skill with a trigger line naming the `make` targets; the harmonics core to an ARCHITECTURE section with a trigger line ("S8 bars a path-scoped rule for a sibling's files"); the module-map copy dropped as identical; State to ROADMAP's Now/Next for failing stability; the halt read ("every proposed change is docs or tooling files"); the CO-OPS pack to two rule files with `paths:`; the rate-limit guard and the datum guard kept as router lines. The same shape the morning's GREEN rep produced from 14.6 KB. |
| fc | the `fat-chain` root | CR1 | PASS. The calibration and pump packs fail breadth as the activities' gotchas and move to two root skills with trigger lines; the vocabulary to a portfolio DOMAIN; the data contracts split into one-line guards plus DOMAIN pointers; the root's part (3,850 tokens) the only part chased; the sub-projects flagged for their own runs. |

## What the reps named (none a failure of a cell)

- S5 against B4 at a container root (both root reps): S5 says create NOTEBOOK and
  VERIFICATION, B4 says never at a container; both followed B4 "because the survey does".
  The survey's line resolves it; the text stays as it is.
- A gotcha a test could enforce has no home among a rule file, a skill and a section (nb):
  "a test would beat any rule file, but the skill can't propose one." Noted as an idea for
  S8's homes, not text.
- A move leaves referrers stale (nb: ARCHITECTURE's "the router warns"); the rep added the
  step itself.
- Whether `.claude/skills/` at an ancestor root loads for a session launched in a
  sub-project (fc): a harness fact the text does not state and the rep could not verify.
- The five-line digest's composition, `paths:` syntax, the README/RELEASING test, breadth
  on a tiny project: judgment calls, as before the trim.

## Verdict

Four families clean, one cell not exercised by its fixture, no clause restored. The trim
ships at 10.4 KB. The cost of the gate: 355k tokens, against the 14.6 KB every future SETUP
run would otherwise have loaded.
