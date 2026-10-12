# docs-architecture-maintain: delta for s8-field-fixes

## MODIFIED Requirements

### Requirement: Graduations targeting a bloated doc are held, never applied into it
The MAINTAIN skill SHALL hold, not apply, any graduate whose charter-selected target
reference doc is already bloated (oversized / dominated by content a split would relocate):
the held graduation is recorded in the dated maintain report (standing-claim + target +
source-disposition, per the M13 persistence rails) and one ROADMAP open-line SHALL name the
pending split job and its shape (SETUP's T5: `split_doc.py`, by `##` topic into a directory
named for the doc, the doc left as the index); the split itself runs as a
separately-adjudicated job (setup/audit territory), after which each held promotion lands in
the part whose heading it belongs under. Applying content into the bloated target and flagging
the split afterward (stuff-then-ask) SHALL be treated as a violation, not as compliance (the
skill text names this red-flag explicitly). Healthy targets are unaffected: their graduations
apply in the same run as always. Held graduations lose nothing (M8's never-lose-the-why
extends to them via the report). Gated on RED→GREEN per the iron law on non-derived fixtures
(the deriving TSM run is poisoned for this rule); no-failure → status-note only.

**Status note (2026-10-12):** a held promotion into a project whose ROADMAP states a halt.
The field case (the ATML umbrella's ten promotions held against the Arty's ARCHITECTURE; the
Arty halted at contract v5 with no further work; the tree's own 2026-09-26 maintain report
sequencing the landings after an unhalt) was misread in the HDL pilot by the plan author, not
by a MAINTAIN rep. RED on the TidePool `s8-field` variant with a 41.7 KB ARCHITECTURE under
its ROADMAP halt ("only documentation and bench records change until the freeze lifts"): the
rep held the promotion (M14), read the halt's terms unprompted, and sequenced the landing
after the split as documentation the halt permits, which is right for that halt. A clause
that holds every promotion until a halt lifts would have been wrong there; the halt's own
terms decide, and the current text's rep read them. No text ships; a full halt (no changes of
any kind) is unprobed and waits for a cell if a run ever lands into one.

#### Scenario: Bloated target, graduate held
- **WHEN** a sweep classifies a journal item `graduate` and its charter-selected target is
  an already-bloated reference doc
- **THEN** the apply step writes nothing into that doc; the graduation is recorded in the
  dated report with target + disposition, ROADMAP gains (or reuses) one open-line naming
  the pending split job and its shape, and the source entry keeps its dated why/when

#### Scenario: Stuff-then-ask is the named failure
- **WHEN** a rep applies a graduation into a bloated target and then surfaces the split as
  a question or note
- **THEN** that run has violated the rule: the ask does not retroactively license the
  stuffing

#### Scenario: Healthy target unaffected
- **WHEN** a graduate's target is a normally-sized reference doc in the same sweep
- **THEN** the promotion applies in that run exactly as before (no over-holding)

#### Scenario: Held work is tracked, not remembered
- **WHEN** the sweep ends with held graduations
- **THEN** the report + the ROADMAP split-job line (naming the script and the landing part)
  are sufficient for a later session (or `whats-next`) to run the split and land the
  promotions waiting on it

#### Scenario: A held promotion under a halt follows the halt's terms
- **WHEN** a held promotion's target project states a halt in its ROADMAP
- **THEN** the report names the halt beside the hold and sequences the landing by the halt's
  terms: a halt that admits documentation changes lets the landing follow the split; a halt
  on all work holds it until the halt lifts
