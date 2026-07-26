# derivability-discriminator — proposal

## Why

When AUDIT finds a stale, cheaply-derivable claim in a reference doc (a count, a version, a
column list — rationale-free, one grep from the truth), every observed rep proposes
`fix-doc` that re-caches the grep (TidePool reps corrected "12 stations" → 18; the TP
benchmark's dominant issue class was exactly this trivia). But a re-primed drift-prone cache
is drift *deferred*, not cured — the same claim rots again by the next audit. The durable
fix is usually to **delete or de-value the claim** (keep "a curated registry" — drop the
perishable "12"), reserving maintained values for claims that carry rationale, contract
force, or gotcha weight. No current rule gives reps that discriminator, so fix-doc is the
reflex. (Origin: user design question 2026-07-26 — "are we documenting what's better derived
from code?"; NOTEBOOK entry same date.)

## What Changes

- **AUDIT**: one new rule (next free ID: R28) — a fix-or-delete discriminator on `fix-doc`
  currency flags: claim cheaply derivable from code AND carrying no rationale / contract /
  gotcha → the proposed fix is **removal or rewording without the perishable value**, with
  the value-update offered as the alternative; otherwise fix normally. No schema change —
  deletion is a `fix-doc` whose fix is removal; the discriminator shapes the proposed fix,
  and the user still adjudicates.
- **Fixture/catalog**: TidePool D4 (station-count live-section control) gains a GREEN-text
  expectation variant — deletion/reword is the *preferred* proposed fix, value-update
  acceptable-but-noted — without weakening D4's role as the R25 live-section control.
- **Gate (iron law)**: RED must show reps don't already do this unguided (strong prior: all
  existing TidePool/TP rep evidence is fix-doc re-caching; a cheap targeted RED confirms),
  GREEN + micro-variants validate the discriminator doesn't over-fire (must NOT delete
  contract claims, gotcha values, or rationale-bearing numbers — e.g. benchmark figures that
  justify a recommendation).

## Capabilities

### New Capabilities

*(none)*

### Modified Capabilities

- `docs-architecture-audit`: currency `fix-doc` gains the derivability discriminator —
  stale rationale-free derivable trivia is proposed for deletion/de-valuing, not re-caching.

## Impact

- `skills/docs-architecture-audit/SKILL.md` — R28 appended (IDs append-only per DOMAIN);
  word delta within family precedent (~+60–80).
- `harness/catalog-tidepool.md` — D4 GREEN-variant note; possibly one added
  rationale-bearing-number control cell (a value that must NOT be deletion-proposed).
- Docs: dated RED/GREEN record + design-doc provenance entry at ship time.
