# journal-rollover: design

## Context

The journal tier is append-only and legibly historical, and the family's answer to its growth
was M3: judged, per-entry archival into `archive/`. Two things the HDL tree showed (ROADMAP,
"Journal rollover and the overflow directory"): the reference tier cites journal entries by
date from other repositories, so moving an entry by judgment breaks pointers nobody re-checks;
and at 10 KB a day a journal outgrows a worker's slice in weeks. The owner chose the
mechanical alternative: roll closed periods out by date, never by judgment, into a directory
named for the file, and index it. The pilot ran on seven journals; this change codifies what
held.

## Goals / Non-Goals

**Goals:** a journal never exceeds one read unit (the budget) in its live file; every rolled
entry stays byte-identical, dated, citable and indexed; the four skills agree on the
directory; the scripts ship with the skill so any project uses them the same way.

**Non-Goals:**
- Splitting a bloated *reference* doc by topic (the overflow rule's other half): unpiloted,
  queued as "The split job's owner". M14 keeps naming the split; this change does not shape it.
- A numeric bloat test for reference docs (M9 stays a content test; the always-on budget item
  revisits the number question for routers).
- Changing what MAINTAIN graduates or how AUDIT judges currency.

## Decisions

- **D1: rollover by date, never by judgment.** A rolled file holds a date range and whatever
  was written in it. Sorting entries by status needs judgment per entry and drifts; a date
  range needs none and never drifts. Open threads are the one exception, and they are carried
  forward rather than sorted (D4).
- **D2: the directory is named for the file, beside it.** `NOTEBOOK/` beside `NOTEBOOK.md`,
  `CHANGELOG/` beside `CHANGELOG.md`. Discoverable without a router line; stays clear of
  `docs/` and its dated-prefix rule and of `archive/` (judged spent records, M3). The live
  file keeps its name, since every router, charter and skill names it.
- **D3: the trigger is size, the unit is a whole day, the name is the first date.** A
  calendar month on a busy tree is 300 KB, the same problem one level down; the budget (40 KB
  by default, about 10k tokens, the harness's per-file warning) is a read unit and a worker's
  slice. Whole days keep together so a date names exactly one file. The live file is cut to
  half the budget so it does not roll again the next day. A dated citation resolves by
  `grep -n "<date>" NOTEBOOK.md NOTEBOOK/*.md`, so no pointer anywhere changes (the pilot
  rewrote none across six repositories).
- **D4: open threads never roll out unannounced.** The dry run lists the entries about to
  roll; the operator carries each still-open item into the live file's "Open threads (carried
  at a rollover)" section as one line naming the rolled file, then applies. `whats-next` reads
  the live file only, so a carried thread is found and an uncarried one is the operator's
  error, visible in the dry run, not a silent loss.
- **D5: rolled files are frozen; the M11 treatment.** Nothing edits a rolled file: a graduate
  from one takes `cross-ref` written in the reference doc, or `stub` (the entry left as the
  evidence), never M6's in-place pointer and never M7. Two consequences: the index never goes
  stale (regenerated over frozen files, every existing line stays), and a sweep can record the
  newest rolled file it covered as a watermark, so the next sweep reads the live file and
  newer rollovers only. M3's archive disposition narrows to dated `docs/` records, where an
  entry is a file of its own and moving it keeps its name.
- **D6: two entry forms.** `## YYYY-MM-DD ...` headings (column-0 bullets inside an entry
  belong to it) and top-level `- YYYY-MM-DD` / `- **YYYY-MM-DD**` bullets (indented lines
  belong to the bullet); the form is read from which occurs, the order (newest first or last)
  from the dates. The fixture's own NOTEBOOK is a newest-first bullet list, which is what made
  the second form a requirement. Anything else refuses, naming both forms: a journal with
  undated entries is a SETUP finding, not a rollover input.
- **D7: the scripts ship with the skill.** `rollover.py` and `journal_index.py` sit beside
  the maintain SKILL.md, deployed with it and copied with `skills/*/` for other harnesses.
  The skill text names them by relative position and states the contract (D3 to D6) so a
  reader without the script still knows what a correct rollover is. The pilot's copies under
  `docs/2026-09-26 - journal-rollover/` stay as the record of what ran on 2026-09-26.
- **D8: a container root's ignore file names its repositories.** Found on the pilot's first
  step: an umbrella that ignored `/*/` with three exceptions would have dropped `NOTEBOOK/`
  without a word, and a kit copied from what is committed would have shipped without it. The
  owner's rule: a directory created in a repository is in git; only the directories that hold
  repositories are ignored, by name, each reason on its own line (git reads a comment only on
  a line of its own; a trailing one makes the pattern literal). SETUP writes such a file for a
  container root and flags a wildcard on encounter as an S1-class safety item.
- **D9: the dated-record pattern is the project's stated convention.** The family's
  `YYYY-MM-DD-<slug>.md` collides with an owner's global naming rule (`YYYY-MM-DD - name`);
  B2's normalization becomes "to the pattern the router's journal line states", default the
  hyphen form. One clause; RED on a prompt-only probe.
- **D10: RED/GREEN shape.** Non-derived fixtures only. MAINTAIN: two on-disk reps on
  TidePool plus the `big-journal` variant (80 KB, newest-first bullets; plants RO1 an open
  thread never closed, RO2 an open thread closed by a later entry, RO3 a dated citation from
  ARCHITECTURE into an old entry), RED with the current text, GREEN with the candidate text
  and the scripts' path; scored on disk (byte-exact concatenation, files under budget, the
  index, RO1 carried, RO2 not, RO3 resolving, the reference docs unedited by any rolled-file
  disposition). SETUP: a prompt-only probe on reefstack with a `/*/` ignore file (D8) and one
  on a router stating the spaced pattern (D9). AUDIT and whats-next: prompt-only probes on a
  rolled file with stale values and a rolled file with a closed open item. No-failure on a
  probe: status note, no text.

## Risks / Trade-offs

- [A rollover breaks a citation that is not a date] The pilot found none in six repositories,
  and the note in every live header says how a dated citation resolves. A line-anchored
  pointer (`NOTEBOOK.md:412`) would break; the pilot grepped for them first (none), and the
  skill text says to.
- [The operator skips the open-thread scan] The dry run prints the roll list before anything
  moves, the GREEN cell RO1 tests the carry, and `whats-next` reading the live file only makes
  a missed carry visible as a lost item rather than a hidden one. Accepted: judgment stays
  with the operator, by design, since it is the one judged step.
- [A journal in neither form] Refuse, naming both. Cost: a SETUP job to give the journal
  dated entries, which the convention already required.
- [Two copies of the scripts] The skill's copies are the product and evolve; the record's
  copies are frozen with the pilot. Named in both READMEs.

## Migration Plan

None (no back-compat by policy). Ships dev, RED/GREEN, main, `deploy.sh`. Consumers with a
journal past the budget roll it at their next maintain sweep or sooner; the HDL tree's seven
journals are already rolled by the pilot's scripts, whose output the skill's scripts reproduce
byte for byte (replay-verified 2026-09-26).

## Open Questions

None blocking. Final wording after RED classification, per house method.
