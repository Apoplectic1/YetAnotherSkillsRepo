# 2026-07-12 — Decision: shipped history moves to CHANGELOG.md (A2 revised)

**What this is / when to read:** decision record — the user, adjudicating the TP ecological
audit's ~20 deferred ROADMAP-history flags, challenged and superseded the 2026-06-28
"git-is-the-changelog / no CHANGELOG.md" rule. Read before editing SETUP's A2/T1, AUDIT's
R14, or running the next RED→GREEN round. Supersedes the design doc's "Shipped history /
'changelog'" paragraph (the design doc edit is the owner's to make).

## The decision
Shipped history lives in **`CHANGELOG.md`** — a **journal-tier** member: append-only, dated,
newest first, never currency-audited; created when history accrues (conditional, like README).
`ROADMAP.md` keeps only a short "Recently shipped" digest plus a one-line pointer. Unchanged:
`archive/` never holds shipped history (A2's second half survives); git remains the
commit-level backstop.

## Why the 2026-06-28 rule fell
- Its recorded rationale was "redundant with git" — untrue for curated history: TP's dated
  ROADMAP entries carry design summaries, test counts, and rationale far richer than `git log`.
  Git holds the facts; the changelog holds the story. Deleting the tail loses the curation.
- The two standing objections to a new file don't apply: a dated append-only file is exactly
  the "legibly historical" staleness-safe form the anti-staleness principles endorse, and
  `CHANGELOG.md` is the strongest filename-implies-function convention in software — the
  enforced-set philosophy itself.
- The original rule generalized from WBPP, whose port-history was low-value; TP is the
  opposite case. (The user's recollection of the WBPP Phase 1 archive/ move was accurate —
  that precedent was already superseded once, by the rule now superseded again.)
- Tier-model fit is cleaner: NOTEBOOK = findings journal, CHANGELOG = shipped journal,
  docs/ = substantial records. The TP audit's ~20 deferred history flags dissolve *by tier*
  (R14), no bespoke rule needed.

## Candidate skill-text deltas (RED→GREEN required before any of this ships)
- **SETUP** — enforced-set table gains a conditional `CHANGELOG.md` row; **A2 rewritten**:
  "Shipped history lives in `CHANGELOG.md` (journal tier: append-only, dated, newest first);
  `ROADMAP.md` keeps a short Recently-shipped digest + pointer; never a long history embedded
  in ROADMAP; never shipped history in `archive/`." **T1** teaches the three-way journal
  split (finding → NOTEBOOK · shipped unit → CHANGELOG · substantial record → docs/).
- **AUDIT** — **R14** journal list gains `CHANGELOG.md`; new placement rule: a reference doc
  embedding a growing dated history is a structural violation → **one** placement flag,
  `move-to CHANGELOG.md`, and the embedded entries are NOT currency-flagged individually
  (field evidence: the TP ecological audit emitted ~20 per-entry flags the adjudicator
  deferred wholesale; the old audit emitted none and left the structure — both generations
  missed the structural read). Separately, **R21** hardening rides along: "same-model
  cross-worker convergence is agreement, not completeness" (field evidence: the ecological
  orchestrator skipped the model switch on exactly that rationalization).
- **MAINTAIN / whats-next** — no rule changes; bundle notes only (CHANGELOG accrues at ship
  time — it is not a graduation target).

## RED→GREEN plan (round 3, synthetic non-derived fixtures)
1. **AUDIT structural flag:** fixture ROADMAP embedding dated history + planted per-entry
   drift. RED (current hybrid text, 2 reps): expect per-entry currency flags. GREEN (revised
   text, 2 reps): expect one `move-to CHANGELOG.md` structural flag, entries untouched.
2. **SETUP A2′:** fixture with in-ROADMAP history. RED: current text's disposition. GREEN:
   relocation to CHANGELOG.md + digest + pointer, content-preserving.
3. **AUDIT R21:** orchestrator handed a converged single-model result set. RED: does it skip
   the switch? GREEN: switches or explicitly justifies against the hardened clause.

## Also recorded from this walk-through session
- The adjudicator's pushback caught the *orchestrator* (session assistant) offering an
  adjudication menu that omitted the house rule — the approve/amend/defer loop working as
  designed, one level up.
- 20 approved doc fixes were applied to the real TargetPlanner via the bridge (uncommitted,
  git-reviewable): CLAUDE.md ×3, ARCHITECTURE.md ×9, README.md ×4, ROADMAP banner ×1,
  RELEASING.md ×3 (installer name adjudicated as `TargetPlanner-win-Setup.exe`).
- TP ROADMAP history relocation to CHANGELOG.md: pending the user's go (now that relocation,
  not deletion, is the operation).
