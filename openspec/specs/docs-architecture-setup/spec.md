# docs-architecture-setup Specification

## Purpose
TBD — created by syncing change `fix-skill-review-findings`. Covers only the requirements that
change established for the SETUP skill (`skills/docs-architecture-setup/SKILL.md`); not a
retroactive full spec of the skill.
## Requirements
### Requirement: Sub-project flag-and-skip
A SETUP run at a root project SHALL NOT scaffold into, restructure, or edit the docs of a nested
sub-project — detected by the sub-project having its own CLAUDE.md router or its own `.git`. On
encountering one, the run SHALL flag it (reporting its path and any unconventional doc names) and
direct the user to run SETUP from the sub-project's own directory. The skill's "coexist, never
clobber / augment" rule SHALL be scoped to the root project's own files so it cannot be read as
license to augment a sub-project's CLAUDE.md.

#### Scenario: Nested own-git project is skipped
- **WHEN** a SETUP-guided agent runs on a fixture whose tree contains a nested directory with its
  own `.git` and `CLAUDE.md`
- **THEN** no files are created or modified inside that directory, its CLAUDE.md is not augmented,
  and the run's report names it with run-from-its-own-dir advice

#### Scenario: Root scaffolding is unaffected
- **WHEN** the same run completes
- **THEN** the root project still receives the full enforced doc set, charter-guarded

### Requirement: Design-heavy code-light projects keep their design doc whole
When a project has minimal code but a large standalone design document, SETUP SHALL treat that
document as the project's `DESIGN.md` slot — chartered and routed, preserved whole as the seed that
graduates into ARCHITECTURE/ROADMAP as code lands. SETUP SHALL NOT force-split such a document into
the enforced set; ARCHITECTURE/ROADMAP remain charter'd-thin alongside it.

#### Scenario: Large design doc is preserved
- **WHEN** a SETUP-guided agent runs on a fixture with only a few code files and one large design
  document
- **THEN** the design document's content is not split or moved, it is chartered/routed as the
  design slot, and ARCHITECTURE/ROADMAP are created charter'd-thin referencing it

### Requirement: Reference tier includes VERIFICATION
The tier conventions SETUP teaches (and writes into the target project's CLAUDE.md) SHALL list the
reference tier as ARCHITECTURE, ROADMAP, the domain doc, and VERIFICATION.

#### Scenario: Tier teaching names VERIFICATION
- **WHEN** SETUP writes the router's tier conventions
- **THEN** VERIFICATION.md is classified in the reference tier alongside ARCHITECTURE/ROADMAP/domain

### Requirement: Legacy-named domain doc is normalized into DOMAIN.md
SETUP SHALL rename/merge a domain/strategy doc that exists under a legacy or content-specific
name (e.g. `OBSERVING.md`, `UI-CONVENTIONS.md`, `PCL InterOp.md`, with no `DOMAIN.md` present)
into `DOMAIN.md` — content-preserving, references updated. SETUP SHALL NOT create a
charter'd-thin `DOMAIN.md` alongside the legacy doc — two domain homes violate single-source.

#### Scenario: OBSERVING.md is renamed, not duplicated
- **WHEN** a SETUP-guided run encounters a project with `OBSERVING.md` (real domain content)
  and no `DOMAIN.md`
- **THEN** the project ends with exactly one domain home, `DOMAIN.md`, carrying the legacy
  doc's content, and inbound references (router, other docs) point at `DOMAIN.md`

#### Scenario: An existing DOMAIN.md is never renamed away
- **WHEN** a project already has `DOMAIN.md`
- **THEN** SETUP keeps that name (no rename to a content-specific name), per the existing
  always-`DOMAIN.md` rule

**Status note (2026-07-07):** satisfied by baseline behavior, not by skill text. RED 2/2 passed —
both reps `git mv`'d `OBSERVING.md` → `DOMAIN.md` (content preserved, router updated, zero
duplicate homes; disk-verified). The existing "whatever the content is, it lives in DOMAIN.md" +
filename-normalization lines already induce the rename. Per the no-failure gate no text was
added; if a future run mints a duplicate domain home, that is the failing test this guidance was
waiting for. Record: design doc, review-round-2 RED/GREEN entry.

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
SETUP SHALL scaffold a router-only `CLAUDE.md` when the survey finds no first-party project
content at the invocation root — only sub-projects (own router/`.git`) and
tooling/scope-exclusions: charter + flag-and-skip routing to each sub-project + the
exclusions. SETUP SHALL NOT create the full enforced set at the container level.

#### Scenario: Portfolio root gets router-only
- **WHEN** a SETUP-guided run is invoked at a directory whose only members are two
  sub-projects and a tooling dir
- **THEN** the container receives `CLAUDE.md` only (routing + redirect notes), no
  ARCHITECTURE/ROADMAP/NOTEBOOK/VERIFICATION/DOMAIN at that level, and the report directs
  the user to run SETUP from each sub-project

### Requirement: Shipped history routes to CHANGELOG.md
The SETUP skill SHALL teach that shipped history lives in `CHANGELOG.md` — journal tier:
append-only, dated, newest first — created conditionally when history accrues (like README).
`ROADMAP.md` SHALL keep only a short "Recently shipped" digest plus a one-line pointer;
a long dated history embedded in ROADMAP is non-conformant. Shipped history SHALL never be
routed into `archive/`; git remains the commit-level backstop. Relocating an embedded
history SHALL be a content-preserving move (safety rule S1).

#### Scenario: Embedded ROADMAP history is relocated, content-preserved
- **WHEN** a SETUP-guided agent standardizes a project whose ROADMAP embeds a long dated
  shipped-history
- **THEN** it creates a charter'd `CHANGELOG.md` holding every entry verbatim (newest
  first), reduces ROADMAP to a short digest + pointer, and updates the router — with zero
  entries dropped or reworded (disk-verifiable against the pre-change tree)

#### Scenario: No history accrued, no CHANGELOG forced
- **WHEN** the target project has no shipped history to speak of
- **THEN** no `CHANGELOG.md` is created (conditional file — don't force content)

### Requirement: Router teaches the three-way journal split
The router/tier guidance SHALL define the journal tier as `docs/YYYY-MM-DD-*.md` +
`NOTEBOOK.md` + `CHANGELOG.md`, split three ways: small finding from doing the work →
NOTEBOOK; shipped unit → CHANGELOG; substantial standalone record → `docs/`.

#### Scenario: CLAUDE.md written by SETUP names the three-way split
- **WHEN** SETUP writes or aligns a project's CLAUDE.md router
- **THEN** the journal tier it teaches includes `CHANGELOG.md` with the shipped-unit
  routing, alongside NOTEBOOK and dated docs/
