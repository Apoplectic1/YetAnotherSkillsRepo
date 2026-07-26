# docs-architecture-maintain Specification

## Purpose
TBD - created by archiving change openspec-archive-awareness. Update Purpose after archive.
## Requirements
### Requirement: Archived openspec design docs are a graduate source, cross-ref-only
The MAINTAIN sweep SHALL include archived openspec design documents
(`openspec/changes/archive/*/design.md`) as a journal-tier source class, classifying their
content like any journal item (graduate / keep / archive / prune-only). For a `graduate` from
this source class, the source-disposition SHALL be pinned to `cross-ref`-only, realized as a
pointer written in the **reference doc** (the graduated truth cites the archived design.md as
its evidence) — the archived file itself SHALL never be edited, stubbed, or relocated: it is an
immutable change record. A project router's generic `openspec/` exclusion note SHALL NOT
exempt this source — the skill rule governs, so pre-existing routers written before this
convention need no edit for the sweep to reach the archive. On a project with no `openspec/`
directory the source class SHALL be a silent no-op.

#### Scenario: Hardened rationale in an archived design doc is graduated
- **WHEN** a MAINTAIN-guided run sweeps a project whose `openspec/changes/archive/<id>/design.md`
  holds rationale for a standing constraint not yet stated in the reference tier
- **THEN** the rationale is proposed as a `graduate` into the charter-owning reference doc,
  with a cross-ref pointer in the reference doc back to the archived design.md as evidence

#### Scenario: The archive is never touched
- **WHEN** any `graduate` from an archived design.md is applied
- **THEN** the file under `openspec/changes/archive/` is byte-identical before and after the
  run (no stub inserted, no content removed, no relocation)

#### Scenario: Old router wording does not block the sweep
- **WHEN** a MAINTAIN-guided run sweeps an existing project whose router still carries the
  blanket "`openspec/` — excluded, tooling" note (written before this convention)
- **THEN** the archived design.md source class is swept anyway (the skill rule overrides the
  router's generic exclusion; no router edit is required first)

#### Scenario: No openspec, no noise
- **WHEN** a MAINTAIN-guided run sweeps a project with no `openspec/` directory
- **THEN** the source class contributes nothing to the run and no openspec-related flags or
  report lines appear

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

### Requirement: Graduations targeting a bloated doc are held, never applied into it
The MAINTAIN skill SHALL hold — not apply — any graduate whose charter-selected target
reference doc is already bloated (oversized / dominated by content a split would relocate):
the held graduation is recorded in the dated maintain report (standing-claim + target +
source-disposition, per the M13 persistence rails) and one ROADMAP open-line SHALL name the
pending split job; the split itself runs as a separately-adjudicated job (setup/audit
territory), after which the held promotions land in the split homes. Applying content into
the bloated target and flagging the split afterward (stuff-then-ask) SHALL be treated as a
violation, not as compliance — the skill text names this red-flag explicitly. Healthy
targets are unaffected: their graduations apply in the same run as always. Held graduations
lose nothing (M8's never-lose-the-why extends to them via the report). Gated on RED→GREEN
per the iron law on non-derived fixtures (the deriving TSM run is poisoned for this rule);
no-failure → status-note only.

#### Scenario: Bloated target, graduate held
- **WHEN** a sweep classifies a journal item `graduate` and its charter-selected target is
  an already-bloated reference doc
- **THEN** the apply step writes nothing into that doc; the graduation is recorded in the
  dated report with target + disposition, ROADMAP gains (or reuses) one open-line naming
  the pending split job, and the source entry keeps its dated why/when

#### Scenario: Stuff-then-ask is the named failure
- **WHEN** a rep applies a graduation into a bloated target and then surfaces the split as
  a question or note
- **THEN** that run has violated the rule — the ask does not retroactively license the
  stuffing

#### Scenario: Healthy target unaffected
- **WHEN** a graduate's target is a normally-sized reference doc in the same sweep
- **THEN** the promotion applies in that run exactly as before (no over-holding)

#### Scenario: Held work is tracked, not remembered
- **WHEN** the sweep ends with held graduations
- **THEN** the report + the ROADMAP split-job line are sufficient for a later session (or
  `whats-next`) to find the pending split and the promotions waiting on it

### Requirement: Portfolio-level graduates target the portfolio DOMAIN or flag-and-ask
The MAINTAIN skill SHALL route a graduate whose standing truth is portfolio-level — it
spans repos, or no reference doc in the current repo's charter set can own it — to the
container's portfolio `DOMAIN.md` when the convention provides one (pointer discipline per
the SETUP amendment: one-way only). When no portfolio DOMAIN exists, the skill SHALL
flag-and-ask — present the graduate with its portfolio-level classification for the user
to place — and SHALL NOT improvise a cross-repo pointer into another project's docs
(two repos improvising produces ownerless cross-ref loops). Gated on RED→GREEN per the
iron law on a synthetic container fixture; the TSM glossary loop is deriving field
evidence (poisoned for validation).

#### Scenario: Portfolio truth with a portfolio DOMAIN available
- **WHEN** a sweep classifies a journal truth as standing and portfolio-level, and the
  container provides a portfolio DOMAIN
- **THEN** the graduate targets that DOMAIN (subject to M9/M14 as usual), and the source
  repo keeps a one-line upward pointer per the normal disposition rules

#### Scenario: Portfolio truth, no portfolio DOMAIN
- **WHEN** the same class of truth surfaces and no portfolio DOMAIN exists
- **THEN** the run flags it for the user (report + adjudication) instead of writing a
  pointer into a sibling repo's docs — no cross-repo improvisation

#### Scenario: Mutual pointer never created
- **WHEN** resolving where a shared term lives
- **THEN** the outcome never leaves two repos pointing at each other for the same truth

### Requirement: Sweep report carries a required prune/growth accounting slot
The dated maintain report SHALL end with a required accounting slot: the prune/archive
candidates found this sweep — or the explicit line "prune candidates: none found" — and a
one-line net reference-tier delta (what the run added to reference docs vs removed or
struck). Silence is not a legal value for either element. No numeric graduation cap is
imposed, and MAINTAIN gains no reference-tier deletion authority (that remains AUDIT's
job). Gating record: the net-delta line was absent in the synthetic RED rep (and in every
prior field/fixture report); ad-hoc prune listings existed but were uncontracted.

#### Scenario: Nothing to prune is stated, not silent
- **WHEN** a sweep finds no prune/archive candidates
- **THEN** the report's accounting slot states "prune candidates: none found" explicitly

#### Scenario: Ratchet visible per run
- **WHEN** any sweep completes
- **THEN** the report states in one line what the run added to the reference tier vs what
  it removed or struck, so add:remove is visible without diffing

#### Scenario: Candidates found are listed in the slot
- **WHEN** the sweep prunes or archives items
- **THEN** they are listed in the accounting slot (not only scattered through prose)

