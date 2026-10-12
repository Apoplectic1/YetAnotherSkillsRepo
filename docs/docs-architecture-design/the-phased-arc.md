# docs-architecture-design: The phased arc (part of ../docs-architecture-design.md)

> One topic of `../docs-architecture-design.md`, split out on 2026-10-12 when the file passed its
> budget; the heading keeps its text, so "docs-architecture-design § The phased arc" resolves by grep over
> the file and `docs-architecture-design/`. The index is `../docs-architecture-design.md`.

## The phased arc

```
Phase 1  STRUCTURE  → write charters · establish tiers · convention-route in CLAUDE.md ·
                      split ROADMAP port-history → archive/ · always-on lean.
                      (Safe, quick; no content-correctness judgment needed — the history
                      split is along a clean seam: history is a record regardless of currency.)

Phase 2  AUDIT      → doc-by-doc placement + currency sweep vs charters & live code.
                      The one-time debt paydown. Scoped to the LIVE reference tier only
                      (Phase 1 having removed history from scope). Agent flags; user
                      adjudicates per-flag. Placement + currency are ONE read, not two.

Phase 3  SKILLIFY   → by EXTRACTION from the worked Phase 1/2 example (do-then-skillify).
                      FOUR skills (refined 2026-06-28: 2 → 3 → 4) — THREE docs-hygiene, by
                      lifecycle moment, plus ONE planning layer on top:
                      • SETUP skill (one-time/project) — generalized Phase 1: bootstraps this
                        whole architecture (charters, tiers, router conventions, anti-staleness,
                        always-on lean) in any project.
                      • AUDIT skill (triggered/periodic) — generalized Phase 2: per-doc parallel
                        fan-out that verifies docs vs charters (placement) + live code (currency),
                        emits evidence-carrying flags → adjudicate → fix. The ONLY skill that
                        catches code-doc drift (the #1 staleness source). When that drift is a *code* contract-violation
                        (not a stale doc), AUDIT emits a **report-only `flag-code-bug`** — it never
                        edits code and never rewrites a contract to match the bug → feeds TRIAGE.
                        Crux = the
                        conservative-evidence rule ("cite the code or mark unverifiable, never
                        guess stale"). **Keys on content, not filename** (user, 2026-06-28) —
                        placement/currency are judged by what a section/doc *is* and whether its
                        claims hold vs code, never by a name pattern (no "PLAN-* → ROADMAP" rule;
                        read the doc's content + currency, then decide where it belongs). Token-heavy
                        (parallel code-grepping agents) → not
                        every-session; depends on SETUP's charters. Distinct from MAINTENANCE:
                        its trigger is suspected drift / post-refactor, not journal backlog.
                        TIER SCOPE: currency-check the reference tier against code; cold-rationale
                        (tier 3) docs get only a decision-consistency check (evergreen, not
                        code-coupled). Also flags **cold-rationale extraction candidates** —
                        sections that are lengthy + cold + evergreen — for the user to adjudicate
                        (this is the standing, demand-driven home for "should this why be split
                        out", not a one-off sweep).
                      • MAINTENANCE skill (ongoing) — periodic graduate & prune sweep (invoked,
                        not a hook; graduation needs judgment). Encodes charter-match +
                        single-source + prune-the-source; runs on the journal backlog.
                      • WHAT'S-NEXT / TRIAGE skill (planning layer — authored LAST; NOT a
                        docs-hygiene peer). A synthesizer that sweeps every backlog source
                        (ROADMAP "Future directions", Known-limitations, CLAUDE gotchas, docs/
                        "pending" notes, code TODO/FIXME, OpenSpec active changes, AUDIT flags)
                        → a categorized, prioritized backlog {urgent | deferred-fix |
                        future-feature | doc-debt} + recommended top-N. Signature feature = a
                        COVERAGE MANIFEST (what it swept / couldn't) — the antidote to the
                        "am I seeing everything when I ask 'what's next?'" uncertainty. Crux =
                        separating a live bug / gotcha-needing-attention from an ACCEPTED
                        constraint (needs a FIXME/pending marker or an AUDIT `flag-code-bug`, else
                        it cries wolf on every gotcha). Consumes the trio's outputs (esp. AUDIT)
                        + project sources; composes AFTER audit (stale docs → stale backlog).
                        Proposes priority; user owns the call. (Authored last as planned,
                        after the trio — built & validated 2026-06-28; record below.)
                      All four GLOBAL (~/.claude/skills/), data-driven (read the project's
                      charters at runtime). Non-redundant with `init` / `improve-architecture`.
                      Author per DOMAIN.md's authoring conventions (vendored
                      2026-07-26 from `superpowers:writing-skills` v6.2.0).
```

Sequencing rationale: Phase 1 enables Phase 2 (charters make the audit objective) *and*
shrinks it (history split out of scope). Phase 3 is derived, not speculative — doing Phases
1–2 well **is** the design effort for the skills: Phase 1 prototypes SETUP, Phase 2 prototypes
AUDIT (the `docs-reorg-phase2-audit` run, completed 2026-06-28 — its agent prompts, flag
schema, and conservative-evidence rule are the skill's spec), and the graduate/prune workflow
prototypes MAINTENANCE.

**AUDIT — built & validated (RED/GREEN, 2026-06-28).** Authored as `docs-architecture-audit`.
RED (2 unguided baselines on TSM `DOMAIN.md`): capable agents already cite code, key on content,
separate placement/currency, and handle descriptive/prescriptive — but **one pass finds only ~half
the issues, non-deterministically** (the 2 baselines overlapped on ~2 of ~10 flags). So the skill's
job is **completeness + a mergeable output**, not per-flag judgment: a structured-schema **fan-out +
cross-reference pass + loop-until-dry**. GREEN (3 schema'd passes + 1 cross-ref): schema / evidence /
modality / cross-ref all worked and the **merge recovered a flag passes 1–2 individually missed**;
but **3 *fixed* passes still missed 2 real flags** a different angle caught (true ground truth ≈30%
larger than any single run) → hardened the skill to mandate **per-section depth + loop-until-dry over
a fixed N** (a calibration, not a defect). Net: fan-out + merge decisively beats single-pass;
coverage needs the *loop*, not just a bigger N.

**AUDIT refined 2026-06-29 (RED/GREEN) — code-bug findings.** Added a **report-only `flag-code-bug`**
action + a **stale-doc-vs-contract-violation discriminator** + an explicit **"AUDIT writes docs only,
never code"** boundary. RED (3 workers, old skill): a doc asserting a contract the code *violates* (a
fail-fast keyword guarantee vs code that silently returns a `"UNKNOWN"` default) was filed `fix-doc` by
**3/3** — faithfully following the skill *rewrites the contract to enshrine the bug*; the correct
"fix the code" call survived only as non-mergeable prose (1/3). GREEN (3 workers, updated skill):
**3/3** emit `flag-code-bug` for the contract violation ("do not fix-doc into agreement") **and 3/3**
keep ordinary value-drift (a cache count 256→512, intentionally raised) as `fix-doc` — discriminator
holds, zero cry-wolf, all reps converged on one shape. Closes the design↔skill gap: the "AUDIT
`flag-code-bug`" TRIAGE consumes is now a real schema action — report-only, never auto-applied, routed
to the dev/diagnose flow + `whats-next`.

**AUDIT worker-model benchmark 2026-06-29 — the per-model ceiling refines loop-until-dry.** A scored
sweep on the post-SETUP TP fixture (Opus/Sonnet/Haiku × replicate reps × effort; full record:
`docs/2026-06-29-audit-model-benchmark.md`) sharpened the original "coverage needs the *loop*, not a
bigger N" thesis with a result the single-model RED/GREEN couldn't see: **looping ONE model to
exhaustion plateaus at *that model's* ceiling, not truth.** Each model converged to a different
~20-of-25 subset sharing only ~16; the full union needed *both* — Opus never found two deep
architecture catches Sonnet got on rep0, Sonnet never found two code-comment orphans Opus got on
rep0, and more reps cured neither. **So the strongest completeness lever is model *diversity* in the
fan-out, not more same-model reps** — once a model's rounds go dry, switch model rather than loop
deeper. (This *extends* loop-until-dry, doesn't replace it: within a model, replicate-passes-to-dry
still recover the different-subset-per-pass gains; the ceiling is the model's, so diversity clears
the next tier.) **Worker-tier recommendation:** Sonnet at **high effort** is the default — per-pass
recall parity with Opus, converges faster, discipline intact (cites `file:line` / marks
`unverifiable`, zero cry-wolf at any tier). **Medium effort and Haiku are first-sweep only:** medium's
cumulative ceiling ran ~3 issues below high (per-pass parity only after rep1) — not worth the recall
loss unless its cost is the consumer's scarce resource; Haiku skipped sections and mislabeled actions,
and *iteration doesn't fix discipline*. Mirrored into the AUDIT skill (fan-out step 1, loop-until-dry
step 3, a "Common mistakes" bullet) 2026-06-29.

**Addendum 2026-10-12 (change `audit-scoped-modes`): the loop's one sanctioned exception.** The
mandate above stands as the meaning of "audit". R29 adds two scoped modes the user invokes and
the run never chooses: `release-close` (one lens over the reference tier for the phrases a
release leaves behind, plus the cross-reference pass) and `small-set` (one per-section round
plus the cross-reference pass). One round at the R22 tier, no loop, no model switch, the
coverage note naming the mode and what a full run would have added. A user-set cost tradeoff,
not an empirical ceiling: RED 4/4 showed the unconditional text left a user's "one round" with
no sanctioned path, every rep improvising the disclosure the mode now prescribes.

**MAINTAIN — built & validated (RED/GREEN, 2026-06-28).** Authored as `docs-architecture-maintain`,
**lean** — it *reuses* AUDIT's fan-out machinery and adds graduation-specific flag types + the
**prune/preserve-why linchpin** (a REQUIRED `disposition: stub | cross-ref | archive` field on every
`graduate`). RED (2 baselines on WBPP's journal): same shape as AUDIT — capable agents judge
graduate/keep/archive/prune well and **prune-while-preserving-why naturally** (the hypothesized
graduate-without-prune failure didn't appear), so the real gap is **completeness** (the promotion
candidate set is a coin-flip). Confound: WBPP's journal was already graduated by the reorg → a weak
fixture, so volume stress-testing defers to the first full-pipeline run (TP). GREEN (2 schema'd
passes): the `disposition` field held on **every** graduate (why/when preserved, no bare promote),
the core converged with the expected margin coin-flip, and **disk-verification caught a pass
overreaching on a false currency claim** (it asserted the router had dangling refs; `grep` showed it
clean) — validating the trust-disk-over-claims rule. Caveat baked into the skill: MAINTAIN
presupposes a *non-bloated* reference tier — graduating into an oversized doc is a SETUP/AUDIT split
job first.

**TRIAGE (`whats-next`) — built & validated (RED/GREEN, 2026-06-28).** The planning-layer capstone:
sweep every backlog source → categorized/prioritized backlog + a **coverage manifest** + an
**accepted-constraints** list, with the live-vs-accepted crux; reuses AUDIT's fan-out. RED exposed a
**fixture trap** — WBPP, the project these skills were *derived from*, **contains the TRIAGE spec**
(this design doc's WBPP-side duplicate, since removed — `1bd0e68`), so both "unguided" baselines read it and reproduced
the manifest + cry-wolf section → contaminated. (MAINTAIN hit the mirror trap: WBPP's journal was
already-graduated.) **Lesson: validate a skill on a project it was NOT derived from.** Clean re-RED
on TSM (no spec): both baselines gave a good ranked list but **omitted the coverage manifest and the
accepted-constraint section entirely** — the genuine, uncontaminated gap (prioritization is innate;
the trustworthiness scaffolding is not). GREEN (2 schema'd passes on TSM): both produced an honest
manifest + a correctly-classified accepted-constraints list (no cry-wolf — `CancellationToken` →
actionable, NINA-upstream / no-migration / do-not-re-litigate → accepted), converged tightly on the
core backlog + sequence, and surfaced a real new doc-debt (a stale `# VERIFYING.md` H1) that
disk-verified true. The skill's value = **guaranteeing the manifest + the accepted-vs-actionable
split**, every time, on any project.

**Family complete (2026-06-28): SETUP · AUDIT · MAINTAIN · `whats-next` — all 4 built, RED/GREEN-
validated, deployed to `~/.claude/skills/`.** Cross-cutting lessons banked: (a) capable agents do the
*judgment* well unguided — every skill's value turned out to be **completeness / consistency /
trustworthy structure**, not the per-item call; (b) **validate on a non-derived project** (WBPP
poisoned both MAINTAIN and TRIAGE; TSM was the clean fixture); (c) **disk-verify agent claims** (a
GREEN pass overreached on a false currency claim, caught by `grep`).

**Family review 2026-07-06 — fix batch, mechanical half (behavioral half follows via RED→GREEN).**
A correctness+intent review of the four shipped skills against this design found two correctness
bugs + polish, fixed without behavior change: (1) **footer links absolute** — the deployed copies'
`../../docs/…` links resolved to `~/docs/…` (dangling; deploy is a plain copy); (2) **AUDIT
`graduate` disambiguated** — an ordinary apply-able doc edit once adjudicated; **"report-only" now
means exactly `flag-code-bug` + `revisit-plan`** (the prescriptive-modality text says "two
non-stale statuses", ending its contradiction with step 5); (3) AUDIT's adjudication step now uses
the schema's action vocabulary (approve / amend / defer the proposed action); (4) SETUP's
reference-tier line gains VERIFICATION (matching the tier table here); (5) SETUP's dev-era "prove
the skill on a small project first" note replaced with evergreen large-project care; (6)
whats-next's rank formula names its risk term **exposure-if-deferred** (implementation riskiness
alone doesn't raise rank) and its frontmatter description is trimmed to SDO triggers + the
"assumes the conventions" clause. Change record:
`openspec/changes/archive/2026-07-07-fix-skill-review-findings/` (archived in this repo).

**Family review 2026-07-06/07 — fix batch, behavioral half (RED→GREEN; TP-fixture worktrees + a
synthetic design-heavy fixture; 2 reps per scenario per phase; Sonnet workers; candidate-text
injection).** Four review gaps were RED-tested before encoding (Iron Law). Two survived to full
guidance, one shrank to a structural line, one was dropped:
- **SETUP sub-project boundary — feared failure absent; omitted element real.** Baseline never
  scaffolded into or augmented a nested own-`.git` project: **4/4 no-touch** (2 reps on an easy
  fixture whose sub-CLAUDE.md declares independence, then 2 on a *hard* fixture with no such prose —
  detection held on `.git`/router alone). What did fail: **0/4 delivered the run-from-its-own-dir
  redirect** (one rep steered toward submodule/subtree instead — repo plumbing, not governance). Per
  match-the-form-to-the-failure this took a structural flag-and-skip line mirroring AUDIT's scope
  rule, **not** a prohibition. GREEN 2/2 (soft + hard): no-touch held, redirect delivered.
- **SETUP design-heavy/code-light — RED 2/2 force-split.** Both reps distributed a 155-line
  standalone `SCHEDULER_DESIGN.md` across ARCHITECTURE/ROADMAP/DOMAIN/VERIFICATION, removed the
  root copy, and archived the original verbatim (rationalizations: "didn't map 1:1 onto one
  canonical file"; archived-verbatim-is-safe). Encoded the **DESIGN-slot** section (keep whole;
  thin set points into it; never split/relocate/archive — "distributed then archived" still
  destroys the living home). GREEN 2/2, disk-verified: doc intact at root both reps (one chartered
  by reference, one added an additive in-file charter).
- **AUDIT cold-rationale (tier 3) — RED 2/2 missed both planted axes** while producing 15–22
  disciplined real flags each: neither rep followed the reference-cited cold doc (its drifted
  code-coupled `DayWindowKey` snapshot escaped both), and both cleared a planted
  lengthy+cold+evergreen section with no extraction concept available. Encoded: the
  journal-exception (follow citations; **decision-consistency check**; code-coupled fact in a cold
  doc = tier violation) + the **`extract-cold`** schema action. GREEN 2/2: both flagged the cold
  doc's snapshot with exact evidence while keeping its sound reasoning (zero cry-wolf), both
  emitted textbook `extract-cold` on the planted section — and **the rule generalized**: both also
  caught the *unplanted* real instance (`docs/design/cache-contract.md`, a code-coupled contract
  doc riding in the journal tier).
- **AUDIT disk-verify gate — DROPPED; baseline passed.** 2/2 orchestrator reps independently
  re-verified every seeded flag against disk and refuted the fabricated one ("conservative
  evidence cuts both ways") — the existing evidence rule already induces orchestrator-level
  verification, so per the no-failure gate the guidance was not added; this record is the
  no-failure documentation. (The seeded list also exercised the group-1 wording: `graduate`
  presented as apply-able post-adjudication, `flag-code-bug` as report-only, approve/amend/defer
  vocabulary in use.)
Word-count REFACTOR: AUDIT's step-1/step-3 model-guidance stacking compressed meaning-preserving
(all benchmark numbers kept) — AUDIT 1287 w, SETUP 927 w after the additions.

**Family review 2026-07-07 — round 2 (mechanical half applied; behavioral half executed — next entry).** A
max-effort correctness+intent review after SETUP's first in-repo run verified: all three synced
spec files satisfied by shipped text, deployed=source byte-identical, AUDIT's benchmark numbers
faithful to the origin record, DOMAIN.md-rename propagation clean — and banked a **live GREEN**:
the sub-project flag-and-skip + redirect (the 0/4 RED gap) fired correctly on a real portfolio
root. Mechanical fixes applied directly: MAINTAIN's description trimmed to SDO triggers (the
whats-next-spec rule, applied family-wide); README's tier line gains VERIFICATION; whats-next's
crux uses the schema term `flag-code-bug`; the journal tier reads "never retconned (edits only
via graduation-prune)" (reconciling MAINTAIN's prune); the charter table labeled as WBPP's
instance; the benchmark catalog's later-assigned IDs (C19/C21 solid, C20 soft) appended. Five
behavioral candidates then ran RED→GREEN (record:
`openspec/changes/archive/2026-07-07-fix-skill-review-round2/`; outcomes next entry): SETUP
legacy-named domain doc (rename-into-`DOMAIN.md` on re-run, else the WBPP/TSM/Library re-runs
mint a duplicate domain home), SETUP non-git-target safety, SETUP container/portfolio-root
router-only case (live RED this session — a scaffolded portfolio-root set was judged noise),
whats-next scoped audit-first, AUDIT small-set right-sizing.

**Round-2 behavioral batch — executed 2026-07-07 (RED→GREEN; synthetic fixtures per the
structural-failure rule; Sonnet workers; 2 reps/scenario; candidate-text injection;
disk-verified throughout).** **3 of 5 passed RED — no-failure gate, no text shipped:**
legacy-named domain doc (2/2 `git mv` `OBSERVING.md`→`DOMAIN.md`, content preserved, zero
duplicate homes — the existing whatever-the-content-is + normalize-filenames lines already
induce the rename), whats-next audit-first (2/2 proceeded on fresh docs; absent audit output
recorded as an honest manifest row, no unconditional-precondition reading), AUDIT small-set
right-sizing (2/2 volume-reasoned plans — "per-section collapses to per-doc", conditional
round 3, loop-until-dry intact; both reps caught both planted drifts + two accidental ones,
zero cry-wolf, one textbook `flag-code-bug`). Their delta-spec requirements carry
disk-verify-style status notes. **2 shipped text:** (1) **SETUP non-git net** — RED 2/2
merged-then-*deleted* originals on the unversioned tree with no net (rep 2 noticed the gap,
"compensated" with self-review, deleted anyway; rep 2 partially confounded by harness
leave-uncommitted wording, rep 1 failed clean); encoded the Safety branch ("Not a git repo?
Create the net first… never merge-and-delete on an unversioned tree; pure-scaffold may
proceed"); GREEN 2/2 — both `git init`'d and committed the originals verbatim *before*
restructuring (baselines disk-verified recoverable). (2) **SETUP container root** — live RED
banked (this session: full set scaffolded at the portfolio root, judged noise, trimmed to
router-only); encoded the container-root router-only rule beside the sub-project rule; GREEN
2/2 — router-only at root, sub-projects untouched (clean trees), redirects delivered, and
both reps *composed* the two new rules (pure-scaffold exception correctly invoked for the
additive router; b-reps correctly judged it not-applicable). Method notes: poisoned-fixture
rule held (no spec-containing project used); footer doc-pointers stripped from injected
texts; fixture D's accidental ROADMAP↔NOTEBOOK mismatch was caught by both whats-next reps
(bonus discipline signal). SETUP 927→970 words after the additions — within precedent, no
compression pass. Change record: `openspec/changes/archive/2026-07-07-fix-skill-review-round2/`.

**AUDIT worker-death hardening — 2026-07-10 (field RED → synthetic RED→GREEN on a non-derived
fixture; 2 reps/phase; script-authoring task, report-only, no fixture tree).** Field evidence:
TSM's `tsm-docs-audit` workflow (`wf_ed9d6885-ddb`) lost a Round-1 section worker (ROADMAP.md
73-260, "2026-07-06..08 shipped entries") to an API `server_error` mid-response; the
orchestrator's script — authored with the then-current skill — had `filter(Boolean)` and nothing
else: no retry, and the adjudication report would never have said the span lost its deep pass
(whole-doc replicates happened to cover it; nothing would have disclosed that). Synthetic RED
(fictional HydroLog fixture — non-derived per the poisoned-fixture rule): **1/2 failed** — rep 1
no retry, dead workers mislabeled as parse failures in a buried stats field; rep 2 organically
retried unparseable output once and named unswept partitions. Non-deterministic omission → text
ships. Mechanism note: hand-rolled JSON parsing is what *prompts* retry thinking; the real
Workflow `schema` API moves validation to the tool layer, leaving `agent()→null` as the sole
failure surface — precisely the path the field run forgot. Shipped (structural recipe elements,
not prohibitions): step 1 "retry a dead worker once; still dead → name it in the coverage note
(step 3)", step 3 the coverage note itself (name the span + what covered it instead), one
Common-mistakes bullet ("Swallowing dead workers"). **GREEN 2/2**: both candidate-text reps
built a retry-once wrapper keyed on null/throw (one correctly distinguishing `[]` = clean slice
from null = dead) and a coverage-note section naming dead spans with their fallback coverage
(one pre-computed a `coveredBy` string per worker class; one refused to count a
round-with-deaths as dry). AUDIT SKILL.md 1287→1382 words — within precedent.

**Hybrid-rulebook rewrite — family-wide, 2026-07-11→13 (RED/GREEN arms 1–2 + TP ecological +
round-3 delta; opsx change `apply-hybrid-rewrite`).** Form decision 2026-07-11: hybrid rulebook
— numbered rule IDs, each carrying a one-clause why — over the house-narrative form; rules that
carry their rationale resist an executing agent rationalizing around a bare rule (RED evidence:
the "archived-verbatim-is-safe" rationalization), and the numbered form matches the dominant
external agent-skill convention (drafts + form options: `docs/archive/2026-07-11-*.md`).
Validation: arm 1 AUDIT+SETUP GREEN 2/2 (FermCtl), arm 2 MAINTAIN+whats-next GREEN 2/2
(TrailKit) — family GREEN 8/8 (`docs/2026-07-12-hybrid-red-green-arm{1,2}-results.md`); TP
ecological replay convergent with the old skills' real output + 3 hybrid-only improvements,
zero regressions (`docs/2026-07-12-tp-ecological-run.md`); round 3 re-validated the
CHANGELOG-convention delta — AUDIT R25 GREEN 2/2, SETUP A2′ GREEN 2/2, R21's hardened
why-clause shipped on field evidence + zero cost despite a null probe delta
(`docs/2026-07-13-round3-red-green-results.md`). Shipped 2026-07-13: all four SKILL.md replaced
(−21% words, zero rule drops, portable GitHub-URL footers). Rule-ID governance adopted with the
rewrite: IDs are append-only — convention + rationale in DOMAIN.md § Authoring conventions.

**Fat-router-lean — 2026-07-17 (RED→GREEN; opsx change `fat-router-lean`; SETUP S7 + AUDIT
R26).** Field origin: the TP ecological run — both skill generations scaffolded around a 24 KB
router but left its glossary/contract weight in place, and AUDIT never placement-flagged the
router itself (`docs/2026-07-12-tp-ecological-run.md`, finding 1). RED reproduced **only at
scale**: small synthetic 0/3 (reps leaned unprompted / flagged under R10+R12), real 24 KB TP
router 2/2 — both reps *saw* the fat, then read B2 "coexist, never clobber" as forbidding the
trim (a rule collision, not inattention) and grew the router 24→26 KB. Shipped: **S7** — lean
the router on encounter via an S1 move with an explicit B2 carve-out; trigger is a content test
(reference content vs routing/gotchas), not a size threshold — the ~40 KB perf line is the
*why*; **R26** — the router is placement-audited, one structural flag per off-charter block,
currency judged orthogonally (R26 suppresses only placement flags — router fat is
reference-tier, unlike journal-tier R25). GREEN 4/4 disk-verified content-preserving
(TP router 24 → 3.5/4.3 KB, every block to its charter home). Ground truth:
`harness/catalog-fat-router.md`; full scorecard: NOTEBOOK 2026-07-13/17.

**Openspec-archive awareness — 2026-07-26 (RED→GREEN on the TidePool fixture, extended with a
planted `openspec/changes/archive/`; opsx change `openspec-archive-awareness`).** Motivating gap
(from this repo's own opsx workflow, so TidePool stays a non-derived fixture): archived
`openspec/changes/archive/*/design.md` holds the *why* behind shipped decisions, and no skill
ever read the archive — audit can't flag absence (the schema requires a claim), maintain didn't
source it, so rationale silently died there. Fixture plants: O1 = archived design doc **cited**
from ARCHITECTURE, dense with design-time values drifted from shipped code (weights/norm/
falloff); O2 = **uncited** archived design doc carrying standing policy ("hand-curated
permanently; decline MDAPI-sync suggestions"); O3 = router with the old blanket "`openspec/` —
excluded, tooling" wording; O4 = the cited doc's cited-vs-uncited control. RED maintain
(1 rep, current text): failure mode sharper than predicted — **not absence but
non-determinism**: the rep found O2 only by declared scope-stretch ("conditional — user call,
since `openspec/` is excluded … arguably outside this sweep"), cited the router wording (O3) as
the basis of the hedge, and chose disposition `stub` while glossing it "archive stays
untouched" — the same output's Flag 1 used `stub` to mean *trim the source*, so the vocabulary
was unpinned and an apply pass could legitimately trim the archive. O4 classified `keep` per M2
**correctly** → per the no-failure gate, no cited-vs-uncited text was added. RED audit (1 rep,
current text): R15 tier-violation flag **fired** on O1 exactly as predicted (all three planted
drifts cited); the rep self-moderated the fix (edit the citation, not the archive), so the
failure is the mislabeling — archive-resident facts branded misplaced, one flag per citation as
archives accrue. Shipped: MAINTAIN **M11** (archived design docs a *first-class sweep source*,
router's generic exclusion does not exempt them, graduate disposition pinned `cross-ref`-only —
pointer lives in the reference doc, the archive is never stubbed/trimmed/relocated); AUDIT
**R14** names `openspec/changes/archive/` in the never-currency-audited set, **R15** gains the
carve-out (consistency check only; code-coupled facts there are design-time values, never tier
violations; standing truth inside is MAINTAIN's graduate job); SETUP **B1** wording clause
(router exclusion note marks archived design docs as maintain-swept historical records —
hygiene only; M11's override carries the behavior). GREEN maintain (1 rep): O2 graduated
unhedged → ARCHITECTURE with explicit "M11 mandates cross-ref only", O3 override stated in the
sources list, O4 still `keep` (and the rep spontaneously refused to back-port the archive's
drifted numbers), tree disk-verified byte-identical. GREEN audit (1 rep): O1 got the
consistency check with verdict *consistent*, the three drifts explicitly classified
"design-time values, not tier violations", zero tier-violation flags, general coverage intact
(R25 single structural flag held, planted D4 and both genuine-drift clusters found). MAINTAIN
SKILL.md 488→568, AUDIT 1070→1118 words — within precedent. Caveat:
1 rep/arm (not 2) — the RED failures were legible in the reps' own rationale, but a replicate
pass is the cheap upgrade if field behavior wobbles.

**Code-bug persistence — 2026-07-26 (field RED → synthetic RED→GREEN on TidePool + CB plant
class; opsx change `code-bug-persistence`; AUDIT R27 + MAINTAIN M12/M13).** Field origin: a
MAINTAIN run on TSM surfaced real code bugs; MAINTAIN had no in-schema channel and AUDIT's
`flag-code-bug` "hand-off" had no disk representation — adjudicated-real findings died with
the chat. Synthetic RED (CB1–CB4 plants: journal-contract-vs-code timeout regression,
no-contract drift control, persistence + dedup cells): both arms reproduced — reps *found*
the bugs (AUDIT discipline flawless) and lost them to ephemeral prose; failure class
omits-an-element → REQUIRED-slot form. Shipped: **R27**/**M13** — surviving report-only
flags persist to the *target project's* tiers before the run ends (dated
`docs/YYYY-MM-DD-<skill>-report.md` + deduplicated ROADMAP open-lines; deferred adjudication
→ single pointer line; the doc system is the bug tracker, `whats-next` sweeps both homes);
**M12** — report-only channel with R7-mirror cardinal-sin protection. Two GREEN-round
refactors, both from observed wobbles: design-time values in archived change records are
never contracts (v1 flagged archived-design drift), and corroboration strengthens but never
substitutes for guarantee language — dated records agreeing on an old value are history
(v2 flagged a two-historical-records TTL mismatch). Final wording micro-tested 2/2. No
fix-round orchestration — fixing stays dev/diagnose work (honesty posture). Full scorecard:
`docs/2026-07-26-code-bug-persistence-red-green.md`.

**Batch 2 — derivability discriminator + hold-on-bloat, 2026-07-26 (two changes, one
validation session; opsx `derivability-discriminator` + `m9-hold-on-bloat`).** Origins: a
user design question ("are we documenting what's better derived from code?") and the same
day's TSM field RED (three graduations into a 38 KB ARCHITECTURE, split asked after — plus
the maintain-vestigial-prune critique). Shipped: AUDIT **R28** — stale cheaply-derivable
rationale-free values get a deletion-led fix proposal, not a re-cached grep (RED 4/4
re-cache; GREEN de-valued on disk, no over-fire on rationale-bearing or contract values);
MAINTAIN **M9** hardened in place — apply-time content test, stuff-then-ask/never-noticing
named as the violation — plus **M14**, the hold procedure (report entry + one deduplicated
ROADMAP split-job line; split runs as its own job; held promotions land in split homes).
M9's RED repeated the fat-router scale lesson precisely: framed probes 0/2 but on-disk 1/1
stuff-silently on a generated 25.7 KB fat-ARCH fixture (25,734→26,859 B, zero split
mention); probes also caught the unpinned-hold non-determinism M14 pins. Full scorecard:
`docs/2026-07-26-batch2-red-green.md`; fixture: `harness/tidepool-fixture-variants/fat-arch/`
+ DV/FA catalog cells.

**B4 portfolio DOMAIN — 2026-07-26 (probe → decision → RED/GREEN; opsx change
`b4-portfolio-domain`; SETUP B4′ + MAINTAIN M15).** Origin: two same-day field signals —
TSM's maintain surfaced a cross-project glossary cross-ref loop, and the observational B4
probe at the real Astronomy container reproduced the S7↔B4 collision (cross-repo contract
prose with no sanctioned home). User adjudicated Option A: container root = router + at
most two thin portfolio docs (optional `DOMAIN.md` chartered *cross-repo truth only*;
optional thin status ROADMAP), owner rule, one-way pointers. RED on the new ReefStack
fixture: 3 resolutions across 4 container reps under old text — including both fixture
reps creating a root DOMAIN while *openly declaring it a B4 exception* (a rule
contradiction: the correct action was criminalized); maintain rep stuffed the portfolio
truth into the container router and half-broke the planted loop. GREEN 5/5: sanctioned
DOMAIN with owner rule 2/2, single-project control clean (no over-fire), maintain hold on
M13 rails with container byte-untouched, PL2 targets the DOMAIN when present. Records:
`docs/2026-07-26-b4-portfolio-probe.md`, `docs/2026-07-26-b4-red-green.md`; fixture
`harness/reefstack-fixture/` + `catalog-reefstack.md`.

**Maintain right-sizing — 2026-07-26 (opsx change `maintain-right-sizing`; MAINTAIN M16;
two halves no-failed).** Origin: TSM field feedback (12:1 add:remove ratchet; same-day
ritual sweeps). Proposed three teeth; the iron law kept one: the description rewording
no-failed (invocation probes 0/2 — agents already decline low-yield sweeps under the
current text) and the mandatory prune pass no-failed (RED rep found both planted prune
cells unforced) — both status-noted in the delta spec, no text. Shipped: **M16** — the
dated report ends with a REQUIRED accounting slot (prune/archive candidates or the
explicit "prune candidates: none found" + a one-line net reference-tier delta; silence
illegal for either). RED: the delta line was absent in the synthetic rep and every prior
report. GREEN 1/1 disk-verified with full M-stack regressions clean. Record:
`docs/2026-07-26-right-sizing-red-green.md`; cells PR1–PR3 in `harness/catalog-tidepool.md`.

