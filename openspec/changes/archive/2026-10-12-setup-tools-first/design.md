# setup-tools-first: design

## Context

By the evening of 2026-10-12 the SETUP skill had taken eight changes in a day and stood at
14.6 KB. The field loop (RED on a non-derived fixture, GREEN with the candidate, the HDL
pilot on real repositories) was finding fewer failures per run: reps already did the right
thing in most cells, and the text added per failure was growing faster than the failures.
The owner's call: stop adding rules, remove the bloat, favor tools over prose.

## Decisions

- **D1: detection moves to a script, judgment stays in prose.** `survey.py` prints what a
  rule keys on, one line per finding with the rule at the end; the rule says what to do.
  The scope test (S8), the content test (S7) and a charter's honesty (S5) are a reader's
  calls and stay in the text. The survey reports a container root, a sub-project, a
  design-slot candidate, a missing or uncharter'd file, a router over its line, an
  always-on rule file, an unnoted exclusion, a journal or reference doc past its budget, a
  split whose index is stale, shipped history embedded in ROADMAP, a wildcard ignore over
  nested repositories, two naming forms in `docs/`, an unversioned or dirty tree.
- **D2: a rule is its action plus one boundary.** Mechanism stays where a rep acts on it
  (S8's homes with their load triggers); rationale goes to the design doc (already there,
  rule by rule); provenance stays in the footer's link. The italic parentheticals go.
- **D3: a script describes itself.** T5 names `split_doc.py` and its switches; what the
  dry run lists is the dry run's to say. T1 names `rollover.py`, S8 names
  `chain_budget.py` through the survey's chain row.
- **D4: the regression gate.** Trimming claims nothing new, so it earns no RED; it ships when
  the representative cells still pass with the trimmed text, one plan-only rep per fixture
  family. A cell that fails names the clause restored, in the shortest form that passes.
- **D5: the survey reads `chain_budget.py` across skills,** found beside the audit skill
  relative to its own location (the deploy puts the four skills side by side); absent, it
  prints the command to run.

## Verification

Script-level: `survey.py` byte-exact on three fresh baselined fixture copies (the base
TidePool, the reefstack root, the `s8-field` variant). The regression GREEN per D4: five
plan-only reps, Sonnet at high, 355k tokens; t2, PC1 to PC3, NB1, SF1 to SF6 and CR1 held;
NB2 not exercised (the rep merged the block by fact and stayed under budget, a merge the
fixture permits); no clause restored. The record:
`docs/2026-10-12 - setup-tools-first-regression.md`.
