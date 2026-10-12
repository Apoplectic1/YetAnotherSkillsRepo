# docs-architecture-setup: delta for reference-doc-split

## ADDED Requirements

### Requirement: A reference doc past its budget splits by topic into a directory named for it
When a reference doc passes the budget (40 KB) and its weight is many `##` topics, the SETUP
skill SHALL split it with `split_doc.py` beside the SKILL.md: each `##` section moves byte
for byte into `<DOC>/<topic>.md`, one charter'd file per topic named by its heading, and the
doc stays as the index (its charter, a split note, one line per part). The router SHALL keep
naming the doc; a heading SHALL keep its text so a section citation resolves by grep over the
file and the directory; a section is never split below `##`. A doc heavy with cold rationale
SHALL extract (T3) instead, and a design doc in a code-light project SHALL stay whole (B5).

#### Scenario: A multi-topic reference doc past the budget is split
- **WHEN** a SETUP run meets a 40 KB ARCHITECTURE of eighteen `##` topics true to code
- **THEN** the plan names the split by the script: one file per topic in `ARCHITECTURE/`, the
  doc as the index, the router naming the doc only, citations resolving by grep; nothing is
  moved into another doc

#### Scenario: A doc bloated by rationale is extracted, not split
- **WHEN** a SETUP run meets a 25 KB ARCHITECTURE dominated by design essays
- **THEN** the plan proposes cold-rationale extraction and no split

#### Scenario: A doc under budget is left alone
- **WHEN** a reference doc is under the budget
- **THEN** no split is proposed, whatever its topic count
