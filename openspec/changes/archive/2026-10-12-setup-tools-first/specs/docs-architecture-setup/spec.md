# docs-architecture-setup: delta for setup-tools-first

## ADDED Requirements

### Requirement: The survey step is scripted
A SETUP run SHALL begin with `survey.py` beside the skill, which SHALL print one line per
finding with the rule it keys at the end and SHALL change nothing; the plan SHALL act on its
lines, while the content tests (S5's honesty, S7's content, S8's breadth and stability)
remain the run's own judgment. The skill text SHALL state each rule as its action plus one
boundary, leaving a script's behavior to the script's output and rationale to the design doc.

#### Scenario: The survey's lines
- **WHEN** the survey runs on a project directory
- **THEN** it reports the shapes (a sub-project, a container root, a design-slot candidate),
  the enforced set with each file's charter line, the router's line count and the chain row
  (through the audit skill's `chain_budget.py`), what the router names and which exclusions
  it notes, always-on rule files, journals and reference docs past their budget, a split
  whose index is stale, shipped history embedded in ROADMAP, a wildcard ignore over nested
  repositories, the `docs/` naming forms, and the git state

#### Scenario: A container root is named by the survey
- **WHEN** the survey runs at a root with no manifest, no reference docs and no source
  within two levels outside its sub-projects
- **THEN** it names the container-root shape with B4 and each sub-project with B3, and the
  plan scaffolds no enforced set there

#### Scenario: A finding the survey cannot make stays the run's
- **WHEN** a router block passes the survey's line count but fails breadth
- **THEN** the plan still moves it (S8): the survey detects, the test decides

#### Scenario: The survey is byte-exact on the fixtures
- **WHEN** it runs on baselined copies of the base TidePool, the reefstack root and the
  `s8-field` variant with `--root <copy> --global none --memory none`
- **THEN** its output matches `harness/survey-fixture/<name>.expected.txt` byte for byte

#### Scenario: The trimmed text keeps its cells
- **WHEN** the rewritten skill text runs plan-only on one fixture copy per family (the base
  TidePool, the reefstack root, `near-budget`, `s8-field`, the `fat-chain` root)
- **THEN** every cell those families earned still passes; a cell that fails names the clause
  restored, in the shortest form that passes
