# Proposal: audit-scoped-modes

## Why

Two ROADMAP items, one mechanism. **Release-close currency lens** (2026-09-26): after a
milestone the reference tier goes stale in predictable phrases ("waits for", "not yet",
"until", "today", "currently", a version, a count). The HDL maintain sweep's best worker was
one such lens over the reference tier, 188k tokens for 13 corrections, against about 2.6M for
the full sweep; the class is AUDIT's currency pass, not graduation, and nothing in the family
offers it cheaply. **AUDIT scaled-coverage mode** (2026-07-17, gated): a one-round mode for a
small, low-drift doc set, its shape refined the same day (one per-section round plus the
cross-reference pass, pinned to the R22 tier, no loop, no model switch, the coverage note
announcing the mode) and held for a RED. Both are sanctioned exceptions to loop-until-dry
(R18, R20, R21), a user-set cost tradeoff rather than an empirical ceiling, and they need the
same companion edits: R18's exception clause, Procedure step 3's branch, the design doc's
coverage mandate given a dated addendum. The owner chose (2026-10-12) to ship them as one
change, two named modes.

## What Changes

- **AUDIT**, modified: a new rule (the next free number) names two **scoped modes**, each
  invoked by the user by name, never chosen by the run: `release-close` (one lens over the
  reference tier for post-release phrasing, plus the R19 cross-reference pass) and
  `small-set` (one per-section round plus the cross-reference pass, for a small and low-drift
  set). Both run one round at the R22 default tier, no loop, no model switch; the coverage
  note names the mode and what a full run would add. R18 gains the sanctioned-exception
  clause; Procedure step 3 branches on the mode. The full loop stays the default.
- **DOMAIN § When to reach**: AUDIT's line names the release-close mode as the shift-left
  for currency, triggered at a release close, never scheduled.
- **The design doc**: the coverage section's unconditional loop gets a dated addendum.
- **`harness/tidepool-fixture-variants/release-lens/`**: post-release phrasings planted in
  the reference tier (cells RL1 to RL6, controls RC1 to RC3 in `harness/catalog-tidepool.md`).

## Capabilities

### Modified Capabilities
- `docs-architecture-audit`: scoped modes as a sanctioned exception to loop-until-dry.

## Impact

Nothing changes for a run invoked without a mode. The "field R26" alias the scaled-coverage
item carried is retired with the item. A release close gains a named, cheap check whose
report says what it did not do.
