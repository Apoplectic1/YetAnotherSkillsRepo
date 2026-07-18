# fat-router-lean — design

## Context

Field finding 1 of the 2026-07-12 TP ecological run: both skill generations left a 24 KB
router's glossary/contract weight in place, and AUDIT never placement-flagged the router
itself. The SETUP enforced-set table *says* "kept thin" but no rule compels a move on
encounter; AUDIT's R25 covers embedded shipped-history in ROADMAP but nothing covers
reference content embedded in CLAUDE.md. Backlog shape refined in NOTEBOOK 2026-07-13;
scope decisions confirmed by the user 2026-07-17 (lean-rule-only change; perform, not
propose; content-test trigger).

## Goals / Non-Goals

**Goals:**
- SETUP performs a content-preserving lean of an encountered fat router (delta spec:
  "Router lean on encounter").
- AUDIT placement-audits the router itself (delta spec: "Router is placement-audited").
- Both rule texts pass RED→GREEN on a non-derived fixture before any deploy.

**Non-Goals:**
- B4 portfolio-DOMAIN amendment (separate item; starts with the Astronomy container probe).
- AUDIT scaled-coverage mode (field "R26"; independently gated, batches only at deploy time
  if both happen to be GREEN together).
- No numeric size threshold anywhere in normative text.
- No MAINTAIN / whats-next changes.

## Decisions

- **D1 — content test over size threshold.** Trigger = "is this passage reference content
  (glossary, contract prose, conventions, mechanics) vs routing / load-bearing gotcha?" The
  ~40 KB perf line appears only as italic rationale. *Alternative rejected:* numeric
  trip-wire — misses small off-charter blocks, false-positives on legitimately gotcha-dense
  routers, and invites threshold-gaming.
- **D2 — perform, not propose.** SETUP executes the move in-run under existing safety rails:
  S1 (content-preserving move), S2 (clean tree + diff presented before commit). The diff
  review *is* the approval gate, so a separate propose step is a redundant round-trip.
  *Alternative rejected:* flag-only — leaves the known gap in place and contradicts how every
  other SETUP restructure (e.g. A2 history relocation) already behaves.
- **D3 — rule placement in SETUP.** New rule lands in the enforced-set section as **S7**
  (adjacent to the "kept thin" table wording it enforces), with the CLAUDE.md table row
  gaining a cross-ref ("kept thin — S7"). Procedure step 2 already says "create/align";
  step 3 stays unchanged. *Alternative considered:* a Boundaries B-rule — but this is
  set-shaping, not scope; S-family keeps discovery adjacent to the table.
- **D4 — rule placement in AUDIT.** One clause as **R26** under Rules, worded parallel to
  R25 (one structural flag, `move-to`, not per-passage currency flags). Note: the NOTEBOOK
  "field R26" label for scaled-coverage is an informal alias, not a claimed number — first
  shipped rule takes the real R26 slot; NOTEBOOK entry for this change notes the alias
  collision so the later item renumbers.
- **D5 — destination selection is charter-driven, named by example.** Rule text gives two
  canonical examples (glossary / CLI-abbreviation conventions → DOMAIN.md; mechanics →
  ARCHITECTURE.md) and defers the general case to the charters. Avoids an exhaustive mapping
  table that would itself be off-charter weight in the skill.
- **D6 — verification per VERIFICATION.md.** Fixture = `harness/tidepool-fixture` copy plus
  a **fat-router variant** (inject a glossary + contract block into the fixture's CLAUDE.md;
  catalog the planted block in `harness/catalog-tidepool.md` or a sibling catalog). Not
  poisoned: the rule derives from the TP ecological run, not TidePool. Reps: SETUP RED 2
  (unguided/current text leaves the fat in place) → GREEN 2 (candidate text moves it,
  content-preserving) + **1 lean-router control** (must NOT trigger; guards the cry-wolf
  scenario). AUDIT narrow probe: RED 1 (no placement flag today) → GREEN 1 (flag emitted,
  structural not per-passage) + control shares the SETUP control fixture. Budget
  ~450–500k subagent tokens. Gate: this item has an ecological failure on record, so the
  standard RED-must-reproduce rule applies (unlike no-failure preference gates).

## Risks / Trade-offs

- [Cry-wolf on gotcha-dense routers] → content test names routing + gotchas as protected
  classes; explicit "regardless of size" in both rule texts; control rep must pass clean.
- [Lean destroys router discoverability] → moves leave the router's pointer intact (router
  still routes to the doc that received the content); S1 forbids loss; S2 diff review.
- [Judgment calls on hybrid passages (gotcha wrapped in contract prose)] → rule instructs
  splitting: gotcha line stays, reference body moves with a pointer; GREEN reps check the
  fixture's planted hybrid block.
- [Fixture reset discipline] → per VERIFICATION.md, `git reset --hard <marker> && git clean
  -fd` after every mutating rep — mandatory, harness copies are disposable.
- [R-number collision with the scaled-coverage backlog label] → D4 NOTEBOOK note; no shipped
  text ever cited "R26" (the revert removed it), so the slot is genuinely free.

## Migration Plan

None — skills are stateless text; consumers see the new rules on next deploy. Deploy only
from `main` via `deploy.sh` after merge (RELEASING.md). No back-compat text (user rule #15).

## Open Questions

- None blocking. Post-GREEN wording polish (superpowers:writing-skills review) happens at
  implementation, inside this change's tasks.
