# docs-architecture-audit: delta for audit-tools-first

## ADDED Requirements

### Requirement: The scope step is scripted
An audit run SHALL begin with `scope.py` beside the skill, which SHALL print one line per
item with the rule it keys and SHALL change nothing; the workers' judgments (a claim's
modality, what a router block is, whether a mismatch is drift or a contract) remain theirs.
The skill text SHALL state each rule as its action plus one boundary, a script's behavior
left to the script and rationale to the design doc.

#### Scenario: The scope's lines
- **WHEN** the script runs on a launch directory
- **THEN** it prints the scope in and out, the chain row, the structural findings a count can
  make and the seed of the cross-reference pass: what the router names, the canonical set, a
  split index's parts, a router-named doc under `docs/`, a router-named spec and a
  router-named leaf inside an excluded tree as in scope with their rules; the journal,
  archives, excluded trees, unnamed specs and sub-projects as out with theirs; the ancestor
  routers that load there; the cold docs the reference tier cites; shipped history embedded
  in ROADMAP and a stale split index; the chain row with its largest items

#### Scenario: The cross-reference seed
- **WHEN** a backtick path or a "DOC § Heading" citation in an in-scope doc does not resolve
  in the tree, the doc or its split directory, or an ancestor router for a `root CLAUDE.md`
  citation
- **THEN** the script lists it with its file and line, naming where a basename of that name
  does exist (a rename-orphan candidate) or that it lives under the ancestor (a sibling's
  file); a bare filename that exists anywhere in the tree resolves

#### Scenario: The lens is an option
- **WHEN** the run is in `release-close` mode
- **THEN** `--lens release` lists every in-scope line carrying a release-close phrase, a
  version or a count, and the workers judge each (a real wait is not a flag)

#### Scenario: The script is byte-exact on the fixtures
- **WHEN** it runs on baselined copies of the base TidePool, the `audit-scope` variant from
  `PulseMonitor/` and the `fat-chain` root with `--root <copy> --global none --memory none`
- **THEN** its output matches `harness/scope-fixture/<name>.expected.txt` byte for byte

#### Scenario: The trimmed text keeps its cells
- **WHEN** the rewritten skill text runs report-only on one fixture copy per family (the
  base TidePool, `audit-scope` from `PulseMonitor/`, the `fat-chain` root and `ReefDash/`
  beneath it, `release-lens` in release-close mode)
- **THEN** every cell those families earned still passes; a cell that fails names the clause
  restored, in the shortest form that passes
