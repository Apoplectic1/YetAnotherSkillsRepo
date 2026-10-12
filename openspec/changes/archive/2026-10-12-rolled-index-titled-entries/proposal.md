# Proposal: rolled-index-titled-entries

## Why

`journal_index.py` takes a title only from a dated line (`## YYYY-MM-DD title`,
`- YYYY-MM-DD title`). A journal that writes a bare date heading with its entries as bold-lead
bullets beneath it (`## 2026-10-04`, then `- **E24: the P6 addition closed.** ...`) gets one
index line per rolled day, the date alone: EP7314600's `NOTEBOOK/INDEX.md` names none of the
about 30 entries in its two rolled files (43 KB), so a reader greps blind. Found by that
project's maintain sweep (2026-10-12); the owner chose this fix over a hand-written summary
line per rolled file (judgment per rollover, can miss an entry).

## What Changes

- **`journal_index.py`**, modified: under a bare date heading, until the next heading, each
  top-level bullet opening with a bold run is an entry, its bold run the title (truncated at
  `TITLE_MAX` as today), one level under its day. A bold-lead bullet under a *titled* dated
  heading stays body (the HDL notebooks write `- **What:**`, `- **Surprise:**` under
  `## 2026-09-20 JTAG bring-up`; indexing those would be noise). The dated-heading and
  dated-bullet forms render byte-identically.
- **`rollover.py`**: unchanged; it splits by date, not by bullet.
- **MAINTAIN** M17, **SETUP** T1, the design doc's rollover paragraph: the "date and title"
  wording names the bold-lead case.
- **`harness/journal-index-fixture/`**: a rolled file in the bare-date form with its expected
  index; the script-level RED/GREEN for the indexer.

## Capabilities

### Modified Capabilities
- `docs-architecture-maintain`: the index's entry rule gains the bold-lead bullet under a
  bare date heading.

## Impact

Every existing `INDEX.md` line stays as it was: the six HDL rolled directories regenerate
with no entry line removed or changed, and Arty's `CHANGELOG/` (bare date headings over
bold-lead shipped units) gains 33 titled lines. EP7314600 regenerates its index after the
deploy. No back-compat: the pilot's copy under `docs/2026-09-26 - journal-rollover/` stays
the frozen record of what ran there.
