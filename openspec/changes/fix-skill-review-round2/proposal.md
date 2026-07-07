# fix-skill-review-round2 — behavioral half of the 2026-07-07 family review

## Why

The 2026-07-07 max-effort correctness+intent review (design doc, "Family review 2026-07-07 —
round 2") surfaced five gaps that change what a run *does* — so per the Iron Law they must be
RED-tested before encoding (the mechanical half shipped directly). Two carry fresh live
evidence from the same session: a portfolio-root SETUP run scaffolded a full set the user
judged noise, and the family's next real customers (WBPP `OBSERVING.md`, TSM `UI-CONVENTIONS`,
Library `PCL InterOp`) will hit the legacy-named-domain-doc case on their very first re-run.

## What Changes

- **SETUP — legacy-named domain doc:** on re-run over a project whose domain doc carries a
  legacy/content-specific name, rename/merge it into `DOMAIN.md` (content-preserving) — never
  create a thin `DOMAIN.md` beside it (duplicate domain home, violates single-source).
- **SETUP — non-git target:** when the target tree is not a git repository, establish a
  recovery net before restructuring (offer `git init`, or snapshot originals) instead of
  silently proceeding without one.
- **SETUP — container/portfolio root:** when the survey finds no first-party project content
  (only sub-projects + tooling), scaffold router-only (with flag-and-skip notes) instead of
  the full enforced set.
- **whats-next — scoped audit-first:** the audit-first step applies when reference docs are
  stale or unaudited since the last major change — not as an unconditional prerequisite.
- **AUDIT — small-set right-sizing:** fan-out width scales with doc volume; a thin fresh doc
  set doesn't warrant the full per-section × model-diversity machinery.

Each item ships **only if its RED fails** (no-failure gate — the disk-verify-gate precedent:
baseline passed 2/2, no text added, spec carries a status note instead).

## Capabilities

### New Capabilities

*(none)*

### Modified Capabilities

- `docs-architecture-setup`: three new requirements — legacy-domain-doc normalization,
  non-git-target recovery net, container-root router-only scaffold.
- `whats-next`: audit-first precondition becomes scoped (stale/unaudited docs), not
  unconditional.
- `docs-architecture-audit`: fan-out scale guidance for small doc sets.

## Impact

- `skills/docs-architecture-setup/SKILL.md` (up to three additions), `skills/whats-next/SKILL.md`
  (one edit), `skills/docs-architecture-audit/SKILL.md` (one addition) — each gated on its RED.
- `docs/docs-architecture-design.md` — RED/GREEN records appended per item.
- Deploy required after merge (SKILL.md changes; only `main` deploys).
- Fixtures: synthetic, per item (see design.md) — the Skills repo itself is a poisoned fixture
  (contains the specs), per the validate-on-non-derived-project lesson.
