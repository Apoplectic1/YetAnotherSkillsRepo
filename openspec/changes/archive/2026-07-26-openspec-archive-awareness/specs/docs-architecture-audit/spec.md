# docs-architecture-audit Delta Specification

## MODIFIED Requirements

### Requirement: Cold-rationale docs get a decision-consistency check
Cold-rationale documents (dated `docs/` rationale notes that a reference doc cites) SHALL be
audited with a decision-consistency check only — does the reasoning still support the decision it
justifies? — not a full code-currency sweep. A code-coupled fact (file, function, flag, or value)
found inside a cold-rationale doc SHALL be flagged as misplaced (tier violation), since code-coupled
content parked in tier 3 escapes the currency sweep.

**Carve-out — archived openspec design docs:** when the cited document is an archived openspec
design doc (`openspec/changes/archive/*/design.md`), the decision-consistency check SHALL still
run, but tier-violation flags for code-coupled facts SHALL be suppressed — such documents are
dense with code-coupled facts by design and are immutable change records. The audit SHALL never
edit a file under `openspec/changes/archive/`. Standing truth found there that belongs in the
reference tier is the MAINTAIN graduate path's job, not a misplacement flag.

#### Scenario: Code-coupled fact in a cold doc is flagged
- **WHEN** an audit worker reads a cold-rationale doc containing a drifted code-coupled fact
- **THEN** it emits a flag identifying the misplacement (not a silent skip, and not an ordinary
  currency fix that leaves the fact in tier 3)

#### Scenario: Sound evergreen reasoning is not flagged
- **WHEN** a cold-rationale doc's reasoning still supports the decision it justifies
- **THEN** no flag is emitted for it (no cry-wolf)

#### Scenario: Cited archived openspec design doc gets consistency-check only
- **WHEN** a reference doc cites `openspec/changes/archive/<id>/design.md` and an audit worker
  follows the citation into a file dense with code-coupled facts that have since drifted
- **THEN** the worker runs the decision-consistency check, emits no tier-violation flags for
  the code-coupled facts, and does not edit the archived file

#### Scenario: Broken reasoning in an archived design doc is still surfaced
- **WHEN** the cited archived design.md's reasoning no longer supports the decision the
  reference doc rests on
- **THEN** a decision-consistency flag is still emitted (the carve-out suppresses tier
  violations, not the consistency check itself)

## ADDED Requirements

### Requirement: OpenSpec change archive is journal-tier
The never-currency-audited journal set (`docs/`, `NOTEBOOK.md`, `CHANGELOG.md`, `archive/`)
SHALL explicitly include `openspec/changes/archive/` — append-only, legibly historical. Generic
"`archive/`" SHALL NOT be left ambiguous as to whether the openspec change archive matches it.

#### Scenario: Archived change artifacts are not currency-audited
- **WHEN** an audited project's `openspec/changes/archive/` holds proposals, specs, and design
  docs whose content no longer matches current code
- **THEN** no currency flags are emitted for those files

#### Scenario: Workers agree on the exclusion
- **WHEN** multiple fan-out workers each encounter `openspec/changes/archive/` content
- **THEN** all treat it as journal-tier (no worker-to-worker inconsistency from reading
  generic "archive/" differently)
