# docs-architecture-maintain Delta Specification

## ADDED Requirements

### Requirement: Archived openspec design docs are a graduate source, cross-ref-only
The MAINTAIN sweep SHALL include archived openspec design documents
(`openspec/changes/archive/*/design.md`) as a journal-tier source class, classifying their
content like any journal item (graduate / keep / archive / prune-only). For a `graduate` from
this source class, the source-disposition SHALL be pinned to `cross-ref`-only, realized as a
pointer written in the **reference doc** (the graduated truth cites the archived design.md as
its evidence) — the archived file itself SHALL never be edited, stubbed, or relocated: it is an
immutable change record. On a project with no `openspec/` directory the source class SHALL be a
silent no-op.

#### Scenario: Hardened rationale in an archived design doc is graduated
- **WHEN** a MAINTAIN-guided run sweeps a project whose `openspec/changes/archive/<id>/design.md`
  holds rationale for a standing constraint not yet stated in the reference tier
- **THEN** the rationale is proposed as a `graduate` into the charter-owning reference doc,
  with a cross-ref pointer in the reference doc back to the archived design.md as evidence

#### Scenario: The archive is never touched
- **WHEN** any `graduate` from an archived design.md is applied
- **THEN** the file under `openspec/changes/archive/` is byte-identical before and after the
  run (no stub inserted, no content removed, no relocation)

#### Scenario: No openspec, no noise
- **WHEN** a MAINTAIN-guided run sweeps a project with no `openspec/` directory
- **THEN** the source class contributes nothing to the run and no openspec-related flags or
  report lines appear
