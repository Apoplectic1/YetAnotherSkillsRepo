# docs-architecture-maintain Specification

## Purpose
The requirements the changes since 2026-07-26 established for the MAINTAIN skill
(`skills/docs-architecture-maintain/SKILL.md`): its sources, its dispositions, its report and
the journal's rollover. Not a retroactive full spec of the skill.

## Requirements

### Requirement: Archived openspec design docs are a graduate source, cross-ref-only
The MAINTAIN sweep SHALL include archived openspec design documents
(`openspec/changes/archive/*/design.md`) as a journal-tier source class, classifying their
content like any journal item (graduate / keep / archive / prune-only). On a project with no
`openspec/` directory the source class SHALL be a silent no-op.

#### Scenario: Hardened rationale in an archived design doc is graduated
- **WHEN** a MAINTAIN-guided run sweeps a project whose `openspec/changes/archive/<id>/design.md`
  holds rationale for a standing constraint not yet stated in the reference tier
- **THEN** the rationale is proposed as a `graduate` into the charter-owning reference doc,
  with a cross-ref pointer in the reference doc back to the archived design.md as evidence

#### Scenario: No openspec, no noise
- **WHEN** a MAINTAIN-guided run sweeps a project with no `openspec/` directory
- **THEN** the source class contributes nothing to the run and no openspec-related flags or
  report lines appear

### Requirement: A graduate from an archived design doc leaves the archive untouched
For a `graduate` from an archived openspec design doc, the source-disposition SHALL be pinned
to `cross-ref`-only, realized as a pointer written in the **reference doc** (the graduated
truth cites the archived design.md as its evidence), and the archived file itself SHALL never
be edited, stubbed, or relocated.

#### Scenario: The archive is never touched
- **WHEN** any `graduate` from an archived design.md is applied
- **THEN** the file under `openspec/changes/archive/` is byte-identical before and after the
  run (no stub inserted, no content removed, no relocation)

### Requirement: A router's generic openspec exclusion does not exempt the archive
A project router's generic `openspec/` exclusion note SHALL NOT exempt archived design docs
from the sweep: the skill rule governs, so a router written before this convention needs no
edit for the sweep to reach the archive.

#### Scenario: Old router wording does not block the sweep
- **WHEN** a MAINTAIN-guided run sweeps an existing project whose router still carries the
  blanket "`openspec/` — excluded, tooling" note (written before this convention)
- **THEN** the archived design.md source class is swept anyway (the skill rule overrides the
  router's generic exclusion; no router edit is required first)

### Requirement: In-schema report-only code-bug channel
The MAINTAIN skill SHALL provide a report-only `flag-code-bug` channel alongside its
classification schema (`graduate | keep | archive | prune-only`): when a journal claim with
contract force (guarantee language — must / always / never / aborts-on-X) is contradicted by
the code, the code is the suspect — the worker emits a `flag-code-bug` with the claim and code
evidence, and SHALL NOT reclassify, stale, or archive the journal entry on account of the code
disagreement. MAINTAIN never edits code.

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

### Requirement: Corroboration never stands in for guarantee language
Corroboration (a test, another doc) strengthens a flag but SHALL NOT substitute for guarantee
language — dated records agreeing on an old value are history, not a contract.

#### Scenario: Historical corroboration does not create a contract
- **WHEN** two or more dated records (e.g. a NOTEBOOK observation and a ROADMAP/CHANGELOG
  shipped entry) agree on an old value that current code and current-truth reference docs
  have moved past, with no guarantee language anywhere
- **THEN** no code-bug flag is emitted — corroborated history is still history

### Requirement: Design-time values in archived change records are never contracts
Design-time values in archived change records (the M11 source class) SHALL never be read as
contracts: implementation drift from an archived design is not flagged.

#### Scenario: Archived-design drift is not a bug
- **WHEN** code-coupled values in an archived openspec design doc (M11 class) differ from
  current code
- **THEN** no code-bug flag is emitted (design-time values; implementation drift from an
  archived design is normal)

### Requirement: The code-bug channel is orthogonal to classification
The code-bug channel SHALL be orthogonal to classification: an entry can be `keep` and still
evidence a live bug.

#### Scenario: A kept entry that evidences a bug
- **WHEN** a journal entry that classifies as `keep` asserts a guarantee the current code
  violates
- **THEN** the entry is classified `keep` and a report-only `flag-code-bug` is emitted for it

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
The MAINTAIN skill SHALL hold, not apply, any graduate whose charter-selected target
reference doc is already bloated (oversized / dominated by content a split would relocate):
the held graduation is recorded in the dated maintain report (standing-claim + target +
source-disposition, per the M13 persistence rails) and one ROADMAP open-line SHALL name the
pending split job and its shape (SETUP's T5: `split_doc.py`, by `##` topic into a directory
named for the doc, the doc left as the index).

#### Scenario: Bloated target, graduate held
- **WHEN** a sweep classifies a journal item `graduate` and its charter-selected target is
  an already-bloated reference doc
- **THEN** the apply step writes nothing into that doc; the graduation is recorded in the
  dated report with target + disposition, ROADMAP gains (or reuses) one open-line naming
  the pending split job and its shape, and the source entry keeps its dated why/when

### Requirement: A held promotion lands after the split, in the part it belongs under
The split SHALL run as a separately-adjudicated job (setup/audit territory), after which each
held promotion lands in the part whose heading it belongs under. Held graduations lose nothing
(M8's never-lose-the-why extends to them via the report).

#### Scenario: Held work is tracked, not remembered
- **WHEN** the sweep ends with held graduations
- **THEN** the report + the ROADMAP split-job line (naming the script and the landing part)
  are sufficient for a later session (or `whats-next`) to run the split and land the
  promotions waiting on it

### Requirement: Stuff-then-ask is a violation
Applying content into the bloated target and flagging the split afterward (stuff-then-ask)
SHALL be treated as a violation, not as compliance (the skill text names this red-flag
explicitly).

#### Scenario: Stuff-then-ask is the named failure
- **WHEN** a rep applies a graduation into a bloated target and then surfaces the split as
  a question or note
- **THEN** that run has violated the rule: the ask does not retroactively license the
  stuffing

### Requirement: A graduate to a healthy target applies in the same run
A graduate whose target reference doc is healthy SHALL apply in the same run as always.

#### Scenario: Healthy target unaffected
- **WHEN** a graduate's target is a normally-sized reference doc in the same sweep
- **THEN** the promotion applies in that run exactly as before (no over-holding)

### Requirement: A held promotion under a halt follows the halt's terms
When a held promotion's target project states a halt in its ROADMAP, the report SHALL name
the halt beside the hold and sequence the landing by the halt's terms: a halt that admits
documentation changes lets the landing follow the split, and a halt on all work holds it until
the halt lifts.

#### Scenario: A held promotion under a halt follows the halt's terms
- **WHEN** a held promotion's target project states a halt in its ROADMAP
- **THEN** the report names the halt beside the hold and sequences the landing by the halt's
  terms: a halt that admits documentation changes lets the landing follow the split; a halt
  on all work holds it until the halt lifts

### Requirement: Portfolio-level graduates target the portfolio DOMAIN or flag-and-ask
The MAINTAIN skill SHALL route a graduate whose standing truth is portfolio-level — it
spans repos, or no reference doc in the current repo's charter set can own it — to the
container's portfolio `DOMAIN.md` when the convention provides one (pointer discipline per
the SETUP amendment: one-way only).

#### Scenario: Portfolio truth with a portfolio DOMAIN available
- **WHEN** a sweep classifies a journal truth as standing and portfolio-level, and the
  container provides a portfolio DOMAIN
- **THEN** the graduate targets that DOMAIN (subject to M9/M14 as usual), and the source
  repo keeps a one-line upward pointer per the normal disposition rules

#### Scenario: Mutual pointer never created
- **WHEN** resolving where a shared term lives
- **THEN** the outcome never leaves two repos pointing at each other for the same truth

### Requirement: With no portfolio DOMAIN, a portfolio-level graduate is put to the user
When no portfolio DOMAIN exists, the skill SHALL flag-and-ask — present the graduate with its
portfolio-level classification for the user to place — and SHALL NOT improvise a cross-repo
pointer into another project's docs.

#### Scenario: Portfolio truth, no portfolio DOMAIN
- **WHEN** the same class of truth surfaces and no portfolio DOMAIN exists
- **THEN** the run flags it for the user (report + adjudication) instead of writing a
  pointer into a sibling repo's docs — no cross-repo improvisation

### Requirement: Sweep report carries a required prune/growth accounting slot
The dated maintain report SHALL end with a required accounting slot: the prune/archive
candidates found this sweep — or the explicit line "prune candidates: none found" — and a
one-line net reference-tier delta (what the run added to reference docs vs removed or
struck). Silence is not a legal value for either element. No numeric graduation cap is
imposed, and MAINTAIN gains no reference-tier deletion authority (that remains AUDIT's
job).

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

### Requirement: Journals roll over by date into a frozen overflow directory
The MAINTAIN skill SHALL roll over, before its fan-out, any journal (`NOTEBOOK.md`,
`CHANGELOG.md`) whose size passes the budget (40 KB by default): the oldest whole days move
into a directory named for the file (`NOTEBOOK/`, `CHANGELOG/`), one file per period named by
its first date, each under the budget, with about half the budget left in the live file;
entries move byte for byte and keep their text. The rollover also runs on its own whenever a
journal passes the budget.

#### Scenario: A journal past its budget is rolled before the sweep
- **WHEN** a MAINTAIN run meets a `NOTEBOOK.md` past the budget
- **THEN** before any graduation worker runs, `NOTEBOOK/` exists with rolled files each under
  the budget and an `INDEX.md`, the live file holds the newest entries with the rollover note
  in its header, and the live entries plus the rolled entries reconstruct the original entries
  byte for byte

### Requirement: A rolled journal's INDEX.md lists every rolled entry by date and title
The overflow directory SHALL carry an `INDEX.md` listing every rolled entry by date and title,
where under a bare date heading (`## YYYY-MM-DD` with nothing after the date) each top-level
bullet opening with a bold run is an entry titled by that run, indented under its day, while a
bold-lead bullet under a titled heading is body.

#### Scenario: A bare-date journal is indexed by its titles
- **WHEN** `journal_index.py` meets a rolled file whose days are bare date headings over
  bold-lead top-level bullets (`## 2026-10-04`, then `- **E24: the P6 addition closed.** ...`)
- **THEN** `INDEX.md` lists each bold run as an entry line indented under its day, a plain or
  indented bullet is not listed, a bold-lead bullet under a titled heading is not listed, and
  every line the previous index held is unchanged

### Requirement: A rolled journal's live header says how a dated citation resolves
The live file's header SHALL state the rule and how a dated citation resolves (by grep over
the file and the directory).

#### Scenario: A dated citation still resolves
- **WHEN** a reference doc cites a journal entry by date and that entry has rolled
- **THEN** `grep -n "<date>" NOTEBOOK.md NOTEBOOK/*.md` finds it, the citation text unchanged

### Requirement: The rollover scripts accept both journal entry forms
The scripts beside the SKILL.md (`rollover.py`, `journal_index.py`) SHALL perform the rollover
and SHALL accept both entry forms (`## YYYY-MM-DD` headings; top-level `- YYYY-MM-DD`
bullets), newest first or last, refusing any other with both forms named.

#### Scenario: A journal in neither form is refused
- **WHEN** the script meets a journal without dated `##` headings or dated top-level bullets
- **THEN** it exits nonzero naming both forms and writes nothing; the journal's shape is a
  SETUP finding

### Requirement: A journal entry is never archived by judgment
A journal entry SHALL never be archived by judgment: M3 and M7 apply to dated `docs/` records
only.

#### Scenario: A spent-looking journal entry stays in the journal
- **WHEN** a sweep meets a `NOTEBOOK.md` entry whose finding reads as spent
- **THEN** the entry is not archived; it stays in the journal until a rollover moves it, byte
  for byte

### Requirement: Open threads are carried into the live file before their entry rolls
Before applying, the operator SHALL carry each open thread of an entry about to roll (not
closed by a later entry, tracked in no ROADMAP) into the live file's "Open threads (carried at
a rollover)" section.

#### Scenario: An open thread is carried, a closed one is not
- **WHEN** an entry about to roll carries an open item that no later entry closes and no
  ROADMAP tracks
- **THEN** the live file's "Open threads (carried at a rollover)" section gains one line for it
  naming the rolled file, while an item a later entry closed is not carried as open

### Requirement: A rolled file is frozen
A rolled file SHALL be frozen: a graduate sourced from one takes `cross-ref` written in the
reference doc or `stub`, never an in-place edit; the sweep slices by the live file and the
rolled files newer than the previous report's watermark, and the report's accounting slot
SHALL name the newest rolled file the sweep covered (or "no rolled files").

#### Scenario: A rolled file is frozen
- **WHEN** a sweep graduates a truth whose source entry is in a rolled file
- **THEN** the rolled file is byte-identical after the run, the pointer or stub lives in the
  reference doc, and the report names the newest rolled file covered as the watermark

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
