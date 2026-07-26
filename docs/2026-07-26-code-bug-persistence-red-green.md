# 2026-07-26 — code-bug-persistence RED/GREEN results

**Charter:** dated validation record for the `code-bug-persistence` change (AUDIT R27,
MAINTAIN M12/M13). Field origin: a MAINTAIN run on TSM (separate session, same day) surfaced
real code bugs with no in-schema channel and no disk persistence — findings died with the
chat. Fixture: TidePool extended with the CB1–CB4 plant class (`harness/catalog-tidepool.md`;
fresh plants, not derived from TSM specifics). All reps Sonnet; RED via Agent tool (effort
inherited), GREEN/micro via Workflow (effort pinned high). Orchestrator-context leak
disclosed per VERIFICATION rule 4 (bias conservative).

## RED — current deployed text (1 rep/arm; failure legible in both)
- **MAINTAIN:** rep FOUND the CB1 timeout violation and escalated in prose ("want this
  surfaced loudly … Recommend an audit pass / code fix") — but had no schema slot; the bug
  lived only in the chat deliverable's "didn't fit the schema" section. Disk: 5 files
  changed, zero bug record, no report, no ROADMAP line. Cardinal-sin check passed (entry not
  demoted); CB2 correctly unflagged. Failure class: omits-an-element → REQUIRED-slot fix
  form.
- **AUDIT:** discipline perfect — CB1 `flag-code-bug` via R7 with exact evidence, plus a
  genuine second contract bug (DOMAIN daylight window; see the two-defect catalog
  annotation) and a `revisit-plan`; R25/R14 held; zero violations. All three report-only
  findings then existed only in chat ("handed to whats-next" = listed in the final message).
  Same failure class.

## GREEN — candidate text injected (1 rep/arm + refactor rounds)
- **AUDIT (deferred path):** clean pass — dated `docs/2026-07-26-audit-report.md` with full
  evidence + verbatim adjudication record; exactly ONE ROADMAP pointer line; CB4 not
  duplicated; source untouched.
- **MAINTAIN v1 (survivors path):** CB1 persisted (ROADMAP line + report, entry intact),
  CB2 gate held, CB4 deduped — but over-triggered on the archived design doc's drifted
  weights (design-time values) and persisted a noise line. → REFACTOR 1: M12 gains the
  R15-mirroring carve-out ("design-time values … never contracts").
- **MAINTAIN v2 (amended):** carve-out honored (explicitly declined the archived-design
  drift), CB1 persisted — but parsed "or corroborated by another doc" as a *substitute* for
  guarantee language and bug-flagged the TTL history mismatch (CB2 axis; two dated records
  agreeing on an old value). → REFACTOR 2: corroboration **strengthens, never substitutes**;
  "history, not a contract" sentence.
- **Micro-test (final wording, 2 fresh-context reps):** 2/2 — timeout case flags, TTL case
  declines, both reps citing the exact tightened clauses. Shipped wording = post-micro-test
  text (meaning-preserving compression applied after validation, per the 2026-07-13
  precedent; all load-bearing clauses verbatim).

## Shipped
AUDIT **R27** (persistence: dated report + ROADMAP open-lines + deferred-pointer + dedup;
step 5 wired) and MAINTAIN **M12** (report-only channel, R7-mirror cardinal-sin protection,
two carve-outs) + **M13** (persistence) + schema `code-bug:` slot + step 4 wired. Word
deltas (same-method): AUDIT 1118→1197 (+79), MAINTAIN 568→~740 post-compression. Change
record: `openspec/changes/` → archive `code-bug-persistence`.

## Notable
- The GREEN wobbles were themselves the REFACTOR evidence — both carve-outs trace to
  observed failures, not speculation (iron law held through refactor).
- Per-run variance: v1 held the CB2 gate that v2 broke — 1-of-2 misparse on ambiguous
  wording is exactly what micro-testing variants is for.
- Rep counts: 1/arm RED + 1/arm GREEN + 1 refactor rep + 2 micro-reps (~0.6M subagent
  tokens total). Replicates are the cheap upgrade if field behavior wobbles.
