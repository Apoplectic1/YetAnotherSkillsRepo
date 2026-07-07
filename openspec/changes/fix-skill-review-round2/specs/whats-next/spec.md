# whats-next — delta (fix-skill-review-round2)

## ADDED Requirements

### Requirement: Audit-first is scoped, not unconditional
The audit-first guidance SHALL apply when the reference docs are stale or unaudited since the
last major change — not as an unconditional prerequisite to every triage. A whats-next run on
demonstrably current docs (fresh SETUP, recent audit, no intervening refactor) SHALL proceed
to the backlog, noting doc freshness in the coverage manifest instead of demanding an audit.

#### Scenario: Fresh docs proceed without an audit
- **WHEN** whats-next runs on a project whose reference docs were set up or audited recently
  with no major change since
- **THEN** the run produces its backlog + manifest (noting the docs' freshness) without
  performing or insisting on a prior audit

#### Scenario: Stale docs still get the audit-first call
- **WHEN** whats-next runs on a project with suspected doc drift (post-refactor, no recent
  audit)
- **THEN** the run recommends running docs-architecture-audit first (stale docs → stale
  backlog)
