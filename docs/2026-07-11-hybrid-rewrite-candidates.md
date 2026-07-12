# 2026-07-11 — Hybrid rewrite candidates: the full four-skill family

**What this is / when to read:** the four candidate SKILL.md texts in the **hybrid-rulebook
form** (Option C of `2026-07-11-audit-rewrite-draft.md`, adopted the same day), implementing the
decisions of `2026-07-11-skill-portability-review.md` §7. Proposal artifacts for the planned
openspec change — nothing under `skills/` is modified; candidates apply only after full
RED→GREEN. Read alongside the audit-draft note, whose conservative candidate doubles as the
content inventory (every rule the reformat must carry).

## Form decision (closes the audit-draft note's pending question)
**Option C — hybrid rulebook** adopted family-wide; final call delegated in-session to the
assistant's judgment. Rationale: the one-clause whys retain the anti-rationalization property
the RED records argue for; rule IDs (S/T/A/B, R, M, W) give the harness and future audits stable
citations for exactly which rule a failure violates; procedures stay numbered flows; flag
schemas stay verbatim; the smaller body cuts the context cost paid at every invocation. House
elements deliberately kept inside the form: worked cues on the subtle discriminators (contract
violation R7, modality R5–R9, DESIGN slot B5), and the enforced-set / sweep tables.

## Word counts — and the honest compression ceiling
| Skill | Shipped | Hybrid | Δ |
|---|---|---|---|
| docs-architecture-audit | 1,382 | 944 | −32% |
| docs-architecture-setup | 970 | 876 | −10% |
| docs-architecture-maintain | 630 | 488 | −23% |
| whats-next | 684 | 505 | −26% |
| **family** | **3,666** | **2,813** | **−23%** |

Two calibration points (conservative dial −12%, hybrid −23%) support one conclusion: **with zero
rule drops this family bottoms out near ~2,800 words.** SETUP compresses least — it was already
rule-dense with little provenance overhead; AUDIT most — it carried the bulk of the asides and
restatements. Anything materially smaller means dropping RED-tested rules (the declined
aggressive-cut option). Portability status: grep-verified zero constellation/local tokens across
all four candidates; footers → one GitHub URL each; model guidance dual-form; benchmark numbers
kept as uncited claims.

## Validation plan (the adjudicated Q4: full RED→GREEN)
- **Fixture: synthetic, non-derived** — per the poisoned-fixture rule and the established
  synthetic-fixture precedent. Planted, cataloged defects give scoreable ground truth (recall
  per rep, like the worker-model benchmark). No standing fixture exists and none is required;
  the reset contract (`git reset --hard <marker> && git clean -fd`) applies after every
  mutating run.
- **A restored-from-backup real project is the escalation, not the default** — most valuable
  for SETUP (real-world doc messiness is what synthetic fixtures under-model) if its synthetic
  GREEN looks weak.
- **Protocol per skill:** RED = 2 unguided reps on the fixture task (re-confirms the failure
  modes the rules exist for, on current models); GREEN = 2 reps with candidate text injected
  (confirms the reworded rules still induce compliance); disk-verify every claim; judge by
  output text, not exit codes.

## Candidate: docs-architecture-setup (876 words)

````markdown
---
name: docs-architecture-setup
description: Use when bootstrapping or standardizing a project's documentation for AI navigation — a new project, or an existing one with no CLAUDE.md router, scattered/missing docs, or inconsistent ARCHITECTURE/ROADMAP. Also when onboarding a project into a portfolio that shares a doc convention.
---

# Docs-architecture setup

Bootstrap a project so an agent navigates it the same way as every other: one always-loaded
`CLAUDE.md` **router** pointing to a canonical, **charter-guarded** doc set. Carry the set as a
rule — never infer it from sibling repos. *(A sibling may not exist; inference drifts between
projects.)*

## Safety — restructure, never destroy (highest priority)
- **S1.** Consolidating = **merge** (drop nothing); moving history = **move**, not delete;
  renames preserve content. Unsure whether something is still needed → move it to `archive/`,
  never delete.
- **S2.** Apply on a **clean git tree** (commit first) and **present the diff for review before
  committing**. *(Every change stays recoverable.)*
- **S3.** Not a git repo? **Create the net first**: `git init` + commit the originals (or
  snapshot them to `archive/pre-setup/`) *before* any restructuring — never merge-and-delete on
  an unversioned tree. A pure-scaffold run (new files only) may proceed, noting the tree is
  unversioned.
- **S4.** A large/diverse project (many existing docs) deserves extra care: survey fully before
  touching anything; prefer several small reviewed applies over one big one.

## The enforced set — create every file, charter-guarded
| File | Role |
|---|---|
| `CLAUDE.md` | always-loaded **router** + load-bearing gotchas (kept thin) |
| `ARCHITECTURE.md` | subsystem mechanics (how it works) |
| `ROADMAP.md` | forward-looking design + a short "Recently shipped" digest |
| `NOTEBOOK.md` | running **lab notebook** (chronological empirical findings) |
| `VERIFICATION.md` | how to verify a change — *even if* just "= `dotnet test` / `npm test`, CI at X" |
| `DOMAIN.md` | the human/strategy home (science / conventions / site-process / UI rules) |
| `docs/` | journal: `YYYY-MM-DD-<slug>.md` per-topic dated records |
| `README.md`, `RELEASING.md` | **conditional** — public entry point; project that ships |

- **S5.** **Charter-guard:** every file opens with a one-line charter (purpose / when to read).
  A thin file states an honest status ("verification = the test suite"; "no subsystems yet") —
  **never blank**. *(Charter'd-thin is legible and a ready home; blank is noise. NOTEBOOK and
  VERIFICATION are the two files unguided runs reliably omit — create them.)*
- **S6.** The domain doc is **always named `DOMAIN.md`** — do not elicit a content-specific
  name; do not rename an existing `DOMAIN.md`. Whatever the content *is*, it lives there; when
  absent, create it charter'd-thin. Never skip it.

## Tiers & routing — teach these in CLAUDE.md
- **T1.** **journal** (dated capture) = `docs/YYYY-MM-DD-*.md` + `NOTEBOOK.md`. Split: small
  finding from doing the work → NOTEBOOK; substantial standalone record → `docs/`.
- **T2.** **reference** (current truth) = ARCHITECTURE / ROADMAP / DOMAIN / VERIFICATION —
  edited in place.
- **T3.** **cold-rationale** (optional) = lengthy *evergreen* "why" not needed for immediate
  reasoning → a dated `docs/` note + a one-line reference back. Extract only when lengthy AND
  cold AND evergreen (not code-coupled).
- **T4.** The router names reference docs **by name**; the journal **by convention**
  (`glob docs/*.md` + grep) — never an enumerated, growing list.

## archive/ and the changelog — do not blur
- **A1.** `archive/` = **archival-only**: not-current-design-relevant, deletable (git is the
  backstop). Routing test: *"still current-design-relevant?"* No → `archive/` (or just let git
  hold it); yes → it stays live.
- **A2.** **git is the changelog**, plus a short "Recently shipped" digest in `ROADMAP.md`. No
  `CHANGELOG.md`; never route shipped history into `archive/`.

## Boundaries
- **B1.** **Hard scope-exclusions — never scaffold into:** vendored trees (`vendor/`,
  `third_party/`, forked upstreams), generated output (`bin/`, `obj/`, `dist/`, `target/`),
  tooling (`.claude/`, `openspec/`). Their own READMEs are not this project's docs; `CLAUDE.md`
  notes them excluded.
- **B2.** **Coexist, never clobber:** augment an existing setup — don't overwrite a present
  `CLAUDE.md` / `openspec/` / `.claude/`. Normalize filenames to the convention (no spaces;
  align casing).
- **B3.** A **sub-project** (nested tree with its own router / own `.git`) is its own
  governance unit: **flag-and-skip** — leave its docs alone, note it excluded in the root
  router, and report *"run this skill from `<sub-dir>` to govern it as its own unit."* *(Not a
  submodule/vendoring call — that's the user's separate decision.)*
- **B4.** A **container root** (the invocation dir holds no first-party project content — only
  sub-projects + tooling/exclusions) gets the **router only**: a `CLAUDE.md` chartered as a
  router with flag-and-skip routing to each sub-project + the exclusions — **not** the full
  enforced set. *(Per-project docs are the truth; a portfolio-level set is noise.)*
- **B5.** **Design-heavy / code-light:** a large standalone design doc **is the project's
  DESIGN slot** — keep it whole: charter it, route it by name, and scaffold the rest of the
  enforced set charter'd-thin pointing into it ("mechanics live in `<doc>` §N until code
  lands"). Its content graduates into ARCHITECTURE/ROADMAP as code arrives (a later MAINTAIN
  job). Never split, relocate, or archive it. *("Distributed then archived verbatim" still
  destroys the single living home.)*

## Procedure
1. **Survey** the tree: existing docs, the exclusions (B1), sub-projects (B3), and the
   container-root / design-slot shapes (B4, B5).
2. **Create/align** the enforced set, charter-guarded (S5, S6).
3. **Write `CLAUDE.md`** as the router (T4; exclusions noted; load-bearing gotchas only).
4. **Don't force content** — thin-but-charter'd is correct for a new/sparse project.

Full rationale + RED/GREEN provenance:
https://github.com/Apoplectic1/YetAnotherSkillsRepo/blob/main/docs/docs-architecture-design.md
````

## Candidate: docs-architecture-audit (944 words)

````markdown
---
name: docs-architecture-audit
description: Use when verifying a project's reference docs still match the code — after a refactor or rename, on suspected doc drift, before trusting a doc as current, or as a periodic doc-health pass. Assumes the docs-architecture conventions (a CLAUDE.md router + charter'd reference set).
---

# Docs-architecture audit

Audit reference docs on two axes, judged separately — **placement** (does each section match its
doc's charter?) and **currency** (does each claim still match the live code?) — producing an
evidence-carrying flag list the user adjudicates, then applying the approved fixes. A single
careful pass finds only ~half the real issues, non-deterministically; per-flag judgment is what a
capable agent already does well, so the rules below force what one pass can't give:
**completeness, and a mergeable, consistent output**.

## Discipline — highest priority; violations poison the run
- **R1.** Every currency flag carries a code citation (`file:line` / symbol) **or** the literal
  `unverifiable → ask user`. Never guess stale.
- **R2.** Judge by content, not filename. *(A name only prioritizes what to read first.)*
- **R3.** Edit **documentation only** — never source, first-party or vendored. *(Code findings
  are reports, not fixes.)*
- **R4.** Report-only actions are exactly `flag-code-bug` and `revisit-plan`: handed off (to the
  dev/diagnose flow and `whats-next`), never auto-applied.

## Currency — claim vs code
- **R5.** Classify modality first. **Descriptive** = how the system *is* (present tense;
  ARCHITECTURE, gotchas, "current status"). **Prescriptive** = how it *should/will* be (future
  tense; ROADMAP "Future", plan docs, open follow-ups).
- **R6.** Descriptive: **code wins** — a mismatch is a stale doc → `fix-doc`.
- **R7.** Exception — contracts: a guarantee the doc asserts (`must` / `always` / `never` /
  aborts-on-X, ideally with rationale, or corroborated by a test or another doc) that the code
  *violates* → `flag-code-bug`; the **code** is the suspect. Never `fix-doc` a contract into
  agreement with suspect code. *(That encodes the bug into the spec.)*
- **R8.** Plain value drift with no guarantee (a count, an intentionally-changed default/path) →
  `fix-doc`; unsure which case → `unverifiable → ask user`.
- **R9.** Prescriptive: **the plan wins** — code-not-matching is expected, never staleness. Plan
  already satisfied by code → `graduate` (an ordinary doc edit once adjudicated: move to
  "Recently shipped" / archive the plan). Plan contradicted by current structure →
  `revisit-plan`. *(Don't edit intent.)*

## Placement — section vs charter
- **R10.** Off-charter section → `move-to <doc>`, or `cross-ref+delete`. *(Single-source every
  fact.)*
- **R11.** `extract-cold` (propose a dated `docs/` cold doc + a one-line reference back) only
  when a section is lengthy **and** cold **and** evergreen — all three; a short, warm, or
  code-coupled section stays put.

## Scope
- **R12.** In-scope = what the `CLAUDE.md` router names, ∪ the canonical reference set.
- **R13.** Default-exclude *unrouted* files in vendored trees (`vendor/`, `third_party/`, forked
  upstreams), generated output (`bin/`, `obj/`, `dist/`, `target/`), and tooling (`.claude/`,
  `openspec/`). A router-named leaf inside them *is* in scope.
- **R14.** Never currency-audit the journal (`docs/`, `NOTEBOOK.md`) or `archive/`.
  *(Append-only, legibly historical.)*
- **R15.** Cold-rationale docs a reference doc cites: follow the citation and run a
  **decision-consistency check only** — does the reasoning still support the decision? A
  code-coupled fact (file / function / flag / value) inside one → flag as a **tier violation**.
  *(Cold docs escape the currency sweep.)*
- **R16.** A sub-project (own router / `.git`) → flag-and-skip; audit it from its own dir.
- **R17.** Vendored *source* is read-only ground truth — check against it, never edit it.

## Coverage — why this skill exists
- **R18.** Never trust one careful pass — or any fixed N of them. *(Each finds a different
  ~half.)*
- **R19.** Fan out **per-section** workers (forces depth everywhere; whole-doc replicates skim),
  plus **one cross-reference pass** over inbound referrers — routers, other docs, source/UI
  files — for rename-orphans and dangling links.
- **R20.** **Loop until dry**: run rounds until one adds nothing new. *(Even three replicate
  passes each missed real flags; ground truth ran ~30% larger than any single run.)*
- **R21.** A dry round is *that model's* ceiling, not truth — **switch worker model** before
  concluding. *(Two models' ~20-of-25 unions shared only ~16; the full union needed both.)*
- **R22.** Worker default: a strong, fast tier at **high** reasoning effort (Claude: Sonnet at
  high) — per-pass parity with a frontier tier, faster convergence, discipline intact. Medium
  effort / the cheapest tier (Claude: Haiku) are a **first sweep only**. *(Medium's ceiling ran
  ~3 real issues below high; cheap tiers skip sections and mislabel actions — iteration doesn't
  fix discipline.)*
- **R23.** **Retry a dead worker once** (a transient API error returns null/empty, and merges
  silently filter it); still dead → name the uncovered span in the coverage note. *(A visible
  gap beats false completeness.)*
- **R24.** Every worker returns flags **in the schema below**. *(Prose doesn't merge across a
  fan-out.)*

## Procedure
1. Fan out per-section workers + the cross-reference pass (R19, R22); collect schema'd flags.
2. Merge + dedup — same location + claim = one flag; log anything dropped.
3. Loop until dry, then diversify the worker model (R20–R21). End with a **coverage note** in
   the adjudication report: any span whose worker died after retry, and what covered it instead
   (R23).
4. **Adjudicate**: present the merged list; the user **approves / amends / defers** each flag's
   proposed action.
5. **Apply** approved doc fixes; re-verify. Report-only flags are handed off, never applied (R4).

## Flag schema — every flag, every worker
```
- location:  doc § + quoted phrase
- axis:      placement | currency
- modality:  descriptive | prescriptive          (currency flags)
- claim:     what the doc asserts
- finding:   what's wrong, or the off-charter target home
- evidence:  file:line / symbol   OR   "unverifiable → ask user"
- severity:  high | medium | low
- action:    fix-doc | move-to <doc> | cross-ref+delete | graduate | extract-cold | revisit-plan | flag-code-bug | keep
```

Full rationale + RED/GREEN provenance:
https://github.com/Apoplectic1/YetAnotherSkillsRepo/blob/main/docs/docs-architecture-design.md
````

## Candidate: docs-architecture-maintain (488 words)

````markdown
---
name: docs-architecture-maintain
description: Use when a project's journal (dated docs/ notes + NOTEBOOK) has accrued findings that may have hardened into standing truth, when the reference docs feel behind the journal, or for a periodic journal-health sweep. Assumes the docs-architecture conventions (a CLAUDE.md router + charter'd reference set).
---

# Docs-architecture maintain (graduate & prune)

A periodic sweep that promotes **hardened standing-truth out of the journal into the reference
tier**, then **prunes the source** so nothing duplicates. Not a currency/placement audit
(`docs-architecture-audit`) and not bootstrap (`docs-architecture-setup`). The linchpin: every
`graduate` carries **both a target and a source-disposition** — graduating *without* pruning
creates the duplication the whole system exists to prevent; pruning *by deleting* the dated
record loses the why/when.

## Classify — every journal item
- **M1.** `graduate` — a standing truth (recurs / decided / now-true) not yet single-sourced in
  the reference tier → promote to the reference doc its **charter** selects.
- **M2.** `keep` — a still-contextual finding; *intentional cold-rationale* a reference doc
  cites; or a single-source the reference tier points INTO (moving it breaks the cross-ref).
  *(A healthy journal is mostly `keep`.)*
- **M3.** `archive` — a fully resolved / superseded record (a done review, an executed plan) →
  `archive/`. *(git is the backstop.)*
- **M4.** `prune-only` — a closed item still sitting in an "open / pending" list → strike it.

## The linchpin — a source-disposition, REQUIRED on every graduate
- **M5.** `stub` — leave the dated *measurement / derivation* as the evidence behind the lifted
  guidance. *(The data is not the guidance — keep it.)*
- **M6.** `cross-ref` — replace the now-duplicated prose with a one-line pointer *up* to the
  reference doc.
- **M7.** `archive` — the whole entry is now spent.
- **M8.** **Never delete the why/when** — a dated entry records *when and why* a decision was
  made; stub or archive it, never erase. *(The two failure modes: graduate-without-prune →
  duplication; prune-by-deletion → lost why.)*
- **M9.** Don't over-graduate — and never graduate into an already-bloated reference doc:
  an oversized target is a **setup/audit split job first**, not more content.

## Coverage
- **M10.** **REQUIRED:** reuse the fan-out from **docs-architecture-audit** — independent
  workers, structured flags, merge + dedup, **loop-until-dry**. *(One pass finds a different
  candidate subset; never a fixed N.)*

## Flag schema — every worker
```
- source:        journal file + section/topic
- classify:      graduate | keep | archive | prune-only
- target:        reference doc (for graduate) — chosen by charter
- disposition:   stub | cross-ref | archive        ← REQUIRED for every graduate
- standing-claim: the durable truth being promoted (for graduate)
- evidence:      why it's standing (recurs / decided / already-cited) — or why keep
- action:        one line
```

## Procedure
1. **Fan out** graduation workers over the journal (M10) → schema'd flags.
2. **Merge + dedup + loop until dry.**
3. **Adjudicate** per item (graduate / keep / archive / prune-only).
4. **Apply**: promote → reference doc; disposition the source (M5–M7); update the router if a
   doc moved. Re-verify: nothing duplicated, no why/when lost.

Full rationale + RED/GREEN provenance:
https://github.com/Apoplectic1/YetAnotherSkillsRepo/blob/main/docs/docs-architecture-design.md
````

## Candidate: whats-next (505 words)

````markdown
---
name: whats-next
description: Use when asked "what should I work on next?", "what's the backlog?", or when planning a session, prioritizing a project's open work, or checking that nothing pending has been missed. Assumes the docs-architecture conventions (a CLAUDE.md router + charter'd reference set).
---

# What's next (backlog triage)

Answer "what's next?" by **sweeping every backlog source**, separating **live-actionable** work
from **accepted constraints**, and returning a **categorized, prioritized backlog plus a
coverage manifest**. Prioritization is innate to a capable agent; the rules below force the two
things unguided runs omit — the manifest ("did I see everything?") and the accepted-constraints
list ("considered; by design; skip") — plus sweep completeness. This is the planning layer on
top of the docs-architecture family (it consumes audit flags and maintain's residue as backlog
inputs; doc hygiene itself belongs to the siblings). **After** an audit when doc currency is in
doubt: stale docs → stale backlog, so currency-check first.

## Sweep — every row; manifest whatever you can't reach
| Source | Yields |
|---|---|
| working tree + `git status` / `log` | uncommitted WIP to finish; recent direction |
| ROADMAP "Future directions" / "Next" / known-limitations | planned features + accepted limits |
| `CLAUDE.md` + docs gotchas | hazards — most are *accepted constraints*, not work (W1–W2) |
| journal `docs/` + `NOTEBOOK.md` "pending / open items" | un-promoted decisions, open questions |
| code `TODO` / `FIXME` (note **whose** — first-party vs vendored/upstream) | actionable only if first-party |
| planning/change-tool state (e.g. `openspec/` changes, issue tracker) | in-flight work |
| **audit findings** (`docs-architecture-audit` output) | doc-drift fixes |
| cross-repo blockers / consumers | dependencies + sequencing |
| tests / build status | red = urgent |

## Rules
- **W1.** Live-actionable requires a **live marker**: a first-party `TODO`/`FIXME`, an audit
  `flag-code-bug`, a ROADMAP "Next" item, or an explicit pending/open marker. Everything else —
  by-design, "do not re-litigate", deferred-by-decision, vendored/upstream — → the
  accepted-constraints list (shown, not actioned).
- **W2.** **Default to accepted when unsure.** *(A false "todo" on every gotcha trains the user
  to ignore the output.)*
- **W3.** Bucket each actionable: **urgent** (red tests / broken) · **deferred-fix** ·
  **future-feature** · **doc-debt**.
- **W4.** Rank by value × (1 / effort) × **exposure-if-deferred** — the cost of *not* doing it
  (what it blocks or de-risks); implementation riskiness alone never raises rank. Tag effort
  (XS/S/M/L) + risk.
- **W5.** Deliver a **top-N with a recommended sequence** (what unblocks / de-risks what) —
  never a flat list. Priority is a *proposal*; the user owns the call.
- **W6.** **REQUIRED:** reuse the fan-out from **docs-architecture-audit** — independent passes,
  merge, **loop-until-dry**. *(Passes agree on the core; the margins are a coin-flip.)*

## Two REQUIRED outputs
- **W7.** **Coverage manifest** — a table over every sweep row: **swept** (with what it yielded)
  or **not reached** (and why — no run logs, vendored, sibling repo). *(Without it the backlog
  reads complete when it isn't — the #1 unguided omission.)*
- **W8.** **Accepted constraints — "considered, not work"** — each with the one-line reason to
  skip. *(Shows the work; prevents re-litigation.)*

Full rationale + RED/GREEN provenance:
https://github.com/Apoplectic1/YetAnotherSkillsRepo/blob/main/docs/docs-architecture-design.md
````
