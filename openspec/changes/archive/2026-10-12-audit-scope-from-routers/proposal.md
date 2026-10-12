# Proposal: audit-scope-from-routers

## Why

Two scope gaps in `docs-architecture-audit`, both from the HDL tree's audits (2026-09-24 and
2026-09-26), queued in ROADMAP as "Ancestor-router conventions" and "Scope precedence;
router-named specs":

- **Ancestor routers.** The audit reads a project's own router and reference set. Every
  `CLAUDE.md` above the project root loads in each session there and carries rules for the
  repositories beneath it (the HDL umbrella's LF rule, the ATML umbrella's Zynq IRQ-wrapper
  check), and nothing audits a repository against them. Seen there: a rule moved between
  umbrellas left the repositories citing it pointing at a router that no longer carries it.
- **Scope precedence.** R14 excludes `docs/` wholesale, while R12 and R13 put a router-named
  file in scope. A project that keeps reference docs in `docs/` has both apply. The owner's
  global rule dates every new `docs/` file, reference and record alike, so a dated name
  cannot tell them apart; the router's routing can. Likewise `openspec/specs`: workflow-only
  by the design doc, but a project whose routers cite its specs by name as its rules has
  them as reference; the HDL sweep's spec lens found 12 false SHALL claims no default sweep
  reaches.

## What Changes

- **AUDIT**, modified: R12 states that the router sets the tier, not the directory or the
  name; R14 yields to it. R13: a router-named spec is currency-audited and never edited, its
  stale claim the new report-only action `spec-change` (persisted by R27 like the other
  report-only actions; R4 and the schema name it). New R29: ancestor routers are convention
  sources, read and never edited: upward pointers resolved, repository-scoped conventions
  checked as contracts, restatements `cross-ref+delete`. Each half ships only where RED shows
  the current text failing (the no-failure gate).
- **The design doc**: "OpenSpec = workflow-only" qualified for router-named specs.
- **`harness/reefstack-fixture-variants/audit-scope/`**: the overlay with the cells
  (catalog: `harness/catalog-reefstack.md`, variant `audit-scope`).

## Capabilities

### Modified Capabilities
- `docs-architecture-audit`: the router sets the tier; router-named specs; ancestor routers.

## Impact

Audits of a repository under an umbrella read its ancestor routers (a few KB each, already in
the session's context). Report-only actions become three; R27's persistence covers the new
one unchanged. A project's spec drift becomes a ROADMAP line naming a cleanup change, never
an in-place spec edit. No consumer project changes until its next audit.
