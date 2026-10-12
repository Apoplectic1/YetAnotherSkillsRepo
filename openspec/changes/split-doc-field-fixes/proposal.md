# Proposal: split-doc-field-fixes

## Why

The HDL pilot of 2026-10-12 ran `split_doc.py`'s dry run on the Arty's ARCHITECTURE, the
umbrella's DOMAIN, ROADMAP and CHANGELOG, and HlsLibrary's router and class READMEs. The
script and T5 held on the Arty (seven parts, byte-exact, applied the same day) and showed
five gaps elsewhere:

- The citation scan walks into child repositories a B3 rule skips and lists every `§` in
  every Markdown file, so the operator's review list is mostly noise (56 for the umbrella's
  ROADMAP, few of them its own).
- It will dry-run a journal (`CHANGELOG.md`, 22 day headings) into per-day parts, which
  contradicts T1's rollover shape; the script should refuse a journal.
- Parts move byte for byte, so prose saying "this file", "beside this file" or a relative
  path (`../..`) goes stale one directory down; the index alone knows the base.
- A dated heading ("Where the system stands (2026-09-29)") is edited in place, and a part's
  filename derives from the heading.
- The citation count is a lower bound (sibling repositories and `openspec/` archives cite
  the doc too), and citations use short forms ("§ Hardware"), which the grep form finds but
  the note's "heading as written" promises more than it should.

Two T5 edge cases surfaced beside them: a doc that crosses the budget because of a move in
the same SETUP run (the Arty's VERIFICATION at 39.3 KB), and a single `##` part of 49.7 KB
made of bold paragraphs, where T5's "never below `##`" leaves the operator no lever.

## What Changes

- **`split_doc.py`**: refuses a journal (dated `##` headings, the rollover's own detection);
  the citation scan stays inside the repository and skips directories holding their own
  router or `.git`; the dry run lists relative paths and "this file" phrasing inside each
  part for the operator to fix after the apply; a heading with a date in it is warned about
  (the filename follows the heading; the date is an edit-in-place liability); the split note
  says "heading as written or any unambiguous short form of it".
- **SETUP T5**: a doc that crosses the budget because of the run's own moves splits in the
  same run; a single part past the budget is reported and left (the author's `###`
  headings are the lever, never the script's judgment).
- Fixtures: the TidePool `fat-topics` variant gains a journal-shaped decoy, relative paths
  and a dated heading; the expected index updated.

## Capabilities

### Modified Capabilities
- `docs-architecture-setup`: T5's two edge cases; the script's contracts.

## Impact

The umbrella's DOMAIN and ROADMAP splits wait on the relative-path listing; the Arty's
split needed none of it. Script-level checks plus one SETUP plan rep on the amended fixture.
