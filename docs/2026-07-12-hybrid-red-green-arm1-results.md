# 2026-07-12 — Hybrid rewrite RED→GREEN, arm 1: AUDIT + SETUP results

**What this is / when to read:** scored results of the first validation arm for the
hybrid-rulebook candidates (`2026-07-11-hybrid-rewrite-candidates.md`): 2 unguided RED reps +
2 candidate-injected GREEN reps per skill, on synthetic non-derived fixtures with cataloged
ground truth, every scored claim disk-verified. Read before adjudicating whether the AUDIT and
SETUP candidates ship. Arm 2 (MAINTAIN + whats-next) not yet run.

## Method
- **Fixtures:** FermCtl (post-convention Python CLI; 11 planted defects P1–P11 spanning every
  AUDIT rule class + 4 cry-wolf controls C1–C4) for AUDIT; TrailKit (ad-hoc docs; 10 expected
  outcomes E1–E10 + 3 must-nots N1–N3, incl. a nested own-`.git` sub-project) for SETUP.
  Ground-truth catalogs kept outside the fixture trees. Fresh disposable copy per rep.
- **Workers:** Sonnet test agents (harness precedent). GREEN = full candidate text injected in
  the task prompt; RED = task only. AUDIT reps report-only; SETUP reps mutate + commit.
- **Disclosures:** (1) The session's Skills-repo CLAUDE.md leaks into every test agent's
  context; one RED rep explicitly noticed and set it aside. Direction of bias: makes RED look
  *better* (convention vocabulary leaked), i.e. conservative for the GREEN-delta claim.
  (2) The AUDIT task prompt named the convention ("router + reference docs + journal") —
  identical in RED and GREEN, and AUDIT legitimately assumes the conventions. (3) The fixture
  is small (≈20 files), which compresses the recall gap an unguided pass shows on real-size doc
  sets — the meaningful signal here is discipline/structure, matching the skills' own honesty
  posture ("per-flag judgment is innate; the skill forces completeness + a mergeable output").
- **Bonus live events:** GREEN-A2's internal retry produced a straggler worker that finished
  *after* report-out — its disclosure-not-drop handling was correct on the information it had
  (R23 exercised for real). GREEN-A1 ran 21 worker dispatches across 3 rounds with a live
  Sonnet→Opus model switch (R21 exercised for real; the Opus round surfaced the two genuine
  interpretive disputes, exactly R21's premise).

## AUDIT scorecard (11 positives, 4 controls)
| Rep | Recall | Controls (cry-wolf) | Evidence rule | `unverifiable` marker | Journal discipline | Report-only vocabulary | Schema | Coverage note |
|---|---|---|---|---|---|---|---|---|
| RED-A1 | 10/11 | 4/4 clean | file:line throughout | never used | respected | escalated P2 in prose; proposed deleting the P8 plan bullet | none (prose) | none |
| RED-A2 | 10/11 | **violated C2** (proposed editing a NOTEBOOK entry to match code) | file:line + live `pytest` | never used | violated | proposed plan-bullet removal | none (prose) | none |
| GREEN-A2 | 11/11 | 4/4 clean | file:line throughout | used correctly (×2) | corroboration-only, cited R14 | `flag-code-bug` + `revisit-plan` held report-only; disputes surfaced for adjudication | every flag | yes + dead-worker disclosure |
| GREEN-A1 | 11/11 (+9 real uncataloged defects) | 4/4 clean | file:line + live execution | used correctly (×2) | corroboration-only; R15 run with decision-consistency pass | held report-only; two DISPUTED items with per-pass vote tallies | every flag, with convergence counts | yes, incl. honest not-fully-dry scoping note |

Both RED reps missed the same discipline behavior (no `unverifiable → ask user` anywhere) and
leaned toward directly editing plans; one retconned the journal. Both GREEN reps closed every
one of those gaps while running real multi-round fan-outs. GREEN-A1's nine uncataloged finds
(dead cache, unwired smoothing, uncalled uploader/`read_sensors`, dead `log_dir`, PYTHONPATH
test failure, untraceable "field notes" citation, orphaned water-profiles doc, router
"logs batches" overclaim) were each disk-verified true — the fixture accidentally contained
real drift beyond the catalog, and the candidate-guided runs found it.

## SETUP scorecard (10 outcomes, 3 must-nots) — all rows disk-verified
| Check | RED-S1 | RED-S2 | GREEN-S1 | GREEN-S2 |
|---|---|---|---|---|
| E1 full charter-guarded set | ✗ | ✗ | ✓ (charters verified) | ✓ (explicit "Charter:" lines) |
| E2 NOTEBOOK + VERIFICATION | ✗ (NOTEBOOK misplaced in `notes/`; no VERIFICATION) | ✗ (neither) | ✓ | ✓ |
| E3 FIELD-GUIDE → DOMAIN.md | ✗ (kept legacy name) | ✗ | ✓ (git-tracked rename) | ✓ (rename cites S6) |
| E4 design_notes merged, no loss | ✓ | ✓ | ✓ | ✓ |
| E5 git-as-changelog, no CHANGELOG/archive misroute | ✓ | ✓ | ✓ | ✓ |
| E6 router by-name + convention + exclusions | partial | partial | ✓ | ✓ |
| E7 journal normalized (`docs/`, no spaces) | ✗ (kept `notes/`) | partial | ✓ | ✓ |
| E8 sub-project untouched + redirect | untouched ✓ / redirect ✗ (gitlink-plumbing framing) | untouched ✓ / redirect ✗ | ✓ + redirect delivered | ✓ + redirect delivered |
| E9 vendor/build untouched | ✓ | ✓ | ✓ | ✓ |
| E10 recoverable git history | ✓ | ✓ | ✓ | ✓ |
| N-violations | 0 | 0 | 0 | 0 |
| **Score** | **≈4.5/10** | **≈4/10** | **10/10** | **10/10** |

(The `diff` flag on every tree's sub-project was `.git/index` stat-cache churn from agents
running `git status`; working files byte-identical in all four — no-touch holds 4/4.)

The RED arm reproduced the original 2026-06/07 findings almost exactly: the reliably-omitted
pair (VERIFICATION 0/2, NOTEBOOK 0/2 at the right location), no domain-doc normalization 0/2,
and the sub-project redirect 0/2 with both reps steering into git-plumbing framing — the same
failure class the round-2 RED caught (0/4 then). The reworded rules closed all of it, 2/2.

## Catalog lessons (fixture/harness refinements, not candidate defects)
1. **P1 accidental corroboration** — the fixture's NOTEBOOK entry + "CSV logger relies on the
   ordering" line unintentionally gave the tuples claim R7-contract corroboration, making
   fix-doc vs flag-code-bug genuinely contestable. Both GREEN reps surfaced the dispute for
   adjudication instead of silently picking — designed behavior — but the permanent harness
   should plant corroborating pairs only deliberately.
2. **P10 catalog action was too loose** — the source-side BREWING.md referrer requires a code
   edit, so `flag-code-bug` (report-only), not `fix-doc`; both GREEN reps were *more* correct
   than the catalog. Catalog updated mentally; fix on promotion to the permanent harness.
3. **P6 folding** — both GREEN reps folded the unverifiable rate-limit claim into the adjacent
   spacing-contract finding rather than a standalone marker flag, while demonstrating the
   marker correctly elsewhere; count P6 as covered-by-fold, and plant a cleaner standalone
   unverifiable in the next fixture revision.

## Verdict — arm 1
- **docs-architecture-audit (hybrid candidate): GREEN 2/2.** Recall 11/11 both reps, zero
  cry-wolf, all discipline rules exercised including live R21/R23 events; behavior meets or
  exceeds the shipped skill's recorded GREEN runs.
- **docs-architecture-setup (hybrid candidate): GREEN 2/2.** 10/10 outcomes both reps,
  disk-verified, zero must-not violations, redirect delivered both reps.
- RED baselines reconfirm every gap the rules exist for. **Both candidates cleared to ship,
  pending user adjudication.** Live skills untouched throughout.

## Cost
≈1.10M subagent tokens this arm: AUDIT RED 64k+70k, AUDIT GREEN 328k+157k (+73k straggler),
SETUP 70k+75k+80k+76k, plus fixture construction in-session. GREEN-A1's 21-dispatch fan-out is
the honest price of the audit skill's full machinery — consistent with DOMAIN.md's
"occasional power tool, real token cost" posture.

## Next
Arm 2: extend FermCtl's fixture (journal graduation candidates for MAINTAIN; backlog sources +
accepted-constraint traps for whats-next), 8 runs, same protocol. Then the openspec change:
apply all four candidates + the two repo-side lines, specs untouched, deploy from `main`.
