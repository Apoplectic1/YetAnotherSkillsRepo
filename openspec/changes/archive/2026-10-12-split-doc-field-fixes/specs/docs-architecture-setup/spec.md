# docs-architecture-setup: delta for split-doc-field-fixes

## MODIFIED Requirements

### Requirement: A reference doc past its budget splits by topic into a directory named for it
When a reference doc passes the budget (40 KB) and its weight is many `##` topics, the SETUP
skill SHALL split it with `split_doc.py` beside the SKILL.md: each `##` section moves byte
for byte into `<DOC>/<topic>.md`, one charter'd file per topic named by its heading, and the
doc stays as the index (its charter, a split note, one line per part). The router SHALL keep
naming the doc; a heading SHALL keep its text so a section citation resolves by grep over the
file and the directory; a section is never split below `##`, and a single topic past the
budget SHALL be reported and left as one part. A doc that the run's own moves push past the
budget SHALL split in the same run, after the moves land. The script SHALL refuse a journal,
keep its citation scan out of sub-projects and child repositories, list the lines a move one
directory down leaves stale, and warn on a dated heading. A doc heavy with cold rationale
SHALL extract (T3) instead, and a design doc in a code-light project SHALL stay whole (B5).

**Status note (2026-10-12):** the same-run split is satisfied by baseline behavior, not by
skill text. RED 2/2 on the TidePool `near-budget` variant (a 38 KB ARCHITECTURE and a router
block S7 moves into it): both reps sequenced the split after the move ("only then is the doc
over budget"), one previewing the dry run at a lowered budget. Per the no-failure gate the
sentence was not added to T5; if a run ever leaves a doc its own moves pushed past the
budget, encode it then. The single-part case is likewise baseline (the HDL pilot's rep
reported the 49.7 KB part and left it, saying the rule offered no lever, which is the rule).
The script's contracts (the journal refusal, the stale-line list, the dated-heading warning,
the scan's scope) are verified at script level (`harness/split-fixture/`).

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

#### Scenario: The run's own moves push a doc past the budget
- **WHEN** a 38 KB ARCHITECTURE receives a 4 KB mechanics block the same run moves out of the
  router (S7)
- **THEN** the plan splits ARCHITECTURE in that run, after the move, citing the script's dry
  run, rather than leaving a 42 KB doc for a later run

#### Scenario: A journal is refused
- **WHEN** `split_doc.py` is pointed at a doc whose `##` headings are dates
- **THEN** it exits naming the rollover and writes nothing
