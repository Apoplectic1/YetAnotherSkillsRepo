# Proposal: audit-tools-first

## Why

The AUDIT skill text is 13.4 KB (3.4k tokens, 182 lines, 30 rules), the largest of the
family, and its weight is where SETUP's was: R30 restating `chain_budget.py` (2.2 KB), the
scope rules (R12 to R17) telling a reader how to find what a script can list, the coverage
rules carrying benchmark rationale the design doc already holds, and the scoped modes'
lens phrases as prose a worker has to grep by hand. The scope and the cross-reference seed
are also where audits have historically missed (the ancestor never read, the spec never
opened, the renamed file never grepped). Same direction as `setup-tools-first`: detection in
a script, judgment in prose, a rule its action plus one boundary.

## What Changes

- **`scope.py` beside the skill:** the scope (what the router names, the canonical set, a
  split index's parts, a router-named dated doc, a router-named spec, a router-named leaf
  inside an excluded tree; the journal, archives, excluded trees, unnamed specs and
  sub-projects out, each with its rule), the ancestor routers that load here, the cold docs
  the reference tier cites (R15's consistency-only list), the structural findings a count
  can make (R25's embedded history, a stale split index, a doc past the budget unsplit),
  the chain row (R30, through `chain_budget.py` beside it, with the largest items), and the
  seed of the cross-reference pass (R19): every path and section citation in the in-scope
  docs that does not resolve, a rename-orphan named with where its basename now lives. With
  `--lens release`, the lines carrying R29's release-close phrases. Detection only.
- **SKILL.md rewritten to the actions:** about 9 KB from 13.4; the rationale parentheticals
  out (the design doc holds them), R30 and R29 keyed to the script, the procedure opening
  with it.
- **A script-level check:** `scope.py` byte-exact on three baselined fixture copies (the
  base TidePool; the reefstack `audit-scope` variant from `PulseMonitor/`; the `fat-chain`
  root), under `harness/scope-fixture/`.
- **A regression GREEN, not a RED:** five report-only single-agent reps, one per family
  (the base TidePool's t1 with CB, DV and O; `audit-scope` from `PulseMonitor/`; the
  `fat-chain` root; the `fat-chain` copy from `ReefDash/`; `release-lens` in release-close
  mode), Sonnet at high through a Workflow. A cell that fails names the clause restored.

## Capabilities

### Modified Capabilities
- `docs-architecture-audit`: the scope step is scripted (a new requirement); the rules'
  wording, no requirement changed.

## Impact

The deployed footer and the spec's requirements stand; `whats-next` reuses the fan-out
unchanged. MAINTAIN follows (`report_check.py`).
