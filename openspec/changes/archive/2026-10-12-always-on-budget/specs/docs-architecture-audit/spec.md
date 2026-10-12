# docs-architecture-audit: delta for always-on-budget

## MODIFIED Requirements

### Requirement: Router is placement-audited
An audit run SHALL treat the `CLAUDE.md` router as an in-scope placement subject: off-charter
reference content found in the router (glossary, contract/API prose, domain conventions,
how-it-works mechanics — anything that is not routing or a load-bearing gotcha) SHALL yield a
structural placement flag proposing a move to the charter-owning reference doc, in the same
family as the embedded-shipped-history flag (R25): one structural placement flag per block,
not per-fact placement flags. Unlike R25's journal-tier history, the block's content is
reference-tier: currency flags on stale claims inside it remain legitimate and orthogonal
(the two axes are judged separately). Routing lines and load-bearing gotchas SHALL NOT be
placement-flagged on the content axis, regardless of router size; a gotcha block still meets
the scope test (the always-on chain requirement).

#### Scenario: Off-charter router content is placement-flagged
- **WHEN** an audit worker reads a `CLAUDE.md` router embedding a glossary or contract prose
- **THEN** it emits a structural placement flag (move-to the charter-owning reference doc)
  identifying the off-charter block, rather than silently skipping it or emitting per-fact
  placement flags (currency flags on stale claims inside the block remain permitted)

#### Scenario: Routing and gotchas are not flagged
- **WHEN** an audit worker reads a router containing only routing entries and gotchas every
  session launched there needs
- **THEN** no placement flag is emitted for the router (no cry-wolf)

## ADDED Requirements

### Requirement: The always-on chain is measured and router blocks pass breadth and stability
An audit run SHALL measure, with `chain_budget.py` beside the skill, what a session launched
in the audited directory loads before its first question (the owner's global file, every
ancestor router, the project's router and always-on rule files, the memory index) in bytes,
lines and estimated tokens against a budget stated as a share of the window (5 percent by
default, the router may state its own), and its coverage note SHALL carry the chain row. Each
block of the project's router and always-on rule files SHALL meet the scope test (breadth:
every session launched here needs it; stability: it changes less often than the audit
cadence); a failing block SHALL yield one placement flag `move-to` an on-demand home (a
path-scoped rule file, a skill, or a reference-doc section) with a trigger line left behind.
An ancestor's weight SHALL be reported in the row and never flagged in this run.

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
