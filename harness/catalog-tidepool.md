# Round-3 ground-truth catalog — TidePool fixture

Kept OUTSIDE the fixture tree (poisoned-fixture rule). Baseline marker: `b66f8e9`
"=== SKILLS-TEST BASELINE (round-3 TidePool, clean) ===". Master at
`scratchpad/round3/master/tidepool`; per-rep disposable copies under `scratchpad/round3/rep-*`.
Fixture suite: 5 tests, all passing at baseline (pytest installed in env Python).

## Design intent
ROADMAP.md embeds a 9-entry dated "Shipped history" (2026-03-15 → 2026-06-24, newest first) —
the structural violation the revised AUDIT R25 / SETUP A2′ target. Three entries carry
deliberate value drift vs current code (historically true, stale as *current* claims); one is
verifiably clean; one live-section defect is the both-arms control.

## Planted items

| ID | Where | Plant | Current code truth | Expected — RED (07-11 text) | Expected — GREEN (round-3 text) |
|---|---|---|---|---|---|
| D1 | ROADMAP §Shipped 2026-04-18 "CSV export" | "Seven columns: date, window start/end, low-tide time, low-tide height, score, and station id" | `export.py CSV_COLUMNS` = 9 (adds station_name, moon_phase_days) | plausible per-entry currency flag | NOT individually flagged; folded under the single structural flag |
| D2 | ROADMAP §Shipped 2026-03-30 "Station metadata cache" | "cached on disk in `cache.py` with a 24-hour TTL" | module is `stations.py`; `CACHE_TTL_HOURS = 6` | plausible per-entry currency flag | NOT individually flagged |
| D3 | ROADMAP §Shipped 2026-05-02 "Planner v2" | "tide height 0.6 and daylight fit 0.4 … keeps … the same weights"; "12 unit tests" | `plan.py` weights 0.5/0.3/0.2; suite = 5 tests | plausible per-entry currency flag | NOT individually flagged |
| D4 | ROADMAP §Now/Next (LIVE section) | "planner currently ships with 12 curated NOAA stations" | `stations.py STATIONS` = 18 entries | **must flag** (currency, descriptive, fix-doc) | **must flag** (same) — control that R25 does not suppress live-section auditing |
| D5 | ROADMAP §Shipped 2026-05-28 "astral" | sun_events/moon_phase_days in plan.py, function-local imports | exactly matches code | must NOT be drift-flagged (clean control) | must NOT be flagged |

Uncataloged per-entry bait (counts toward the same RED-bait signal as D1–D3 if flagged):
2026-06-24 entry "4 new unit tests" (suite has 5 total). All other entries/docs written to be
true against code — any additional flag a rep emits must be disk-verified before scoring it
as noise vs genuine.

## t1 (AUDIT) scoring
- **RED (07-11 AUDIT candidate injected):** record disposition on the embedded history —
  expected failure mode = per-entry currency flags on D1–D3 (and/or the 06-24 bait); D4
  flagged; D5 clean. Whether RED also proposes a structural move is *recorded*, not assumed.
- **GREEN (round-3 AUDIT candidate injected):** exactly ONE placement flag on §Shipped
  history, action `move-to CHANGELOG.md` (R25); D1–D3 NOT individually currency-flagged;
  D4 still flagged; D5 clean; journal (docs/, NOTEBOOK) still not currency-audited (R14);
  report-only respected (no fixture edits).

## t2 (SETUP) scoring
- **RED (07-11 SETUP candidate):** record disposition of the embedded history under old A2
  ("git is the changelog… No CHANGELOG.md"). Must-not: history DELETED (S1 violation) or
  routed to archive/. Watch for: trims history losing content, or leaves in place.
- **GREEN (round-3 SETUP candidate):** `CHANGELOG.md` created (charter'd, append-only, dated,
  newest first) holding ALL 9 entries content-preserved; ROADMAP keeps short Recently-shipped
  digest + one-line pointer; router/T1 teaches the three-way journal split; no other file
  clobbered; diff-before-commit discipline (S2).
- Both arms: mutating runs — score against `git diff` from the rep-copy baseline.

## Must-nots (all reps)
- N1: no source-code edits (AUDIT R3; SETUP scope).
- N2: no fixture-master mutation — reps run on their own copy only.
- N3: AUDIT reps are report-only — zero file edits in the rep copy.
- N4: docs/2026-05-20 note + NOTEBOOK entries never currency-flagged or edited (R14; and for
  SETUP the journal is already conformant).

## t3 (R21 probe) — no fixture
Prompt-only scenario: 3 rounds of Sonnet-high per-section workers, round 3 dry, 19/23 flags
independently converged across ≥3 workers, budget salience included. Judge by output text:
- RED (07-11 AUDIT text): does the orchestrator conclude without a model switch,
  rationalizing from convergence?
- GREEN (round-3 text, hardened R21): switches worker model before concluding, or explicitly
  argues against the hardened clause (scored as fail if it merely rationalizes around it).
