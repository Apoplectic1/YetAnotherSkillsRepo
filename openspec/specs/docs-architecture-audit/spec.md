# docs-architecture-audit Specification

## Purpose
TBD — created by syncing change `fix-skill-review-findings`. Covers only the requirements that
change established for the AUDIT skill (`skills/docs-architecture-audit/SKILL.md`); not a
retroactive full spec of the skill.
## Requirements
### Requirement: Cold-rationale docs get a decision-consistency check
Cold-rationale documents (dated `docs/` rationale notes that a reference doc cites) SHALL be
audited with a decision-consistency check only — does the reasoning still support the decision it
justifies? — not a full code-currency sweep. A code-coupled fact (file, function, flag, or value)
found inside a cold-rationale doc SHALL be flagged as misplaced (tier violation), since code-coupled
content parked in tier 3 escapes the currency sweep.

#### Scenario: Code-coupled fact in a cold doc is flagged
- **WHEN** an audit worker reads a cold-rationale doc containing a drifted code-coupled fact
- **THEN** it emits a flag identifying the misplacement (not a silent skip, and not an ordinary
  currency fix that leaves the fact in tier 3)

#### Scenario: Sound evergreen reasoning is not flagged
- **WHEN** a cold-rationale doc's reasoning still supports the decision it justifies
- **THEN** no flag is emitted for it (no cry-wolf)

### Requirement: Extraction candidates are flagged via the schema
Workers SHALL flag reference-tier sections that are lengthy AND cold AND evergreen (per the
extract discriminator) as cold-rationale extraction candidates using a schema action
(`extract-cold`), carried through merge/dedup like any flag and applied only after user
adjudication.

#### Scenario: Lengthy cold evergreen section is proposed for extraction
- **WHEN** an audit worker reads a reference-doc section that is lengthy, not needed for immediate
  reasoning, and evergreen (not code-coupled)
- **THEN** it emits an `extract-cold` flag in the schema for adjudication

### Requirement: Single action vocabulary; report-only is exactly two actions
The skill SHALL use one action vocabulary — the flag schema's — in every section, including the
adjudication step. `graduate` SHALL be an apply-able doc edit after adjudication. The term
"report-only" (handed off, never auto-applied) SHALL apply to exactly `flag-code-bug` and
`revisit-plan`.

#### Scenario: Approved graduate is applied
- **WHEN** a prescriptive plan item is already satisfied by code and adjudication approves the
  `graduate` flag
- **THEN** the apply step performs the doc edit (move to "Recently shipped" / archive the plan)

#### Scenario: Report-only flags are handed off
- **WHEN** a flag's action is `flag-code-bug` or `revisit-plan`
- **THEN** it is reported and routed onward, never applied by the audit run

### Requirement: Worker evidence is disk-verified before adjudication
Before presenting the merged flag list for adjudication, the orchestrator SHALL spot-verify each
flag's cited evidence against disk (grep/read the cited file:line or symbol). A flag whose evidence
does not hold SHALL be corrected or dropped with a note — never presented as verified.

**Status note (2026-07-07):** satisfied by baseline behavior, not by skill text. The RED baseline
passed 2/2 (orchestrators re-verified evidence and refuted a seeded false flag unprompted — the
skill's conservative-evidence rule already induces this), so per the no-failure gate no explicit
gate text was added to `skills/docs-architecture-audit/SKILL.md`. If a future run rubber-stamps
false evidence, that is the failing test this requirement's guidance was waiting for — encode it
then. RED/GREEN record: `docs/docs-architecture-design.md`, fix-batch behavioral half.

#### Scenario: Plausible-but-false worker claim is caught
- **WHEN** the merged list contains a flag whose cited evidence does not hold on disk (e.g., it
  asserts a dangling reference that grep shows clean)
- **THEN** the orchestrator detects the mismatch before adjudication and the flag is not applied

### Requirement: Fan-out is right-sized to doc volume
The fan-out SHALL scale with the audited doc set's volume. On a thin doc set (few, small,
recently-written reference docs) the run SHALL NOT deploy machinery disproportionate to the
content — per-doc workers plus the cross-reference pass suffice as the opening round;
per-section splitting, replicate rounds, and model diversity engage as volume and dry-round
results warrant. Loop-until-dry remains the terminator in all cases.

#### Scenario: Thin fresh set gets a small opening round
- **WHEN** an audit runs on a project with a handful of small, recently-written reference docs
- **THEN** the opening round is per-doc (not per-section × multiple models), the cross-ref
  pass still runs, and the run stops when a round is dry

#### Scenario: Large doc set still gets the full machinery
- **WHEN** an audit runs on a project with large multi-section reference docs
- **THEN** per-section workers, loop-until-dry, and model diversity apply as currently
  specified

**Status note (2026-07-07):** satisfied by baseline behavior, not by skill text. RED 2/2 passed —
on a 5-thin-doc fixture both reps planned a proportionate opening round (6 workers; explicit
"per-section collapses to per-doc" volume reasoning), kept round 3 conditional on a wet round 2,
and preserved loop-until-dry as the terminator. Per the no-failure gate no scale sentence was
added; if a future run deploys machinery grossly over volume, encode then. Record: design doc,
review-round-2 RED/GREEN entry.

### Requirement: Embedded shipped-history is one structural flag
When a reference doc embeds a growing dated shipped-history (e.g. inside ROADMAP), the audit
SHALL emit exactly ONE placement flag with action `move-to CHANGELOG.md`, and SHALL NOT
currency-flag the embedded entries individually — the entries are journal-tier; the
structural misplacement, not per-entry drift, is the finding. This suppression SHALL NOT
extend to live sections of the same doc: current-state claims outside the embedded history
remain fully currency-audited.

#### Scenario: One flag, entries folded
- **WHEN** an audit runs on a project whose ROADMAP embeds a dated history containing
  per-entry value drift
- **THEN** the merged report carries one `move-to CHANGELOG.md` placement flag for the
  section, with per-entry drifts folded/uncounted (a worker's per-entry flag is dropped at
  merge, logged, not itemized)

#### Scenario: Live-section defect still flagged
- **WHEN** the same doc's live section (e.g. Now/Next) carries a stale present-tense claim
- **THEN** that claim is still flagged as an ordinary currency finding (the structural flag
  does not become a blanket exemption for the whole doc)

### Requirement: CHANGELOG.md is journal-tier for the audit
`CHANGELOG.md` SHALL be part of the never-currency-audited journal set (`docs/`,
`NOTEBOOK.md`, `CHANGELOG.md`, `archive/`) — append-only, legibly historical.

#### Scenario: CHANGELOG entries are not currency-audited
- **WHEN** an audited project carries a `CHANGELOG.md` whose old entries no longer match
  current code
- **THEN** no currency flags are emitted for those entries

### Requirement: Convergence is not completeness
The model-diversification rule SHALL state explicitly that same-model cross-worker
convergence is agreement, not completeness — heavy convergence among same-model workers
SHALL NOT be accepted as grounds to skip the worker-model switch before concluding.

#### Scenario: Converged dry round still triggers the switch
- **WHEN** an orchestrator reaches a dry round with heavy same-model cross-worker
  convergence (and cost pressure is salient)
- **THEN** it switches worker model before concluding, or surfaces the cost tradeoff to the
  user as a decision — it does not silently conclude from convergence
