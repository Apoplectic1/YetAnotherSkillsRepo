---
name: docs-architecture-audit
description: Use when verifying a project's reference docs still match the code — after a refactor or rename, on suspected doc drift, before trusting a doc as current, or as a periodic doc-health pass. Assumes the docs-architecture conventions (a CLAUDE.md router + charter'd reference set).
---

# Docs-architecture audit

Audit reference docs on two axes, judged separately: **placement** (does each section match its
doc's charter?) and **currency** (does each claim still match the live code?), producing an
evidence-carrying flag list the user adjudicates, then applying the approved fixes. One careful
pass finds about half the real issues; the rules force what one pass cannot give,
**completeness and a mergeable, consistent output**. `python scope.py <dir>` (beside this
SKILL.md) prints the scope, the chain row, the structural findings a count can make and the
seed of the cross-reference pass, one line per item with the rule it keys; what a claim means,
what a router block is, and whether a mismatch is drift or a contract are the workers' calls.

## Discipline (highest priority; violations poison the run)
- **R1.** Every currency flag carries a code citation (`file:line` / symbol) **or** the literal
  `unverifiable → ask user`. Never guess stale.
- **R2.** Judge by content, not filename.
- **R3.** Edit **documentation only**, never source, first-party or vendored: code findings
  are reports, not fixes.
- **R4.** Report-only actions are exactly `flag-code-bug`, `revisit-plan` and `spec-change`:
  handed off (to the dev/diagnose flow, `whats-next`, the project's change workflow), never
  auto-applied.
- **R27.** Surviving report-only flags **persist to the target project's own tiers before
  the run ends**: full flags and evidence in a dated `docs/YYYY-MM-DD-audit-report.md`, one
  line per adjudicated-surviving finding in the ROADMAP's open list, deduplicated against
  lines already there; adjudication deferred → one open-list line pointing at the report.

## Currency: claim vs code
- **R5.** Classify modality first. **Descriptive** = how the system *is* (present tense;
  ARCHITECTURE, gotchas, status). **Prescriptive** = how it *should or will* be (ROADMAP
  futures, plan docs, open follow-ups).
- **R6.** Descriptive: **code wins**; a mismatch is a stale doc → `fix-doc`.
- **R7.** Exception, contracts: a guarantee the doc asserts (`must` / `always` / `never` /
  aborts-on-X, with rationale or corroborated by a test or another doc) that the code
  *violates* → `flag-code-bug`; the **code** is the suspect. Never `fix-doc` a contract into
  agreement with suspect code.
- **R8.** Plain value drift with no guarantee (a count, a changed default or path) →
  `fix-doc`; unsure which case → `unverifiable → ask user`.
- **R9.** Prescriptive: **the plan wins**; code-not-matching is expected, never staleness.
  Plan satisfied by code → `graduate`; plan contradicted by the current structure →
  `revisit-plan`. Don't edit intent.
- **R28.** A `fix-doc` on a stale value that is **cheaply derivable** (one grep re-derives
  it) **and rationale-free** leads with removing or de-valuing the claim ("a curated station
  registry", not "12 stations"), the value update as the stated alternative. A value carrying
  rationale, contract force (R7) or gotcha weight gets a normal fix.

## Placement: section vs charter
- **R10.** Off-charter section → `move-to <doc>`, or `cross-ref+delete`. Single-source every
  fact.
- **R11.** `extract-cold` (a dated `docs/` cold doc + one line back) only when a section is
  lengthy **and** cold **and** evergreen, all three.
- **R25.** A growing dated shipped-history inside a reference doc (the scope script counts
  it) is **one structural flag** → `move-to CHANGELOG.md`; its entries are journal-tier,
  never currency-flagged one by one.
- **R26.** The router is **itself placement-audited**: reference content in it (glossary,
  contract/API prose, conventions, mechanics: neither routing nor a load-bearing gotcha) →
  **one structural flag per block** → `move-to <charter home>`; never per-fact placement
  flags, never routing lines or gotchas on the content axis (a gotcha block still meets
  R30's scope test). Currency flags on stale claims inside a block stay legitimate.
- **R30.** **The chain is measured, and every router block passes breadth and stability.**
  The scope script's chain row (`chain_budget.py`: the owner's global file, every ancestor
  router, this router, the always-on rule files, the memory index; against 5 percent of the
  window, about 10k tokens unless the router states its own share, and 200 lines per file)
  goes in the **coverage note**: the total and verdict, the largest items, this project's
  part apart from the ancestors' and the owner's, the files over their own line. Each block
  of this router and its always-on rule files passes **breadth** (every session launched
  here needs it) and **stability** (it changes less often than a release) or gets **one
  placement flag** → `move-to` an on-demand home (a path-scoped rule file for a file-keyed
  need, a skill for an activity, a reference-doc section for prose) with a one-line trigger
  left behind. An ancestor's weight is reported, never flagged here; the owner's is the
  owner's. **The number detects, the test decides**: a router under budget still flags a
  block that fails.

## Scope
- **R12.** In scope = the scope script's list: what the router names, the canonical
  reference set, and the parts a split index names (each the index's tier and charter).
- **R13.** Out by default: unrouted files in vendored trees, generated output and tooling
  (`.claude/`, `openspec/`); a router-named leaf inside them is in. A router-named spec
  under `openspec/specs/` is currency-audited but never edited: a claim it makes that the
  code, the router and the reference docs agree is wrong → `spec-change`, naming the change
  that would correct it; R7's code-is-suspect holds only while the spec stands
  uncontradicted.
- **R14.** Never currency-audit the journal (`docs/` records, `NOTEBOOK.md`,
  `CHANGELOG.md`, their rolled directories) or archives.
- **R15.** A cold-rationale doc a reference doc cites gets a **decision-consistency check
  only** (does the reasoning still support the decision?); a code-coupled fact inside one is
  a **tier violation**. An archived openspec design doc gets the consistency check only: its
  code-coupled facts are design-time values, never tier violations, and it is never edited
  (standing truth inside it is MAINTAIN's job).
- **R16.** A sub-project (own router or `.git`) → flag-and-skip; audit it from its own dir.
- **R17.** Vendored *source* is read-only ground truth: check against it, never edit it.

## Coverage
- **R18.** Never trust one careful pass, or any fixed N of them (each finds a different
  half); the one exception is a **scoped mode** the user invokes (R29).
- **R19.** Fan out **per-section** workers (whole-doc replicates skim), plus **one
  cross-reference pass** over inbound referrers (routers, other docs, source and UI files)
  for rename-orphans and dangling links; the scope script seeds it with every path and
  section citation that does not resolve (a section citation resolves in the doc or its
  split directory, a dated one in the journal's).
- **R20.** **Loop until dry**: rounds until one adds nothing new.
- **R21.** A dry round is *that model's* ceiling: **switch the worker model** before
  concluding; same-model convergence is agreement, not completeness.
- **R22.** Worker default: a strong, fast tier at **high** effort (Claude: Sonnet at high);
  medium effort or the cheapest tier is a **first sweep only**.
- **R23.** **Retry a dead worker once**; still dead → name the uncovered span in the
  coverage note.
- **R24.** Every worker returns flags **in the schema below**.
- **R29.** **Scoped modes: invoked by the user, never chosen by the run.** The user names
  one, or asks for one round or a cheap run and the run names which fits and says so.
  `release-close`: one lens over the reference tier for the phrases a release leaves behind
  ("waits for", "not yet", "until", "today", "currently", "pending", "in progress", a
  version, a count; `scope.py --lens release` lists the lines) plus the R19 pass.
  `small-set`: one per-section round plus the R19 pass, for a small, low-drift doc set.
  Either mode: one round at the R22 tier, no loop, no model switch, every other rule intact;
  the coverage note names the mode and what a full run would have added. Without a mode
  named, "audit" means the full loop.

## Procedure
1. `python scope.py <dir>`: the scope (R12 to R16), the chain row (R30), the structural
   findings (R25, a stale split index), the cross-reference seed (R19); in `release-close`
   mode, `--lens release`.
2. Fan out per-section workers and the cross-reference pass (R19, R22); collect schema'd
   flags. In a scoped mode (R29) the workers are the mode's one round.
3. Merge + dedup (same location + claim = one flag; log what was dropped). Loop until dry,
   then switch the model (R20, R21); in a scoped mode stop after the round. End with the
   **coverage note**: the chain row (R30); any span whose worker died after retry and what
   covered it (R23); in a scoped mode, the mode and what a full run would have added.
4. **Adjudicate**: the user approves, amends or defers each flag's action.
5. **Apply** approved doc fixes; re-verify. Report-only flags are never applied: **persist
   them (R27)**, then hand off (R4).

## Flag schema (every flag, every worker)
```
- location:  doc § + quoted phrase
- axis:      placement | currency
- modality:  descriptive | prescriptive          (currency flags)
- claim:     what the doc asserts
- finding:   what's wrong, or the off-charter target home
- evidence:  file:line / symbol   OR   "unverifiable → ask user"
- severity:  high | medium | low
- action:    fix-doc | move-to <doc> | cross-ref+delete | graduate | extract-cold | revisit-plan | flag-code-bug | spec-change | keep
```

Full rationale + RED/GREEN provenance:
https://github.com/Apoplectic1/YetAnotherSkillsRepo/blob/main/docs/docs-architecture-design.md
