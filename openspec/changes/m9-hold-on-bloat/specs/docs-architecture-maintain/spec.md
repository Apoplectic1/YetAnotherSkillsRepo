# docs-architecture-maintain — delta: m9-hold-on-bloat

## ADDED Requirements

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
