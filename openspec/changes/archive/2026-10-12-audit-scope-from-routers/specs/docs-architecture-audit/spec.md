# docs-architecture-audit: delta for audit-scope-from-routers

## RENAMED Requirements
- FROM: `### Requirement: Single action vocabulary; report-only is exactly two actions`
- TO: `### Requirement: Single action vocabulary; report-only is exactly three actions`

## MODIFIED Requirements

### Requirement: Single action vocabulary; report-only is exactly three actions
The skill SHALL use one action vocabulary — the flag schema's — in every section, including the
adjudication step. `graduate` SHALL be an apply-able doc edit after adjudication. The term
"report-only" (handed off, never auto-applied) SHALL apply to exactly `flag-code-bug`,
`revisit-plan` and `spec-change`.

#### Scenario: Approved graduate is applied
- **WHEN** a prescriptive plan item is already satisfied by code and adjudication approves the
  `graduate` flag
- **THEN** the apply step performs the doc edit (move to "Recently shipped" / archive the plan)

#### Scenario: Report-only flags are handed off
- **WHEN** a flag's action is `flag-code-bug`, `revisit-plan` or `spec-change`
- **THEN** it is reported and routed onward, never applied by the audit run

### Requirement: Report-only flags persist to the target project's tiers
The AUDIT skill's apply step SHALL persist report-only findings (`flag-code-bug`,
`revisit-plan`, `spec-change`) to the target project's own doc tiers before the run ends: the
full flags with evidence in a dated `docs/YYYY-MM-DD-<skill>-report.md`, and one line per
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

## ADDED Requirements

### Requirement: A router-named spec is currency-audited and never edited
A spec under `openspec/specs/` that the project's router names as its rules SHALL be in the
currency audit's scope as reference-tier, and SHALL never be edited by the audit: a claim the
spec makes that the code, the router and the reference docs agree is wrong SHALL be flagged
with the report-only action `spec-change`, naming the change that would correct it, and R7's
code-is-suspect reading SHALL apply only while the spec stands uncontradicted. A spec the
router does not name stays excluded as tooling (R13). RED 2/2 on the reefstack `audit-scope`
variant (SS1): the stale SHALL went out as `flag-code-bug` by R7's letter, the reps naming
the missing action.

#### Scenario: A router-named spec's stale SHALL
- **WHEN** a router-named spec says the poll loop writes every 5 seconds, and the code, the
  router and the schema doc all say 10
- **THEN** the merged list carries one currency flag on the spec with action `spec-change`,
  the spec file is byte-identical after the run, and no `flag-code-bug` is raised against
  the code for that claim

#### Scenario: An unnamed spec stays out
- **WHEN** `openspec/specs/` holds a spec the router does not name, for unbuilt work
- **THEN** no flag is emitted for it

### Requirement: The router sets the tier, not the directory or the name
A doc the router routes as current truth SHALL be audited as reference-tier wherever it
sits, a dated filename in `docs/` included; R14's journal exclusion SHALL cover only what the
router does not route that way. The name cannot be the test: a project that dates every new
`docs/` file dates its reference docs too.

**Status note (2026-10-12):** satisfied by baseline behavior, not by skill text. RED 2/2 on
the reefstack `audit-scope` variant (SP1, a router-routed `docs/2026-07-01 - probe-wiring.md`
with a drifted channel map beside an unrouted dated record): both reps audited the routed
doc under R12 and R2 and left the record out under R14, while listing "the skill does not
say how to resolve a dated-name reference doc in `docs/`". Per the no-failure gate the audit
text was not changed; the candidate sentence for R12 is held in the change's design record.
If a future run skips a routed doc for its directory or its date, encode it then.

#### Scenario: A routed dated reference doc is audited
- **WHEN** the router routes `docs/<date> - <name>.md` as current truth, edited in place, and
  a value in it has drifted from code
- **THEN** a currency flag is emitted for it as for any reference doc

#### Scenario: An unrouted dated record is not
- **WHEN** a dated record in `docs/` carries the same old value and the router routes `docs/`
  only as journal
- **THEN** no currency flag is emitted for it

### Requirement: Ancestor routers are convention sources
Every `CLAUDE.md` above the audited project's root (each loads in every session launched
there) SHALL be read as a convention source and never edited: the cross-reference pass SHALL
resolve each upward pointer against the ancestor's current text, a convention the ancestor
scopes to the repositories beneath it SHALL be checked as a contract (code violating it →
`flag-code-bug` citing the ancestor line, R7; a repo doc agreeing with that code is not
evidence against the convention), and a repo doc restating an ancestor's rule SHALL be a
placement flag `cross-ref+delete`. The ancestor's own defects belong to its own audit (R16).

**Status note (2026-10-12):** satisfied by baseline behavior, not by skill text. RED 6/6 on
the reefstack `audit-scope` variant: on ReefDash (whose router points up twice) both reps
resolved the dangling "Alert palette" pointer, raised `flag-code-bug` for naive local time
against the root's UTC rule, and `cross-ref+delete` for the restated TOML rule (AR1 to AR3),
leaving the valid pointer alone (AR4); on DoseKeeper (whose router never points up) both
reps read the parent "as an ancestor, auto-loaded" unprompted and raised `flag-code-bug` for
both violated conventions (AR5, AR6). Every rep listed "the skill does not say whether an
ancestor router counts" among its uncertainties. Per the no-failure gate no R29 was added;
the candidate text is held in the change's design record. The field case (the ATML audit,
2026-09-24, a Sonnet fan-out over a 27 KB router) remains the evidence that a real run can
miss it; if one does again, encode it then.

#### Scenario: An uncited ancestor convention is checked
- **WHEN** an ancestor router states a convention for every repository beneath it, the
  audited repo's router never cites it, and the repo's code violates it with its doc agreeing
- **THEN** a `flag-code-bug` is raised citing the ancestor line, and the doc is not fixed
  toward the code

#### Scenario: A pointer to a rule the ancestor no longer carries
- **WHEN** the audited repo's router cites a named rule in an ancestor's section and that
  section does not hold it
- **THEN** the cross-reference pass reports the pointer as dangling

#### Scenario: A restated ancestor rule
- **WHEN** a repo reference doc restates, unattributed, a rule the ancestor router carries
- **THEN** one placement flag proposes `cross-ref+delete`
