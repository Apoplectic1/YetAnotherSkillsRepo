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

**Metrics to compute on completion:**
- Per-model **cumulative-recall curve** (rep0→rep3): does each climb to, and converge on, the union?
- **Rounds-to-dry** per model (the cost driver): does Sonnet need more rounds than Opus?
- Per-rep recall mean + spread (the variance N=1 couldn't measure).

_(Results + conclusion to be appended here when `wybmpvx1w` returns.)_

## Pending / next axes
- **Effort sweep (#2):** Sonnet medium vs high, *after* convergence is settled — held separate to
  avoid confounding effort with model/iteration. (Switching to medium *now* would confound Exp 2:
  the baseline/ground-truth and rep0 are all high-effort.)
