# docs-architecture-maintain — delta: code-bug-persistence

## ADDED Requirements

### Requirement: In-schema report-only code-bug channel
The MAINTAIN skill SHALL provide a report-only `flag-code-bug` channel alongside its
classification schema (`graduate | keep | archive | prune-only`), mirroring AUDIT R4/R7
semantics: when a journal claim with contract force (guarantee language — must / always /
never / aborts-on-X) is contradicted by the code, the code is the suspect — the worker
emits a `flag-code-bug` with the claim and code evidence, and SHALL NOT reclassify, stale,
or archive the journal entry on account of the code disagreement. Corroboration (a test,
another doc) strengthens a flag but SHALL NOT substitute for guarantee language — dated
records agreeing on an old value are history, not a contract. Design-time values in
archived change records (the M11 source class) are never contracts — implementation drift
from an archived design is not flagged. The channel is orthogonal to classification (an
entry can be `keep` and still evidence a live bug). MAINTAIN never edits code. Gated on
RED→GREEN per the iron law on a non-derived fixture with a new journal-claim-vs-buggy-code
plant class.

#### Scenario: Journal contract claim violated by code
- **WHEN** a MAINTAIN worker verifies a journal entry asserting a contract (e.g. "X always
  aborts on missing Y") and the current code violates it
- **THEN** the worker emits a report-only `flag-code-bug` citing the claim and the code
  evidence, and the journal entry's own classification is decided on its normal merits
  (not demoted for the mismatch)

#### Scenario: Plain drift without contract force
- **WHEN** a journal entry's incidental detail merely drifted from the code (no guarantee
  asserted)
- **THEN** no code-bug flag is emitted; the entry is classified normally (the journal
  records history — a dated finding is not made false by later code change)

#### Scenario: Historical corroboration does not create a contract
- **WHEN** two or more dated records (e.g. a NOTEBOOK observation and a ROADMAP/CHANGELOG
  shipped entry) agree on an old value that current code and current-truth reference docs
  have moved past, with no guarantee language anywhere
- **THEN** no code-bug flag is emitted — corroborated history is still history

#### Scenario: Archived-design drift is not a bug
- **WHEN** code-coupled values in an archived openspec design doc (M11 class) differ from
  current code
- **THEN** no code-bug flag is emitted (design-time values; implementation drift from an
  archived design is normal)

### Requirement: Report-only flags persist to the target project's tiers
The MAINTAIN skill's apply step SHALL persist surviving `flag-code-bug` findings exactly as
AUDIT does: full evidence in a dated `docs/YYYY-MM-DD-<skill>-report.md` in the target
project, one deduplicated line per adjudicated-surviving bug in the target project's
ROADMAP § Open, and a single pointer line instead when adjudication is deferred.

#### Scenario: MAINTAIN sweep surfaces bugs
- **WHEN** a MAINTAIN sweep's workers emit `flag-code-bug` findings and the run reaches
  apply
- **THEN** the run ends with the dated report on disk in the target project and the
  surviving bugs (or the deferred-report pointer) present in that project's ROADMAP § Open
