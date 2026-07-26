# 2026-07-13 — Hybrid candidates, round 3: CHANGELOG deltas applied (SETUP + AUDIT revised)

**What this is / when to read:** the round-3 revision of the hybrid candidate SKILL texts —
the `2026-07-11-hybrid-rewrite-candidates.md` bases with the CHANGELOG-convention deltas of
`2026-07-12-changelog-convention-adopted.md` §"Candidate skill-text deltas" applied. These are
the **GREEN injection payloads** for round 3 (the round-3 RED arm injects the unmodified 07-11
texts — this round is A/B current-vs-revised, not unguided-vs-guided). Re-derived fresh
2026-07-13 after the Cowork crash destroyed the first derivation (per the handoff doc's
decision #1). Nothing under `skills/` is modified; these apply only after round-3 GREEN via
the planned openspec change.

## What changed vs the 07-11 candidates

- **SETUP** — three deltas:
  1. Enforced-set table gains a **conditional `CHANGELOG.md` row** (journal-tier shipped
     history; created when history accrues — conditional like README).
  2. **A2 rewritten** to the 00:00-doc spec text: shipped history lives in `CHANGELOG.md`
     (journal tier: append-only, dated, newest first); ROADMAP keeps a short Recently-shipped
     digest + pointer; never a long history embedded in ROADMAP; never shipped history in
     `archive/`. Git stays the commit-level backstop (A2's surviving second half).
  3. **T1** now teaches the **three-way journal split**: finding → NOTEBOOK · shipped unit →
     CHANGELOG · substantial record → `docs/`.
- **AUDIT** — three deltas:
  1. **R14** journal list gains `CHANGELOG.md`.
  2. **New R25** (structural placement rule): a reference doc embedding a growing dated
     shipped-history = **one** placement flag `move-to CHANGELOG.md`; embedded entries are
     NOT currency-flagged individually. Appended under a fresh ID per the in-session
     **ID-stability rule — never renumber existing rule IDs** (journal docs cite
     R14/R21/R22/R23); R25 sits textually in the Placement section, numbered after the
     family's last used ID (R24).
  3. **R21** why-clause hardened: "same-model cross-worker convergence is agreement, not
     completeness" (ecological field finding 2 — the orchestrator skipped the model switch on
     exactly that rationalization).
- **MAINTAIN / whats-next** — **no rule changes**; the 07-11 candidate texts stand as-is for
  the openspec change (bundle note: CHANGELOG accrues at ship time — it is not a graduation
  target — so MAINTAIN's classify verbs are untouched).

## Word counts
| Skill | 07-11 hybrid | Round-3 revised | Δ |
|---|---|---|---|
| docs-architecture-setup | 876 | 921 | +45 |
| docs-architecture-audit | 944 | 996 | +52 |
| docs-architecture-maintain | 488 | 488 | unchanged |
| whats-next | 505 | 505 | unchanged |
| **family** | **2,813** | **2,910** | **+97 (+3.4%)** |

## Candidate: docs-architecture-setup (round 3)

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
| `CHANGELOG.md` | **conditional** — shipped-history journal (append-only, dated, newest first); create when history accrues |
| `README.md`, `RELEASING.md` | **conditional** — public entry point; project that ships |

- **S5.** **Charter-guard:** every file opens with a one-line charter (purpose / when to read).
  A thin file states an honest status ("verification = the test suite"; "no subsystems yet") —
  **never blank**. *(Charter'd-thin is legible and a ready home; blank is noise. NOTEBOOK and
  VERIFICATION are the two files unguided runs reliably omit — create them.)*
- **S6.** The domain doc is **always named `DOMAIN.md`** — do not elicit a content-specific
  name; do not rename an existing `DOMAIN.md`. Whatever the content *is*, it lives there; when
  absent, create it charter'd-thin. Never skip it.

## Tiers & routing — teach these in CLAUDE.md
- **T1.** **journal** (dated capture) = `docs/YYYY-MM-DD-*.md` + `NOTEBOOK.md` +
  `CHANGELOG.md`. Three-way split: small finding from doing the work → NOTEBOOK; **shipped
  unit → CHANGELOG**; substantial standalone record → `docs/`.
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
- **A2.** **Shipped history lives in `CHANGELOG.md`** (journal tier: append-only, dated,
  newest first); `ROADMAP.md` keeps a short Recently-shipped **digest + pointer**; never a
  long history embedded in ROADMAP; never shipped history in `archive/`. Git remains the
  commit-level backstop. Relocating an embedded history = **move**, content-preserving (S1).

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

## Candidate: docs-architecture-audit (round 3)

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
- **R25.** A reference doc embedding a **growing dated shipped-history** (e.g. inside ROADMAP)
  is **one structural placement flag** → `move-to CHANGELOG.md` — the embedded entries are
  **not** currency-flagged individually. *(The entries are journal-tier; the structural
  misplacement, not per-entry drift, is the finding — per-entry flags bury it.)*

## Scope
- **R12.** In-scope = what the `CLAUDE.md` router names, ∪ the canonical reference set.
- **R13.** Default-exclude *unrouted* files in vendored trees (`vendor/`, `third_party/`, forked
  upstreams), generated output (`bin/`, `obj/`, `dist/`, `target/`), and tooling (`.claude/`,
  `openspec/`). A router-named leaf inside them *is* in scope.
- **R14.** Never currency-audit the journal (`docs/`, `NOTEBOOK.md`, `CHANGELOG.md`) or
  `archive/`. *(Append-only, legibly historical.)*
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
  concluding. **Same-model cross-worker convergence is agreement, not completeness.** *(Two
  models' ~20-of-25 unions shared only ~16; the full union needed both.)*
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

## MAINTAIN and whats-next
Unchanged from `2026-07-11-hybrid-rewrite-candidates.md` — those texts are the openspec-change
payloads as-is. Bundle note carried from the 00:00 doc: CHANGELOG accrues at ship time; it is
not a graduation target, so MAINTAIN's classify verbs and whats-next's sweep rows need no new
rules (whats-next's ROADMAP sweep row naturally reads the digest; the CHANGELOG itself is
journal-tier and not a backlog source).
