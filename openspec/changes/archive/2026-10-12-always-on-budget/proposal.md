# Proposal: always-on-budget

## Why

The family's one size rule, the 40 KB gate, is the harness's per-file warning applied to one
file: the right budget at the wrong scope. What a session pays before its first question is the
chain: the owner's global file, every ancestor router, the project's router, the memory index.
Measured 2026-09-26 on the HDL tree at 52 to 79 KB, and again 2026-10-12 at 83 KB for a
session under HlsLibrary or the Arty (26.7 global, 4.5 + 12.1 ancestors, 39.9 or 26.6 the
router; about 21k tokens, a tenth of the window), with no rule counting it. The owner's
question (2026-09-26): the gate is brute force, is there a better way?

S7 leans a router by content: reference prose moves, routing and gotchas stay "regardless of
router size". HlsLibrary's router passes S7 and is 39.9 KB: 16.2 KB of HLS synthesis gotchas
(30 of them, every one a gotcha) and 12.6 KB of element maps the class READMEs already hold.
Every line passes the content test and fails a scope test nobody states: a session that fixes
a README never needs `array_partition` on file-scope statics. The cost of that is not only
context room (linear in tokens) but interference (a gotcha misapplied where it does not
belong, scaling with the count of directives a session does not need) and staleness (scaling
with volatility).

## What Changes

- **The rule, in SETUP beside S7:** an item is always-on only if it passes *breadth* (every
  session launched here needs it) and *stability* (it changes less often than the audit
  cadence). S7's content test decides where a thing lives; the scope test decides whether it
  is always-on at all. A failing block goes on demand behind a one-line always-on trigger, in
  the home its need is keyed to: a path-scoped rule file (`.claude/rules/<name>.md` with
  `paths:`, loaded when a matching file is touched) for a file-keyed need such as a toolchain's
  gotcha pack; a skill (its body loads on invocation) for an activity-keyed need such as a
  build procedure; a reference-doc section read by heading (`grep -n "^## "`, then the span)
  for prose. Verified against the harness docs 2026-10-12: `@imports` expand at launch and do
  not help; a rules file without `paths:` loads at launch and counts.
- **The tripwire, in AUDIT:** `chain_budget.py` beside the audit skill measures the chain for a
  launch directory in bytes, lines and estimated tokens, against a budget stated as a share of
  the window (5 percent of 200k by default, about 10k tokens; the project may state its own in
  the router), the harness's 200-line per-file guidance marked, the project's own part
  subtotaled from the ancestors' and the owner's. The coverage note carries the chain row; a
  router block that fails breadth or stability gets one placement flag `move-to <on-demand
  home>`. The number detects, the test decides. An ancestor's weight is reported, never
  flagged here: it is its own audit's.
- **R26 reconciled:** its "never flag routing lines or gotchas, regardless of router size"
  stays true on the content axis; a gotcha block still meets the scope test.
- **The design doc:** the cost model (room, interference, staleness) and the on-demand homes
  with the harness facts behind them.
- **Fixtures:** `harness/chain-fixture/` (a generated tree with known sizes and the expected
  output), the reefstack `fat-chain` overlay (a container root carrying one sub-project's
  gotcha pack and a glossary), the TidePool `fat-gotchas` overlay (a router whose gotcha pack
  passes content and fails breadth).

## Capabilities

### Modified Capabilities
- `docs-architecture-setup`: the scope half of the lean rule and the on-demand homes.
- `docs-architecture-audit`: the chain measured and reported; the scope test as a placement
  axis beside R26.

## Impact

Nothing moves in any consumer until its next SETUP or AUDIT run. The pilot the ROADMAP names
(HlsLibrary's router: element maps to the class READMEs, the HLS gotchas to a path-scoped rule
file or a skill, the ATML DOMAIN read by section, the Arty's router) is consumer adoption from
an HDL session after the ship, queued in ROADMAP. The owner's global file is a third of every
chain on this machine and outside any project's reach; the chain row reports it as the owner's.
