# Proposal: setup-tools-first

## Why

The SETUP skill text is 14.6 KB (3.6k tokens, 188 lines, 21 rules), and about half of it is
not the rules' actions: prose restating what the scripts beside it do (T5 is 2.9 KB, S8
3.4 KB), the preconditions of the shape rules written out for a reader to detect (B3 to B6,
A2, T1), rationale the design doc already holds, and clauses accreted one per RED failure.
A skill body loads whole on invocation, so every run pays all of it, and a rep reads a long
rule worse than a short one (the HDL pilot's reps quoted S8's middle and missed its ends).
The owner's direction (2026-10-12): remove the bloat, favoring tools over prose.

## What Changes

- **`survey.py` beside the skill:** one line per finding, the rule it keys at the end: the
  shapes (sub-project, container root, a design-slot candidate), the enforced set with each
  file's charter line, the router's line count and the chain row (through
  `chain_budget.py`), what the router names and which exclusions it notes, always-on rule
  files, journals past budget, reference docs past budget and their split state, shipped
  history embedded in ROADMAP, the ignore file's wildcard over nested repositories, the
  `docs/` naming forms, the git state. Detection only: the content tests stay the reader's.
- **SKILL.md rewritten to the actions:** each rule its action plus one boundary; a script's
  behavior left to the script's output; rationale to the design doc, which holds it; the
  procedure opens with the survey. About half the size.
- **A script-level check:** `survey.py`'s output on three fixture copies (the base TidePool,
  the reefstack root, the `s8-field` variant) byte-exact against `harness/survey-fixture/`.
- **A regression GREEN, not a RED:** the trimmed text claims nothing new, so it ships only
  when the representative cells still pass with it: one plan-only rep per fixture family
  (the base TidePool's t2, the reefstack root's PC1 to PC3, `near-budget`'s NB1 and NB2,
  `s8-field`'s SF1 to SF6, the `fat-chain` root's CR1), Sonnet at high through a Workflow.
  A cell that fails names the clause to restore.

## Capabilities

### Modified Capabilities
- `docs-architecture-setup`: the survey step is scripted (a new requirement); the rules'
  wording, no requirement changed.

## Impact

The deployed footer and the spec's requirements stand. AUDIT and MAINTAIN get the same
treatment in their own changes (`scope.py`, `report_check.py`).
