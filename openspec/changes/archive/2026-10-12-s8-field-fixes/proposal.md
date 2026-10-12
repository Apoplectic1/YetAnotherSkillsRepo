# Proposal: s8-field-fixes

## Why

The HDL pilot of 2026-10-12 (three plan-only SETUP reps on HlsLibrary, ArtyZ7 and the
AtmlBoards umbrella, with the deployed skills) found the always-on rule shipped that morning
wanting in the same places on all three repositories:

- **The budget cannot be met from inside a unit.** The owner's global file plus the ancestor
  routers weigh 11.1k tokens before the project's router counts; S8 says "the number detects,
  the test decides" and gives no instruction for a chain the project cannot bring under the
  line. Every rep said so.
- **A rule file loads on file touch, not on a command, and its `paths:` cannot reach a
  sibling repository.** A build, XMODEM or bench-NIC guard never fires in a session that only
  runs `MakeAll.bat`; the Arty's gotchas about HLS kernels in `../../../Library/` have no
  file in the repo to key on. S8 names a skill for an activity-keyed need, but B1 lets S8
  write only a rule file under `.claude/`, so two reps fell back to reference-doc sections.
- **S1 against S8 on duplicates.** A third of each router's gotchas already live in
  ARCHITECTURE, a README or an ancestor router; S8's "move" would make another copy. The
  reps asked for the cross-ref-and-delete S1 allows and S8 does not name.
- **An ancestor loads in every session beneath it**, and one rep believed the opposite (a
  board session never loads the umbrella router) and could not place board-keyed gotchas:
  the container-root breadth clause recorded as no-failure that morning has failed in the
  field.
- **Stability has no cadence**, and a status line that changes at release cadence (the
  Arty's halt, HlsLibrary's State block touched in 35 of 45 commits) is a judgment call the
  text does not help with.
- **Shapes the enforced set does not cover:** an umbrella with first-party content (not B4
  by the letter), a 70 KB `README.html` script guide, generated output under `docs/`, class
  READMEs that are the library's reference docs but not the enforced set.

## What Changes

- **SETUP S8**: the project tests what it controls; the ancestors' and the owner's shares
  are reported, not chased; the three homes become four with their load triggers stated (a
  rule file loads on a matching file's first touch, a skill on invocation, a section on a
  read, and an activity with no file and no skill keeps a one-line always-on guard); a block
  a reference doc or an ancestor already holds is cross-referenced and deleted, never moved;
  an ancestor's always-on content loads in every session beneath it, so a container root's
  breadth is every session launched at or below it; the stability cadence is the audit's;
  a status line that changes at release cadence is ROADMAP's.
- **SETUP B1**: S8 may write a skill under `.claude/skills/` as well as a rule file, each
  named by the router.
- **SETUP B4**: an umbrella with first-party content keeps the enforced set for what is its
  own and routes the children's as B3.
- **The enforced-set table**: a row for a project's own reference docs outside the set
  (class READMEs, a script guide), chartered and budgeted like T2.
- **AUDIT R30**: the same breadth reading for a container root.
- Fixtures: the reefstack `fat-chain` variant gains the command-only and sibling-keyed
  cells; a new TidePool `dup-router` variant for the duplicate case.

## Capabilities

### Modified Capabilities
- `docs-architecture-setup`: S8, B1, B4, the enforced set.
- `docs-architecture-audit`: R30's breadth at a container root.

## Impact

The HDL router leans wait on this change; the Arty's ARCHITECTURE split did not. Gated on
RED/GREEN on non-derived fixtures: the HDL tree derived every finding and is poisoned for
them.

## Outcome (2026-10-12)

RED on the `s8-field` variant and the reefstack `fat-chain` root failed the budget (3/3),
the command-keyed block (3/3) and the sibling's files (1/2); those ship, with B1's skill and
the stability wording. The duplicate rule, the status block, the halt bound, breadth beneath
a container root and the held-under-halt clause were no-failure and are status notes; B4 and
the enforced-set row wait for a cell. The `dup-router` variant was not built: the duplicate
case is a cell of the `s8-field` variant. Record:
`docs/2026-10-12 - s8-field-fixes-red-green.md`.
