# Tasks

## 1. The tool
- [x] 1.1 `skills/docs-architecture-audit/scope.py`: the scope with its rules, the ancestors, the cold docs cited, the structural findings, the chain row with the largest items, the cross-reference seed (a bare filename resolves anywhere in the tree; a path that does not names where its basename lives, or that it is a sibling's under the ancestor), `--lens release`; run on this repo as well as the fixtures
- [x] 1.2 `harness/scope-fixture/`: expected outputs on the base TidePool, `audit-scope` from `PulseMonitor/`, the `fat-chain` root, byte-exact on fresh baselined copies; `VERIFICATION.md` names the check; `harness/README.md`; `ARCHITECTURE.md` names the script

## 2. The text
- [x] 2.1 SKILL.md rewritten: each rule to its action plus one boundary; R30 and R29 keyed to the script; the procedure opens with it; rationale out: 13.4 KB, 182 lines to 10.2 KB, 149 lines after R29's sentence came back (candidate in scratch until the regression passed)

## 3. The regression GREEN
- [x] 3.1 Five report-only reps, Sonnet/high, one Workflow (344k tokens): base TidePool (t1, O1, CB1, CB4, DV2), `audit-scope` from `PulseMonitor/` (SS1, SS2, SP1, SP2), `fat-chain` root (SC1 to SC3), `fat-chain` from `ReefDash/` (CH1, CH2), `release-lens` (RL1 to RL6, RC1 to RC3) all held; SM2 failed (the mode not named) on R29's cut sentence, restored and re-run (one rep); the PulseMonitor rep's finding on the script (a spaced dated name) fixed

## 4. The reference tier and the record
- [x] 4.1 The audit spec: ADDED "The scope step is scripted"; the design doc's "Tools over prose" part gains the AUDIT sentence; the design's D6 names the restored clause
- [x] 4.2 `docs/2026-10-12 - audit-tools-first-regression.md`; ROADMAP (the item shipped, MAINTAIN's follow-on narrowed), CHANGELOG, NOTEBOOK
- [x] 4.3 validate (the requirement text under the validator's 500-character line, the scope's lines in a scenario), archive `--yes` judged by output text, `main` fast-forwarded, `deploy.sh`, the live scope run on this repo
