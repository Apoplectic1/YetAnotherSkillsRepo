# Proposal: spec-wording-2026-10-12

## Why

The release-close audit of 2026-10-12 (`docs/2026-10-12 - audit-report.md`, flags 12 and 13)
found two spec passages the day's changes had made stale, and a spec changes only through a
change (R13).

## What Changes

- **github-distribution**, modified: the footer requirement and its scenario "Design doc
  stays at its published path" said moving *or splitting* the design doc breaks the footer
  URL; the T5 split of 2026-10-12 left the file in place as the index and the URL held. The
  wording now says a move or a rename breaks it and a split does not.
- **docs-architecture-audit**, modified: the ancestor-router requirement's status note said
  "no R29 was added", meaning the held ancestor-router candidate; R29 has since been taken by
  the scoped-modes rule. The note now names the candidate without the number and says it
  takes the next free number if it ever ships.

## Capabilities

### Modified Capabilities
- `github-distribution`: the split carve-out.
- `docs-architecture-audit`: the status note's wording.

## Impact

Wording only; no skill text, no deploy.
