# docs-architecture-setup: delta for split-index-written-lines

## ADDED Requirements

### Requirement: A split index states what each part holds in a written line
The index of a split reference doc SHALL carry one entry per part on one physical line: the
heading as written, the part's file and size, and a written line saying what the part holds.
The run that splits the doc SHALL author the lines and pass them to `split_doc.py` in a
lines file; the script SHALL NOT derive a line from the part's text, and SHALL refuse the
apply, writing nothing, when a part has no line.

#### Scenario: The apply writes the lines it is given
- **WHEN** `split_doc.py --apply` runs with a lines file holding a line for each `##` heading
  of the doc
- **THEN** each entry of the index's Parts list is one physical line carrying the heading,
  the part's file, its size and that line byte for byte

#### Scenario: A part with no line is refused
- **WHEN** the lines file holds no line for one of the doc's `##` headings
- **THEN** the script exits naming the heading, and neither the directory, the parts nor the
  index is written

#### Scenario: An apply with no lines file is refused
- **WHEN** `--apply` runs with no lines file
- **THEN** the script exits saying every part takes a written line and that the dry run prints
  the headings, and writes nothing

#### Scenario: A heading the doc does not have is refused
- **WHEN** the lines file carries a `##` heading that matches none of the doc's
- **THEN** the script exits naming that heading and writes nothing

#### Scenario: One grep over the index returns the part to open
- **WHEN** a reader greps the index for a term a written line carries
- **THEN** the matching line names the part's file and its size, with no second read needed
  to find them

#### Scenario: The dry run states the form
- **WHEN** the dry run finishes its report on a doc past the budget
- **THEN** it states what a line says (what the part holds, in the part's own terms), the
  cap, the term rule and the form of the lines file

#### Scenario: The fixture's index is byte-exact
- **WHEN** the script is applied with `--today 2026-10-12` and
  `harness/split-fixture/lines.md` to a scratch copy of the TidePool `fat-topics`
  ARCHITECTURE
- **THEN** the index equals `harness/split-fixture/index.expected.md` byte for byte and the
  parts reconstruct the doc as before

### Requirement: A written line names only terms its part contains and stays within the cap
`split_doc.py` SHALL refuse a written line longer than 320 characters and a written line
carrying a code-formatted term (a span between single backticks) that does not occur
verbatim in its part. The refusal SHALL name the part and the fault, and nothing SHALL be
written.

#### Scenario: A term the part does not contain is refused
- **WHEN** a line supplied for a part carries `` `fetch_tides()` `` and the part's text has
  no such string
- **THEN** the script exits naming the part and the term, and writes nothing

#### Scenario: A line past the cap is refused
- **WHEN** a supplied line is 321 characters long
- **THEN** the script exits naming the part and the length, and writes nothing

#### Scenario: A line whose terms resolve passes
- **WHEN** every code-formatted term in a supplied line occurs in its part and the line is
  within the cap
- **THEN** the line is written as given

### Requirement: Reindexing keeps the written lines and puts a changed part's line to review
`split_doc.py --reindex` SHALL keep each written line byte for byte and refresh only the
heading, the file and the size of each entry. It SHALL list for review, with its line, each
part whose size differs from the size the index recorded. It SHALL refuse, writing nothing,
when a part in the directory has no line or a line fails its checks, and SHALL take a line
for such a part from a lines file.

#### Scenario: Nothing changed
- **WHEN** `--reindex` runs on a split whose parts are as the index recorded them
- **THEN** the index is byte-identical afterwards and no part is listed for review

#### Scenario: An edited part is listed for review
- **WHEN** a part has grown since the index was written and its line's terms still occur in
  it
- **THEN** the entry's size is refreshed, its line is unchanged, and the output lists the
  part with its old and new size and its line

#### Scenario: A new part with no line is refused
- **WHEN** a file is added to the split directory and `--reindex` runs with no lines file
- **THEN** the script exits naming the part and the index is unchanged

#### Scenario: A new part is entered from a lines file
- **WHEN** `--reindex` runs with a lines file holding a line for the new part's heading
- **THEN** the part is entered after the listed parts with that line, and the other entries
  keep theirs

#### Scenario: A renamed identifier is caught
- **WHEN** an identifier a written line carries in backticks has been renamed in its part
- **THEN** `--reindex` exits naming the part and the term, and the index is unchanged until
  the line is corrected

### Requirement: A split index that no longer matches its parts is reported stale
`split_doc.py --check` SHALL change nothing and SHALL report a split index stale when the
directory and the index list different files, a part's size differs from the size the index
records, a part has no line, or a line fails its checks. The survey SHALL print that finding
on the doc's line with the rule (T5) and the remedy (`--reindex`).

#### Scenario: A fresh split is clean
- **WHEN** `--check` runs on a split just applied or just reindexed
- **THEN** it reports nothing stale and exits zero

#### Scenario: An edited part makes the index stale
- **WHEN** a part is edited so that its size differs from the size the index records
- **THEN** `--check` names the part and both sizes, exits non-zero and writes nothing

#### Scenario: The survey prints the finding
- **WHEN** the survey runs on a project whose split doc has an edited part
- **THEN** the doc's line in the survey says the index is stale and ends with T5 and
  `--reindex`
