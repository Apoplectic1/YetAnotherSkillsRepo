# split-doc field fixes: RED/GREEN record (2026-10-12)

Change `split-doc-field-fixes`, from the HDL pilot of the same day (findings 5 and 8 of
`docs/2026-10-12 - hdl-pilot.md`). Mostly script contracts, verified at script level; one
behavioral cell, RED through a Workflow at Sonnet/high (two plan-only SETUP reps, 154k
tokens).

## Script-level checks

| Contract | Check | Result |
|---|---|---|
| a journal is refused | a generated heading journal (forty dated `##` sections, 41 KB) | "a journal rolls over by date with rollover.py, it never splits by topic" |
| the citation scan skips sub-projects and child repositories | the reefstack root (three sub-projects with routers), budget forced to 10 KB | 0 citations found below the root; the sub-projects not walked |
| the stale-line list and the dated-heading warning | the fat-topics doc with a `## State (2026-07-10)` section carrying `../ROADMAP.md`, `../openspec/` and "this file" | the heading flagged, four lines listed (one a false positive: "does not belong in this file" about a test file); `harness/split-fixture/dryrun.expected.txt` |
| the index and the parts | the same doc, `--apply --today 2026-10-12` | nineteen parts, byte-exact, `index.expected.md` regenerated |

## The behavioral cell

| Cell | Plant | RED (current text) |
|---|---|---|
| NB2 | a 38 KB ARCHITECTURE and a router block S7 moves into it (41.8 KB after) | 2/2 no failure: both reps sequenced the split after the move ("the split must come after the move, because only then is the doc over budget"); one previewed the dry run at a lowered budget and read its fourteen citations |

So the same-run sentence drafted for T5 was not shipped: the text says "past its budget" and
the reps apply it at the point the doc passes it. The single-part case (the HDL pilot's
49.7 KB ROADMAP part) is likewise baseline: the rep reported it and left it, saying the rule
offered no lever, which is the rule. Both are status notes in the setup spec.

## Shipped

`split_doc.py`: the journal refusal; the citation scan's scope (a directory with its own
router or `.git` is skipped; the count is the repository's own); the per-part list of lines a
move one directory down leaves stale; the dated-heading warning; UTF-8 output; the note's
"unambiguous short form". T5's text names the stale-line list, the dated-heading warning and
the journal refusal, since they are the operator's steps around the tool. Fixtures:
`near-budget`, the fat-topics doc extended, `dryrun.expected.txt`.
