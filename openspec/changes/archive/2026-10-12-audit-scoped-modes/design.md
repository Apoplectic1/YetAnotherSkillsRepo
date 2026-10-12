# audit-scoped-modes: design

## Context

AUDIT's coverage rules (R18, R20, R21, Procedure step 3) are unconditional by design: the
2026-06-28 RED showed one pass finds about half the real issues, and the 2026-06-29 benchmark
showed one model loops to its own ceiling. Two field needs sit outside that: a cheap check
at a release close (the HDL sweep's phrase lens, 188k tokens for 13 corrections against 2.6M
for the full sweep) and a one-round run on a small, recently written set (the 2026-07-17
scaled-coverage item, shape refined and gated). The ROADMAP left the home to the owner, who
chose (2026-10-12) to ship both as named modes in AUDIT, one change.

## Decisions

- **D1: two named modes, one rule.** `release-close` is one lens over the reference tier for
  the phrases a release leaves behind ("waits for", "not yet", "until", "today",
  "currently", "pending", "in progress", a version, a count) plus the R19 cross-reference
  pass. `small-set` is one per-section round plus the cross-reference pass for a set that is
  small and low-drift. Both: one round at the R22 default tier, no loop, no model switch,
  every other rule intact. The companion edits are identical (R18's exception clause,
  Procedure steps 1 and 3), so they share R29.
- **D2: invoked by the user, never chosen by the run.** The run must not decide on its own
  to go cheap; a user who names a mode, or asks for one round or a cheap run, has invoked
  one, and the run names which fits and says so. Without that, "audit" means the full loop.
  (The first candidate said "by name"; RED's prompts said "one round" and "cheaply" without
  naming anything, which is how a user talks, so the clause widened before GREEN.)
- **D3: the coverage note carries the mode.** A scoped run's report names the mode and what
  a full run would have added (the further rounds, the model switch), so the lower bound is
  visible to whoever reads it later. RED's reps all disclosed the gap by extending R23 on
  their own judgment; the text now sanctions exactly that.
- **D4: cost comes from fewer rounds, not a weaker tier.** All four RED reps read "cheaply"
  as fewer rounds and kept the R22 default tier, citing R22's warning that cheap tiers skip
  sections and mislabel actions. The mode text pins the tier so that reading is the only
  one.
- **D5: the number.** R29 is the next free number in the skill. The archived
  `audit-scope-from-routers` design record labels its unshipped ancestor-router candidate
  "R29"; that label is not a claim on the number, and the candidate takes the next free one
  if it ever ships.

## What RED showed (2026-10-12)

Four single-agent reps on the current text, prompt-only: two "a release just closed, run it
cheaply, one round" on the `release-lens` overlay, two "one round only, no model switch" on
the plain fixture. All four: "the skill text gave me no sanctioned way"; all four ran one
round on the user's word and disclosed R18, R20 and R21 unmet by extending R23's visible-gap
principle ("that extension is mine, not a sanctioned path"). The overlay's six plants were
found 6/6 by both reps; the controls held, except RC3 placement-flagged once as off-charter
for ARCHITECTURE (a plant-design flaw, not a currency miss). Cost per rep was the same as
the plain-fixture reps (105k to 118k tokens): the lens's saving is in the fan-out (one
worker against per-section workers) and a single-agent rep cannot show it.

## Verification

Single-agent reps (report-only, no spawning), Sonnet: RED 4, GREEN 4 with the candidate and
the same prompts. GREEN passes when the rep names the mode it is in, runs one round, finds
RL1 to RL6 (release-close) or D4 with D1 to D3 folded under R25 (small-set), holds the
controls, and ends with a coverage note naming the mode and what a full run would add.
Record: `docs/2026-10-12 - audit-scoped-modes-red-green.md`.
