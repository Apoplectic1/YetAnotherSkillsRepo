# docs-architecture-setup: delta for always-on-budget

## MODIFIED Requirements

### Requirement: Router lean on encounter
When a SETUP run encounters an existing `CLAUDE.md` router carrying off-charter reference
content, it SHALL relocate that content to the charter-owning reference doc(s) as a
content-preserving move (S1 semantics) in the same run — not leave it in place, and not merely
recommend a move. The trigger SHALL be a content test — is the passage reference content
(glossary, contract/API prose, domain conventions, how-it-works mechanics) rather than routing
or a load-bearing gotcha? — never a numeric size threshold. The router perf line (~40 KB) may be
cited as rationale only. Destination selection SHALL follow the charters (e.g. glossary and
CLI-abbreviation conventions → `DOMAIN.md`; subsystem mechanics → `ARCHITECTURE.md`), and each
move SHALL be reported in the run summary (what moved, from → to). Beside the content test, the
run SHALL apply a scope test to every item that loads at launch (the router, an always-on rule
file): an item stays always-on only if it passes breadth (every session launched here needs
it) and stability (it changes less often than the audit cadence); that test is what
"load-bearing" means. A block or line that fails SHALL move behind a one-line always-on
trigger to the home its need is keyed to: a path-scoped rule file (`.claude/rules/<name>.md`
with `paths:`) for a file-keyed need, a skill for an activity-keyed need, a reference-doc
section read by heading for prose; the router SHALL name a rule file it writes. The chain a
session loads SHALL be measurable by the audit skill's `chain_budget.py`; the number detects,
the test decides, and a router under budget still moves a block that fails.

#### Scenario: Fat router is leaned during setup
- **WHEN** a SETUP-guided agent runs on a fixture whose existing `CLAUDE.md` embeds a glossary
  and contract prose alongside valid routing
- **THEN** the glossary/contract content is moved intact to the charter-owning reference docs,
  the router retains routing + load-bearing gotchas (plus pointers where needed), no content is
  lost, and the run summary names each move

#### Scenario: Lean router is left alone
- **WHEN** a SETUP-guided agent runs on a fixture whose `CLAUDE.md` contains only routing and
  gotchas every session launched there needs (regardless of its byte size)
- **THEN** no router content is relocated and no lean action is reported

#### Scenario: A gotcha pack that fails breadth moves behind a trigger
- **WHEN** the router carries, beside its load-bearing gotchas, a pack of true gotchas that
  only sessions on one module or one activity need
- **THEN** the pack (its one-line guards included) moves to a path-scoped rule file naming
  those files, or to a skill, with one trigger line left in the router; the load-bearing
  gotchas stay; the plan cites the scope test, not the router's size
