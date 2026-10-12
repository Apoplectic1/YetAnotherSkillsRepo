# docs-architecture-maintain: delta for maintain-tools-first

## ADDED Requirements

### Requirement: The sweep's sources and the report's check are scripted
A maintain run SHALL begin with `sweep.py` beside the skill (the sources and budgets, one
line per item with its rule, changing nothing) and SHALL end with `sweep.py --check`, which
names each required line the report lacks by its rule; what graduates, where and with which
disposition remain the sweep's judgment. The skill text SHALL state each rule as its action
plus one boundary, a script's behavior left to the script and rationale to the design doc.

#### Scenario: The sources mode
- **WHEN** the script runs on a project directory
- **THEN** it lists the live journals against their budget (a journal past it keyed to M17),
  each rolled directory with the files newer than the last report's watermark (M19), the
  dated records, the archived openspec designs (M11), the targets with their sizes and
  splits (one past its budget keyed to M14, one past half of it to M9's content test), a
  portfolio DOMAIN beside the ancestor router or its absence (M15), the last report with its
  watermark, and the slices (M10)

#### Scenario: The check mode
- **WHEN** `--check` runs after a sweep whose report lacks one of the accounting slot's lines,
  or mentions a code-bug flag, a held promotion or a portfolio-level graduate that the
  ROADMAP carries no line for
- **THEN** it names each missing line by its rule (M16, M13, M14, M15), says nothing against
  a report and ROADMAP that carry them, and counts no line that says none, no or nothing
  beside the word it looks for

#### Scenario: The script is byte-exact on the fixtures
- **WHEN** the sources mode runs on baselined copies of the base TidePool, `big-journal` and
  `fat-arch`, and the check mode on the crafted `checked/`, `unchecked/` and `empty/` fixtures
- **THEN** its output matches `harness/sweep-fixture/<name>.expected.txt` byte for byte

#### Scenario: The trimmed text keeps its cells
- **WHEN** the rewritten skill text runs plan-only on one fixture copy per family (the base
  TidePool, `fat-arch`, `big-journal`, the reefstack from `ReefDash/` with and without a
  portfolio DOMAIN)
- **THEN** every cell those families earned still passes; a cell that fails names the clause
  restored, in the shortest form that passes
