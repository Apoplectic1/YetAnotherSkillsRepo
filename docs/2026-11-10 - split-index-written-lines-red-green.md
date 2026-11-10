# Split index written lines: RED/GREEN record (2026-11-10)

Change `split-index-written-lines` (the ROADMAP's "The split index says what each part
holds"). A split reference doc's index carries one written line per part in place of the
part's first sentence. This record opens with the retrieval questions, frozen before any
written line existed (task 1.1); the cells and results follow when the reps run.

## Retrieval questions (frozen 2026-11-10, before any line was written)

A reader rep sees one index and nothing else, gets these questions, and names for each the
part it would open first. The score is the right part at the first pick. Each question is
answered in exactly one part, checked by grepping its answer string over every part (the
script below), and is worded without that part's heading. The questions were chosen one per
part over eight different parts of each doc, by what a working session would plausibly look
up, before the authoring reps wrote any line; the authoring reps never see them.

### The TidePool `fat-topics` ARCHITECTURE (19 parts)

| Id | Question | Answering part | Answer string |
|---|---|---|---|
| F1 | What is raised when NOAA answers 200 with an HTML page instead of JSON? | Errors and exit paths | `JSONDecodeError` |
| F2 | How much of a cold `plan` run goes to loading the astronomy library's tables? | Requests and the network budget | "about 200 ms" |
| F3 | Why does the exported low-tide height keep NOAA's text instead of a parsed number? | The window dict: nine keys and their contract | "trailing zero" |
| F4 | What is the most a low that falls outside daylight can earn, and what setting would exclude it? | Worked scoring examples | "maximum score for a window outside daylight is 0.7" |
| F5 | Would a change to the daylight factor's one-hour margin be caught by the suite? | Testing and the pure core | "margin would pass" |
| F6 | After a new gauge goes in, how many lines should the listing command print? | Adding a station: what changes where | "nineteen lines" |
| F7 | Is a stored station record judged fresh by NOAA's refit date or by when its file was written? | Station registry and the metadata cache (`stations.py`) | "not since the record's own" |
| F8 | Why is the output file opened with `newline=""`? | CSV export (`export.py`) | "Windows does not double it" |

The extract index (`harness/split-fixture/index.expected.md` as of 2026-10-12) carries none
of the eight answer strings.

### This repository's design doc (14 parts)

| Id | Question | Answering part | Answer string |
|---|---|---|---|
| D1 | Which of the agent's ways of reaching a doc is paid in every session? | How Claude actually accesses docs | "paid **every session**" |
| D2 | What should a dated record's opening line carry so a grep hit can be triaged from one line? | The index that auto-scales | "First line" |
| D3 | What three factors multiply into how dangerous a stale fact is? | Anti-staleness design principles | "how always-on" |
| D4 | Which worker tier does the audit fan-out default to, and why are the cheaper tiers first-sweep only? | The phased arc | "Sonnet at **high effort** is the default" |
| D5 | Which files of the enforced set are created only when a condition holds? | SETUP-skill spec | "README/RELEASING" |
| D6 | How large was the lab notebook the date-based overflow was derived on? | Journal rollover: 2026-09-26 | "311 KB" |
| D7 | What per-file limit applies to every file that loads at launch? | Always-on budget: 2026-10-12 | "200 lines" |
| D8 | How much skill text did the three script-backed trims remove, in KB? | Tools over prose: 2026-10-12 | "29.3 KB" |

The extract index carries one of the eight: D3's answer is the opening of the
Anti-staleness part's first sentence, so on that question the extract does its job. The
written lines for this doc are authored by the session that wrote these questions; that
bias is the reason the fixture cells, whose lines come from authoring reps that never saw
the questions, are the primary evidence.

The uniqueness check: for each answer string, the parts whose text contains it (the
fixture split by `## `, the design doc's parts as files); a question passes with exactly one
hit, the part it names. All sixteen passed on 2026-11-10.

## Cells and results

One Workflow at Sonnet/high, nine reps (two authoring, five reading, one reviewing, one
auditing), 632k tokens. The projects are `harness/split-fixture/build_cells.py`'s; the
cells are SD6 to SD9 in `harness/catalog-tidepool.md`. Every rep had the dev SKILL.md by
path and the dev scripts beside it. No cell failed, so no clause, refusal or rule was added
(task 5.3 needed none of the three).

| Cell | Result |
|---|---|
| SD6 authoring, two reps | 2/2 pass. Both ran the survey, the dry run, a lines file checked with `--lines`, then `--apply` and `--check`. Both tripped the term check on the same paraphrase, `` `id  name` `` for the stations part (the part writes the f-string), and fixed it in one step; it was also the first fault in this change's own `lines.md`. No line restates its part's first sentence: the highest similarity to the extract is 0.46 (rep 1, a line opening with the same file name and then listing contents), and none opens with the extract's first 40 characters. Both fixed the stale lines the dry run listed; rep 2 left the testing part's "this file" as a false positive, rep 1 made it explicit (`tests/test_plan.py`), both keep its meaning. |
| SD7 reading, five reps | First pick, scored against the frozen key: the fixture's extract index 6/8; its index from SD6 rep 1, 6/8; from SD6 rep 2, 7/8; the design doc's extract index 7/8; its written index 7/8. |
| SD8 reviewing | Pass. The rep ran the survey (stale: the tides part 1.2 KB recorded, 2.0 KB now), read the part, and rewrote the line to cover the new topic ("checking a listing against NOAA's station tide table"). The cap refused its first draft at 351 characters with nothing written; the second passed. D7's refusal is not needed: the printed review list was acted on. |
| SD9 auditing, one round | Pass. Among 23 flags, one on the planted index line: "the part describes the terminal table's layout", evidence `csv-export.md` lines 7 to 28 and "the table is in the-cli.md", action `fix-doc` on the index line, noting that "an agent routing by the index would skip the part that answers CSV questions". No AUDIT rule is needed (D11). |

### What the reading cells show

On the pre-registered score, the written lines gain at most one pick: 6/8 and 7/8 against
6/8 on the fixture, a tie at 7/8 on the design doc. The readers route most lookups from the
headings alone (six or seven of eight with the extract), so the questions left little room.

Every miss reads the same way once the misses are opened. Each index's misses split into
two kinds:

- **A single-part question the index failed to route.** The extracts missed two: F1 (the
  fixture extract sent the HTML-body question to the CO-OPS client) and D2 (the design
  extract sent the opening-line convention to the tiers part). Both written indexes got F1
  and the written design index got D2: their lines name `JSONDecodeError` and "the
  filename and first-line conventions that make grep triage cheap".
- **A question with a second defensible part.** F4 (all three fixture indexes picked
  Window scoring, where the formula and the weights give the same 0.7), F6 (SD6 rep 1's
  index picked the stations listing part, which says the listing "grows by one per admitted
  station") and D1 (the written design index picked the always-on budget part, whose line
  begins "what a session pays at launch", and whose text answers the question in its own
  terms). Every miss of the written indexes is of this kind.

Read post hoc, with F4, F6 and D1 set aside as two-part questions (flagged as post hoc: the
key was frozen before the reps and these are excluded after them), the written indexes
route every remaining question and the extracts miss one per doc: the fixture 6/6 and 6/6
against 5/6, the design doc 7/7 against 6/7. The evidence is that the extract's failures are
real and the written lines fix them. Whether the lift is large is not shown: headings carry
most of the routing on docs whose headings are this descriptive.

Two method lessons. The uniqueness check matched answer strings, so it missed answers a
reader can derive in a second part (F4's 0.7 from the weights, F6's nineteen from
"eighteen ... grows by one"); a later question set should be checked by asking whether any
other part would let a reader answer it. And D1's miss came from a line written by the
session that wrote the questions; the bias the questions were frozen against ran the other
way.
