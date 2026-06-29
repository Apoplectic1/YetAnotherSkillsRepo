---
name: docs-architecture-audit
description: Use when verifying a project's reference docs still match the code — after a refactor or rename, on suspected doc drift, before trusting a doc as current, or as a periodic doc-health pass. Assumes the docs-architecture conventions (a CLAUDE.md router + charter'd reference set).
---

# Docs-architecture audit

## Overview
Audit reference docs on two axes — **placement** (does each section match its doc's charter?) and
**currency** (does each claim still match the live code?) — producing an evidence-carrying flag list
to adjudicate, then fix. **Core finding from baseline testing: a single careful pass finds only
~half the real issues, non-deterministically.** So AUDIT is a *fan-out that converges coverage*,
not one careful read. Quality-per-flag is what a capable agent already does well; **completeness +
a mergeable, consistent output** is what the skill must force.

## When to use
- After a refactor/rename, or when code and a doc may have drifted.
- Before trusting a reference doc as current; or a periodic doc-health pass.
- **Not** the journal (`docs/`, `NOTEBOOK.md`) — append-only, not currency-audited; **not** `archive/`.

## The two axes — never conflate
- **PLACEMENT** — does this section belong in THIS doc, per its charter? Off-charter → move, or
  cross-ref-and-delete (single-source).
- **CURRENCY** — is each claim true vs the live code? Verify by grepping the actual source.

## Currency: code is ground truth — but classify modality first
- **Descriptive** (how the system *is* — ARCHITECTURE, gotchas, "current status"): **code wins.**
  Mismatch = stale doc → `fix-doc`. **Exception — a contract the code is *meant* to honor:** when the
  doc asserts a guarantee (a `must`/`always`/`never`/aborts-on-X rule — ideally stating its rationale,
  or corroborated by a test / another doc) and the code *violates* it, the **code is the suspected bug,
  not the doc stale** → `flag-code-bug` (report-only). **Never `fix-doc` a contract into agreement with
  code you suspect is buggy** — that silently encodes the bug into the spec. Plain value drift with no
  guarantee (a count, an intentionally-changed default/path) is ordinary staleness → `fix-doc`;
  genuinely unsure which → `unverifiable → ask user`.
- **Prescriptive** (how it *should/will* be — ROADMAP "Future", `PLAN-*`, "Open follow-ups"):
  **the plan wins.** Code-not-matching is *expected*, NOT staleness — never flag "planned X absent
  from code" as stale. Two report-only exceptions: plan **already satisfied** by code → `graduate`
  (→ "Recently shipped" / archive the `PLAN-`); plan **contradicted** by current structure →
  `revisit-plan` (don't edit intent). Tense/charter decides: future "will/planned/TODO" +
  ROADMAP-Future/`PLAN-` = prescriptive; present "is/does/returns" + ARCHITECTURE = descriptive.

## AUDIT writes docs only — code findings are report-only
AUDIT edits **documentation**, never source — not first-party, not vendored. When currency analysis
implicates the *code* (a contract violation, an apparent bug), AUDIT **does not fix it**: it emits
`flag-code-bug` carrying `file:line` evidence and hands it off to the dev/diagnose flow (and to
`whats-next`/TRIAGE as a backlog input). `flag-code-bug` — like `revisit-plan` — is **report-only:
never auto-applied** in step 5.

## Conservative evidence — required, not optional
Every currency flag carries **either a code citation (`file:line` / symbol) OR the literal marker
`unverifiable → ask user`. Never guess stale.** Key on **content, not filename** — the name may
prioritize *what to read*; the verdict comes only from reading + grepping.

## Fan out for coverage — the heart of the skill
1. **Fan out** independent audit workers. **Prefer per-section** (one worker per major section) — it
   forces depth everywhere; replicate whole-doc passes skim uniformly and miss section-local detail.
   Replicate passes also help **because independent passes find _different_ subsets** — so use them
   *with* loop-until-dry (step 3), never a fixed N. Each worker returns flags in the schema below.
2. **Cross-reference pass** (one worker): check **inbound references** to the doc (routers, other
   docs, code comments, e.g. `.xaml`/`.cs`) for rename-orphans / dangling links, plus code↔doc
   drift the per-section workers miss. (Catches the rename-orphan class — a doc renamed, its
   referrers not updated.)
3. **Merge + dedup** (same location+claim = one flag). **Loop-until-dry is mandatory, not a fixed N**:
   keep running rounds until one adds nothing — in testing, *three* replicate passes each still missed
   real flags a different angle caught (ground truth was ~30% larger than any single run). Don't
   silently cap — `log` what was dropped.
4. **Adjudicate** — present the merged list for a per-flag call (fix / move / delete / keep / defer).
5. **Apply** approved doc fixes; re-verify. **Report-only** flags (`flag-code-bug`, `revisit-plan`)
   are **handed off, never auto-applied** — `flag-code-bug` routes to the dev/diagnose flow + `whats-next`.

## Flag schema — every flag, every worker (this is what makes the fan-out mergeable)
```
- location:  doc § + quoted phrase
- axis:      placement | currency
- modality:  descriptive | prescriptive          (currency flags)
- claim:     what the doc asserts
- finding:   what's wrong, or the off-charter target home
- evidence:  file:line / symbol   OR   "unverifiable → ask user"
- severity:  high | medium | low
- action:    fix-doc | move-to <doc> | cross-ref+delete | graduate | revisit-plan | flag-code-bug | keep
```

## Scope — router-anchored
In-scope = what the **CLAUDE.md router names** (∪ the canonical reference set). Default-exclude
*unrouted* files in **vendored** (`PCL/`, `nsg-v8-fork/` — but a router-named playbook leaf like
`NOTICE.md` *is* in scope), **generated** (`bin`/`obj`), **tooling** (`.claude/`, `openspec/`).
A **sub-project** (own router / `.git`) → flag-and-skip; audit it by running from its own dir.
Vendored *source* = read-only ground-truth to check against, never edit.

## Common mistakes
- **One careful pass, or a fixed number of them** — each finds a *different* ~half; in testing even 3
  passes missed real flags. Prefer per-section depth + loop-until-dry until a round is genuinely dry.
- **Guessing stale** instead of citing code or marking `unverifiable → ask user`.
- **Flagging a forward plan as stale** (modality error) — prescriptive code-absence is expected.
- **Rewriting a doc to match buggy code** — a contract the code *violates* is a `flag-code-bug`
  (report-only), never a `fix-doc`. AUDIT never edits code and never encodes a suspected bug into the spec.
- **Unstructured prose flags** — they don't merge across the fan-out; use the schema.
- **Skipping the cross-reference pass** — rename-orphans / dangling links hide *outside* the doc.
- **Auditing the journal/archive**, or scaffolding into vendored/generated trees.

Full rationale + the RED baseline that justifies the fan-out: `../../docs/docs-architecture-design.md`.
