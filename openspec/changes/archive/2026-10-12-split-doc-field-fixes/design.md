# split-doc-field-fixes: design

## Context

T5 and `split_doc.py` shipped on 2026-10-12 and ran the same afternoon on the HDL tree's
real docs (the pilot record, `docs/2026-10-12 - hdl-pilot.md`). The Arty's ARCHITECTURE
split cleanly; the umbrella's DOMAIN, ROADMAP and CHANGELOG, and HlsLibrary's router and
class READMEs, showed the script's contract was narrower than the docs it met.

## Decisions

- **D1: a journal is refused, by the rollover's own detection.** Dated `##` headings (half
  or more of the sections) or three or more dated top-level bullets mark a journal; a
  journal rolls over by date (T1) and never splits by topic. The umbrella's CHANGELOG was
  one dry run from becoming per-day parts.
- **D2: the citation scan stays inside the unit.** A directory holding its own `CLAUDE.md`
  or `.git` is a sub-project or a child repository (B3) and is skipped; the count is the
  repository's own, stated as such. Citations from outside remain the operator's to grep
  (the dry run says so).
- **D3: stale lines are listed, not rewritten.** A part moves byte for byte (the contract
  that makes the split mechanical), so a relative path or "this file" inside it is wrong
  one directory down. The dry run lists them per part for the operator to fix after the
  apply; the script never edits a body. The list has false positives ("does not belong in
  this file" meaning a test file); that is the operator's judgment, cheap at the list.
- **D4: a dated heading is a warning, not a refusal.** The part's filename follows the
  heading; a heading like "State (2026-07-10)" is edited in place and would rename the part.
  The author chooses: rename the heading first, or accept the drift.
- **D5: the same-run split.** When the run's own moves (S7, S8) push a doc past the budget,
  T5 applies after the moves land, in the same run, so the run does not hand a 42 KB doc to
  a later one. RED's cell is exactly this shape (a 38 KB doc, a 3.8 KB block).
- **D6: a single part past the budget is reported and left.** T5's "never below `##`"
  stands; the script says so beside the part; the author's `###` headings are the lever.
  The umbrella's ROADMAP (a 49.7 KB "Next, in order" of bold paragraphs) is the case. A
  status note, not a cell: the pilot rep did the right thing and said the rule offered no
  lever, which is the rule.

## Verification

Script-level: a generated heading journal is refused; the reefstack root's scan skips its
three sub-projects; the fat-topics doc's dry run (a dated State section and relative paths
added) prints `harness/split-fixture/dryrun.expected.txt` and its apply the regenerated
`index.expected.md`. Reps: two RED and two GREEN plan-only SETUP reps on the `near-budget`
variant (NB2), through a Workflow at Sonnet/high. Record:
`docs/2026-10-12 - split-doc-field-fixes-red-green.md`.
