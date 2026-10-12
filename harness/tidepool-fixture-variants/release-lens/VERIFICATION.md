# VERIFICATION.md — TidePool

**Charter:** how to verify a change.

Verification = `pytest tests/` from the repo root (pure math, no network, no `astral`
needed). CLI smoke: `python -m tidepool.cli stations` (offline) and
`python -m tidepool.cli tides 9414290 --days 2` (hits the live NOAA API — needs network).
Until the `export` subcommand lands, CSV output is verified from a REPL:
`export.export_csv(windows, Path("windows.csv"))` and a row count check.
