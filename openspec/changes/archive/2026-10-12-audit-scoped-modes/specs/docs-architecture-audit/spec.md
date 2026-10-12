# docs-architecture-audit: delta for audit-scoped-modes

## ADDED Requirements

### Requirement: Scoped modes are the one sanctioned exception to loop-until-dry
The AUDIT skill SHALL offer two scoped modes that the user invokes and the run never chooses:
`release-close` (one lens over the reference tier for post-release phrasing, plus the
cross-reference pass) and `small-set` (one per-section round plus the cross-reference pass).
A scoped run SHALL be one round at the default worker tier with no loop and no model switch,
every other rule intact, and its coverage note SHALL name the mode and what a full run would
have added. Without a mode invoked, an audit SHALL run the full loop.

#### Scenario: A release just closed, the user asks for one cheap round
- **WHEN** the user asks for a cheap one-round audit at a release close
- **THEN** the run names `release-close`, lenses the reference tier for the phrases a
  release leaves behind, runs the cross-reference pass, stops after the one round, and its
  coverage note names the mode and the rounds and model switch not run

#### Scenario: A small set, one round only
- **WHEN** the user asks for one round and no model switch on a small, recently written set
- **THEN** the run names `small-set`, runs one per-section round plus the cross-reference
  pass at the default tier, stops, and its coverage note names the mode

#### Scenario: No mode invoked
- **WHEN** the user asks for an audit without naming a mode or asking for one round
- **THEN** the run loops until dry and switches worker model as before

#### Scenario: A real wait is not flagged
- **WHEN** a `release-close` lens meets "waits for" or "future" over something the code has
  not done
- **THEN** no currency flag is emitted for it
