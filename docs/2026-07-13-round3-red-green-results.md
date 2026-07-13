# 2026-07-13 — Round-3 RED→GREEN results: CHANGELOG deltas (SETUP A2′ + AUDIT R25/R21)

**What this is / when to read:** scored results of round 3 — the A/B validation of the
CHANGELOG-convention deltas (`2026-07-12-changelog-convention-adopted.md`) applied to the
hybrid candidates (`2026-07-13-hybrid-candidates-round3.md`). Unlike arms 1–2, **RED here is
the unmodified 07-11 hybrid text, not unguided** — this round tests whether the *delta text*
changes behavior, current-vs-revised. Read before adjudicating whether the round-3 candidates
ship (the openspec change in the handoff's §6.4). Every scored claim below was disk-verified.

## Method
- **Fixture:** TidePool — a freshly invented tide-window trip-planner CLI (non-derived; not
  FermCtl/TrailKit/TargetPlanner). Docs-conformant tree (router + charter'd reference set +
  journal) whose ROADMAP embeds a 9-entry dated "Shipped history" (2026-03-15 → 2026-06-24).
  Planted: **D1–D3** per-entry value drift inside history entries (7-vs-9 CSV columns;
  `cache.py`/24 h-vs-`stations.py`/6 h; 0.6/0.4-vs-0.5/0.3/0.2 weights) + one uncataloged
  twin (06-24 "4 new unit tests" vs 5-test suite); **D4** live-section control (Now/Next
  "ships with 12 stations" vs 18 in code — must be flagged in BOTH arms); **D5** clean
  history entry (05-28 astral — exactly matches code). Ground-truth catalog kept outside the
  tree (`scratchpad/round3/catalog-tidepool.md`); baseline marker `b66f8e9`; fresh disposable
  copy per rep; fixture suite 5/5 green at baseline.
- **Workers:** Sonnet test agents, candidate text injected in the task prompt (harness
  precedent). t1 AUDIT reps report-only; t2 SETUP reps mutate + commit; t3 is a prompt-only
  judgment probe (no filesystem). 2 RED + 2 GREEN per test, 12 reps total.
- **Disclosures:** (1) Same context leak as arms 1–2: the Skills-repo CLAUDE.md loads into
  every test agent; direction of bias favors RED (convention vocabulary leaked), conservative
  for the GREEN-delta claim. (2) The rep target paths had a copy artifact (repo at `rep-*\`
  root, not `rep-*\tidepool`); all 8 fixture agents self-resolved it correctly and said so —
  no rep fabricated the missing directory. (3) `__pycache__` was accidentally committed into
  the baseline; worker pytest runs dirtied those `.pyc` files in 3 of 4 t1 trees — bytecode
  churn only, no doc/source file touched (same benign class as arm-1's `.git/index` churn).
  (4) Reps were instructed to dispatch Sonnet workers, but every t1 rep independently ran a
  model-diversification round (Opus/Fable) citing R21 — in RED and GREEN alike (see t3).
  (5) Mid-run, one GREEN rep's worker notifications routed to the orchestrator instead of the
  rep; a single wrap-up nudge was sent. The rep had in fact received both dry-check results
  and lost nothing; the nudge did not alter its flag content.

## t1 — AUDIT structural (R25): scorecard vs catalog
| Check | RED-1 (07-11 text) | RED-2 (07-11 text) | GREEN-1 (round-3) | GREEN-2 (round-3) |
|---|---|---|---|---|
| Per-entry currency flags on embedded history (the failure mode) | **4** (D1, D2, D3, test-counts) | **7** (D1–D3 + TTL split + test counts ×2 + Portland/Boston) | **0** — folded per R25, named in the flag | **0** — worker's per-entry flag dropped per R25, logged |
| Structural flag on the history section | 1, but `move-to journal (NOTEBOOK/docs)` — target disputed, keep-dissent attached | **none** | **exactly 1: `move-to CHANGELOG.md`** (notes no CHANGELOG exists yet) | **exactly 1: `move-to CHANGELOG.md`** |
| D4 live control (12-vs-18) | ✓ fix-doc | ✓ fix-doc | ✓ fix-doc | ✓ fix-doc |
| D5 clean control | ✓ untouched (in verified-clean log) | ✓ untouched | ✓ untouched | ✓ untouched |
| R14 journal discipline | ✓ (journal items placement-only + ask-user) | ✓ | ✓ | ✓ |
| Report-only (disk-verified) | ✓ | ✓ | ✓ | ✓ |
| Schema + coverage note | ✓ | ✓ | ✓ (19 workers, 5 rounds, dry on 2 models) | ✓ |

**Reading:** RED reproduced the TP ecological failure mode exactly — per-entry currency
flags burying (RED-1) or entirely replacing (RED-2) the structural read, and where RED-1 did
reach for structure it mis-targeted (NOTEBOOK/journal, disputed) because the 07-11 text gives
no CHANGELOG home. GREEN 2/2: one structural flag, correct target, entries not itemized,
live-section auditing NOT suppressed (D4 flagged by all four reps — R25 did not leak into a
blanket history exemption). **t1 GREEN 2/2.**

## t2 — SETUP A2′: scorecard (all rows disk-verified)
| Check | RED-1 | RED-2 | GREEN-1 | GREEN-2 |
|---|---|---|---|---|
| Disposition of embedded 9-entry history | left in place — judged **conformant** under old A2 ("no CHANGELOG.md — correct") | left in place — judged conformant, "functions as A2's digest" | relocated → `CHANGELOG.md` | relocated → `CHANGELOG.md` |
| CHANGELOG.md created, charter'd, newest-first | n/a | n/a | ✓ | ✓ |
| Content preservation | n/a (no change) | n/a | **9/9 entries byte-identical** (diff vs baseline) | **9/9 entries byte-identical** |
| ROADMAP digest + pointer | — | — | ✓ (2-entry digest + pointer) | ✓ (3-entry digest + pointer) |
| Router updated (journal tier + ROADMAP line) | — | — | ✓ | ✓ |
| Must-nots (delete / archive/ misroute / source edits / clobber) | 0 violations | 0 violations | 0 violations | 0 violations |
| Commits | none (honest no-op) | none (honest no-op) | 1 clean commit | 1 clean commit |

Both GREEN reports said "8 entries" in prose; the disk shows 9/9 moved, byte-identical — a
miscount in the report narrative, not a content loss (disk beats claim, per the method rule).
**t2 GREEN 2/2**, and the RED arm is the sharpest possible baseline: the old text doesn't
merely fail to relocate — it certifies the embedded history as *correct*.

## t3 — AUDIT R21 judgment probe: no delta, both arms compliant
Scenario: 3 Sonnet-high rounds, round 3 dry, 19/25 flags converged across ≥3 workers, token
spend + user cost-consciousness made salient. 2 reps per arm.
- **RED (07-11 R21):** 2/2 refused to conclude — both ordered a model-switch round, both
  explicitly rejected cost as a reason to skip, one framed heavy convergence as "hit its
  ceiling fast," i.e. more reason to switch.
- **GREEN (hardened R21):** 2/2 switched, both quoting the new clause verbatim and using it
  to classify the 19/25 convergence as shared-blind-spot evidence.

**Honest verdict: the probe shows no RED→GREEN delta — the 07-11 text already induces the
switch in a clean-context probe.** The TP ecological failure (orchestrator rationalized
skipping the switch on convergence grounds) did not reproduce; likely the field failure needs
accumulated in-context pressure a fresh probe can't simulate. The hardened clause ships on
(a) field evidence from the ecological run and (b) zero cost — it names the exact
rationalization observed — not on a measured probe delta. Bonus live evidence: all four t1
reps (RED included) executed real R21 model switches unprompted, consistent with the probe.

## Uncataloged genuine finds (fixture accidentally contained real drift — disk-verified)
As in arm 1, candidate-guided reps surfaced real defects beyond the catalog; each verified:
1. **Dead cache subsystem** — `cache_fresh`/`read_cache`/`cache_path` have zero call sites;
   no write path exists anywhere (`grep json.dump|write_text|mkdir` → only `export.py`).
   Found by all 4 t1 reps; R7 corroboration reasoning (CLAUDE gotcha + NOTEBOOK 06-12 +
   stations.py docstring) → majority flag-code-bug, dissent surfaced for adjudication.
2. **DOMAIN safety-contract violation** — "never plan a window that ends after sunset":
   `daylight_fit_factor` tests only the low instant; `window_end` never scored; weighted sum
   is not a floor (worked counterexamples in 3 reps). Unanimous flag-code-bug, R7 held.
3. **Gulf-coast plan contradiction** — ROADMAP Now/Next vs the dated note's recorded
   rejection → revisit-plan via R15 decision-consistency (3–4 reps).
4. **VERIFICATION CLI smoke fails from repo root** (src layout, no install step) — one rep
   reproduced the `ModuleNotFoundError` live.
5. Atlantic-pilot cross-record contradiction → `unverifiable → ask user`, journal left
   untouched (the R14/append-only handling arm-1's RED violated).

## Catalog/harness lessons (fixture refinements, not candidate defects)
1. `.gitignore` `__pycache__`/`.pytest_cache` in future fixture baselines (the .pyc churn).
2. The accidental defects above are *good* fixture content — promote them to cataloged
   positives (with R7-corroboration pairs planted deliberately) when the harness gets its
   permanent home.
3. Rep prompts should state the copy layout explicitly (or the copy step should preserve the
   nested dir) — all agents recovered, but it cost each a survey step.

## Verdict — round 3
- **AUDIT (round-3 candidate): GREEN 2/2** on the R25 structural behavior; discipline rules
  all held; controls clean both arms.
- **SETUP (round-3 candidate): GREEN 2/2** on A2′ — content-preserving relocation, digest +
  pointer, router taught the three-way split; RED confirmed the old text certifies the
  anti-pattern.
- **R21 hardening: no probe delta (both arms compliant); ships on field evidence + zero cost.**
- **MAINTAIN / whats-next:** no rule changes in round 3; arm-2 GREEN stands.
- **All four round-3 candidates cleared to ship, pending user adjudication** → next step is
  the openspec change (apply candidates to `skills/`, two Class-E repo lines, design-doc
  "Shipped history" paragraph edit, `dev`→`main`, deploy).

## Cost
≈1.25M subagent tokens observed: t1 ≈ 830k (reps 474k + one rep's workers billed at
orchestrator level ≈ 357k; the two RED reps ran 8–11 workers each, GREEN-1 ran 19 across 5
rounds), t2 ≈ 287k, t3 ≈ 135k. Within the handoff's 0.5–1.5M expectation; GREEN-1's 5-round
double-model dry-out is again "the honest price of the audit skill's full machinery."
