# docs-architecture-setup — delta (fix-skill-review-round2)

## ADDED Requirements

### Requirement: Legacy-named domain doc is normalized into DOMAIN.md
On a project whose domain/strategy doc exists under a legacy or content-specific name (e.g.
`OBSERVING.md`, `UI-CONVENTIONS.md`, `PCL InterOp.md`) and no `DOMAIN.md` exists, SETUP SHALL
rename/merge that doc into `DOMAIN.md` (content-preserving, references updated). SETUP SHALL
NOT create a charter'd-thin `DOMAIN.md` alongside the legacy doc — two domain homes violate
single-source.

#### Scenario: OBSERVING.md is renamed, not duplicated
- **WHEN** a SETUP-guided run encounters a project with `OBSERVING.md` (real domain content)
  and no `DOMAIN.md`
- **THEN** the project ends with exactly one domain home, `DOMAIN.md`, carrying the legacy
  doc's content, and inbound references (router, other docs) point at `DOMAIN.md`

#### Scenario: An existing DOMAIN.md is never renamed away
- **WHEN** a project already has `DOMAIN.md`
- **THEN** SETUP keeps that name (no rename to a content-specific name), per the existing
  always-`DOMAIN.md` rule

### Requirement: Non-git targets get a recovery net before restructuring
When the target tree is not a git repository, SETUP SHALL establish a recovery net before any
restructuring apply (offer `git init` + an initial commit, or snapshot the originals) rather
than silently proceeding without one. A pure-scaffold run (creating new files only) MAY
proceed without a net.

#### Scenario: Restructure on a non-repo is preceded by a net
- **WHEN** a SETUP-guided run must merge/move existing docs in a tree with no `.git`
- **THEN** the run establishes (or explicitly offers) a recovery mechanism before applying,
  and says so in its report

#### Scenario: Pure scaffold proceeds
- **WHEN** the non-repo target has no existing docs to restructure
- **THEN** the run may scaffold without a net, noting the tree is unversioned

### Requirement: Container roots get a router only
When the survey finds no first-party project content at the invocation root — only
sub-projects (own router/`.git`) and tooling/scope-exclusions — SETUP SHALL scaffold a
router-only `CLAUDE.md` (charter + flag-and-skip routing to each sub-project + exclusions)
and SHALL NOT create the full enforced set at the container level.

#### Scenario: Portfolio root gets router-only
- **WHEN** a SETUP-guided run is invoked at a directory whose only members are two
  sub-projects and a tooling dir
- **THEN** the container receives `CLAUDE.md` only (routing + redirect notes), no
  ARCHITECTURE/ROADMAP/NOTEBOOK/VERIFICATION/DOMAIN at that level, and the report directs
  the user to run SETUP from each sub-project
