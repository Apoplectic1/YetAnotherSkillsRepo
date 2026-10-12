# maintain-tools-first: design

## Context

The third trim of 2026-10-12, after SETUP and AUDIT. MAINTAIN's prose carried the most
arithmetic a worker was told to do by hand (what is past budget, which rolled files are newer
than the last watermark, which archived designs exist) and the one output reps had reliably
omitted (the report's accounting slot, PR3). The design doc's "Tools over prose" part states
the shape; this change closes it for the family.

## Decisions

- **D1: two modes, before and after.** The sources mode prints what the sweep slices and
  what it must do first (roll a journal past budget, hold a promotion into a target past
  budget); the check mode reads the run's own report back and says which required line is
  missing, by rule. A lint on the run's output is the only way the accounting slot stops
  being a sentence the rep has to remember.
- **D2: the watermark is read, not remembered.** The newest `docs/*maintain-report*.md`
  names the newest rolled file the last sweep covered; the script lists the rolled files
  newer than it as the slices (M19) and says "every file is a slice" when no report exists.
- **D3: a rule is its action plus one boundary.** M17 names `rollover.py` and its two
  switches and what breaks (a line-anchored pointer); what the dry run lists is the dry run's
  to say. M16 names the three lines and the check that reads them. The rationale goes to the
  design doc.
- **D4: what the script does not judge.** Whether an entry is standing truth, which charter
  owns it, whether a contract claim has guarantee language, and whether a halted target's
  terms admit a landing stay prose and judgment (the s8-field-fixes status note stands).
- **D5: the regression gate**, as for the other two: no RED, one plan-only rep per family, a
  failing cell names the clause restored.

- **D6: the check counts no negation.** The reps' first run showed the check counting "Held
  promotions: none" as a hold and "flag-code-bug: none" as a flag, so three of them wrote
  around it; a line that says none, no or nothing beside the word does not count, and the
  `empty/` fixture holds that case.

## Verification

Script-level: `sweep.py` byte-exact on three fixture copies in the sources mode and on three
crafted reports in the check mode. The regression GREEN per D5: five plan-only reps (446k
tokens), PR1 to PR3, CB1, CB2, CB4, O2 to O4, FA1, FA2, RO1 to RO5, PL1 and PL2 held, L1
noticed; nothing restored. The record:
`docs/2026-10-12 - maintain-tools-first-regression.md`.
