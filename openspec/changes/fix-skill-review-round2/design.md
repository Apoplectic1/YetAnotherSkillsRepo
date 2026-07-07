# Design — fix-skill-review-round2

## Context

Five behavioral candidates from the 2026-07-07 family review (design doc, "Family review
2026-07-07 — round 2"). Method follows the 2026-07-06/07 behavioral fix batch: RED-test each
gap with the *current* skill text before encoding anything (Iron Law), candidate-text
injection (test agents get SKILL.md text inline — the live Skill tool only sees
deployed/main), Sonnet workers, 2 reps per scenario per phase, disk-verify every claim,
match-the-form-to-the-failure (a prohibition only if the failure is commission; a structural
line if omission), and the **no-failure gate** (baseline passes → no text added; the spec
requirement gets a status note — the disk-verify-gate precedent).

## Goals / Non-Goals

**Goals:** encode only what demonstrably fails; keep SETUP/AUDIT/whats-next word counts near
current (compress if additions land); bank RED/GREEN records in the design doc per item.

**Non-Goals:** no re-validation of already-GREEN behavior (sub-project redirect, DESIGN slot);
no README/portability work (that's the publish-to-GitHub pre-item in ROADMAP); no MAINTAIN
changes (nothing behavioral was found).

## Decisions

**D1 — Fixtures are synthetic, built per item.** A real-world project copy is NOT required:
these five failure modes are *structural* (presence/absence of a file, a `.git`, content
shape), which small synthetic fixtures represent exactly — the 2026-07-06/07 batch already
validated the design-heavy case on a synthetic fixture. Real copies earn their keep only when
the failure depends on *organic mess* (naturally accumulated drift, scale, tangled history) a
synthetic build under-represents — none of these five does. Two standing rules apply
regardless: never use a spec-containing project (WBPP, this repo — the poisoned-fixture
lesson), and give every fixture a `SKILLS-TEST BASELINE` marker + reset per `VERIFICATION.md`.

**D2 — Item 3 (container root) accepts the live session as its RED.** The failure was
observed in production 2026-07-07 with current skill text (full set scaffolded at a portfolio
root; user judged it noise, kept router-only). No synthetic RED needed; build the fixture for
GREEN only.

**D3 — Failure definitions, per item.**
| # | Item | Fixture | RED failure = |
|---|---|---|---|
| 1 | legacy domain doc | git project: router + ARCHITECTURE/ROADMAP + `OBSERVING.md` (real domain content), no `DOMAIN.md` | run creates `DOMAIN.md` *beside* `OBSERVING.md` (two domain homes), or leaves no `DOMAIN.md` |
| 2 | non-git target | same shape, `.git` removed, docs messy enough to restructure | run restructures/merges files with **no recovery net** (no git-init offer, no snapshot) and no mention of the risk |
| 3 | container root | dir with 2 sub-projects (own `.git`+router each) + `.claude/`, no first-party content | *(live RED banked)* — full enforced set scaffolded at the container level |
| 4 | audit-first scope | freshly-SETUP project (docs demonstrably current) + visible backlog sources | whats-next run insists on / performs an audit before triage despite fresh docs, or brands its output untrustworthy without one |
| 5 | small-set sizing | 5–6 thin charter'd docs, ~10-file code base, 2 planted drifts | audit run spins up a fan-out grossly disproportionate to volume (e.g. per-section workers ≫ sections, multi-model rounds after round 1 is dry) instead of adapting |

**D4 — Encode targets (only on RED failure).** Item 1 → SETUP Procedure step 2 (one
sentence: legacy-named domain doc is renamed/merged into `DOMAIN.md`, content-preserving) +
design-doc §"Domain-doc name fixed" alignment. Item 2 → SETUP Safety (non-git branch). Item
3 → SETUP, either the Procedure or the sub-project section (container case: router-only).
Item 4 → whats-next "When to use" + Common-mistakes bullet rewording. Item 5 → AUDIT step 1
(one scale sentence).

**D5 — Expected splits.** Item 1's RED may show agents merge naturally (like the sub-project
no-touch RED) — then only the *ambiguity* needs a line, or nothing ships. Item 5 is the most
likely full no-failure (loop-until-dry already self-terminates); its requirement would then
carry a disk-verify-style status note.

## Risks / Trade-offs

- [Fixture too easy → false GREEN] → item 1's fixture gives `OBSERVING.md` real, chartered
  domain content (not a stub), so "create a fresh thin DOMAIN.md" is genuinely tempting.
- [Item 4 verdict subjectivity] → define the observable: does the run *proceed to a backlog*
  and note doc freshness, or *block/perform an audit*? Judge only that.
- [Word-count creep on SETUP] → three candidate additions target one skill; if all three
  fail RED, compress Safety/Procedure while encoding (the 2026-07-07 REFACTOR precedent).

## Open Questions

- Item 5 threshold: is "workers > major sections" the right disproportion test, or should the
  verdict simply be "did round 2 launch after a dry round 1"?
- Item 2: if RED shows agents *mention* the risk but proceed anyway, does that count as
  failure? (Lean yes — the net must exist, not be waved at.)
