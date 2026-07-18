# Fat-router-lean ground-truth catalog — TidePool fat-router variant

Kept OUTSIDE the fixture tree (poisoned-fixture rule). Supports the `fat-router-lean` opsx
change (SETUP S7 lean rule + AUDIT R26 router-placement clause). Per-run copy:
`scratchpad/tidepool-lean-test` (session-local, disposable). Two tagged states:
- `baseline-lean` — the stock fixture CLAUDE.md (routing + gotchas only, ~1.2 KB): the
  **control** state; no lean action / no placement flag may fire here.
- `fat-variant` — CLAUDE.md with three planted off-charter blocks (below), reference docs
  untouched. Reset contract: `git reset --hard <tag> && git clean -fd` after every mutating
  rep.

## Design intent
The router embeds reference content the tier model says belongs in DOMAIN/ARCHITECTURE —
the shape of TP ecological field finding 1 (2026-07-12). SETUP under current text is
expected to leave it (RED); under S7 it must move each block to its charter home,
content-preserving, and report the moves (GREEN). AUDIT under current text emits no
router-placement flag (RED); under R26 it emits **one structural flag per misplaced block
family** (`move-to`), not per-fact currency flags (GREEN).

## Planted blocks (all in CLAUDE.md, commit tag `fat-variant`)

| ID | Block | Kind | Expected destination | GREEN expectation (SETUP) |
|---|---|---|---|---|
| F1 | `## Glossary & abbreviations` — 7 term defs + CLI short forms | pure reference (domain terms + authoring/CLI conventions) | `DOMAIN.md` | whole block moved intact; router keeps no glossary content |
| F2 | `## NOAA CO-OPS request contract` — endpoint, params, response shape, cache file layout | pure reference (API/module contract prose) | `ARCHITECTURE.md` | whole block moved intact |
| F3 | `## CSV export column contract` — 9-column enumeration + formatting rules **wrapping one bolded load-bearing gotcha** ("column order is load-bearing … never reorder") | **hybrid**: reference body + embedded gotcha | body → `ARCHITECTURE.md`; gotcha line **stays in the router** (Load-bearing gotchas section), pointer allowed | split, not wholesale move; losing the gotcha from the router OR moving nothing both fail |

Must-keep in router (never moved, any rep): the charter line, both routing sections, the
three original `## Load-bearing gotchas` bullets.

## Scoring
- **SETUP RED (current deployed text ×2):** expected — F1–F3 remain in CLAUDE.md (field
  finding 1 reproduces). A rep that spontaneously leans is a RED-failure-to-reproduce data
  point; record, don't discard.
- **SETUP GREEN (S7 candidate ×2):** all three blocks land per table, zero content loss
  (disk-diff the moved text), run summary names each move (what, from → to). F3 split
  correct.
- **SETUP control (×1, `baseline-lean`):** no relocation performed or proposed; no lean
  mentioned in the summary beyond (at most) a "router is lean" observation.
- **AUDIT RED (current text ×1, `fat-variant`):** no placement flag on CLAUDE.md itself.
- **AUDIT GREEN (R26 candidate ×1):** structural `move-to` flag(s) naming F1/F2/F3 blocks
  and charter destinations; F1–F3 facts NOT individually currency-flagged; no flag on the
  routing sections or original gotchas.
- **All reps:** disk-verify claims (grep the tree); agent assertions are not evidence.
