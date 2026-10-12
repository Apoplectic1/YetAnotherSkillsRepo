# ARCHITECTURE.md — DoseKeeper

**Charter:** scheduler mechanics: dose queue (`src/sched.py`), lockout gate
(`src/lockout.py`) driven by event detection over readings.db.

## Dose log
Every dose is appended to the dose log with its local wall-clock time (`log_dose()` in
`src/doselog.py`), so the log reads in the tank room's own hours.

## Settings
Pump calibration and dose sizes live in `settings.json` at the repo root, loaded once at
start.
