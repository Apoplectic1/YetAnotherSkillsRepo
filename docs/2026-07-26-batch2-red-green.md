# 2026-07-26 — batch-2 RED/GREEN results (derivability-discriminator + m9-hold-on-bloat)

**Charter:** shared dated validation record for the batched changes `derivability-discriminator`
(AUDIT R28) and `m9-hold-on-bloat` (MAINTAIN M9 hardened + M14). One session, two independent
RED/GREEN rounds, one deploy. All reps Sonnet-high via Workflow (effort pinned). Fixtures:
TidePool + new DV/FA plant classes (`harness/catalog-tidepool.md`); fat-ARCH variant at
`harness/tidepool-fixture-variants/fat-arch/` (25.7 KB, essays 93%, code-true). Orchestrator
context leak disclosed per VERIFICATION rule 4.

## derivability-discriminator (AUDIT R28)
- **RED (4/4 re-cache):** 2 micro-probes + 2 incidental full-rep observations — every rep
  fix-doc'd "12→18" with clean R5/R6/R8 reasoning; none questioned the count's presence.
  DV1 rationale-TTL control clean. Failure class: compliant-but-wrong-fix-shape →
  conditional + positive recipe.
- **GREEN (2 micro 3/3 cells each + 1 on-disk):** station count de-valued on disk
  ("a curated NOAA station registry", update offered as alternative); drifted
  rationale-bearing TTL got the normal value fix (no over-fire); daylight contract →
  `flag-code-bug`, never fix-doc'd. R25/R27 regressions clean (CHANGELOG created, report +
  ROADMAP persistence held).

## m9-hold-on-bloat (MAINTAIN M9′ + M14)
- **RED, composite:** field 1/1 stuff-then-ask (TSM: 3 graduations into a 38 KB doc, split
  asked after); prompt-framed probes 0/2 (rule holds when bloat facts are handed over —
  fat-router scale lesson); **on-disk 1/1 stuff-silently** (rep graduated FA1 into the
  25.7 KB fat doc, 25,734→26,859 bytes, zero split mention anywhere — it read the fat
  essays yet never evaluated the target). Mechanism: a *noticing* failure at apply time,
  not ignorance — hence M9's explicit apply-time check. Plus probe disposition split 1/1
  (one improvised a ROADMAP line "per the spirit of M13", one left the hold chat-only) —
  the unpinned-procedure non-determinism M14 pins.
- **GREEN (2 probes + 1 on-disk):** FA1 held — fat ARCH **byte-identical**, hold recorded in
  the dated report (claim + target + disposition), exactly one ROADMAP split-job line,
  source entry intact; FA2 applied normally (no over-holding); probes 2/2 incl. correct
  dedup-across-holds. M12/M13 rode along clean throughout.

## Shipped
AUDIT **R28** (fix-or-delete discriminator, Currency section) and MAINTAIN **M9** hardened
in place (apply-time content test + stuff-then-ask red-flag) + **M14** (hold procedure on
M13 rails). Word deltas within precedent. Change records: `openspec/changes/archive/`
`2026-07-26-derivability-discriminator` + `2026-07-26-m9-hold-on-bloat`.

## Notable
- The M9 evidence pattern (framed-probe pass, at-scale fail) repeats fat-router-lean
  exactly — second confirmation that scale-dependent failures need on-disk reps; prompt
  probes alone would have hit the no-failure gate and wrongly shelved the fix.
- The GREEN m9 on-disk rep independently reproduced TSM's split *recommendation* (lean
  mechanics doc + design-rationale doc) in its ROADMAP line — the held-promotion pipeline
  reads naturally to a fresh agent.
- Rep economy: ~0.7M subagent tokens for both rounds combined (probes carried half the
  evidence at ~1/15 the cost of full reps).
