# docs-architecture-setup — delta spec

Scope note: this spec covers only the requirements this change establishes for the SETUP skill
(`skills/docs-architecture-setup/SKILL.md`); it is not a retroactive full spec of the skill.

## ADDED Requirements

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
