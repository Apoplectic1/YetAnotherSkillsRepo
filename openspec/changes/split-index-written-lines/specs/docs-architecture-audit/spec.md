# docs-architecture-audit: delta for split-index-written-lines

## ADDED Requirements

### Requirement: The scope step reports a split index that no longer matches its parts
The audit's scope step SHALL report a split index stale by the test the setup skill's
`split_doc.py --check` applies (the files listed, each part's recorded size, each part's
written line and its checks), and SHALL name `split_doc.py --reindex` as the remedy. The
scope step SHALL change nothing.

#### Scenario: An edited part is reported
- **WHEN** the scope step runs on a project whose split ARCHITECTURE has a part edited since
  its index was written
- **THEN** the line for the split's parts says the index is stale, names the part and points
  at `split_doc.py --reindex`

#### Scenario: A line naming a term its part lost is reported
- **WHEN** a written line carries a code-formatted term that no longer occurs in its part
- **THEN** the scope step's line says the index is stale and names the part and the term

#### Scenario: A current index draws no remark
- **WHEN** every part is as its index records it and every line passes its checks
- **THEN** the line for the split's parts carries no stale remark
