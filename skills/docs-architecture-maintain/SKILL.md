---
name: docs-architecture-maintain
description: Use when a project's journal (dated docs/ notes + NOTEBOOK) has accrued findings that may have hardened into standing truth — a periodic graduate-and-prune sweep to keep the reference docs current and the journal from becoming a stale pile. Assumes the docs-architecture conventions.
---

# Docs-architecture maintain (graduate & prune)

## Overview
A periodic sweep that promotes **hardened standing-truth out of the journal into the reference tier**,
then **prunes the source** so nothing duplicates. Same machinery as the audit skill — scan → structured
flags → fan-out → merge → adjudicate → apply — with graduation-specific actions. **The linchpin is
prune-the-source-while-preserving-the-why:** graduate *without* pruning and you create the duplication
the whole system fights; prune by *deleting* the dated record and you lose the why/when. So every
graduate carries **both** a target and a source-disposition.

## When to use
- Periodic journal-health sweep; or when `docs/` / `NOTEBOOK.md` has grown and the reference docs feel behind.
- **Not** a currency/placement audit (that's **docs-architecture-audit**); **not** bootstrap (**docs-architecture-setup**).

## Reuse the audit machinery
**REQUIRED:** use the fan-out from **docs-architecture-audit** — independent workers (per-section or
N replicate passes), **loop-until-dry**, **merge + dedup**, structured flags. One pass finds a
*different* subset of candidates; never a fixed N (the same coverage-coin-flip the audit RED found).

## Classify each journal item
- **graduate** — a standing truth (recurs / decided / now-true) not yet single-sourced in the
  reference tier → promote to the right reference doc (its **charter** decides which).
- **keep** — still-contextual finding, *intentional cold-rationale* (evergreen "why" a reference doc
  cites), or a single-source the reference tier points INTO (moving it breaks the cross-ref). Most of
  a healthy journal is `keep`.
- **archive** — a fully resolved / superseded record (a done review, an executed plan) → `archive/`
  (git is the backstop).
- **prune-only** — a closed item still sitting in an "open / pending" list → strike it.

## The linchpin — every `graduate` gets a source-disposition
After promoting, the source must do exactly ONE of:
- **stub** — leave the dated *measurement / derivation* as the evidence behind the lifted guidance
  (the data is not the guidance — keep it).
- **cross-ref** — replace the now-duplicated prose with a one-line pointer *up* to the reference doc.
- **archive** — if the whole entry is now spent.

**Never delete the why/when.** A dated entry is the record of *when and why* a decision was made —
preserve it (stub or archive), don't erase it. The two failures are **graduate-without-prune**
(duplication) and **prune-by-deletion** (lost why).

## Flag schema — every worker (mergeable)
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
1. **Fan out** graduation workers over the journal (per the audit fan-out) → schema'd flags.
2. **Merge + dedup + loop-until-dry.**
3. **Adjudicate** per item (graduate / keep / archive / prune).
4. **Apply**: promote → reference doc; disposition the source (stub / cross-ref / archive); update the
   router if a doc moved. Re-verify: nothing duplicated, no why/when lost.

## Common mistakes
- **Graduate without prune** → duplication (the #1 failure the whole system exists to prevent).
- **Prune by deleting the dated entry** → the why/when is gone; stub or archive instead.
- **Over-graduate** — moving still-contextual findings, or cold-rationale the reference tier *cites*
  (breaks the cross-ref). A healthy journal is mostly `keep`.
- **Single careful pass / fixed N** — the candidate set is a coin-flip; fan out + loop-until-dry.
- **Graduating into an already-bloated reference doc** — if the target is oversized, that's a
  **setup/audit split** job *first*, not more content.

Full rationale + the RED baseline: `../../docs/docs-architecture-design.md`.
