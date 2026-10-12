# Proposal: reference-doc-split

## Why

M9 and M14 hold a promotion whose target is bloated "until the split, setup/audit territory",
and no skill describes the split: the HDL maintain sweep of 2026-09-26 held ten promotions
against three docs past 40 KB, the ATML umbrella's report naming the job nobody owns. The
Arty's ARCHITECTURE is 70.4 KB in seven `##` topics (Board app 24 KB, Hardware 14,
Transactions 10, Build chain 8, three small ones), each a real reference section; a session
that needs the build chain reads 18k tokens for it, or must know to grep the headings first.
The journal already has the mechanical half of this answer (rollover by date into a directory
named for the file); this is the other half: a reference doc past its budget splits by topic
into a directory named for it, the parent left as the index.

## What Changes

- **SETUP**, modified: a new rule beside T2. A reference doc past the budget (40 KB, the
  read unit) whose weight is many topics splits by `##` heading into `<DOC>/`, one charter'd
  file per topic, bodies byte for byte; the parent stays as the index (preamble, a split
  note, one line per part) and the router keeps naming the parent only; a heading keeps its
  text so "DOC § heading" resolves by grep over the file and the directory. A doc bloated by
  cold rationale extracts instead (T3, R11); a design doc in a code-light project stays
  whole (B5); a single topic past the budget stays one part. `split_doc.py` beside the
  SKILL.md does it (dry run lists the parts and every section citation it finds; `--apply`
  writes and byte-checks).
- **MAINTAIN**, modified: M9 and M14 name the shape (the script, the part the held
  promotion lands in).
- **AUDIT**, modified: R12's in-scope set reaches a split doc's parts through its index; the
  cross-reference pass resolves a section citation in the file or the directory.
- **The design doc**: the tier section's overflow rule gains its second half.
- **Fixtures**: TidePool `fat-topics` (a 45 KB ARCHITECTURE of six true-to-code mechanics
  topics); the existing `fat-arch` variant as the control (rationale bloat: extract, never
  split); `harness/split-fixture/` for the script's byte-exact check.

## Capabilities

### Modified Capabilities
- `docs-architecture-setup`: the reference-doc split.
- `docs-architecture-maintain`: M9 and M14 name the split's shape.
- `docs-architecture-audit`: a split doc's parts in scope; section citations resolve.

## Impact

No consumer changes until a split runs. The Arty pilot (the dry run from here is the
derivation evidence; the apply is consumer work from an HDL session after the ship) is queued
with the always-on pilot. The TSM precedent (an ARCH split into a SUBSYSTEMS doc beside the
specs, "two homes for one truth") is the shape this rule avoids: a part is the same section,
in the same tier, under the same charter, in a file of its own.
