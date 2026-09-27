# docs-architecture-maintain: delta for journal-rollover

## ADDED Requirements

### Requirement: Journals roll over by date into a frozen overflow directory
The MAINTAIN skill SHALL roll over, before its fan-out, any journal (`NOTEBOOK.md`,
`CHANGELOG.md`) whose size passes the budget (40 KB by default): the oldest whole days move
into a directory named for the file (`NOTEBOOK/`, `CHANGELOG/`), one file per period named by
its first date, each under the budget, with about half the budget left in the live file;
entries move byte for byte and keep their text; the directory carries an `INDEX.md` listing
every rolled entry by date and title; the live file's header states the rule and how a dated
citation resolves (by grep over the file and the directory). The scripts beside the SKILL.md
(`rollover.py`, `journal_index.py`) perform it and SHALL accept both entry forms
(`## YYYY-MM-DD` headings; top-level `- YYYY-MM-DD` bullets), newest first or last, refusing
any other with both forms named. A journal entry SHALL never be archived by judgment: M3 and
M7 apply to dated `docs/` records only. Before applying, the operator SHALL carry each open
thread of an entry about to roll (not closed by a later entry, tracked in no ROADMAP) into the
live file's "Open threads (carried at a rollover)" section. A rolled file SHALL be frozen: a
graduate sourced from one takes `cross-ref` written in the reference doc or `stub`, never an
in-place edit; the sweep slices by the live file and the rolled files newer than the previous
report's watermark, and the report's accounting slot SHALL name the newest rolled file the
sweep covered (or "no rolled files"). The rollover also runs on its own whenever a journal
passes the budget. Gated on RED/GREEN on a non-derived fixture (TidePool with the
`big-journal` variant); the HDL tree, where the rule was derived, is poisoned for it.

#### Scenario: A journal past its budget is rolled before the sweep
- **WHEN** a MAINTAIN run meets a `NOTEBOOK.md` past the budget
- **THEN** before any graduation worker runs, `NOTEBOOK/` exists with rolled files each under
  the budget and an `INDEX.md`, the live file holds the newest entries with the rollover note
  in its header, and the live entries plus the rolled entries reconstruct the original entries
  byte for byte

#### Scenario: An open thread is carried, a closed one is not
- **WHEN** an entry about to roll carries an open item that no later entry closes and no
  ROADMAP tracks
- **THEN** the live file's "Open threads (carried at a rollover)" section gains one line for it
  naming the rolled file, while an item a later entry closed is not carried as open

#### Scenario: A dated citation still resolves
- **WHEN** a reference doc cites a journal entry by date and that entry has rolled
- **THEN** `grep -n "<date>" NOTEBOOK.md NOTEBOOK/*.md` finds it, the citation text unchanged

#### Scenario: A rolled file is frozen
- **WHEN** a sweep graduates a truth whose source entry is in a rolled file
- **THEN** the rolled file is byte-identical after the run, the pointer or stub lives in the
  reference doc, and the report names the newest rolled file covered as the watermark

#### Scenario: A journal in neither form is refused
- **WHEN** the script meets a journal without dated `##` headings or dated top-level bullets
- **THEN** it exits nonzero naming both forms and writes nothing; the journal's shape is a
  SETUP finding
