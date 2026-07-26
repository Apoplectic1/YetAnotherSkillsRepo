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
- **M9.** Don't over-graduate — and **check every graduate's target at apply time** (content
  test: is the doc already dominated by content a split would relocate?). Never promote into
  an already-bloated reference doc — an oversized target is a **setup/audit split job
  first**, not more content; applying the promotion and flagging the split afterward — or
  never noticing — is the violation, not compliance. Bloated → hold (M14).
- **M14.** A graduate whose target is bloated is **held, not applied**: record it in the
  dated maintain report (standing-claim + target + disposition — M13 rails) and add **one**
  ROADMAP open-line naming the pending split job (deduplicated across holds); the split runs
  as its own adjudicated job, then held promotions land in the split homes. Healthy targets
  in the same sweep apply normally. *(The report keeps the why (M8); the ROADMAP line keeps
  it tracked — `whats-next` sweeps both homes.)*

## Sources — one class beyond the dated journal
- **M11.** Archived openspec design docs (`openspec/changes/archive/*/design.md`) are a
  **first-class sweep source**, not a scope judgment call — a router's generic `openspec/`
  exclusion does not exempt them (no `openspec/`? silently skip). A graduate from this class
  takes disposition **`cross-ref` only**, written as the pointer in the *reference doc*; the
  archived file is an immutable change record — never stub, trim, or relocate it. *(Shipped
  rationale concentrates there and nothing else ever reads the archive.)*

## Portfolio truth
- **M15.** A **portfolio-level** graduate (the truth spans repos, or no doc in this repo's
  charter set can own it) targets the **container's portfolio `DOMAIN.md`** where one
  exists (pointers one-way per the setup convention; M9/M14 apply). None exists →
  **flag-and-ask** — record it in the dated maintain report with its portfolio-level
  classification and add one ROADMAP open-line for the user's placement decision; **never
  improvise the placement** into the container router, a sibling repo's docs, or a new
  cross-repo pointer. *(Improvised placement is how ownerless loops form and container
  routers fatten.)*

## Code bugs — a report-only channel
- **M12.** A journal claim with **contract force** — guarantee language: must / always /
  never / aborts-on-X — that current code *violates* → a report-only **`flag-code-bug`**
  (claim + `file:line`) *alongside* the entry's normal classification; the **code is the
  suspect** — never stale, demote, or archive the entry because code disagrees. Corroboration
  (a test, another doc) strengthens a flag, **never substitutes** for guarantee language —
  dated records agreeing on an old value are history, not a contract, and design-time values
  in archived change records (M11 class) are never contracts. Plain drift: classify normally,
  no flag. *(MAINTAIN never edits code.)*
- **M13.** Surviving `flag-code-bug` flags **persist to the target project's own tiers before
  the run ends** — full evidence in a dated `docs/YYYY-MM-DD-maintain-report.md`, plus one
  deduplicated line per adjudicated-surviving bug in the ROADMAP's open/backlog list;
  adjudication deferred → a single open-list line pointing at the report. *(A chat-only
  hand-off dies with the chat — the doc system is the bug tracker; `whats-next` sweeps both
  homes.)*

## The report — accounting
- **M16.** The dated maintain report **ends with a REQUIRED accounting slot**: the
  prune/archive candidates found this sweep — or the explicit line "prune candidates: none
  found" — and a one-line **net reference-tier delta** (what the run added to reference
  docs vs removed or struck). Silence is not a legal value for either element. *(Graduate
  always finds another truth to lift; the cut side and the ratchet must be visible every
  run.)*

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
- code-bug:      optional report-only `flag-code-bug` (M12) — contract claim + `file:line`
- action:        one line
```

## Procedure
1. **Fan out** graduation workers over the journal (M10) → schema'd flags.
2. **Merge + dedup + loop until dry.**
3. **Adjudicate** per item (graduate / keep / archive / prune-only).
4. **Apply**: promote → reference doc; disposition the source (M5–M7); **persist code-bug
   flags (M13)**; **portfolio-level graduates per M15**; update the router if a doc moved.
   Re-verify: nothing duplicated, no why/when lost; **the report closes with the M16
   accounting slot**.

Full rationale + RED/GREEN provenance:
https://github.com/Apoplectic1/YetAnotherSkillsRepo/blob/main/docs/docs-architecture-design.md
