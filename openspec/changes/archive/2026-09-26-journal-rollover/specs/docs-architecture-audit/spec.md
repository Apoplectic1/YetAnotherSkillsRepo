# docs-architecture-audit: delta for journal-rollover

## ADDED Requirements

### Requirement: A journal's overflow directory is journal-tier
The never-currency-audited journal set (`docs/`, `NOTEBOOK.md`, `CHANGELOG.md`, `archive/`,
`openspec/changes/archive/`) SHALL include a journal's overflow directory (`NOTEBOOK/`,
`CHANGELOG/`) and its `INDEX.md`: rolled periods of the journal, frozen, legibly historical.
The cross-reference pass SHALL resolve a dated citation of a journal entry in the live file or
the overflow directory.

#### Scenario: A rolled file with a superseded value is not flagged
- **WHEN** an audit worker is assigned `NOTEBOOK/<date>.md` and an entry there states a value
  the current code and reference docs have moved past
- **THEN** no currency flag and no code-bug flag is emitted for it

#### Scenario: A citation into a rolled entry resolves
- **WHEN** the cross-reference pass meets "the NOTEBOOK entry of 2026-01-22" and that entry
  has rolled
- **THEN** the citation is not reported as dangling

**Status note (2026-09-26):** satisfied by baseline behavior, not by skill text. The RED probe
(a worker assigned a rolled file whose 2026-01-22 entry says `CACHE_TTL_HOURS = 24` against
code at 6) treated the file as journal under R14 by inheritance from the router's journal line
(which SETUP now writes) and emitted no flags, while naming the ambiguity. Per the no-failure
gate the audit text was not changed; if a future run currency-flags a rolled file, encode then.
