# AUDIT scope from the routers: RED/GREEN record (2026-10-12)

Change `audit-scope-from-routers` (the ROADMAP's "Ancestor-router conventions" and "Scope
precedence; router-named specs", both from the HDL tree's audits of 2026-09-24 and
2026-09-26). Fixture: the reefstack container with the `audit-scope` overlay
(`harness/reefstack-fixture-variants/audit-scope/`; cells in `harness/catalog-reefstack.md`).
Method: single-agent audit reps (one round, report-only, R18 to R23 and R27 waived), Sonnet,
each on its own baselined copy; every copy byte-untouched afterward. About 0.7M tokens for
eight reps.

## Cells and results

| Cell | Plant | RED (current text) | GREEN (candidate) |
|---|---|---|---|
| AR1 | ReefDash router cites an "Alert palette" rule the root does not carry | 2/2 dangling (r1, r2) | not rerun |
| AR2 | root "UTC everywhere" vs `feed.py` naive local time, ARCHITECTURE agreeing | 2/2 `flag-code-bug` citing the root line | not rerun |
| AR3 | ARCHITECTURE restates the root's TOML rule | 2/2 `cross-ref+delete` | not rerun |
| AR4 | a valid pointer up (control) | 2/2 unflagged | not rerun |
| AR5 | DoseKeeper (router never points up): root UTC rule vs `doselog.py` | 2/2 `flag-code-bug` citing the root (r5, r6) | not rerun |
| AR6 | DoseKeeper: root TOML rule vs `settings.json` | 2/2 `flag-code-bug` | not rerun |
| SP1 | router-routed `docs/2026-07-01 - probe-wiring.md`, channels swapped vs code | 2/2 `fix-doc` (r3, r4) | 2/2 unchanged |
| SP2 | unrouted dated record with the old map (control) | 2/2 unflagged | 2/2 unflagged |
| SS1 | router-named `poll-loop` spec, "every 5 seconds" vs code, router, SCHEMA at 10 | **2/2 `flag-code-bug`** by R7's letter | **2/2 `spec-change`**, spec untouched, correcting change named |
| SS2 | unnamed `alert-webhook` spec (control) | 2/2 unflagged | 2/2 unflagged |

## What RED taught

- **The baseline already reads ancestor routers.** All six reps read the root `CLAUDE.md`;
  r5 and r6, on a router that never points up, read it "as an ancestor, auto-loaded",
  unprompted, and applied R7 across it. Every rep also listed "the skill does not say whether
  an ancestor router counts" among its uncertainties: right behavior, silent text, the
  no-failure pattern. Per the gate, status notes, not text; the candidate R29 is in the
  change's design record.
- **A fixture for an unprompted behavior needs a target that gives no prompt.** The first
  four reps ran on ReefDash, whose router points up twice (AR1, AR4); that alone could have
  led the reader into the parent. AR5 and AR6 were added on DoseKeeper to close that hole.
- **The spec half failed the same way twice.** Both PulseMonitor reps put the spec in scope
  (R13's router-named leaf), saw code, router and SCHEMA agree against it, and still went
  `flag-code-bug` because R7 says a violated contract makes the code the suspect; r3: "the
  schema action is single-valued, so 'spec needs an openspec change' rides in finding". The
  missing piece was an action, not scope.
- **R12 over R14 held without text** (SP1), with the same "the skill does not say" caveat.

## What GREEN taught

- `spec-change` lands cleanly: both reps named the correcting change (a MODIFIED delta on
  "Poll cadence") and kept the spec byte-identical. g2 quoted the new R13 clause back as its
  reason ("R7 holds only while the spec stands uncontradicted").
- New uncertainties, not acted on: the modality field has no value for a normative SHALL
  (both reps wrote "descriptive" with a note); a reference doc edited in place under a dated
  name will carry a stale date after its first edit (no rule covers whole-doc placement).

## Shipped

`spec-change` in R4, R13 and the flag schema; the audit spec's report-only requirement renamed
to three actions, R27's list extended, an ADDED requirement for router-named specs, and two
ADDED requirements with status notes (the router sets the tier; ancestor routers as
convention sources). The design doc's "OpenSpec = workflow-only" qualified.
