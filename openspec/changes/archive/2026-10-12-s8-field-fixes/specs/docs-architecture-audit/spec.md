# docs-architecture-audit: delta for s8-field-fixes

## MODIFIED Requirements

### Requirement: The always-on chain is measured and router blocks pass breadth and stability
An audit run SHALL measure, with `chain_budget.py` beside the skill, what a session launched
in the audited directory loads before its first question (the owner's global file, every
ancestor router, the project's router and always-on rule files, the memory index) in bytes,
lines and estimated tokens against a budget stated as a share of the window (5 percent by
default, the router may state its own) and each file against its own line (200 lines, the
harness's guidance: the budget a unit can act on; the chain's share is met when every level
meets its own), and its coverage note SHALL carry the chain row. Each block of the project's
router and always-on rule files SHALL meet the scope test (breadth: every session launched
here needs it; stability: it changes less often than a release); a failing block SHALL yield
one placement flag `move-to` an on-demand home (a path-scoped rule file, a skill, or a
reference-doc section) with a trigger line left behind. An ancestor's weight SHALL be
reported in the row and never flagged in this run.

#### Scenario: A sub-project under a fat ancestor
- **WHEN** an audit runs from a sub-project whose own router is thin and whose ancestor router
  carries another sub-project's gotcha pack, the chain over budget
- **THEN** the coverage note carries the chain row naming the ancestor as the largest item and
  routing it to its own audit, and no placement flag is raised on the sub-project's router

#### Scenario: A container root carrying a sub-project's gotcha pack
- **WHEN** an audit runs at a container root whose router holds a pack of true gotchas that
  only one sub-project's sessions need
- **THEN** one placement flag per such block proposes `move-to` an on-demand home with a
  trigger line, while the root's routing table stays unflagged

#### Scenario: A router under budget still faces the test
- **WHEN** the chain is within budget and the router holds a block that fails breadth
- **THEN** the block is still flagged (the number detects, the test decides)

#### Scenario: A router over its own line under an unmeetable chain
- **WHEN** the owner's global file and the ancestors exceed the chain budget and the audited
  router is past 200 lines
- **THEN** the row says which files are over their own line and whose they are, and the
  scope test runs on the audited router's blocks regardless of the chain's verdict
