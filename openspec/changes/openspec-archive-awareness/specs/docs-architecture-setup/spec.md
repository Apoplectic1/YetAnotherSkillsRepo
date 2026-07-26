# docs-architecture-setup Delta Specification

## ADDED Requirements

### Requirement: Router exclusion wording carves out archived openspec design docs
When SETUP writes the router's scope-exclusion note on a project carrying an `openspec/`
directory, the wording SHALL keep `openspec/` excluded from scaffolding while noting that
archived design docs (`openspec/changes/archive/*/design.md`) are historical records the
MAINTAIN sweep reads — so the router does not contradict maintain's source class or nudge a
maintain worker into skipping it. SETUP SHALL NOT scaffold into `openspec/` (the existing
hard exclusion stands), and SHALL NOT add archived design docs to the three-way journal
authoring split (they are tool-produced, never an authoring target).

#### Scenario: Router exclusion note carries the carve-out
- **WHEN** a SETUP-guided run writes or aligns the router of a project with an `openspec/`
  directory
- **THEN** the exclusion note marks `openspec/` excluded but identifies
  `changes/archive/*/design.md` as maintain-swept historical records, and no files are
  scaffolded inside `openspec/`

#### Scenario: No openspec, standard wording
- **WHEN** the target project has no `openspec/` directory
- **THEN** the router's exclusion wording is unchanged from current behavior (no speculative
  openspec clause)
