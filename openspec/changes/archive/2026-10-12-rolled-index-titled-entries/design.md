# rolled-index-titled-entries: design

## Context

The index exists so a reader finds a rolled entry without opening the rolled files. Its
entry detection was written for the two journal forms the rollover accepts, and for those the
dated line carries the title. A third habit, a bare date heading over bold-lead bullets, is a
heading journal to the rollover (it splits by `## YYYY-MM-DD`) and so rolls correctly, but the
index then shows only the dates.

## Decisions

- **D1: the bold run is the title, as written.** The author chose the bold run as the lead;
  the index repeats it, truncated at `TITLE_MAX` like a dated bullet's text. No summary, no
  judgment: regenerating the index at the next rollover reproduces every line.
- **D2: only under a bare date heading.** The first cut indexed bold-lead bullets under any
  dated heading; regenerating the six HDL indexes showed it: under `## 2026-09-20 JTAG
  bring-up` the notebooks write `- **What:**`, `- **Surprise:**`, `- **Toolchain gotcha:**`,
  structure of the entry, not entries (Arty's NOTEBOOK would have gained 90 such lines). A
  bare date heading (nothing after the date) is the signal that the entries are below it. A
  titled dated sub-heading (`### 2026-10-02 afternoon: ...`) is itself the entry, so bullets
  under it are body too.
- **D3: the state resets at any heading.** Bold-lead bullets count from a bare date heading
  until the next heading of any level, so an `## Open threads` section's bold bullets stay
  out, and a day's `###` sub-heading closes the day's bullet list.
- **D4: nesting by the heading's level.** A bold-lead entry sits one level under its heading
  (`## day` gives `  - title`); the renderer indents two spaces per level, which renders the
  existing level-2 and level-3 lines exactly as before.
- **D5: the span still comes from dated lines only.** A bold-lead entry carries no date; the
  file's "from X to Y" and the "no dated entries" refusal read the dated lines, as today.
- **D6: `rollover.py` untouched.** Its detection counts `## YYYY-MM-DD` lines and bullets
  only decide the form when no such headings exist; a dry run on the fixture in live form
  reports the heading form with three dated entries and passes its byte-for-byte assertion.

## Verification

Script-level, no subagent run: RED is today's script on `harness/journal-index-fixture/`
(three date-only lines), GREEN the new script's output byte-matching `INDEX.expected.md`;
the regression is the old and the new script on copies of the six HDL rolled directories
(five identical in every entry line, Arty's `CHANGELOG/` gaining 33 lines and losing none).
The MAINTAIN skill text changes by one parenthesis in M17, so no on-disk rep.
