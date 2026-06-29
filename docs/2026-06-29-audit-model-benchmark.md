# AUDIT worker-model benchmark — findings

**Charter — empirical record of how the `docs-architecture-audit` skill performs across worker
models and iterations.** Captures method, ground-truth issue catalog, per-model/per-rep scores, and
conclusions that inform the model recommendation for AUDIT's fan-out workers. Raw flag data lives in
`docs/audit-benchmark/*.json`. Dated record; append new experiments, don't rewrite old ones.

## Why this exists
AUDIT's thesis (see `docs-architecture-design.md`): *a single careful pass finds only ~half the real
issues, non-deterministically; coverage comes from a fan-out + loop-until-dry, not single-pass model
quality.* If that holds, a **cheaper worker model iterated more** should converge to the same
ground-truth as an expensive model — trading model cost for iteration cost. These experiments test
that on a real fixture.

## Method (constant across experiments unless noted)
- **Fixture:** `E:\Projects\AI\TargetPlanner` at the **post-SETUP restore point** (commit `0080879`)
  — a close-to-worst-case copy with known drift + planted issues. Reset contract:
  `git reset --hard 9034e6f && git clean -fd` returns it to pristine pre-SETUP baseline.
- **Orchestrator:** Opus (held constant). Only the **worker model** varies.
- **Fan-out:** fixed — 6 per-section workers over `CLAUDE.md` (glossary, conventions, architecture,
  deps-build, core-contract, docmap) + 1 cross-reference worker. **Single round per rep** (not
  loop-until-dry — deliberately, so the only variable is model/rep).
- **Workers:** read-only `Explore` agents (fixture provably unmutated), `effort=high`, forced to the
  AUDIT flag schema.
- **Held constant — sibling library absent:** the `Astronomy.Core`/`NINA` sibling isn't in the
  fixture. Workers are instructed to mark dependent claims `unverifiable → ask user`, never guess.
  This makes the honesty axis (honest-unverifiable vs guessing) a measured signal.
- **Scoring:** the Opus orchestrator adjudicates every flag against the source, dedups into the
  issue catalog below, and scores **recall** (real issues found) + **precision** (false positives).
  Ground truth = adjudicated union of all runs + the planted positive; all findings are code-cited.

## Ground-truth issue catalog (from Exp 1; grows as reps accumulate)
23 **solid** issues (high-confidence, actionable) + 4 **soft** (minor / judgment / needs-user).
Columns: which Exp-1 model found it (O=Opus, S=Sonnet, H=Haiku).

| ID | Issue | O | S | H |
|---|---|:-:|:-:|:-:|
| C1 | `ChartEvaluation` now 3-field (EnsureWork/RenderWork), not "single-field" | ✓ | ✓ | ✓ |
| C2 | `DayWindowKey.Range` member does not exist | ✓ | ✓ | ✓ |
| C3 | yearDays axis keyed by `Target` only, not `(Location,Target)` | | ✓ | ✓ |
| C5 | `EnsureAsync` gained a 3rd `IProgress` param; coordinator threads progress | ✓ | | |
| C6 | `Sky` `Log.Diag` category retired (no callsite) | ✓ | | ✓ |
| C7 | Velopack `0.0.1298` → actual `0.0.1589-ga2c5a97` | ✓ | ✓ | ✓ |
| C8 | "AnyCPU" configs stale — project is x64-only | ✓ | ✓ | ✓ |
| C9 | "one project authored here" → two (incl. `.Tests`) | ✓ | ✓ | |
| C10 | "two sibling-library projects" → three in sln (Core/XISF/NINA) | ✓ | | |
| C11 | Missing 3rd `ProjectReference` `Astronomy.Diagnostics` | ✓ | ✓ | |
| C12 | `Button_Graph_Click` "single render entry point" understates the `RunGraphBuildAsync` funnel | ✓ | ✓ | ✓ |
| C13 | `RenderArea` is 4-step (omits `ResizeAltitudeChartArea`) | | ✓ | |
| C14 | `mFormClosingCts` observed at 2 sites, not "only at WhenAny" (`TargetScanner.ScanAsync`) | | ✓ | |
| C15 | `DayWindowKey` used in 4+ places, not "only inside `ChartLayout.BuildDayWindow`" | | ✓ | |
| C17 | DiagnosticsDialog OK-button screenshot routes via shared `ScreenCapture`, not direct `CopyFromScreen`; doc self-inconsistent | | ✓ | |
| P1 | Build bullets stranded under "Tool preference", leaving "Build / run" empty | ✓ | ✓ | ✓ |
| P2 | "Core consumer contract" is reference-grade — belongs in ARCHITECTURE/DOMAIN, not the router | ✓ | ✓ | |
| X1 | **(planted)** dangling parent `..\CLAUDE.md` reference | ✓ | ✓ | ✓ |
| X2 | `ROADMAP.md` link to `docs/code-quality-audit.md` — rename-orphan (SETUP-created) | ✓ | ✓ | ✓ |
| X3 | `README.md` `docs/screenshot.png` dangling image | ✓ | ✓ | ✓ |
| X4 | `ARCHITECTURE.md` dangling anchor `#sky-brightness-day-sky-sub-mode` | ✓ | ✓ | |
| X5 | `.cs` comments still cite renamed `code-quality-audit.md` (report-only) | ✓ | | ✓ |
| X6 | `.cs` comment cites missing `mode-removal-against-current-dev.md` (report-only) | ✓ | | |
| **Solid recall** | **/23** | **18** | **18** | **12** |

Soft issues: **C4** cache pre-pop "2–4 s" vs code-comment "1–2 s" (perf unverifiable; O=keep, S=fix);
**C16** `PlanningPolicy` `MaxOfHorizonProfile` floor-gate phrasing (S); **C18** `docs/design/*.md`
naming convention overstated (S); **C-loc** sibling-lib absolute path possibly stale post-move (O).

## Experiment 1 — model comparison (single round, high effort)
Run `wf_1086285c-9b2` (task `wf0ozweuh`), 21 agents, 1.29M tokens, ~7.5 min. Raw:
`docs/audit-benchmark/exp1-model-compare.json`.

| Metric | Opus | Sonnet | Haiku |
|---|---|---|---|
| Flags emitted | 25 | 23 | 13 |
| Solid recall (of 23) | 18 | 18 | 12 |
| Recall incl. 4 soft (of 27) | 20 | 21 | 12 |
| **False positives** | 0 | 0 | 0 |
| Correct `unverifiable` (absent lib) | 4 | 1 | 0 (skipped section) |
| Action/modality mislabels | 0 | 0 | ~3–4 |

**Findings:**
- **No cry-wolf at any tier** — zero fabricated findings; **no model committed the skill's cardinal
  sins** (none flagged a forward plan as stale; none `fix-doc`'d a contract violation). Guardrails
  hold even on Haiku.
- **Sonnet tied Opus on solid recall (18=18)** but on *different* subsets — overlap 13/18 (~72%),
  each found 5 unique, neither alone reached the union of 23. Sonnet's uniques (C13/C14/C15/C17) are
  the *deepest* architecture catches; Opus's uniques (C5/C6/C10/X5/X6) skew to the cross-ref tail.
  This is the "independent passes find different ~halves" signature — across models.
- **Opus cleanest on discipline:** held absent-library Core claims as `unverifiable` *with
  consumer-callsite corroboration* (4 honest dispositions); used `flag-code-bug` correctly for stale
  `.cs` comments.
- **Haiku ~52%:** caught the high-signal/obvious drift but missed subtle currency, **skipped the
  absent-lib section entirely** (coverage hole), and **mislabeled actions** (`fix-doc` on a `.cs`
  comment it can't edit; `cross-ref+delete` for a dangling image; evidence overreach). Its errors are
  quality/discipline, not false alarms — and **iteration won't fix discipline**, so Haiku is a cheap
  first-sweep at best, not a convergence candidate.
- **Composition win:** the cross-ref pass caught two orphans *SETUP itself created* an hour earlier
  (the ROADMAP link + `.cs` comments to the renamed audit doc) plus the planted parent-ref — concrete
  evidence the SETUP→AUDIT pipeline closes its own loops.

**Caveats:** N=1 per model (no within-model variance measured); "ground truth" is union-of-3 so recall
is vs *best-known*, not truth (skill says truth is ~30% larger still); Opus adjudicated (mild
Opus-favorable bias, mitigated by code citations).

## Experiment 2 — convergence (Opus vs Sonnet, high effort, replicate reps)
**Status: running** — `wf_2b4223ef-f77` (task `wybmpvx1w`), 42 agents (Opus+Sonnet × rep1–3 × 7
workers). Reuses Exp-1 high-effort runs as rep0 → 4 reps each.

**Hypothesis under test:** Sonnet iterated-to-dry converges to the same ground-truth union as Opus
iterated-to-dry (worker tier). Reframe vs naive form: convergence is to the **union**, not to
"near-identical runs" — two Opus runs wouldn't be identical either.

**What Exp 1 already licenses:** Sonnet has *no per-pass recall deficit* (18=18), so there's no
capability gap for iteration to overcome — encouraging but not proof.

**Data provenance (read this — it affects nothing in the numbers but explains the run count):**
The first convergence run `wf_2b4223ef-f77` (`wybmpvx1w`) had **12 of 42 workers fail on a session
rate-limit** (Sonnet rep2×4, rep3×7; Opus rep3×1). The backfill `wf_0be84d4b-bc0` (`w02p76xdr`) was
*intended* to re-run only those 12, but `args.cells` did not restrict it and it **re-ran the full
42-cell matrix** (~2.67M tokens, unintended cost). Upside: that rerun was clean (all 42 succeeded),
giving a self-consistent rep1–3 matrix. **Scored dataset = rep0 (from Exp 1) + rep1–3 (from the
clean rerun) = 4 reps/model.** Raw: `raw/exp2-fullrerun-w02p76xdr.output.json`; scored summary +
classifier: `exp2-convergence.json`, `score.py`.

### Results (solid issues only; classifier-scored)
Per-rep single-pass recall, then cumulative as reps accumulate:

| | rep0 | rep1 | rep2 | rep3 | **cumulative curve** | **union** |
|---|:-:|:-:|:-:|:-:|---|:-:|
| **Opus** | 17 | 15 | 14 | 15 | 17 → 18 → 19 → **21** (still climbing) | 21 |
| **Sonnet** | 18 | 18 | 14 | 15 | 18 → 20 → 20 → **20** (flat by rep1) | 20 |

Union overlap: **16 shared**, Opus-only 5 (`C5, C10, C21, X5, X6`), Sonnet-only 4 (`C3, C9, C13,
C15`). **Overall union across both models = 25** (+ a long tail of ~14 rare singletons the classifier
didn't catalog — e.g. `..\IntervalScheduler\ROADMAP` cross-refs, `AstrometryUi` deletion, settings
seed details — so true total is even larger, per the skill's "truth keeps growing" thesis).

### Conclusion — hypothesis partially confirmed, with a key refinement
**Confirmed:** (1) **No per-pass capability deficit** — Sonnet's single-pass recall (18,18,14,15)
matches or beats Opus's (17,15,14,15) across all 4 reps; the Exp-1 18=18 tie was not luck.
(2) **Sonnet converges *faster/cheaper*** — flat at its ceiling by rep1–2, while Opus is still
climbing at rep3. So cheaper-model + iteration genuinely substitutes for an expensive model on
coverage *volume*.

**Refutes the naive form:** iterating one model does **not** converge to "nearly identical" runs or
to the full ground truth. Each model has **systematic blind spots that more reps don't cure**: Opus
ran 4 reps and *never* found `C3` (yearDays key) or `C13` (RenderArea 4-step) — Sonnet got both on
rep0; Sonnet ran 4 reps and never found `X5/X6` (code-comment orphans) — Opus got them on rep0. Each
model converges to a *different* ~20-issue ceiling sharing only 16; the union of 25 needs **both**.

**Therefore the real completeness lever is model diversity in the fan-out, not just more reps of one
model.** A mixed-model fan-out (or a cheap-model base + one pass of a different model) beats deeper
iteration of either alone. Loop-until-dry on a single model hits a model-specific ceiling (~20–21 of
25 here), not truth.

**Practical recommendation for AUDIT workers:** Sonnet is a strong, cheaper default for the worker
tier (per-pass parity, faster convergence). For thoroughness, prefer **diversifying the worker model
across the fan-out** over piling more same-model reps. Haiku stays a cheap first-sweep only (Exp 1
discipline gap). *(Candidate skill note: loop-until-dry guidance should acknowledge the per-model
ceiling and suggest model diversity — feed to `docs-architecture-design.md`.)*

**Caveats:** classifier is heuristic (long-tail singletons uncounted → unions are lower bounds);
rep0 came from the Exp-1 script (identical prompts, no "pass #N" prefix); precision not exhaustively
re-adjudicated per-rep (matched flags map to catalogued real issues; no cry-wolf seen in spot-checks);
N=4 reps, single fixture.

## Harness gotcha — `args` arrives as a JSON string (root-caused 2026-06-29)
The backfill's full-matrix overrun was traced (via a zero-agent `args-probe.js`) to this: the
**Workflow tool delivers `args` to the script as a JSON *string*, not a parsed object** (or
`undefined` when omitted). So `args.cells` was silently `undefined` and the script took its
full-matrix branch — a 42-cell run where 12 were intended. **Fix:** normalize at the top of every
workflow that reads `args` — `const A = (typeof args === 'string') ? JSON.parse(args) : (args || {})`
— and read `A.x`, never `args.x`. Confirmed both ways with the probe (raw `args` type = `string`;
post-parse `A.cells` length correct, backfill branch taken). `audit-convergence.js` also now `log()`s
its mode + cell count at launch so a targeting failure is visible in `/workflows`, not silent.

## Pending / next axes
- **Effort sweep (#2):** Sonnet medium vs high, *after* convergence is settled — held separate to
  avoid confounding effort with model/iteration. (Switching to medium *now* would confound Exp 2:
  the baseline/ground-truth and rep0 are all high-effort.)
