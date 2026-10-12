# docs-architecture-setup: delta for s8-field-fixes

## MODIFIED Requirements

### Requirement: Router lean on encounter
When a SETUP run encounters an existing `CLAUDE.md` router carrying off-charter reference
content, it SHALL relocate that content to the charter-owning reference doc(s) as a
content-preserving move (S1 semantics) in the same run, not leave it in place and not merely
recommend a move. The trigger SHALL be a content test (is the passage reference content,
glossary, contract/API prose, domain conventions, how-it-works mechanics, rather than routing
or a load-bearing gotcha?), never a numeric size threshold. The router perf line (~40 KB) may be
cited as rationale only. Destination selection SHALL follow the charters (e.g. glossary and
CLI-abbreviation conventions → `DOMAIN.md`; subsystem mechanics → `ARCHITECTURE.md`), and each
move SHALL be reported in the run summary (what moved, from → to). Beside the content test, the
run SHALL apply a scope test to every item that loads at launch (the router, an always-on rule
file): an item stays always-on only if it passes breadth (every session launched here needs
it) and stability (it changes less often than a release); that test is what "load-bearing"
means. A block or line that fails SHALL move behind a one-line always-on trigger to the home
its need is keyed to, each home with its own load trigger: a path-scoped rule file
(`.claude/rules/<name>.md` with `paths:`, loaded on a matching file's first touch, for files in
this repository only), a skill (`.claude/skills/<name>/SKILL.md`, loaded on invocation, for an
activity), a reference-doc section read by heading for prose; a guard keyed to neither keeps
one router line. The router SHALL name every rule file and skill it writes. Every file that
loads at launch SHALL be tested against its own line (200 lines, the harness's guidance); the
chain a session loads SHALL be measured by the audit skill's `chain_budget.py`, the ancestors'
and the owner's shares reported and never chased from below; the number detects, the test
decides, and a router under its line still moves a block that fails.

**Status note (2026-10-12):** four clauses drafted from the HDL pilot were RED no-failure on
the TidePool `s8-field` and reefstack `fat-chain` variants and are not skill text: a block a
reference doc already holds is dropped with a cross-reference (both reps deleted the
duplicated module map as S1's merge); a status block at release cadence goes to ROADMAP (both
reps sent "State" there for failing stability); a halt the ROADMAP states bounds the plan to
docs-only moves (the rep read the halt and said so); breadth at a container root counts the
sessions beneath it (the root rep counted them: "every session under the container pays").
The field case for the last (the AtmlBoards rep of the pilot, which believed a board session
never loads the umbrella router) stands as the evidence that a run can misread it; if one
does again on a non-derived fixture, encode it then. The umbrella-with-first-party-content
shape (B4) and a project's reference docs outside the enforced set were not probed; they wait
for a cell.

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

#### Scenario: A guard keyed to a command, not a file
- **WHEN** the router carries a block of gotchas about a build or a bench procedure that no
  file in the repository keys
- **THEN** the plan moves it to a skill or keeps a one-line guard, never to a path-scoped
  rule file, and says why

#### Scenario: A guard about a sibling repository's files
- **WHEN** the router carries gotchas about files in a sibling repository
- **THEN** the plan does not key a rule file to globs for files this repository lacks; it
  moves the block to a reference-doc section or keeps a one-line guard, and says why

#### Scenario: The chain cannot be met from here
- **WHEN** the owner's global file and the ancestor routers exceed the chain budget before the
  project's router counts
- **THEN** the plan tests the router against its own 200 lines, reports the ancestors' and
  the owner's shares as theirs, and does not propose chasing the chain from below

#### Scenario: A block a reference doc already holds
- **WHEN** the router carries a block that ARCHITECTURE, a README or an ancestor router
  already holds
- **THEN** the plan cross-references it and drops the copy rather than moving it

#### Scenario: A halt bounds the plan
- **WHEN** the project's ROADMAP states a halt or freeze
- **THEN** the plan proposes docs-only moves and says the halt bounds it
