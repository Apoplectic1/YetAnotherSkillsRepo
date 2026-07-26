# docs-architecture-audit — delta: code-bug-persistence

## ADDED Requirements

### Requirement: Report-only flags persist to the target project's tiers
The AUDIT skill's apply step SHALL persist report-only findings (`flag-code-bug`,
`revisit-plan`) to the target project's own doc tiers before the run ends: the full flags
with evidence in a dated `docs/YYYY-MM-DD-<skill>-report.md`, and one line per
adjudicated-surviving finding in ROADMAP § Open (deduplicated against existing open lines).
If adjudication is deferred, a single ROADMAP § Open line SHALL point at the unadjudicated
report instead. Persistence is disk-write only — the skill still never edits code and never
initiates fix work. Gated on RED→GREEN per the iron law: this requirement's skill text ships
only after a synthetic RED reproduces the loss on a non-derived fixture (no-failure →
status-note only).

#### Scenario: Bugs found, user adjudicates
- **WHEN** an AUDIT run produces `flag-code-bug` findings and the user adjudicates them as
  real
- **THEN** the apply step writes a dated `docs/` report carrying every report-only flag with
  its evidence, and adds one deduplicated line per surviving bug to the target project's
  ROADMAP § Open

#### Scenario: Bugs found, adjudication deferred
- **WHEN** an AUDIT run produces `flag-code-bug` findings and the user defers adjudication
- **THEN** the dated `docs/` report is still written, and ROADMAP § Open gains a single
  pointer line naming the unadjudicated report

#### Scenario: Re-run on the same project
- **WHEN** a later AUDIT run re-finds a defect already listed in the target ROADMAP § Open
- **THEN** no duplicate ROADMAP line is added (the existing line stands; the new report may
  cite it)
