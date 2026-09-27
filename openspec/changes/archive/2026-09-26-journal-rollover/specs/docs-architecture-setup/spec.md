# docs-architecture-setup: delta for journal-rollover

## MODIFIED Requirements

### Requirement: Router teaches the three-way journal split
The router/tier guidance SHALL define the journal tier as `docs/YYYY-MM-DD-*.md` +
`NOTEBOOK.md` + `CHANGELOG.md`, split three ways: small finding from doing the work →
NOTEBOOK; shipped unit → CHANGELOG; substantial standalone record → `docs/`; and SHALL name
the journals' overflow directories (`NOTEBOOK/`, `CHANGELOG/`): a journal past its budget
rolls its oldest whole days into a directory named for the file, one frozen file per period
named by its first date with an `INDEX.md`, the maintain skill's job. The router's journal
line SHALL state the project's dated-record pattern and that a dated citation resolves by
grep over a journal and its overflow directory.

#### Scenario: CLAUDE.md written by SETUP names the three-way split
- **WHEN** SETUP writes or aligns a project's CLAUDE.md router
- **THEN** the journal tier it teaches includes `CHANGELOG.md` with the shipped-unit
  routing, alongside NOTEBOOK and dated docs/

#### Scenario: The router's journal line names the overflow directory and the pattern
- **WHEN** SETUP writes or aligns a project's CLAUDE.md router
- **THEN** its journal line states the dated-record pattern in force and that a journal's
  rolled periods live in `NOTEBOOK/` (and `CHANGELOG/`), a dated citation resolving by grep
  over the file and the directory

## ADDED Requirements

### Requirement: Dated-record filenames follow the project's stated pattern
SETUP SHALL normalize a journal filename to the dated-record pattern the project's router
states, the default being `YYYY-MM-DD-<slug>.md`, and SHALL NOT impose the default over a
pattern the project states (a rename breaks every citation of the file). Gated on a RED probe
(2026-09-26: an unguided run renamed three files against the project's stated rule).

#### Scenario: A stated pattern is kept
- **WHEN** the router's journal line states `YYYY-MM-DD - <slug>.md` and the records follow it
- **THEN** SETUP leaves the names as they are and aligns only casing or a record that breaks
  the stated pattern

#### Scenario: No stated pattern, the default applies
- **WHEN** the router states no pattern and a record is named `notes3.md`
- **THEN** SETUP proposes the default form, content-preserving (S1)

### Requirement: A container root's ignore file names its repositories
SETUP SHALL write a container root's `.gitignore` by name: one line per nested repository,
each reason on its own line, and never a wildcard over the root's directories. On encounter
SETUP SHALL flag a wildcard form (`/*/` with exceptions) as a safety item and rewrite it by
name in the run, keeping the same directories out. Reason: a wildcard drops any new directory
silently (an overflow directory first), and a kit copied from what is committed ships without
it. Gated on a RED probe (2026-09-26: an unguided run left the wildcard, having no rule).

#### Scenario: A wildcard ignore file is met
- **WHEN** a container root's `.gitignore` reads `/*/` with exceptions for `docs/`,
  `openspec/` and `.claude/`
- **THEN** SETUP flags it and rewrites it to name each nested repository with its reason,
  and `git status` afterwards shows the same repositories untracked and nothing else changed

#### Scenario: A new directory at the root is tracked
- **WHEN** a later session creates a directory at a container root written this way
- **THEN** `git status` lists it as untracked and it is committed like any file
