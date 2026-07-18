# docs-architecture-setup — delta spec (fat-router-lean)

## ADDED Requirements

### Requirement: Router lean on encounter
When a SETUP run encounters an existing `CLAUDE.md` router carrying off-charter reference
content, it SHALL relocate that content to the charter-owning reference doc(s) as a
content-preserving move (S1 semantics) in the same run — not leave it in place, and not merely
recommend a move. The trigger SHALL be a content test — is the passage reference content
(glossary, contract/API prose, domain conventions, how-it-works mechanics) rather than routing
or a load-bearing gotcha? — never a numeric size threshold. The router perf line (~40 KB) may be
cited as rationale only. Destination selection SHALL follow the charters (e.g. glossary and
CLI-abbreviation conventions → `DOMAIN.md`; subsystem mechanics → `ARCHITECTURE.md`), and each
move SHALL be reported in the run summary (what moved, from → to).

#### Scenario: Fat router is leaned during setup
- **WHEN** a SETUP-guided agent runs on a fixture whose existing `CLAUDE.md` embeds a glossary
  and contract prose alongside valid routing
- **THEN** the glossary/contract content is moved intact to the charter-owning reference docs,
  the router retains routing + load-bearing gotchas (plus pointers where needed), no content is
  lost, and the run summary names each move

#### Scenario: Lean router is left alone
- **WHEN** a SETUP-guided agent runs on a fixture whose `CLAUDE.md` contains only routing and
  load-bearing gotchas (regardless of its byte size)
- **THEN** no router content is relocated and no lean action is reported
