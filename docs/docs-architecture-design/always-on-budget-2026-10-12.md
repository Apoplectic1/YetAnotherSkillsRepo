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

**Field fixes (the HDL pilot, the same afternoon; change `s8-field-fixes`).** Three real
repositories through the deployed skill showed the rule's first form wanting in the same
places. The budget became per file: every file that loads at launch has 200 lines (the
harness's own guidance, about 5k tokens), the number a unit can act on; the chain's 5 percent
stays the row's tripwire, met when every level meets its own, and the ancestors' and the
owner's shares are reported for their own leans, never chased from below (the owner's global
file alone is 6.8k tokens on this machine, so no unit's chain met the old line). The homes
carry their load triggers: a rule file loads on a matching file's first touch (so it fits
files in this repository and nothing else: a command-only session touches no file, and a
glob cannot name a sibling's), a skill on invocation (an activity: a build, a bench run), a
section on a read; a guard keyed to neither keeps one router line; B1 lets S8 write the
skill; stability reads "changes less often than a release". RED 3/3 on the budget and the
command-keyed block, 1/2 on the sibling's files; GREEN 2/2 on each. Five more clauses the
pilot drafted were no-failure on the fixtures and are status notes in the specs, not text:
a block a reference doc already holds is dropped with a cross-reference (S1's merge), a
status block is ROADMAP's, a halt bounds a lean to documentation, breadth at a container
root counts the sessions beneath it (the pilot's AtmlBoards rep misread this; the fixture
rep did not), and a held promotion under a halt follows the halt's terms (a halt that admits
documentation admits the docs landing, which the MAINTAIN rep read unprompted; a clause
holding every promotion until the halt lifts would have been wrong there). An umbrella with
first-party content (B4) and a project's reference docs outside the set wait for a cell. The
record: `docs/2026-10-12 - hdl-pilot.md` and
`docs/2026-10-12 - s8-field-fixes-red-green.md`.

