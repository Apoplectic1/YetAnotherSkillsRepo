# AUDIT scoped modes: RED/GREEN record (2026-10-12)

Change `audit-scoped-modes` (the ROADMAP's "Release-close currency lens" and "AUDIT
scaled-coverage mode", shipped as one rule, R29). Fixture: TidePool, plain for the
`small-set` reps, with the `release-lens` overlay for the `release-close` reps
(`harness/tidepool-fixture-variants/release-lens/`; cells in `harness/catalog-tidepool.md`).
Method: single-agent reps as orchestrator and only worker (report-only, no spawning), Sonnet,
each on its own baselined copy; every copy byte-untouched afterward (one rep's `python -c`
left gitignored bytecode). Prompts, verbatim: "Our 0.6 release just closed. Run the docs
audit cheaply: one round, I don't want the full loop today." and "Small project, the docs
were written recently. Audit it, but one round only please, and no model switch." About
0.9M tokens for eight reps, 105k to 118k each.

## Cells and results

| Cell | Plant or probe | RED (current text) | GREEN (candidate) |
|---|---|---|---|
| SM2 | the release-close ask | 2/2 "the skill text gave me no sanctioned way"; one round on the user's word; R18, R20, R21 disclosed unmet by extending R23 ("that extension is mine, not a sanctioned path") | 2/2 named `release-close`, rejected `small-set` ("a just-closed release is the opposite of low-drift"); one lens round plus cross-ref; the coverage note names the mode and what a full run adds |
| SM1 | the one-round ask | 2/2 the same: "no sanctioned way", one round, disclosed by judgment; "whether the skill should have declined or asked first is unclear" | 2/2 named `small-set` ("the user's request did not override a rule, it triggered one"); one per-section round plus cross-ref; the note names the mode |
| RL1 to RL6 | six post-release phrasings the code has moved past | 6/6 found by both reps | 6/6 found by both reps, R28 leads on the version and the counts, a normal fix on the gotcha |
| RC1, RC2 | a prescriptive "Next" and a "future NDBC factor" | held 2/2 | held 2/2 |
| RC3 | "Offline harmonics wait for a local source" in ARCHITECTURE | held on currency 2/2; one rep placement-flagged it as off-charter for a how-it-works doc (fair: a plant-design flaw) | held 2/2 |
| D1 to D5, PR1, CB1 | the base plants, in the small-set reps | D4 `fix-doc` (R28 lead), D1 to D3 folded under R25, PR1 `graduate`, CB1 and the daylight contract `flag-code-bug`, 2/2 | the same, 2/2 |

## What RED taught

- **The failure was the absence of a path, not a wrong action.** All four reps read the
  coverage rules as unconditional, said so with the rules quoted, and then did what the mode
  now prescribes: one round at the default tier, the gap disclosed in the coverage note.
  R22 was the nearest rule each found ("a first sweep only"), and each rejected it as a
  license to stop. The text's job was to sanction the disclosure and name the shape.
- **"Cheaply" meant fewer rounds to every rep, never a weaker tier**, each citing R22's
  warning about cheap tiers. The mode pins the tier so that stays the only reading.
- **Cost does not show at single-agent scale.** A release-close rep cost the same as a
  plain-fixture rep (105k to 118k). The lens's saving is one worker against per-section
  workers in a fan-out; a rep that is its own only worker reads everything either way.
- **A probe's working directory must stay out of the fixture.** `openspec new change` ran
  with the shell's directory drifted into `harness/tidepool-fixture/` and scaffolded the
  change there, so the four RED copies carried a README naming "scoped modes as sanctioned
  exceptions". All four reps saw it and gave it no authority (unrouted tooling, R13); the
  master was untracked and moved back; the GREEN copies were rebuilt clean.

## What GREEN taught

- **The widened invocation clause held.** The first candidate said "invoked by name"; RED's
  prompts never named a mode, so before GREEN the clause became "names one, or asks for one
  round or a cheap run and the run names which fits and says so". All four GREEN reps named
  the right mode on that clause and said so first.
- **Two behaviors the text does not state, done the same way by both reps of a pair
  (no-failure, recorded here, not encoded):** the release-close reps kept verified findings
  outside the lens (a missing timeout, the daylight contract) and labeled them incidental,
  asking whether to suppress them; the small-set reps noticed the round found more drift
  than "low-drift" promises (8 flags, 2 contract violations in 5 small docs), said so in the
  coverage note, and recommended a full run. If a future run suppresses an incidental
  contract violation, or runs `small-set` on a drifting set without saying so, encode then.
- **Open questions the reps raised, not acted on:** a tie-break when both modes fit; whether
  "one round, no model switch" alone (loop, no switch) deserves a shape; whether the run
  should confirm the mode before running; whether "a count" covers a constant like "30 s".

## Shipped

R29 (two scoped modes), R18's exception clause, Procedure steps 1 and 3; DOMAIN § When to
reach names `release-close` as the shift-left for currency; the design doc's coverage section
gets its dated addendum; the audit spec an ADDED requirement. The scaled-coverage item's
"field R26" alias retires with it.
