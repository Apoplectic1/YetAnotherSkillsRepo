# docs-architecture-design: Always-on budget: 2026-10-12 (part of ../docs-architecture-design.md)

> One topic of `../docs-architecture-design.md`, split out on 2026-10-12 when the file passed its
> budget; the heading keeps its text, so "docs-architecture-design § Always-on budget: 2026-10-12" resolves by grep over
> the file and `docs-architecture-design/`. The index is `../docs-architecture-design.md`.

## Always-on budget: 2026-10-12

The 40 KB gate was the harness's per-file warning applied to one file: the right budget at
the wrong scope. What a session pays before its first question is the chain: the owner's
global file, every ancestor router, the project's router, the always-on rule files, the memory
index (measured 2026-10-12: 83 KB, about 21k tokens, for a session under HlsLibrary or the
Arty; 36 KB here). The cost model has three terms: **context room**, linear in tokens;
**interference**, scaling with the count of directives a session does not need (a gotcha
misapplied where it does not belong); **staleness**, scaling with volatility. A gotcha-dense
router passes S7's content test and pays all three.

So always-on is a scope, not a size (SETUP S8, AUDIT R30): an item loads at launch only if it
passes breadth (every session launched there needs it) and stability (it changes less often
than the audit cadence), and that test is what "load-bearing" means. A failing block goes on
demand behind a one-line trigger, in the home its need is keyed to. The harness facts behind
the homes (verified against the Claude Code docs 2026-10-12): a `.claude/rules/<name>.md`
with `paths:` frontmatter loads when a matching file is read, written or edited (file-keyed;
without `paths:` it loads at launch and counts); a skill's body loads on invocation
(activity-keyed); a reference-doc section is read by heading (prose); `@imports` expand at
launch and do not help; the harness itself warns at 200 lines per CLAUDE.md and at an
undocumented combined size. `chain_budget.py` beside the audit skill measures the chain against
a share of the window (5 percent, about 10k tokens, by default; the router may state its own),
marks files over 200 lines, and subtotals the project's part from the ancestors' and the
owner's; AUDIT's coverage note carries the row. The number detects, the test decides: a
router under budget still moves a block that fails; an ancestor's weight is reported, never
flagged below it. Provenance: derived on the HDL tree (the 2026-09-26 measurement, the
2026-10-12 remeasurement), RED 6/6 on non-derived fixtures (TidePool `fat-gotchas`, reefstack
`fat-chain`): the SETUP text improvised a criterion and measured nothing, the audit from a
sub-project never saw the ancestor, the audit at the root shielded 12 KB of per-repo gotchas
under R26's carve-out. GREEN in the record:
`docs/2026-10-12 - always-on-budget-red-green.md`; the change:
`openspec/changes/archive/2026-10-12-always-on-budget`.

