# whats-next Specification

## Purpose
TBD — created by syncing change `fix-skill-review-findings`. Covers only the requirements that
change established for the whats-next skill (`skills/whats-next/SKILL.md`); not a retroactive full
spec of the skill.
## Requirements
### Requirement: Ranking risk semantics are unambiguous
The ranking guidance SHALL define the risk term as exposure-if-deferred (the cost of NOT doing the
item — what it blocks or de-risks), which raises priority. Implementation riskiness alone SHALL NOT
raise an item's rank.

#### Scenario: Exposure ranks higher
- **WHEN** two actionable items have comparable value and effort and one carries higher
  exposure-if-deferred
- **THEN** that item ranks higher in the top-N

#### Scenario: Risky-to-implement is not promoted
- **WHEN** an item is merely risky to implement, with no exposure-if-deferred
- **THEN** that riskiness alone does not raise its rank

### Requirement: Description is trigger-scoped and states its assumption
The skill's frontmatter description SHALL contain triggering conditions only — no summary of the
skill's outputs or process (per the SDO rule: workflow-summarizing descriptions cause agents to act
from the description and skip the body) — and SHALL state that the skill assumes the
docs-architecture conventions, matching its sibling skills.

#### Scenario: Description passes the SDO check
- **WHEN** the frontmatter description is reviewed against the writing-skills SDO rule
- **THEN** it contains trigger phrases (e.g., "what should I work on next?", backlog
  prioritization) with no output/process summary, and names the conventions assumption

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

**Status note (2026-07-07):** satisfied by baseline behavior, not by skill text. RED 2/2 passed —
on a fresh-docs fixture both reps proceeded straight to backlog + manifest without demanding or
performing an audit, recording the absent audit output as an honest manifest row. The feared
unconditional-precondition reading did not occur. Per the no-failure gate the When-to-use text
was not changed; if a future run blocks on or performs an unneeded audit, encode then. Record:
design doc, review-round-2 RED/GREEN entry.

