# Maintain report, 2026-10-12 (a crafted fixture for `sweep.py --check`)

**Charter:** test content for the check mode: a report that omits the accounting slot and
whose ROADMAP carries none of the required lines.

## Graduations
- NOTEBOOK 2026-07-08 (the retry policy) → ARCHITECTURE.md: **held**, the target is past
  its budget.
- NOTEBOOK 2026-07-06 (the regression practice) → VERIFICATION.md: applied.

## Code bugs (report-only)
- flag-code-bug: `src/tidepool/tides.py:25` calls `requests.get` without the 30 s timeout
  the NOTEBOOK 2026-07-04 contract requires.

Done.
