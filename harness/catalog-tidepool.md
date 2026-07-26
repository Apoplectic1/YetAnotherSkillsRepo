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

## Openspec-archive extension (added 2026-07-26, change `openspec-archive-awareness`)
Planted for the archive-awareness RED/GREEN runs. Ground truth:

| ID | Where | Plant | Expected — RED (current deployed text) | Expected — GREEN (candidate text) |
|---|---|---|---|---|
| O1 | `openspec/changes/archive/2026-06-08-three-factor-scoring/design.md`, cited from ARCHITECTURE §Design constraints | Drifted code-coupled facts: weights "0.5/0.35/0.15" (code: 0.5/0.3/0.2), phase normalization "7.0" (code: 7.4), falloff "zero at +3.0 ft" (code: 2.5). Reasoning itself still sound (matches DOMAIN syzygy claims). | AUDIT: workers follow the citation; expected failure = tier-violation / misplacement flags on the code-coupled facts (or currency flags). Record verbatim. | AUDIT: decision-consistency check only; ZERO tier-violation/currency flags on O1 facts; file never edited. Consistency verdict: reasoning sound → no flag. |
| O2 | `openspec/changes/archive/2026-06-20-station-curation/design.md` — UNCITED, D1 "curated by hand, permanently" + 3-item access checklist | Standing policy absent from reference tier (ARCHITECTURE says nothing on why-curated; DOMAIN nothing on admission criteria). | MAINTAIN: expected failure = archive not swept at all (journal = docs/ + NOTEBOOK only; router brands openspec/ excluded). | MAINTAIN: O2/D1 classified `graduate` (target ARCHITECTURE or DOMAIN — either defensible), disposition `cross-ref` with the pointer written in the reference doc; archive file byte-identical. |
| O3 | Fixture `CLAUDE.md` "Excluded from the doc set — openspec/" (old blanket wording) | The nudge the override clause targets. | MAINTAIN: old wording reinforces the O2 miss (record whether the rep cites it). | MAINTAIN: sweep proceeds despite the router note (override clause honored); router may be left as-is (healing it is setup's job, not maintain's). |
| O4 | `2026-06-08` design.md D1 rationale — CITED from ARCHITECTURE | Cited cold rationale. | — | MAINTAIN: classified `keep` (M2 — intentional cold-rationale a reference doc cites), NOT graduate; distinguishes cited vs uncited archive content. |

Scoring notes: three-factor design.md drifted facts are design→implementation drift, normal
for archived designs — any GREEN flag on them is a fail. MAINTAIN reps are report-through-
adjudication (flag list) runs; if a rep applies, score the applied tree. O1–O4 leave D1–D5
expectations unchanged.

## Code-bug-persistence extension (added 2026-07-26, change `code-bug-persistence`)
Planted for the CB RED/GREEN runs (MAINTAIN primary; AUDIT persistence). Not derived from the
TSM field finding — fresh plants on the TidePool fiction. Ground truth:

| ID | Where | Plant | Expected — RED (current deployed text) | Expected — GREEN (candidate text) |
|---|---|---|---|---|
| CB1 | NOTEBOOK 2026-07-04 entry (contract: `fetch_predictions` **must always** carry 30 s timeout + `raise_for_status`) vs `tides.py` — `timeout=30` removed from the `requests.get` call (`raise_for_status` still present) | Journal contract with explicit must/never language, corroborated by ROADMAP §Shipped 2026-04-05 + NOTEBOOK 2026-04-02 Monterey story; code violates the timeout half | MAINTAIN: no in-schema channel — record verbatim how the rep handles it (expected failure modes: ignores the mismatch; reclassifies the entry stale/archive **(cardinal sin)**; improvises out-of-schema). Persistence: nothing lands on disk | MAINTAIN: entry classified on its own merits (`keep`) AND a report-only `flag-code-bug` emitted citing the claim + `tides.py` callsite (timeout specifically; `raise_for_status` present — evidence precision). Entry NOT demoted for the mismatch |
| CB2 | NOTEBOOK 2026-07-01 perf note — "24-hour metadata cache TTL" (code: `CACHE_TTL_HOURS = 6`, D2's drift axis) | Plain incidental drift, zero contract force | Must NOT be code-bug-flagged (either arm) — a dated observation is not made false by later code change | Same must-not: classify normally (`keep`), no `flag-code-bug`. Discrimination control vs CB1 |
| CB3 | Fixture ROADMAP open section ("Now / Next") — at baseline contains **no** line about CB1's defect | Persistence observability cell | RED: after a full run through apply, disk shows no dated report + no ROADMAP line for CB1 (the loss being fixed) | GREEN: dated `docs/YYYY-MM-DD-<skill>-report.md` exists in the rep copy carrying every report-only flag + evidence; one line per adjudicated-surviving bug in ROADMAP's open section (Now / Next or a new Open subsection — either defensible); deferred-adjudication variant → single pointer line to the report |
| CB4 | ROADMAP Now / Next "Known bug (2026-06-26 …) `low_tides()` passes every L row through" + NOTEBOOK 2026-06-26 decided-must entry; code indeed doesn't filter | Already-tracked defect (dedup cell) | — | GREEN: the flag may appear in the report, but ROADMAP gains **no duplicate line** — the existing Known-bug line stands (dedup honored). Adding a second line for the same defect = fail |

Scoring notes: CB1's corroborating ROADMAP 2026-04-05 entry now also drifts vs code (timeout
claim) — under AUDIT that is R7 contract territory (`flag-code-bug`), NOT R25-folded plain
drift and NOT `fix-doc`; record which way reps jump. CB plants leave D1–D5 and O1–O4
expectations unchanged. Fixture suite still 5 tests, all passing (plants touch no tested
code path).

## Genuine-drift annotation (2026-07-26): the DOMAIN daylight-contract violation is TWO defects
The pre-existing kept drift ("hard 0 after sunset" vs code) decomposes — credit reps that
separate them, note reps that lump them:
- **(a) scope mismatch** — the DOMAIN safety rule constrains a *window*; `daylight_fit_factor`
  (plan.py) evaluates the low *instant*, while cli.py builds low ± 1 h. Correct predicate is
  containment ([low−1h, low+1h] ⊆ [sunrise, sunset]), not membership of the midpoint.
- **(b) shape mismatch** — doc says "a hard 0 … not a discount"; the code's <1 h-margin ramp
  returns ≈0.5. Falsifiable from plan.py alone.
- **Interaction (the expert read):** (b) masks (a) — the accidental ramp depresses scores
  exactly where the instant-check is least trustworthy; fixing (b) alone (true hard 0 at the
  instant) makes a low 30 min before sunset score 1.0 while its window spills past sunset — a
  safety regression dressed as doc-compliance. A rep filing them as one item + one fix is
  scoring below ground truth. Also note the test suite inherits the code's misconception
  (checks the instant), so green tests can't catch either — evidence for the family's
  docs-vs-code-as-separate-pass thesis.

## Derivability extension (added 2026-07-26, change `derivability-discriminator`)
For the AUDIT R28 fix-or-delete rounds. DV2 reuses D4 (no new plant).

| ID | Where | Plant | Expected — RED (current text) | Expected — GREEN (R28 candidate) |
|---|---|---|---|---|
| DV1 | ARCHITECTURE.md module map — `CACHE_TTL_HOURS = 6` now carries its rationale inline ("deliberately short of a day: NOAA re-fits harmonics within hours after storms; 6 h keeps a same-day return trip fresh") | Rationale-bearing derivable value (control) | Value matches code — no flag either way | Must NOT receive a deletion/de-value proposal in any rep; the attached rationale disqualifies it from R28's reach. A deletion proposal here = over-fire, fail |
| DV2 | = D4 (ROADMAP Now/Next "12 curated NOAA stations" vs 18 in code) — rationale-free derivable count | Existing plant, reused | fix-doc re-caching the value (every rep to date did exactly this — the RED baseline) | Flag unchanged (still fired, still evidenced — D4's live-section-control role intact); the proposed fix LEADS with removal/de-valuing ("a curated station registry"), value-update offered as the stated alternative. A bare update-to-18 = R28 miss |

## Fat-ARCH variant (added 2026-07-26, change `m9-hold-on-bloat`)
Separate variant, swapped at copy time (fat-router precedent): copy the standing fixture,
replace `ARCHITECTURE.md` with `harness/tidepool-fixture-variants/fat-arch/ARCHITECTURE.md`
(24–30 KB; four feature-design sections dominate; every code-coupled value true to src
except the original's single 30 s-timeout drift line, which rides along unchanged), prepend
the two entries in `tidepool-fixture-variants/fat-arch/NOTEBOOK-append.md`, then git init +
baseline as usual.

| ID | Where | Plant | Expected — RED (current text) | Expected — GREEN (M9-hardened + M14) |
|---|---|---|---|---|
| FA1 | Variant NOTEBOOK 2026-07-08 (CO-OPS resilience policy — decided, standing) — charter target = the bloated ARCHITECTURE.md | Graduate whose target is bloated | Expected failure: promotion applied INTO the fat doc (stuff-then-ask or stuff-silently); capture verbatim rationale | Promotion HELD: fat ARCHITECTURE byte-identical; graduation recorded in the dated maintain report (claim + target + disposition); ROADMAP gains exactly ONE open-line naming the pending split job; source entry keeps its why/when |
| FA2 | Variant NOTEBOOK 2026-07-06 (scoring-regression-test practice — decided, standing) — charter target = VERIFICATION.md (healthy, ~1 KB) | Over-holding control | Applies normally (record) | MUST still apply in the same run — holding FA2 = over-fire, fail |

Scoring notes: CB/O/D expectations ride along unchanged in the variant tree. The fat doc's
essays are deliberately placement-suspect — a rep *flagging* the bloat/split (report or
ROADMAP line) is correct at any stage; only *writing more content into it* is the failure.

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
