# 2026-07-26 — maintain-right-sizing RED/GREEN results

**Charter:** dated validation record for `maintain-right-sizing`. Origin: TSM field
feedback (12:1 add:remove ratchet; same-day ritual sweeps — NOTEBOOK 2026-07-26). Fixture:
TidePool + PR1–PR3 cells (`harness/catalog-tidepool.md`); TSM is deriving evidence
(poisoned). Reps Sonnet-high via Workflow.

## Gating outcomes — two halves no-failed, one shipped (iron law working as intended)
- **Description rewording ("periodic" → triggers): NO-FAIL 0/2.** Both invocation probes,
  judging from the *current* description alone, declined a low-yield sweep (2 h after the
  last, one archived change since) — "far too soon to count as a periodic check." Agents
  already right-size invocation; the TSM double-run stays field-only evidence. No text
  ships; DOMAIN § When-to-reach remains the trigger guidance's home.
- **Mandatory dedicated prune pass: NO-FAIL.** The RED rep found both planted prune cells
  unforced — PR1 (shipped item still in Now/Next) struck with a candid scope note, PR2
  (spent Monterey entry) archived. Findability doesn't fail at fixture scale; the 12:1
  ratio remains a scale phenomenon with no synthetic reproduction. No mandate ships.
- **Report accounting (PR3): RED confirmed → M16 ships.** The RED rep's report itemized its
  prunes ad hoc but stated **no net reference-tier delta anywhere** (grep-verified) and
  carried no contract that a no-prune run would say so — the ratchet is invisible without
  diffing. Classic omission → REQUIRED slot.

## GREEN (1 on-disk rep, M16 injected)
Report closes with a dedicated "Accounting (M16 — required)" section — prune/archive
candidates itemized (1 archived, 2 trimmed, 1 struck) + the net reference-tier delta —
disk-verified. Regressions clean across the whole M-stack in the same run: M9/M14 checks,
M11 cross-ref-only, M12 gates (design-time values unflagged; "fix queued" correctly read
as acknowledged-TODO not violation), M13 persistence, M15 portfolio check ("none found"
noted). Sources untouched where required; code untouched; suite passes.

## Shipped
MAINTAIN **M16** (required report accounting slot: prune candidates or explicit none +
net reference-tier delta) + procedure step 4 tail. Description and forced-pass halves:
status-noted in the delta spec, not shipped. Change record:
`openspec/changes/archive/2026-07-26-maintain-right-sizing`.

## Notable
- Two of three proposed teeth failed RED and were dropped — the leanest outcome of the
  day's five changes, and the right one: the visibility lever (accounting) shipped, the
  unproven behavior mandates didn't. The 12:1 ratchet now gets a per-run number the user
  reads; whether that alone bends the curve is a field question for future sweeps.
