# docs-architecture-audit — delta spec (fat-router-lean)

## ADDED Requirements

### Requirement: Router is placement-audited
An audit run SHALL treat the `CLAUDE.md` router as an in-scope placement subject: off-charter
reference content found in the router (glossary, contract/API prose, domain conventions,
how-it-works mechanics — anything that is not routing or a load-bearing gotcha) SHALL yield a
structural placement flag proposing a move to the charter-owning reference doc, in the same
family as the embedded-shipped-history flag (R25): one structural placement flag per block,
not per-fact placement flags. Unlike R25's journal-tier history, the block's content is
reference-tier: currency flags on stale claims inside it remain legitimate and orthogonal
(the two axes are judged separately). Routing lines and load-bearing gotchas SHALL NOT be
placement-flagged, regardless of router size.

#### Scenario: Off-charter router content is placement-flagged
- **WHEN** an audit worker reads a `CLAUDE.md` router embedding a glossary or contract prose
- **THEN** it emits a structural placement flag (move-to the charter-owning reference doc)
  identifying the off-charter block, rather than silently skipping it or emitting per-fact
  placement flags (currency flags on stale claims inside the block remain permitted)

#### Scenario: Routing and gotchas are not flagged
- **WHEN** an audit worker reads a router containing only routing entries and load-bearing
  gotchas
- **THEN** no placement flag is emitted for the router (no cry-wolf)
