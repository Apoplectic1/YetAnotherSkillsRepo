# Tasks

## 1. The retrieval questions, before any line exists

- [x] 1.1 Start the record `docs/<the day it is written> - split-index-written-lines-red-green.md` with eight lookup questions on the TidePool `fat-topics` ARCHITECTURE and eight on this repository's design doc, each naming its one answering part and worded without that part's heading; verify each with a grep that finds the answer in the named part and in no other

## 2. `split_doc.py`: written lines at the apply

- [x] 2.1 The lines file (D5), its refusals (no file, a heading with no line, a heading the doc lacks), D4's two checks, `first_sentence()` deleted, the dry run's closing statement of what a line says and the file's form; verify each refusal exits non-zero on a scratch copy of `fat-topics`, names its cause, and leaves no `ARCHITECTURE/` directory and the doc unchanged
- [x] 2.2 `harness/split-fixture/lines.md`: nineteen written lines for `fat-topics`, each from a read of its part; regenerate `index.expected.md` and `dryrun.expected.txt`; verify the apply with `--today 2026-10-12 --lines harness/split-fixture/lines.md` leaves an index byte-equal to the expected one, the parts reconstruct the doc, the dry run equals the expected text, and the CRLF run passes `eol_check.py`

## 3. `--reindex`, `--check`, and the two scripts that run it

- [x] 3.1 `--reindex` (D6, D7): lines kept by the file token, the heading, file and size refreshed, the review list, the refusals, a lines file setting lines; verify on a scratch split: untouched, the index is byte-identical; a grown part, its size refreshed, its line kept and the part listed with both sizes; a new part, refused and then entered with `--lines`; a renamed identifier, refused naming the part and the term with the index unchanged
- [x] 3.2 `--check` (D8): read-only, one line per finding, exit zero when clean; verify it prints nothing on the fresh split, names each of the five findings after its planted cause, and leaves `git status` of the scratch copy unchanged
- [x] 3.3 `survey.py` and `scope.py` run `--check` in place of their own list comparison; verify that on a scratch project holding the split both print the stale finding with `--reindex` after a part is edited and no remark when it is current, and that the six existing expected outputs under `harness/survey-fixture/` and `harness/scope-fixture/` still match byte for byte
- [x] 3.4 `VERIFICATION.md`'s split paragraph (the lines file, the new cases, `--check`), `ARCHITECTURE.md`'s layout entry (`--check`; `scope.py` runs `split_doc.py`), `harness/README.md` (names `lines.md`); verify every command the paragraph names runs as written

## 4. Backfill: this repository's design doc

- [x] 4.1 Copy the extract index to scratch for the reader reps, then write the fourteen lines in `docs/docs-architecture-design.md`, each from a read of its part; verify `--reindex` exits clean, `--check` reports nothing, and `git diff` shows the Parts entries as the only lines changed, the file's path untouched

## 5. The reps

- [x] 5.1 Catalog cells SD6 (authoring), SD7 (reading), SD8 (reviewing: a part given a topic its line does not name) and SD9 (auditing: a planted line that passes D4 and no longer describes its part) in `harness/catalog-tidepool.md`, each with its scratch recipe and pass line; verify each recipe reproduces from a clean fixture copy
- [x] 5.2 One Workflow at Sonnet/high, every label carrying `[sonnet/high]`: two authoring reps, four reading reps, one reviewing rep, one auditing rep; verify the record holds each rep's verdict against its pass line, the first-pick score per reading cell (a tie stated as a tie) and the token total
- [x] 5.3 On a failed cell only: the T5 clause (SD6), D7's refusal with its scenario added to the setup delta (SD8), the AUDIT rule with its scenario added to the audit delta (SD9); rerun the cell as GREEN; verify the rerun passes and the record says which of the three were needed, or that none was
- [x] 5.4 The reset contract of `VERIFICATION.md` after the mutating reps; verify `git status` shows no fixture residue

## 6. The reference tier and the record

- [x] 6.1 The design doc's tier part: the overflow rule's index line is written, D2 amended (the line is the one place judgment enters a split); then `--reindex` on the design doc and act on its review list for the edited part; verify `--check` reports nothing
- [x] 6.2 `CHANGELOG.md` entry; ROADMAP: the item removed, the Recently-shipped digest kept at five lines, one line queuing the three HDL backfills (rewrite the lines in the index, then `--reindex`) behind the owner's release of `E:\Projects\HDL\Projects\AtmlBoards`; a NOTEBOOK entry for any finding the reps leave; verify ROADMAP stays under its budget
- [x] 6.3 The standing-truth question answered in the ship commit (the line from 6.1, or an explicit "not standing yet"); verify `openspec validate split-index-written-lines --strict` passes

## Workflow follow-up

- Archive with `openspec archive split-index-written-lines --yes`, judged by the output text, never the exit code.
- Fast-forward `main`, run `deploy.sh`, confirm the three scripts in the deployed copies.
- The HDL backfills run from an HDL session once the owner releases the AtmlBoards path.
