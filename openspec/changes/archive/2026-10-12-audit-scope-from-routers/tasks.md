# Tasks

## 1. The fixture
- [x] 1.1 `harness/reefstack-fixture-variants/audit-scope/`: root conventions, ReefDash (AR1 to AR4), PulseMonitor (SP1, SP2, SS1, SS2); catalog cells in `harness/catalog-reefstack.md`; `harness/README.md` names the variant
- [x] 1.2 After the first RED pass: DoseKeeper (AR5, AR6, the uncited case) added, catalog extended

## 2. RED
- [x] 2.1 Six single-agent reps on the current text (ReefDash 2, PulseMonitor 2, DoseKeeper 2): AR1 to AR6 and SP1 pass, SS1 fails 2/2, controls hold, copies untouched

## 3. The skill text
- [x] 3.1 AUDIT: `spec-change` in R4, R13 and the schema (the SS1 half)
- [x] 3.2 The candidate R29 and the R12 tier sentence held in the record, not shipped (D4)

## 4. GREEN
- [x] 4.1 Two reps on PulseMonitor with the candidate: SS1 → `spec-change`, the spec untouched, SP1 and the controls unchanged

## 5. The reference tier and the record
- [x] 5.1 The audit spec: the report-only requirement renamed to three actions, R27's list, an ADDED requirement for router-named specs, ADDED requirements with status notes for ancestor routers and router-routed docs
- [x] 5.2 The design doc: "OpenSpec = workflow-only" qualified; the provenance entry (the 2026-07-06 "exactly two" line is a dated record, left as written)
- [x] 5.3 `docs/2026-10-12 - audit-scope-red-green.md`; ROADMAP: both items to Recently shipped, the stale sub-bullet (c) dropped with them; NOTEBOOK entry
- [x] 5.4 `openspec validate audit-scope-from-routers --strict`; archive with `--yes`, judged by output text; `main` fast-forwarded; `deploy.sh`
