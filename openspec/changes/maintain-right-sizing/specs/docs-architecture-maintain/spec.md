# docs-architecture-maintain — delta: maintain-right-sizing

## ADDED Requirements

### Requirement: Trigger-based description, no periodic invitation
The MAINTAIN skill's frontmatter `description` SHALL state triggering conditions only and
SHALL NOT invite scheduled/periodic runs: the "periodic journal-health sweep" clause is
replaced by field-calibrated triggers (on the order of ten archived changes since the last
sweep, a subsystem rewrite, or the journal visibly ahead of the reference tier). Gated on a
probe-RED (agents under the current description recommending a sweep in a low-yield
situation); no workflow summary is added to the description.

#### Scenario: Low-yield situation does not trigger
- **WHEN** an agent with the new description considers "should maintain run?" two hours
  after the last sweep with one archived change since
- **THEN** it does not recommend running (no trigger matches), and cites what would
  trigger later

#### Scenario: Real trigger still fires
- **WHEN** ~10 changes have archived since the last sweep, or a subsystem rewrite landed,
  or the journal is visibly ahead
- **THEN** the description's triggers match and the skill is invoked as before

### Requirement: Required prune pass and net-delta accounting
Every MAINTAIN sweep SHALL run a dedicated prune pass — the ROADMAP's open/pending lists
checked for closed items (M4 class) and the journal for spent records (M3 class) — and the
dated maintain report SHALL carry a REQUIRED accounting slot: the prune/archive candidates
found, or the explicit statement that none were found, plus a one-line net reference-tier
delta for the run (what the sweep added to reference docs vs what it removed or struck).
No numeric graduation cap is imposed. Ships only for the halves whose synthetic RED
reproduces (planted PR cells; no-failure → status-note).

#### Scenario: Closed item in an open list is found
- **WHEN** a ROADMAP open/pending item's completion is visible in the journal or shipped
  history
- **THEN** the sweep's prune pass flags it prune-only and the report lists it

#### Scenario: Nothing to prune is stated, not silent
- **WHEN** a sweep finds no prune/archive candidates
- **THEN** the report says so explicitly in the accounting slot ("prune candidates: none
  found"), and states the net reference-tier delta

#### Scenario: Ratchet visible per run
- **WHEN** any sweep completes
- **THEN** the user can read from the report how much the reference tier grew vs shrank in
  that run
