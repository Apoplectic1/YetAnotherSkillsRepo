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
