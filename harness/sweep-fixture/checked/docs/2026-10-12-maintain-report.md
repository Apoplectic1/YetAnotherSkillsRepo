# Maintain report, 2026-10-12 (a crafted fixture for `sweep.py --check`)

**Charter:** test content for the check mode: a report that carries everything M13, M14,
M15 and M16 require, with a ROADMAP beside it that carries the lines.

## Graduations
- NOTEBOOK 2026-07-08 (the retry policy) → ARCHITECTURE.md § Requests: **held**, the target
  is past its budget (41.7 KB); disposition on landing: cross-ref.
- NOTEBOOK 2026-07-06 (the regression practice) → VERIFICATION.md: applied; disposition:
  cross-ref.
- ReefDash NOTEBOOK 2026-07-18 (the salinity event): portfolio-level, no portfolio DOMAIN
  exists: **flag-and-ask**, the placement is the owner's.

## Code bugs (report-only)
- flag-code-bug: NOTEBOOK 2026-07-04 says `fetch_predictions` must always carry the 30 s
  timeout; `src/tidepool/tides.py:25` calls `requests.get` without one.

## Accounting
- prune candidates: one prune-only (the ROADMAP export line, struck); archive candidates:
  none found.
- net reference-tier delta: +1 VERIFICATION bullet, +2 ROADMAP open lines, -1 ROADMAP line.
- watermark: NOTEBOOK/2026-03-27.md.
