# maintain-right-sizing — proposal

## Why

TSM's 2026-07-26 field feedback (NOTEBOOK same date) measured two MAINTAIN cost problems:
(a) the skill's `description` invites ritual runs — "or as a periodic journal-health sweep"
— and the field consequence was two sweeps in one day with sharply diminishing yield
(~2.4M tokens/6 rounds for 12 one-line claims); (b) the **add:remove ratchet ran 12:1** —
graduate always finds another truth to lift, while prune/archive candidates go unsought
("never an obviously dead one to cut"), so sweeps grow the reference tier they exist to
keep healthy. M9/M14 now stop bloated-target stuffing and AUDIT R28 deletes derivable
trivia, but nothing makes MAINTAIN *look for* the cut side, and nothing shows the user a
run's net growth.

## What Changes

- **Description reworded to trigger conditions** (authoring convention: triggers only):
  drop "or as a periodic journal-health sweep"; add the field-calibrated triggers (~10
  archived changes since the last sweep / a subsystem rewrite / the journal visibly ahead
  of the reference tier). No workflow summary added.
- **MAINTAIN M16 (appended): a REQUIRED prune pass + report accounting.** Every sweep runs
  a dedicated pass over (1) the ROADMAP's open/pending lists for closed items (M4's class,
  made mandatory rather than opportunistic) and (2) the journal for spent records (M3's
  class); the dated report carries a REQUIRED slot: prune/archive candidates found — or
  "none found" stated explicitly — plus a one-line **net reference-tier delta** (what the
  sweep added vs removed). Visibility and a forced search, not a numeric cap (house
  precedent: content tests over thresholds).
- **Gates (iron law, per half):** (a) probe-RED — does an agent under the current
  description recommend/run a sweep in a low-yield situation (sweep 2 h ago, 1 archived
  change since)? (b) planted-cells RED on TidePool (new PR cells: a shipped item still in
  an open list; a spent journal record) — do reps under current text find them while
  graduating? Honest risk: (b) may no-fail on a small fixture (today's reps pruned legibly
  planted items fine; TSM's failure was ratio-at-scale) → status-note for that half, ship
  (a) + the report-slot form only if it independently REDs. TSM is the deriving project —
  poisoned.

## Capabilities

### New Capabilities

*(none)*

### Modified Capabilities

- `docs-architecture-maintain`: trigger-based description (no "periodic" invitation);
  REQUIRED prune pass + report accounting slot (prune candidates or explicit none; net
  reference-tier delta).

## Impact

- `skills/docs-architecture-maintain/SKILL.md` — description rewrite + M16 appended (IDs
  append-only); word delta ≤ ~70.
- `harness/tidepool-fixture/` + catalog — two PR plant cells.
- DOMAIN § When-to-reach already carries the trigger guidance (doc-side, shipped
  2026-07-26); this change moves it into the skill's own trigger surface.
