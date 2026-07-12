# 2026-07-11 — AUDIT rewrite draft: calibration results + the form-factor decision

**What this is / when to read:** the candidate `docs-architecture-audit/SKILL.md` implementing
the decisions in `2026-07-11-skill-portability-review.md` §7, with its change log, judgment
calls, an honest correction to that review's §4 compression floor, and the form-factor question
raised the same day (a rule-by-rule generic-instructions expectation vs the shipped
narrative-justified style). Read before drafting the remaining three skills. Calibration
artifact only — nothing under `skills/` has been touched; candidate text ships solely via the
planned openspec change after RED→GREEN.

## Result against the two goals

**Portability: complete.** Grep-verified zero remaining constellation/local tokens in the
candidate (`E:\` paths, PCL, nsg-v8-fork, 3rdparty, BenchmarkDotNet, OBSERVING, NOTICE, xaml,
superpowers, TRIAGE, `PLAN-*`). Footer → one GitHub blob URL; worker-model guidance dual-form
(generic rule, Claude tiers as parenthetical examples); benchmark numbers retained as bare,
uncited claims.

**Compression at the conservative dial: 1,382 → 1,215 words (−12%), zero rules dropped.**
Correction to the review's §4, which estimated a ~900–1,000-word floor: that floor is **not
reachable by phrasing alone**. The review over-attributed AUDIT's length to overhead — the
Common-mistakes section plus provenance asides total ~290 words, not ~400 — and the rest is
rule-dense text where each clause traces to a RED failure. Reaching ~1,000 requires structural
folds; reaching below that requires a different *form* (below).

## Why the shipped text reads "full of external project dependencies"

Three separable ingredients produced that impression on GitHub:

1. **Literal constellation tokens** (`PCL/`, `nsg-v8-fork/`, `OBSERVING.md`, `dotnet test`,
   `.xaml`/`.cs`, `E:\…` footers) — real dependencies in the reading sense. **Removed** in this
   draft.
2. **Provenance references** — dated experiments, RED/GREEN vocabulary, benchmark citations
   ("the 2026-06-29 benchmark"). These gesture at artifacts a visitor can't see. **Removed**:
   the numbers stay (per Q2) but now read as bare calibration claims, not pointers.
3. **The house form itself** — narrative-justified rules (each rule carries its rationale
   inline) plus family vocabulary (tiers, charters, graduate, cold-rationale). This is a *style*,
   not a dependency, and it survives the portability pass by design. It is also the largest
   contributor to the "not a generic rulebook" reading.

The expectation the review conversation surfaced — a bulletized, priority-ordered, rule-by-rule
set of generic instructions — is the dominant public form for agent skills. The house form is a
deliberate outlier with a recorded rationale: the RED baselines repeatedly showed capable agents
*rationalizing around* bare-but-sensible rules (e.g. the design-heavy RED's
"archived-verbatim-is-safe" rationalization), and a rule that carries its why resists being
argued away by the executing agent. Both forms can encode identical content; with full RED→GREEN
already chosen, either is testable rather than a matter of taste. Note: the family is authored
under the `superpowers:writing-skills` convention — a form change should be checked against (or
consciously depart from) that convention.

## Form options for the family (decided same day: Option C — full-family candidates + rationale in `2026-07-11-hybrid-rewrite-candidates.md`)

| Option | Form | Est. AUDIT | Est. family (3,666 w) | Trade-off |
|---|---|---|---|---|
| A | House narrative, conservative (this draft) | 1,215 | ~3,200 (−12%) | minimal wording distance; lowest GREEN risk; still reads dense |
| B | House narrative + structural folds | ~1,000–1,050 | ~2,800 (−24%) | merge discipline sections, terser maxims; moderate distance |
| C | Hybrid rulebook — numbered, priority-ordered imperatives, each with a one-clause why; procedure stays a numbered flow; schema verbatim | ~850–950 | ~2,400–2,600 (−32%) | matches the raised expectation while keeping the anti-rationalization whys; largest distance, fully covered by RED→GREEN |
| D | Bare rulebook — imperatives only | ~700 | ~2,000 (−45%) | smallest and most conventional-looking; strips the whys the REDs argue for — highest GREEN risk |

### The same rule in each form (calibration sample — the conservative-evidence rule)

House narrative (A/B):
> Every currency flag carries **either a code citation (`file:line` / symbol) OR the literal
> marker `unverifiable → ask user`. Never guess stale.** Key on **content, not filename** — a
> name may prioritize *what to read*; the verdict comes only from reading + grepping.

Hybrid rulebook (C):
> R7. Evidence every currency flag: `file:line`/symbol, or the literal `unverifiable → ask user`
> — never guess stale.
> R8. Judge by content, not filename. *(Names only prioritize reading order.)*

Bare rulebook (D):
> 7. Every flag cites `file:line` or is marked `unverifiable → ask user`.
> 8. Judge content, not filenames.

## Change log for this draft (conservative dial)

- **Footer** → single GitHub URL
  (`github.com/Apoplectic1/YetAnotherSkillsRepo/blob/main/docs/docs-architecture-design.md`).
  *Judgment call:* Q1 (footers → GitHub) and Q2 (numbers uncited) overlap on AUDIT's second
  footer line, the benchmark citation. Resolved by dropping it — the design doc carries the
  benchmark summary and its link one hop away. Alternative: keep both URLs (+1 line).
- **Token swaps** (word-neutral): `PCL/`/`nsg-v8-fork/`/`*/3rdparty/` → `vendor/`,
  `third_party/`, "a forked upstream"; `NOTICE.md` example → "a router-named playbook leaf
  inside one"; `bin`/`obj` → `bin/`, `obj/`, `dist/`, `target/`; `.xaml`/`.cs` → "source/UI
  files"; `PLAN-*` → "plan docs" (content-not-filename remains the governing rule); `TRIAGE`
  alias dropped (`whats-next` referenced by skill name only).
- **Numbers kept verbatim, uncited:** ~half per pass · 3 passes still missed / ground truth ~30%
  larger · ~20-of-25 unions sharing ~16 · medium ~3 below high.
- **Model guidance dual-form:** "a strong, fast tier at high reasoning effort (Claude: Sonnet at
  high)"; "the cheapest tier (Claude: Haiku)".
- **Compression:** Common-mistakes 9/9 concepts kept, tersed (~230 → ~90 w); step-5 routing
  dedup (stated once, in "AUDIT writes docs only"); "Core finding from baseline testing"
  framing removed (claim kept); micro-trims in the modality section (no clause dropped).

## Candidate text (conservative dial)

````markdown
---
name: docs-architecture-audit
description: Use when verifying a project's reference docs still match the code — after a refactor or rename, on suspected doc drift, before trusting a doc as current, or as a periodic doc-health pass. Assumes the docs-architecture conventions (a CLAUDE.md router + charter'd reference set).
---

# Docs-architecture audit

## Overview
Audit reference docs on two axes — **placement** (does each section match its doc's charter?) and
**currency** (does each claim still match the live code?) — producing an evidence-carrying flag
list to adjudicate, then fix. **A single careful pass finds only ~half the real issues,
non-deterministically** — so AUDIT is a *fan-out that converges coverage*, not one careful read.
Per-flag judgment is what a capable agent already does well; what the skill must force is
**completeness + a mergeable, consistent output**.

## When to use
- After a refactor/rename; on suspected code↔doc drift; before trusting a reference doc as
  current; or a periodic doc-health pass.
- **Not** the journal (`docs/`, `NOTEBOOK.md`) — append-only, never currency-audited — and **not**
  `archive/`. **Exception — cold-rationale docs** (dated `docs/` notes a reference doc cites as
  its "why"): follow the citation and check **decision-consistency only** — does the reasoning
  still support the decision? A **code-coupled fact** (file / function / flag / value) inside one
  is a **tier violation** → flag it: cold docs escape the currency sweep, so code-coupled content
  must live in the audited reference tier.

## The two axes — never conflate
- **PLACEMENT** — does this section belong in THIS doc, per its charter? Off-charter → move, or
  cross-ref-and-delete (single-source). A section that is **lengthy AND cold AND evergreen**
  (pure "why" — not code-coupled, not needed for immediate reasoning) → `extract-cold`: propose a
  dated `docs/` cold doc + a one-line reference back. All three tests must hold — a short, warm,
  or code-coupled section stays put.
- **CURRENCY** — is each claim true against the live code? Verify by reading/grepping the actual
  source.

## Currency: code is ground truth — classify modality first
- **Descriptive** (how the system *is* — ARCHITECTURE, gotchas, "current status"): **code wins**;
  mismatch = stale doc → `fix-doc`. **Exception — a contract the code is *meant* to honor:** when
  the doc asserts a guarantee (a `must`/`always`/`never`/aborts-on-X rule — ideally stating its
  rationale, or corroborated by a test or another doc) and the code *violates* it, the **code is
  the suspected bug, not the doc stale** → `flag-code-bug` (report-only). **Never `fix-doc` a
  contract into agreement with code you suspect is buggy** — that encodes the bug into the spec.
  Plain value drift with no guarantee (a count, an intentionally-changed default/path) →
  `fix-doc`; unsure which → `unverifiable → ask user`.
- **Prescriptive** (how it *should/will* be — ROADMAP "Future", plan docs, "Open follow-ups"):
  **the plan wins.** Code-not-matching is *expected*, never staleness. Two non-stale statuses:
  plan **already satisfied** by code → `graduate` (an ordinary doc edit once adjudicated: → 
  "Recently shipped" / archive the plan); plan **contradicted** by current structure →
  `revisit-plan` (**report-only** — don't edit intent). Tense/charter decides: future
  "will/planned/TODO" + ROADMAP-Future/plan doc = prescriptive; present "is/does/returns" +
  ARCHITECTURE = descriptive.

## AUDIT writes docs only
AUDIT edits **documentation**, never source — not first-party, not vendored. When currency
analysis implicates the *code* (a contract violation, an apparent bug), AUDIT emits
`flag-code-bug` carrying `file:line` evidence and hands it to the dev/diagnose flow and to
`whats-next` as a backlog input. `flag-code-bug` — like `revisit-plan` — is **report-only: never
auto-applied** in step 5.

## Conservative evidence — required
Every currency flag carries **either a code citation (`file:line` / symbol) OR the literal marker
`unverifiable → ask user`. Never guess stale.** Key on **content, not filename** — a name may
prioritize *what to read*; the verdict comes only from reading + grepping.

## Fan out for coverage — the heart of the skill
1. **Fan out** independent audit workers, **per-section** (one worker per major section) — this
   forces depth everywhere; whole-doc replicate passes skim uniformly and miss section-local
   detail. Replicate passes find *different* subsets — use them *with* loop-until-dry (step 3),
   never as a fixed N. Each worker returns flags in the schema below. **Worker model — default to
   a strong, fast tier at high reasoning effort** (Claude: Sonnet at high): benchmarked at
   per-pass parity with a frontier-tier model, converging faster, discipline intact (cites
   `file:line` or marks `unverifiable`; no cry-wolf). **Medium effort / the cheapest tier**
   (Claude: Haiku) **are a first-sweep only** — medium's cumulative ceiling runs ~3 real issues
   below high, and the cheapest tier skips sections and mislabels actions; iteration doesn't fix
   discipline. For coverage, diversify the worker model across the fan-out (step 3). **Workers
   die** — a transient API error returns null/empty, which a merge silently filters: **retry a
   dead worker once; still dead → name it in the coverage note (step 3).**
2. **Cross-reference pass** (one worker): check **inbound references** to the doc — routers, other
   docs, code comments in source/UI files — for rename-orphans (a doc renamed, referrers not
   updated) and dangling links, plus code↔doc drift the per-section workers miss.
3. **Merge + dedup** (same location+claim = one flag). **Loop-until-dry is mandatory, not a fixed
   N**: keep running rounds until one adds nothing — even three replicate passes each still missed
   real flags a different angle caught (ground truth ran ~30% larger than any single run). Don't
   silently cap — log what was dropped — and end with a **coverage note** in the adjudication
   report naming any span whose worker died after retry (step 1) and what covered it instead. A
   visible gap beats false completeness. **A single model's dry round is *that model's* ceiling,
   not truth** (two models' ~20-of-25 unions shared only ~16; the full union needed both) — so
   **model diversity in the fan-out beats more same-model reps**: once one model's rounds go dry,
   switch worker model rather than loop deeper.
4. **Adjudicate** — present the merged list; per flag the user **approves / amends / defers** its
   proposed schema action.
5. **Apply** approved doc fixes; re-verify. **Report-only** flags (`flag-code-bug`,
   `revisit-plan`) are handed off, never auto-applied.

## Flag schema — every flag, every worker (this is what makes the fan-out mergeable)
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

## Scope — router-anchored
In-scope = what the **CLAUDE.md router names** (∪ the canonical reference set). Default-exclude
*unrouted* files in **vendored** trees (`vendor/`, `third_party/`, a forked upstream — though a
router-named playbook leaf inside one *is* in scope), **generated** output (`bin/`, `obj/`,
`dist/`, `target/`), and **tooling** (`.claude/`, `openspec/`). A **sub-project** (own router /
`.git`) → flag-and-skip; audit it by running from its own dir. Vendored *source* = read-only
ground truth to check against, never edit.

## Common mistakes
- A single careful pass, or any fixed N — each finds a different ~half; loop until dry.
- Trusting one model's dry round as complete — that's its ceiling; switch models.
- Guessing stale (cite code or mark `unverifiable → ask user`).
- Flagging a forward plan as stale — prescriptive code-absence is expected.
- `fix-doc`ing a violated contract — that's `flag-code-bug`, report-only.
- Prose flags that don't merge — use the schema.
- Skipping the cross-reference pass — orphans hide *outside* the doc.
- Swallowing dead workers — retry once; name the gap in the coverage note.
- Auditing the journal/archive; scanning vendored/generated trees.

Full rationale + RED/GREEN provenance:
https://github.com/Apoplectic1/YetAnotherSkillsRepo/blob/main/docs/docs-architecture-design.md
````
