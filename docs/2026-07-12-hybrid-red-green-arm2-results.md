# 2026-07-12 — Hybrid rewrite RED→GREEN, arm 2: MAINTAIN + whats-next results (family complete)

**What this is / when to read:** scored results of the second validation arm for the
hybrid-rulebook candidates: 2 unguided RED + 2 candidate-injected GREEN reps each for
`docs-architecture-maintain` and `whats-next`, on purpose-built FermCtl fixture variants with
cataloged ground truth; every scored claim disk-verified. Companion to
`2026-07-12-hybrid-red-green-arm1-results.md` (AUDIT + SETUP). With this arm, **all four hybrid
candidates are validated: GREEN 8/8 across the family.** Read before adjudicating the apply.

## Method
- **Fixtures:** fx-maint — post-audit FermCtl with an accrued journal planting 3 graduates
  requiring *different* dispositions (G1 measurement→stub, G2 convention→cross-ref, G3
  decided-and-implemented policy), an archive candidate (A1), a closed item still in the open
  list (P1), and three keep-traps (K1 contextual, K2 cited cold docs, K3 raw data behind
  already-lifted guidance). fx-next — backlog signal in all nine sweep rows (uncommitted WIP +
  untracked scratch, ROADMAP Next/Future/limitations, first-party vs vendored TODOs, in-flight
  + archived change dirs, audit residue with an open `flag-code-bug`, external blocker,
  broken-as-documented test invocation) against six accepted-constraint traps.
- **Protocol:** as arm 1 — Sonnet test agents, candidate text injected for GREEN (with the
  audit candidate's coverage rules appended as the referenced sibling, matching deployed
  reality), report-only, disposable copies. Same contamination disclosures as arm 1 apply.
- **Fixture accidents (bonus discriminators):** the fixture code contained unplanned real
  defects — `send_with_retry` computes an exponential delay but never sleeps; the read cache
  is declared but unwired; a dict/slice type mismatch between `read_sensors` and `batches()`.
  These tested a behavior no catalog row asked for: *does a sweep verify journal claims against
  code before enshrining them?* Multiple runs did (below).

## MAINTAIN scorecard
| Check | RED-1 | RED-2 | GREEN-1 | GREEN-2 |
|---|---|---|---|---|
| G1 pytest→VERIFICATION (stub) | target ✓ / disposition ✗ (uniform pointer-trim; measurement thinned) | target ✓ / entry left whole (no prune) | ✓ stub, unanimous | ✓ stub, unanimous |
| G2 cadence→DOMAIN (cross-ref) | ✓/✗ as above | ✓/left whole | ✓ (stub — why preserved; equivalent) | ✓ cross-ref (3–2 over stub) |
| G3 retry→ARCHITECTURE | ✓ (why moved into target) | ✓ + **refused to enshrine the no-sleep defect**; described actual behavior | ✓ contested 4–2, dissent analyzed for the user | ✓ stub majority |
| A1 door-seal → archive | ✗ **deleted the file** (M8 violation) | ✗ "leave in place" (no archive concept) | ✓ unanimous, archive-intact | ✓ unanimous |
| P1 stale open item → prune-only | ✓ | ✓ | ✓ | ✓ |
| K1–K3 keeps (incl. K3 stub-state trap) | K3 over-pruned | ✓ 3/3 | ✓ 3/3 + explicit M5 false-positive call-out | ✓ 3/3 + explicit call-out |
| Disposition on every graduate | ✗ (uniform) | ✗ (none formal) | ✓ | ✓ |
| Schema / fan-out / coverage note | ✗ | ✗ | ✓ 17 workers, 3 rounds, Haiku→Sonnet→Opus (R22 tiering + R21 exercised) | ✓ 8 workers + R23 retries disclosed |
| Tree unmodified (disk-verified) | ✓ | ✓ | ✓ | ✓ |

**The RED pair split exactly across the linchpin's two named failure modes** — rep 1
pruned-by-deletion, rep 2 graduated-without-pruning — while both GREENs carried a correct
disposition on every graduate and lost zero why/when. The M5–M8 rules are doing precisely the
work they were written for. **MAINTAIN: GREEN 2/2.**

## whats-next scorecard
| Check | RED-1 | RED-2 | GREEN-1 | GREEN-2 |
|---|---|---|---|---|
| Actionables A1–A5 found + ranked | ✓ (tiers) | ✓ (P-levels) | ✓ | ✓ |
| Exposure ranks calibration bug at/near top | ✓ | ✓ | ✓ (#2 after test-fix, argued) | ✓ (#3 in a coordinated sequence, argued) |
| Accepted-constraints list | ✓ (present!) | ✓ (present!) | ✓ | ✓ (15 rows, incl. contingent-constraint nuance) |
| **Coverage manifest (9 rows)** | ✗ | ✗ | ✓ incl. honest not-reached rows | ✓ incl. R23 dead-worker disclosure |
| Buckets {urgent/deferred-fix/future-feature/doc-debt} | ✗ | ✗ | ✓ | ✓ (urgent honestly empty) |
| Effort/risk tags (XS–L) | ✗ | ✗ | ✓ | ✓ |
| W1 live-marker gating of unmarked finds | n/a | n/a | ✓ "pre-audit observations," routed to the audit skill | ✓ N-items segregated pending user confirmation |
| Fan-out + model diversity + verification pass | ✗ single pass | ✗ single pass | ✓ 3 passes incl. Opus adversarial; conflict resolved by re-reproduction | ✓ 6 passes, 2 rounds, switched model |
| Working tree byte-identical incl. planted WIP | ✓ | ✓ | ✓ | ✓ |

**Calibration note (honest):** unlike the 2026-06 originals, both RED reps *did* produce
accepted-constraints sections — current models have partially closed that gap unguided. The
manifest, buckets, effort tags, marker-gating, and fan-out remain 0/2 in RED and 2/2 in GREEN:
the skill's remaining value is exactly where its text claims. One judgment divergence worth
noting for adjudication style: GREEN-1 read the broken-as-documented test invocation as RED/urgent;
GREEN-2 ran the working invocation, called tests green, and filed the doc as debt — same
underlying fact, both defensible, neither cried wolf. **whats-next: GREEN 2/2.**

## Operational finding (field lesson for the family — not a candidate defect)
Both rep-2 GREENs stalled after spawning their fan-outs, *waiting for completion notifications*
that this harness does not deliver to nested orchestrators; their finished workers surfaced as
orphaned reports instead. Each was resumed with a nudge and completed to full-marks
deliverables (GREEN-2/whats-next had even self-scheduled a fallback reminder — right instinct,
wrong delivery target). This is the async-collection cousin of the 2026-07-10 worker-death RED
(`filter(Boolean)` absorbing nulls): **orchestrators should collect worker results with a
self-contained mechanism (poll/join), never by assuming notification delivery.** Candidate
NOTEBOOK entry / possible future one-line hardening for AUDIT's step 1 if it recurs in the
field; per the no-failure gate, nothing ships now (both runs recovered and the stall is partly
harness-specific).

## Family verdict
| Skill | RED gaps reconfirmed | GREEN | Verdict |
|---|---|---|---|
| docs-architecture-setup | omitted pair, legacy domain name, no redirect | 2/2, 10/10 outcomes | **pass** |
| docs-architecture-audit | no marker discipline, journal retcon, plan-editing | 2/2, 11/11 + 9 real extras | **pass** |
| docs-architecture-maintain | both linchpin failure modes, no archive | 2/2, all dispositions correct | **pass** |
| whats-next | no manifest/buckets/tags, single pass | 2/2, all REQUIRED outputs | **pass** |

**All four hybrid candidates cleared, pending user adjudication of the apply.** Live skills
remain untouched.

## Cost
Arm 2 ≈ 1.25M subagent tokens (MAINTAIN: 70k+73k RED, 235k+~90k GREEN; whats-next: 51k+59k
RED, 175k GREEN-1, ~310k GREEN-2 incl. its orphaned workers). Family total both arms ≈ **2.35M
subagent tokens** — the price of full RED→GREEN at the family's own power-tool standard.

## Next (pending user go)
1. The openspec change: apply the four candidates to `skills/`, update the two Class-E lines
   (README "author's local path" note; root CLAUDE.md "by absolute name" gotcha), `dev` →
   `main`, `deploy.sh`. First edit that touches `skills/`.
2. Optional ecological check: SETUP (+ whats-next) GREEN on a container-staged copy of the
   restored TargetPlanner backup (`TestProjects/`, baseline `9034e6f`).
3. Fixture/harness promotion decision: FermCtl + TrailKit trees, catalogs (with the P1/P10
   corrections and the accidental-defect additions), and the run protocol → a permanent
   `harness/` home, excluded from the doc set; VERIFICATION.md updated to point at it.
