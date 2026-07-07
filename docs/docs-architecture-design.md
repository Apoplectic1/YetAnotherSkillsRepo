# Docs-architecture skill family — design & spec (canonical)

**Canonical design** for the global docs-architecture skills (SETUP · AUDIT · MAINTAIN ·
TRIAGE), maintained here in `E:\Projects\AI\Skills`. The goal these skills serve: make an AI
agent's work in any project trustworthy — every fact current, single-sourced, and accessible
**token-efficiently, without being pointed at files**.

**Genesis / worked example:** derived by reorganizing the WBPP project's docs (2026-06-28 —
"Phase 1" structure + "Phase 2" audit). The WBPP-specific *execution* record stays in WBPP
(removed from there later); the WBPP examples kept below are the grounding worked-example.

> **Note (2026-06-28):** graduated out of WBPP `docs/2026-06-28-docs-reorg-plan.md` — that copy
> is a pending-removal duplicate; **this** file is canonical. Some body text still uses WBPP-first
> "Phase 1/2 executed" framing; it'll be generalized as each skill is authored.

> **Status:** Phases 1 & 2 **executed 2026-06-28**. Phase 1 (structure, `docs-reorg-phase1`) —
> CLAUDE.md router + always-on lean (20→14 KB), ROADMAP port-history → `archive/`, per-doc
> charters. Phase 2 (content/currency audit, `docs-reorg-phase2-audit`) — 41 flags adjudicated
> & applied across the live reference tier (currency fixes, single-source relocations, GPU +
> correspondence → archive/design-doc). **Phase 3 (skillify) is the remaining arc.** This note
> follows the conventions it proposes (dated journal entry, purpose-first header, cross-refs)
> — dog-fooding the model.

---

## Why — the meta-goal

The overriding objective is **not** "tidy the docs." It is to **make current work
trustworthy**: every fact the agent acts on should be current, single-sourced, and legibly
so. Reducing stale / superseded / outright-wrong information from polluting active work is the
spine; structure is in service of that. A secondary, explicit constraint: optimize for
**AI-access first** (the user reads these too, but the transparency target is the agent).

## How Claude actually accesses docs — the model that drives everything

**Only three files auto-load into context each session** (verified from this session's
start-up context block):

- `~/.claude/CLAUDE.md` — global cross-project rules (genuinely global; does **not** move into
  the repo).
- `<project>/CLAUDE.md` — project orientation + gotchas. **The router.**
- `<memory>/MEMORY.md` — a ~1.3 KB stub that already delegates project knowledge to the repo
  docs (memory was migrated out 2026-06-16). Harness-fixed path; cannot be relocated into the
  tree — but it carries no content worth moving.

Consequence: **everything else (ROADMAP, ARCHITECTURE, OBSERVING, VERIFICATION, NOTEBOOK,
docs/*, NOTICE.md) is pull-on-demand.** The agent finds those *only because CLAUDE.md
describes and routes to them.* CLAUDE.md is a router; the organization is "accessible" exactly
to the degree CLAUDE.md indexes every leaf. (This is why `NOTEBOOK.md`, absent from the
router, was effectively invisible — the bug that motivated this review.)

The agent's four access primitives and their costs:

| Primitive | Cost | Gives |
|---|---|---|
| Auto-load (CLAUDE.md, MEMORY.md) | paid **every session** | always-on context — must stay small + high-value |
| `Glob docs/*.md` | ~free | the **filename list** — a live table of contents *if names self-describe* |
| `Grep` across docs | ~free | content search — file+line for a keyword without reading |
| `Read` w/ offset | cheap if sliced | one section, *if* the agent knows which |

**Key inference:** a hand-maintained manifest file (a `DOCS.md`) is just a drift-prone cache
of what `Glob` + `Grep` already compute live. The most automatic, always-current manifest is
**no manifest** — a self-describing file tree the agent's free tools read directly.

Two access patterns, wanting opposite structures:

- **Retrieval** ("I know the topic, where's the fact?") → served by many small, well-named,
  greppable files. Fragmentation *helps*.
- **Synthesis** ("what do I need to know about subsystem X?") → served by one consolidated
  narrative. Fragmentation *hurts*, and worse: a pile of dated files leaves the agent unable
  to tell **stale from current** cheaply. This is "detail/nuance lost in a plethora of
  files," stated mechanically.

## The doc tiers: journal · reference · cold rationale

Resolves the two-patterns tension. (Latent already — `NOTEBOOK.md`'s own header says
findings "should graduate into OBSERVING.md / ROADMAP.md"; this formalizes it.) **Refined
2026-06-28 (the CC-tuning split) from two tiers to three** — adding *cold rationale* for
lengthy evergreen "why" that isn't needed for immediate reasoning.

```
JOURNAL  (capture; the user's divide-and-conquer instinct — KEEP IT) — TWO members:
  • docs/YYYY-MM-DD-<slug>.md  = per-topic substantial dated records (decision/review/design)
  • NOTEBOOK.md              = the running lab notebook (short chronological empirical findings)
  split: small finding-from-doing-the-work → NOTEBOOK; substantial standalone record → docs/
  append-only · dated · never edited · legibly historical
  answers "what did we decide/find on date X"
        │  GRADUATE: fold standing truth upward, then PRUNE the source;
        │  the dated entry remains as the why/when record (or → archive/)
        ▼
REFERENCE  (truth; the ONE always-current source per topic)
  ROADMAP · ARCHITECTURE · OBSERVING · VERIFICATION
  topic-organized · edited in place · superseded prose deleted
  answers "what is true about subsystem X right now"
        │  EXTRACT: lengthy evergreen *reasoning* not needed for immediate
        │  reasoning → a dated cold doc + a one-line reference back
        ▼
COLD RATIONALE  (the *why*, kept but off the daily path)
  docs/YYYY-MM-DD-<topic>-rationale.md
  dated · evergreen reasoning · referenced, never inlined
  answers "WHY is this the right principle" (signal-processing / design theory)
```

Journal = retrieval + capture; reference = synthesis + truth; cold rationale = the lengthy
*why* a reference decision is correct, parked so the daily-path doc stays scannable.
**Graduation (with prune) is what stops the journal becoming the stale pile that defeats
synthesis.** Pruning is the linchpin: graduate without deleting the source and you've created
the duplication you were avoiding.

**The extract discriminator (what's safe to cold-store).** Extract to cold rationale ONLY
content that is BOTH (a) **cold** — not needed for immediate reasoning — AND (b) **evergreen
reasoning**, not code-coupled: it explains *why a principle holds* and would still be true if
the code were never written. Anything naming a **file / function / flag / value** stays in the
audited reference tier. (CC worked example: "why high sigma sheds the noise tail" / "denoise
late" → cold doc; `configureAutoCC` → ROADMAP; `ccDarkK = 18` → OBSERVING.) Extract
**selectively** — fragmentation hurts synthesis, so split only when the why is genuinely
lengthy *and* cold.

## The index that auto-scales — convention-routing, not enumeration

CLAUDE.md routes the two tiers **differently**, and that asymmetry is the whole trick:

- **Reference docs → enumerate by name.** ~5 docs, stable, rarely added. A few router lines.
  Manual enumeration is fine *because the set doesn't grow* (graduation consolidates, it
  doesn't multiply).
- **Journal → route by convention, never list.** One drift-proof line, e.g.: *"`docs/` holds
  dated decision records & reviews — `glob docs/*.md` for the current list (filenames are
  self-describing), grep for content; standing truths graduate into the reference docs
  above."* Add 50 files and that line is still accurate. (Enumerating a *growing* set is the
  anti-pattern that orphaned NOTEBOOK.)

No `DOCS.md`. Router lines are **purpose/use-centric** ("what it's for / when to read / what
to grep") — the high-signal form for both a human skimming and the agent routing.

Two cheap conventions make the free tools sing (the docs/ entries already do both):
1. **Self-describing filenames:** `2026-06-28-nsg-drizzle-ordering.md`, not `notes3.md`.
2. **First line `# <date> — <purpose>` + a one-sentence "what this is / when to read"** — so
   the agent can `Read` line 1 only of each grep hit to triage.

## Per-doc charters — the placement test

A one-line charter per reference doc makes the Phase 2 audit objective (does this section
match its doc's charter? else move / cross-ref-and-delete):

| Doc | Charter |
|---|---|
| `CLAUDE.md` | always-on **router** + load-bearing gotchas only (no volatile content) |
| `ROADMAP.md` | feature-architecture · constant-rename table · validation matrix · *(port history → archive/)* |
| `ARCHITECTURE.md` | subsystem mechanics deep-dives (how it works) |
| `OBSERVING.md` | site · targets · workflow · NSG tuning · XFM keyword contract · repo conventions |
| `VERIFICATION.md` | run-verification runbook |
| `NOTEBOOK.md` | dated empirical findings (journal / lab notebook) |
| `docs/` | dated decision records, reviews & **cold-rationale** notes (journal + tier-3) |
| `nsg-v8-fork/NOTICE.md` | vendor fork playbook (patches, re-fork procedure) |
| `MEMORY.md` | stub delegating to repo docs (leave; cannot move) |

## Anti-staleness design principles

Staleness danger scales as **(how always-on) × (how duplicated) × (how volatile / code-coupled)**.
Antidotes, in severity order:

1. **Keep the always-on layer thin + routing-only.** A wrong fact in CLAUDE.md/MEMORY is in
   the agent's head *before it reads anything*, every session. Push volatile detail **down**
   into on-demand reference docs read fresh. (= the "always-on lean," approved.)
2. **Single-source every fact; cross-reference, never copy.** Duplication is the #1 drift
   source. Charters enforce one home per fact.
3. **Make currency legible.** Dated journal files are *good* here (self-evidently snapshots).
   The danger is **undated reference prose** silently gone stale → use grep-pointers ("grep
   the headers, they drift" — ARCHITECTURE.md already does this) or last-verified stamps on
   volatile sections.
4. **Docs describe *why / contract*, not line-by-line *how*.** The tighter prose mirrors exact
   code, the faster it rots; point at code (always current) for the "how."
5. **Cold rationale (tier 3) stays evergreen-only.** Lengthy "why" extracted to a dated cold
   doc must be *reasoning*, never code-coupled facts. The AUDIT skill **currency-checks the
   reference tier against code**, but only **decision-consistency-checks** cold docs (does the
   reasoning still match the decision?) — so a code-coupled fact parked in a cold doc escapes
   the currency sweep (stale-prone *and* unaudited). Extract selectively; fragmentation hurts
   synthesis.

**`archive/` — strict archival-only convention (user, 2026-06-28).** `archive/` holds **only
not-current-design-relevant** material — superseded / done / obsolete. It is **deletable without
losing current information**; **git is the backstop** for the history. Nothing an agent needs for
*current* work lives here. The routing **test** is exactly that criterion — *"still
current-design-relevant?"* No → `archive/` (or just let git hold it); Yes → it stays in the live
set (journal / reference / a short ROADMAP digest). Physical separation makes the tier legible.
(Distinct from `openspec/changes/archive/`, OpenSpec's completed-change store.)

**Shipped history / "changelog": git is the changelog.** Keep a short "Recently shipped" digest in
`ROADMAP.md` (current-relevant); the long tail is `git log`. **No `CHANGELOG.md`** (redundant with
git) and **never route shipped-history into `archive/`** — a still-referenced changelog isn't
archival, and routing it there blurs the term. Referenceable history (decision records, findings,
the *why* behind current things) is the **journal** (`docs/YYYY-MM-DD-*.md`), not archive.
(Resolves the RED-baseline split — rep1 shipped→archive, rep2 invented CHANGELOG — by adopting
neither.)

OpenSpec role: **workflow/task only** (explore / propose rituals). It is *not* a third
knowledge home — durable knowledge stays in `.md` docs. `openspec/specs/` stays sparse by
choice. (Decision records like the NSG-drizzle note belong in `docs/`, not as spec deltas —
the friction that surfaced this.)

`graphify-out/` — **deleted** 2026-06-28 and not used for this project: a static graph
snapshot competes with always-current native tools, is low-value at this repo's scale, and its
staleness actively works against the meta-goal (it asserts relationships authoritatively).

## Decisions locked

- CLAUDE.md = router; two-tier (journal → reference) + graduation/prune workflow adopted.
- Convention-routing for the journal; enumerate-by-name only the stable reference set; **no
  DOCS.md**. Purpose/use-centric router lines.
- Always-on lean: agent will propose cuts to CLAUDE.md (volatile detail down, routing +
  load-bearing gotchas stay).
- OpenSpec = workflow-only. graphify dropped. `archive/` adopted.
- Global `~/.claude/CLAUDE.md` and the memory stub stay put (not project-specific / harness-fixed).

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
                        Proposes priority; user owns the call. No Phase prototypes it yet —
                        author after the trio, once real audit/maintain outputs exist to consume.
                      All four GLOBAL (~/.claude/skills/), data-driven (read the project's
                      charters at runtime). Non-redundant with `init` / `improve-architecture`.
                      Author with `superpowers:writing-skills`.
```

Sequencing rationale: Phase 1 enables Phase 2 (charters make the audit objective) *and*
shrinks it (history split out of scope). Phase 3 is derived, not speculative — doing Phases
1–2 well **is** the design effort for the skills: Phase 1 prototypes SETUP, Phase 2 prototypes
AUDIT (the in-flight `docs-reorg-phase2-audit` run — its agent prompts, flag schema, and
conservative-evidence rule are the skill's spec), and the graduate/prune workflow prototypes
MAINTENANCE.

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
(this design doc's pending-removal duplicate), so both "unguided" baselines read it and reproduced
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
`openspec/changes/fix-skill-review-findings/` (in this repo).

## SETUP-skill spec (Phase 3 design — grounded in target projects)

Grounded 2026-06-28 in a survey of the projects the skills will first run on (sibling C#/.NET
Astronomy projects + this one): **TargetPlanner (TP)**, **TargetSchedulerManager (TSM)**,
**Library** (shared, multi-consumer), **XisfFileManager (XFM)**, **IntervalScheduler (IS)**,
**WBPP** (here). Enforce the *shape*, not a rigid filename list:

**Enforce the canonical filename SET, not just the principles** (user directive 2026-06-28):
consistent names across projects are what make switching frictionless — `ARCHITECTURE.md` is
*always* the deep-dive; `VERIFICATION.md` *always* answers "how do I verify a change here." So
SETUP creates the full named set every time (charter-guarded — see reconciliation below), with
only README/RELEASING genuinely conditional.

| Doc | Enforcement | Survey evidence / note |
|---|---|---|
| `CLAUDE.md` (router) | **enforced — universal** | the router; in all 5 already |
| `ARCHITECTURE.md` | **enforced by name** | **Library + XFM lack it** (180 / 77 .cs) → scaffold (charter-guarded if thin) |
| `ROADMAP.md` | **enforced by name** | all 5 have it |
| `NOTEBOOK.md` | **enforced by name** | the lab-notebook home — present even if empty (charter'd; invites use as findings accrue) |
| `VERIFICATION.md` | **enforced by name** | always answers "how do I verify a change here" — even when that's just "= `dotnet test`, CI at X" (so it's useful for the test-backed apps too, *revising* the earlier "conditional") |
| `docs/` + `YYYY-MM-DD-*` journal | **enforced — the tier** | all have `docs/`; convention varies (TP subdirs, XFM **undated**) → standardize |
| domain/strategy doc | **enforced slot — name elicited** | name varies: TSM `UI-CONVENTIONS`, Library `PCL InterOp`, WBPP `OBSERVING` |
| `README.md` | conditional (public/GitHub entry) | distinct audience from CLAUDE.md; TP has one |
| `RELEASING.md` | conditional (project ships) | TP has one |

**Hard scope-exclusion list — the key new requirement the survey surfaced.** SETUP never
scaffolds into, and AUDIT never scans: **vendored** trees (Library `PCL/` + its `3rdparty/`
lz4/zstd, each with their own READMEs; WBPP `nsg-v8-fork/`), **generated** artifacts
(`BenchmarkDotNet.Artifacts`, `bin`/`obj`), and **tooling** dirs (`.claude/`, `.superpowers/`,
`openspec/`). Without this, an audit of Library drowns in vendored docs.

**Refinement candidate — router-anchored scope (surfaced by the WBPP re-apply, 2026-06-28).**
A flat dir-glob exclusion is too coarse: a vendored tree can hold a *router-listed project doc*
(`nsg-v8-fork/NOTICE.md` is the fork's own playbook, in the router — but the Library `PCL/`
READMEs are *not*). Better rule: **in-scope iff the router names it** (∪ the canonical set ∪ the
journal convention); the vendored/generated/tooling exclusions become the *default for unrouted
files*, not a hard wall. This dissolves the "excluded-tree-with-an-included-leaf" case. Pairs
with the **re-fork lifecycle**: fork *source* = read-only ground-truth (AUDIT currency-checks
references *against* it, never edits it); the fork *playbook* (router-named) = a maintained doc.
Needs a failing test before encoding in SETUP/AUDIT (Iron Law).

**Sub-projects vs vendored — distinct cases (user policy, 2026-06-28).** *Vendored* = third-party
(exclude the source; keep only router-named leaves correct, per above). A *sub-project* is the
user's OWN nested project with its own governance — detect it by its **own router / `.git`**.
Policy: **the root project's `.md` suite governs the whole tree**; SETUP does **not** scaffold a
canonical set into every sub-dir, and a root run **never reaches into a sub-project to restructure
its docs**. On encountering a sub-project it **flags-and-skips** (reports it + any unconventional
names) and notifies the user to **run the skill from the sub-project's dir** to govern it as its
own unit. Cross-boundary references (root↔sub) are kept correct/consistent. Clean per-sub-project
recursion *from* the root is an acceptable **future** enhancement, but flag-and-skip is the safe
v1. Needs a failing test before encoding (Iron Law).

**Coexist, never clobber:** TSM already has `openspec/` + opsx + `.superpowers/sdd/`; TP has
`.claude/skills/verify-ui`. SETUP augments an existing setup.

**Enforce names, not content — the charter-guard reconciliation.** Enforcing the full named set
is what makes switching projects frictionless; the empty-stub worry is resolved by the **charter
line** — an enforced file is *never blank*. It carries its purpose + either content or an honest
status ("verification = `dotnet test`"; "no subsystems yet"). A thin charter'd file is *legible*
("nothing substantial here yet") and a ready home the moment content accrues — not hollow. So
SETUP **creates the full set every time**, charter-guarded; content scales with the project.

**Project-shape variance SETUP must handle:** the survey spans populated apps (TP 95 .cs), a
multi-project lib (Library 180 .cs / 11 projs), and a **design-heavy / code-light** project
(**IS**: 3 .cs but a **75 KB `SCHEDULER_DESIGN.md`** + stub ARCHITECTURE/ROADMAP). So SETUP must
not assume code-rich — a big standalone design doc is architecture-in-waiting: treat it as a
**`DESIGN.md` slot** (the seed that graduates into ARCHITECTURE/ROADMAP as code lands), don't
force-split it. VERIFICATION is moot pre-code.

**First customers / killer demo:** TP's **125 KB ROADMAP + 70 KB ARCHITECTURE** (and Library's
33 KB ROADMAP) are the pre-split WBPP state → the SETUP+AUDIT skills' first real targets, TP the
lean/split demo. XFM is critical/daily-use and **mid-migration to Library** (a consumer of the
multi-consumer lib; *upstream* of WBPP's XFM keyword contract), so cross-project doc consistency
there compounds.

## Open / still to decide

- ROADMAP history split: confirm the exact seam (what is "history / phase-log" vs "live
  feature-architecture") when Phase 1 runs.
- Whether the SETUP skill is authored after Phase 1 alone or after Phase 2 (so it captures the
  audit step as part of bootstrap).
- Each phase to be formalized as its own effort when leaving explore mode (Phase 1 first).
