# Proposal: three-factor-scoring

## Why
The two-factor model (tide height 0.6, daylight 0.4) ranks neap-tide windows above visibly
better syzygy lows — the model can't see moon phase, so the best minus tides don't sort first.

## What Changes
- Add a moon-phase factor to `score_window`; reweight all three factors.
- No CLI surface change; `plan` output ordering improves silently.

## Impact
- `src/tidepool/plan.py` — new factor + weights; tests updated.
