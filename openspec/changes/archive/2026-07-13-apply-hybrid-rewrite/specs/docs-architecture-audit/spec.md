# Delta: docs-architecture-audit — apply-hybrid-rewrite

## ADDED Requirements

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
