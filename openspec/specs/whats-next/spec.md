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
