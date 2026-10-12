# s8-field-fixes: RED/GREEN record (2026-10-12)

**Charter:** the dated record of the change's runs: the cells, the RED scores on the current
text, the GREEN scores on the candidate, what shipped and what did not. The design is
`openspec/changes/archive/2026-10-12-s8-field-fixes/design.md`; the standing truth is SETUP
S8, B1 and T5, AUDIT R30, and the design doc's always-on part.

## The question

The HDL pilot (`docs/2026-10-12 - hdl-pilot.md`) ran the deployed SETUP skill on three real
repositories and found S8 silent or wrong in the same places on all three. The tree derived
every finding, so it is poisoned for them; the cells below are on TidePool and reefstack
variants built to carry the same shapes, and only a clause a rep fails there ships.

## The fixture

`harness/tidepool-fixture-variants/s8-field/build_variant.py` composes, on a copy of the
base fixture, a router of 204 lines and 14.0 KB: the base router, a dated State block, the
base ARCHITECTURE's module map copied verbatim, a build-flash-bench procedure keyed to no
file, a bench-network block, three rules about a sibling repository's files, the CO-OPS
gotcha pack and the conventions; a ROADMAP with "Halted at v0.6 (2026-07-10): only
documentation and bench records change until the freeze lifts"; a NOTEBOOK with the
fat-arch entries (the 2026-07-08 retry policy graduates to ARCHITECTURE) and a halt
decision. The sm2 copy is the same variant with the 41.7 KB fat-topics ARCHITECTURE in
place of the base one. The reefstack `fat-chain` root serves CR1. Every rep: Sonnet at
high, plan-only or report-only, through a Workflow; each ran `chain_budget.py` unprompted
(the owner's global file 6,846 tokens of the 10,000; the router 3,498, 204 lines).

## RED, the current texts (four reps, 339k tokens)

| Cell | Result |
|---|---|
| SF1 the budget a unit cannot meet | FAIL 3/3. sf1: "the overage is this project's to fix", and chased the chain; sf2 planned to the chain total and named the gap itself ("nothing about when the project's part is fine but the chain is still over"); fr1 at the reefstack root: "the 206-line flag is the tool's, not the skill's", "the global file alone is 68% of the budget; the skill does not say". |
| SF2 a block keyed to a command | FAIL 3/3. All three named B1 against S8 (S8 offers a skill, B1 allows only a rule file under `.claude/`): sf1 wrote the skill regardless, sf2 a rule file whose `paths:` (`Makefile`, `bench/`) never fire for a session that only runs the command, fr1 a skill "with no allowed location". |
| SF3 gotchas about a sibling repository's files | FAIL 1/2. sf1: `.claude/rules/harmonics-core.md` with globs for files the repository lacks; sf2 keyed it to the local callers (defensible). |
| SF4 a block ARCHITECTURE already holds | no failure 2/2: the copy dropped as S1's merge. |
| SF5 a State block | no failure 2/2: to ROADMAP, for failing stability. |
| SF6 the halt | no failure: "docs only: every change above is docs or rules". |
| CR1 breadth at a container root | no failure: "every session under the container pays the 3850". |
| SM1 a promotion into the halted project (healthy target) | moot: the fixture's halt admits documentation, and a docs promotion into a healthy target lands under it. The field case is a held promotion, so sm2 was built. |

## The candidate

SETUP S8: the budget is per file (200 lines, the harness's own guidance, about 5k tokens;
`chain_budget.py` marks each file over it and reports the chain against 5 percent of the
window, met when every level meets its own, the ancestors' and the owner's shares reported
for their own leans and never chased from below); the homes carry their load triggers (a
rule file loads on a matching file's first touch, so it fits files in this repository and
nothing else: a command-only session touches no file, a glob cannot name a sibling's; a
skill loads on invocation, for an activity; a section is read by heading, for prose); a
guard keyed to neither keeps one router line; the router names every rule file and skill
it writes. B1: the only things written under `.claude/` are what S8 moves a block to, a
rule file or a skill. Stability reads "changes less often than a release" (was "the audit
cadence", a term no project defines; a wording clarification, the SF5 cell no-failure under
either). AUDIT R30: the row carries each file against its own line. Dropped from the draft
after RED: the duplicate rule, status blocks to ROADMAP, the halt bound, breadth beneath a
container root, S7's list addition, B4 for an umbrella, the enforced-set row.

## GREEN, the candidate (two SETUP reps; 243k tokens with sm2)

| Cell | Result |
|---|---|
| SF1 | PASS 2/2. sf3: "The budget is per file ... the project file is at 204 lines against 200, so it fails its own line. Only this file is mine to lean. The owner's global file (6846 tokens, 187 lines) meets its own line. It is never chased from below." sf4: "Lean only the project file ... The owner's global file is reported and not chased from below." Both then ran the content test block by block ("not trim 344 tokens") to a router of about 45 lines. |
| SF2 | PASS 2/2. The build-flash-bench block and the bench network to one skill in both (`bench-and-release`, `tidepool-bench`), the trigger line naming the `make` targets: "S8 names a build, a bench run, a release step as skill territory". The rate-limit guard, keyed to a file and to a command at once, split them: sf3 kept it as one router line ("a session that only runs a command touches no file, so no path glob can load a rule for it ... too small for a skill"); sf4 moved it to the CO-OPS rule file and named the doubt. sf3 on B1: "only the last sentence of B1 resolves it", which is the sentence. |
| SF3 | PASS 2/2. "A glob cannot name a sibling repo's files, so a path rule is ruled out (S8)": a skill in both (`harmonics-core`, `tidepool-core`), its intro paragraph as the skill's context. |

Both reps also dropped the module-map copy, sent State to ROADMAP, created CHANGELOG (A2),
read the halt as bounding the plan to documentation, and left the graduations to MAINTAIN.
Gaps they named, none a failure of a cell: breadth has no yardstick for a single-purpose
project (the datum guard is a judgment either way); the granularity of rule files; S7 names
no home for a dated status snapshot (ROADMAP by inference); release mechanics could be a
`RELEASING.md` or a skill; whether a halt on code covers `.claude/` files.

## sm2: a held promotion under a halt (MAINTAIN, current text)

Held (M14: 41.7 KB, seventeen topics, "a topic split would relocate nearly all of it"), the
report and one ROADMAP line for the split, the landing sequenced after the split into the
network-budget part. On the halt, unprompted: "A T5 split and the promotion are
documentation only, so the halt does not block them. The retry code and the timeout fix are
code, so the halt blocks them. The promoted text must therefore say decided, not
implemented; frozen with the planner." That is the right reading of that halt. The clause
drafted for M14 ("stays held until the halt lifts, whatever the split's state") would have
been wrong on this fixture; the Arty's halt is on all work, and the plan author, not a
MAINTAIN rep, misread it in the pilot. No failure, no text: the halt's terms decide, and a
rep reads them. A halt on all work is unprobed and waits for a cell.

## What shipped

SETUP S8 and B1 and the T5 line (`--reindex`), AUDIT R30, `chain_budget.py` (each file
against its own line in the summary; the chain fixture's expected output regenerated),
`split_doc.py --reindex` (an edited part's size and first sentence back into the index, in
the index's order; found when this repo's design doc part was edited). Status notes in the
specs for the five no-failure clauses; B4 for an umbrella with first-party content and a
row for a project's reference docs outside the set wait for a cell. The maintain skill's
text is unchanged.

## Cost

Seven reps, 582k tokens, in two Workflows. The pilot that found the cases cost 320k; the
lean each repository was about to get from the old text would have keyed its guards to
files that never load.
