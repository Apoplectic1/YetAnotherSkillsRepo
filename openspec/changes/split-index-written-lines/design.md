# split-index-written-lines: design

## Context

See `proposal.md` for the motivation. The state this design starts from:

- `split_doc.py` writes each index entry as one line, `- **<heading>** (`<DOC>/<file>`,
  <size> KB): <extract>`, the extract coming from `first_sentence()`. `--reindex` rebuilds
  every entry from the directory, extract included.
- Three readers parse that entry by its file token: `--reindex` itself, `survey.py` (SETUP)
  and `scope.py` (AUDIT). The last two call an index stale only when its list of files
  differs from the directory.
- `survey.py` already runs a script from the other skill's directory (`chain_budget.py`,
  beside the audit skill); the two skills deploy side by side.
- No survey or scope fixture holds a split, so their expected outputs do not change.
- Four splits exist: this repository's design doc, and three under the ATML umbrella's
  path, which this change does not read or write.

The reader this design serves is an agent that opens the index to choose a part. Each
decision below is taken by what that reader does next: a grep or a read.

## Goals / Non-Goals

**Goals:**

- A line that carries the terms a search would use, guaranteed to resolve in its part.
- One grep over the index returns the file to open and its cost.
- Drift that a script can see is seen by a script, at the next survey or audit.
- One implementation of the stale test, not three.

**Non-Goals:**

- A check that a line is a good description. That is judgment, tested by reps.
- A written line per rolled file in the journal's `INDEX.md`.
- Any path for an old extract line: no detection, no conversion.
- The three HDL backfills.

## Decisions

- **D1: the entry keeps its form and is one physical line.** `- **<heading>**
  (`<DOC>/<file>`, <size> KB): <written line>`. A grep for a term returns the heading, the
  file, the size and the line together, so the reader's next call is the read. Rejected: the
  precedent's table. In raw text it adds pipes and a header row, it would rewrite three
  parsers and four indexes, and it buys nothing a reader of raw text uses.
- **D2: the size stays.** It tells the reader how to open the part: whole when small,
  `grep -n '^###'` first when large. Rejected: listing each part's `###` headings in the
  index. It never drifts, but it is paid on every read of the index for a benefit on the
  few large parts, and the size already sends the reader to that one grep.
- **D3: what a line is.** What the part holds, in the part's own terms: the things, names
  and rules a reader would search for. Not its opening restated, not its history, not a
  judgment of it. The dry run prints this with the cap and the term rule; the skill text
  says nothing unless a rep fails (the no-failure gate).
- **D4: two mechanical checks on a line.** At most 320 characters (the precedent's eight
  lines run 117 to 310; a twenty-part index stays under 8 KB with every line at the cap). Every span between single
  backticks occurs verbatim in the part's section text. The term check is the one that
  serves the reader: a backticked term in a line is a search term, and the check is the
  promise that the search lands in that part. It catches a term invented at the split and
  an identifier renamed later. Rejected: checking prose words (no stable match), and
  requiring a backticked term (a part of pure argument has none).
- **D5: the lines arrive in a lines file.** Markdown: a `## <heading as written>` line, the
  written line on the next non-empty line. Headings match the doc's by text and order; a
  heading the doc lacks is refused by name, as is a part left without a line. The run writes
  the file in its scratch space; it is an input, not a doc. Rejected: an apply that writes
  placeholders to be filled afterwards (a broken map on disk, and nothing to refuse), and
  storing the line in each part's head with the index derived from it (the reader of the
  map never opens that head, and a line edit becomes a part edit).
- **D6: the index is the line's one home.** `--reindex` reads each entry by its file token
  and keeps the text after `KB): ` byte for byte. A line is changed by editing the index in
  place, or by a lines file passed to `--reindex`, which sets the line of each heading it
  names. Either way `--reindex` re-runs D4's checks, so it is also the check for a hand
  edit, the backfills included.
- **D7: a changed part is the one whose size moved.** The entry's recorded size text is
  compared with the same formatting of the part's current size. `--reindex` refreshes the
  size and prints the part with both sizes and its line under a review heading; it never
  edits the line. Rejected: a content hash in the entry (exact, but a token in every entry
  that no reader uses; the term check already covers the same-size rename). Considered and
  left to the reps: refusing the reindex until the run confirms each changed part's line in
  a lines file. It makes the review unskippable and invites a rubber stamp; one rep cell
  shows whether a run acts on the printed list, and the refusal is the fallback if it does
  not.
- **D8: `--check` is the stale test, and the other two scripts run it.** Read-only; one
  line per finding (a file listed and gone, a part unlisted, a size moved, a line missing,
  a line failing D4); exit zero when clean. `survey.py` and `scope.py` drop their own list
  comparison and run it by subprocess, as each runs `chain_budget.py` today, folding the
  findings into the line they already print for the split with `-> T5 (--reindex)`.
  `scope.py` finds the script in the setup skill's directory beside its own; when it is not
  there the line says so and gives the command, as the chain row does. Rejected: the test
  written three times, where the entry parser and the term rule would drift apart.
- **D9: the journal's `INDEX.md` is left as it is.** A rolled file is a date range. Its
  entries' titles, as the author wrote them, are what a search matches; a written summary
  per file would be a lossy second copy, regenerated under a rule that no existing line
  changes and with nothing to check it against.
- **D10: no compatibility.** `first_sentence()` is deleted. The script does not recognize
  an extract. This repository's fourteen lines are rewritten in the index and `--reindex`
  checks them; the HDL three follow the same two steps from their own session.
- **D11: AUDIT gets the mechanical half only, unless a rep says otherwise.** `scope.py`
  reports what `--check` finds on every audit. A rule that reads each line against its part
  is added only if an audit rep misses a planted line that passes D4 and no longer
  describes its part.

## Risks / Trade-offs

- [A line is true to D4 and still unhelpful] -> the retrieval check measures it once on two
  docs; after that it is the reindexing run's judgment and the audit's.
- [A run ignores the review list, and the refreshed size erases the signal] -> the rep cell
  in Verification; D7's refusal is the fallback.
- [The size text has 0.1 KB resolution: a small edit is not flagged] -> the term check
  covers the small edit that matters to a search, a rename. A small edit that changes what
  a part holds without touching a named term is accepted as missed.
- [The term check refuses a fair line that code-formats a term from outside its part] ->
  the refusal names the term and the rule; the author drops the backticks or the term.
- [After the deploy, surveys and audits report every existing split with an edited part] ->
  intended: those indexes are stale today and nothing says so.
- [`scope.py` now depends on a script in the setup skill's directory] -> the dependency
  already runs the other way (`survey.py` on `chain_budget.py`); `deploy.sh` ships all
  skills together, and a missing script prints a line naming it.
- [The retrieval questions are written by the session that also writes the design doc's
  lines] -> the questions are written and frozen in the record before any line, and the
  fixture's reader reps score lines written by authoring reps that never saw the questions.

## Migration Plan

`split_doc.py`, `survey.py` and `scope.py` ship together in one deploy from `main`. No
stored state changes form. Rollback is a revert of the ship commit and a redeploy; the
fourteen rewritten lines of the design doc index stay valid under the old script, which
would overwrite them only if someone ran its `--reindex`.

## Verification

Script-level, byte-exact: the apply on a scratch copy of the TidePool `fat-topics`
ARCHITECTURE with `harness/split-fixture/lines.md` and `--today 2026-10-12` leaves
`index.expected.md`, the parts reconstructing the doc as before; the dry run prints the
regenerated `dryrun.expected.txt`; the refusals (no lines file, a heading with no line, a
stray heading, a term its part lacks, a line of 321 characters) each write nothing;
`--reindex` on the untouched split leaves the index byte-identical; after a part is grown
it refreshes the size, keeps the line and lists the part; a new part is refused, then
entered from a lines file; `--check` is clean on a fresh split and names each finding
otherwise; the CRLF run still passes `eol_check.py`. `survey.py` and `scope.py` on a scratch
project holding that split print the stale finding after a part is edited and nothing when
it is current.

Reps, one Workflow at Sonnet/high, every label carrying `[sonnet/high]`:

- **Authoring, two reps.** SETUP with the unchanged T5 text and the new script, each
  splitting a scratch copy of `fat-topics`. Pass: the apply succeeds, and no line restates
  its part's opening sentence. A fail adds a clause to T5 and reruns as GREEN.
- **Reading, four reps.** Eight lookup questions per doc, each answered in exactly one part
  and worded without that part's heading; a reader sees the index alone and names the part
  it would open first. Cells: the fixture's extract index, the fixture's written index (an
  authoring rep's), the design doc's extract index, the design doc's written index. The
  score is the right part at the first pick; the record states it per cell, including a
  cell where the two indexes tie.
- **Reviewing, one rep.** A split whose part gained a topic its line does not name; the rep
  is asked to bring the index current. Pass: the line is rewritten to cover the topic. A
  fail turns D7's refusal on.
- **Auditing, one rep.** D11's planted line. A miss adds the rule to AUDIT and reruns.

Record: a dated file under `docs/`, the questions first.
