# Proposal: split-index-written-lines

## Why

A split reference doc's index is the map a session opens first, and its line per part is what
lets a reader pick one part without opening the others. `split_doc.py` fills that line with
an extract (D2 of `reference-doc-split`, 2026-10-12: the heading, the file and size, the
part's first prose sentence), and the extract rarely says what the part holds. This
repository's own design doc index shows it: "The doc tiers" reads "Resolves the two-patterns
tension.", and "The phased arc", the largest part at 34.1 KB, reads "Sequencing rationale:
Phase 1 enables Phase 2 (charters make the audit objective) *and*" (the extract is the first
physical line up to its first full stop, so hard-wrapped prose is cut at the wrap). The
ROADMAP item reports the same from the field: the Conventions part of the ATML umbrella's
`DOMAIN.md` reads as its first convention.

The precedent the script missed is the Astronomy Library's `ARCHITECTURE.md`, split by hand
on 2026-08-11. Its index is a "What it covers" table, one written line per module file, each
naming what is found there ("The contract bench pinning the `CONSUMERS.md` pinout:
covered-or-registered rule, bench scope, the `LogProcessGlobal` collection rule."). A reader
picks the file from the line. The owner asked for that shape then and asked again on
2026-11-10, with four scripted splits already carrying extracts.

The criterion for every choice below is the owner's (2026-11-10): the reader these skills
serve is an agent, and the index is right when it lets that agent reach the fact with the
fewest reads and greps.

## What Changes

- **`split_doc.py --apply`, BREAKING**: the line per part is written, not extracted. The
  run that splits a doc authors one line per part saying what the part holds, in the part's
  own terms (the things, names and rules a reader would search for), and passes the lines in
  a file. The apply refuses, before it writes anything, when a part has no line.
  `first_sentence()` is removed: there is no fallback.
- **A written line is checked where a check is possible**: it stays within a length cap, and
  every code-formatted term in it occurs verbatim in its part. The second check is what
  makes a line a set of search terms that resolve where it points: an invented term is
  refused at the split, and an identifier renamed in a part later turns up as a fault, not
  as a line that quietly misleads.
- **An entry is one physical line**: the heading, the file, the size, the written line. One
  grep over the index for a term returns the file to open and what it costs to open.
- **`split_doc.py --reindex`**: keeps each written line byte for byte and refreshes only
  the heading, the file and the size. A part whose size moved since the index recorded it is
  listed for review with its line (does the line still say what the part holds?); the script
  never rewrites a line. A part with no line, or a line that fails its checks, is refused.
- **`split_doc.py --check`**, new and read-only: reports an index that no longer matches
  its parts (the files listed, a part's size, a missing line, a line failing its checks).
  `survey.py` (SETUP) and `scope.py` (AUDIT) run it, where today each compares only the list
  of files, so an edited part reaches the review at the next survey or audit. Today an
  edited part leaves a wrong size in the index and nothing reports it.
- **SETUP's T5 text** changes only if the reps show it must (the no-failure gate). The form
  of the lines file and what a line should say are the script's output.
- **Fixtures and checks**: `harness/split-fixture/` gains the lines file for the TidePool
  `fat-topics` doc (19 written lines); its `index.expected.md` and `dryrun.expected.txt` are
  regenerated; script-level cases cover the refusals, the kept lines, the review list and
  `--check`; `VERIFICATION.md`'s split paragraph follows.
- **A retrieval check** is the evidence that the change does its job: fresh reader reps get
  lookup questions and the index alone, and name the part they would open; the extract index
  and the written index are scored on the right part at the first pick.
- **Backfill, this repository**: the 14 lines of the Parts list in
  `docs/docs-architecture-design.md` are written. The file stays in place, so the link in
  every deployed skill footer holds.
- **Backfill, the HDL tree, outside this change's apply**: the ATML umbrella's `DOMAIN.md`
  and `ROADMAP.md` and the Arty's `ARCHITECTURE.md` are consumer work from an HDL session
  after the ship, as the Arty's split was (D7 of `reference-doc-split`). All three sit under
  `E:\Projects\HDL\Projects\AtmlBoards`, which stays untouched until the owner releases it;
  this change leaves one ROADMAP line queuing them.
- **No compatibility path**: the script cannot tell an old extract from a written line and
  is not taught to. The four existing indexes are rewritten by hand, and `--reindex` then
  checks them.

## Decided (2026-11-10, by the criterion above)

- **The layout stays a bullet list.** An agent reads the raw text, where a table adds
  pipes and a header row and nothing else. The form is already what `survey.py`, `scope.py`
  and `--reindex` parse, and the fault was the line's content. The precedent's table is not
  copied; its written line is.
- **The size stays in the entry.** It is the reader's cost signal: a 2 KB part is read
  whole, a 34 KB part is grepped for its `###` headings first.
- **A changed part is marked by its size, a wrong term by the term check; no content hash.**
  The recorded size needs no new state and prompts the review; the term check is exact for
  the drift that misleads a search. A hash would put a token in every entry that no reader
  uses.
- **The journal's `INDEX.md` gets no written line per rolled file** (the ROADMAP item's open
  question). A rolled file is a date range, not a topic, and the INDEX already lists every
  entry by the author's own title, which is the text a search matches. A written summary of
  a date range would be a second, lossy copy with nothing to check it against.
- **The run that reindexes judges a line against its part.** AUDIT gets the mechanical half
  through `scope.py` on every run. Whether it also needs a rule that reads each line against
  its part is settled by one rep on an index with a planted line that passes the checks and
  no longer describes its part: a rule is added only if the rep misses it.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `docs-architecture-setup`: the split index's entry (a written line, its checks, the
  refusal), `--reindex` (lines kept, a changed part put to review) and `--check` (the stale
  test the survey prints).
- `docs-architecture-audit`: the scope step's stale-split-index finding, by the same test.

## Impact

- **Code**: `skills/docs-architecture-setup/split_doc.py` (the lines input, the checks,
  `--reindex`, `--check`, `first_sentence()` removed); `skills/docs-architecture-setup/survey.py`
  and `skills/docs-architecture-audit/scope.py` (each runs `--check` in place of its own
  list comparison). `scope.py` reaches the setup skill's script as `survey.py` reaches the
  audit skill's `chain_budget.py`: the two skills deploy side by side.
- **Skill text**: T5, and an AUDIT rule, only on a failed rep. Deploy from `main` after
  the reps.
- **Docs**: the design doc's tier section (D2 amended: the line is the one place judgment
  enters a split, while the boundaries and the moves stay mechanical), `ARCHITECTURE.md`,
  `VERIFICATION.md`, `CHANGELOG.md`, the ROADMAP item closed and the HDL backfill queued.
- **Harness**: byte-exact script checks; one Workflow at Sonnet/high for the authoring
  reps, the reader reps and the one audit rep.
- **Consumers**: a split run after the ship reads the doc and writes a lines file. A survey
  or audit after the deploy reports every existing split whose parts were edited since their
  index was written, which is the finding working as meant. `--reindex` on the four existing
  indexes keeps their extract lines until the backfill rewrites them.
- **The cost accepted**: D2's reason stands. A written line takes judgment and can drift
  from its part. The review list and the term check are the counter; they catch a changed
  part and a term that is gone, not a line that is true and unhelpful.
