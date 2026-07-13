# ROADMAP.md — TidePool

**Charter:** forward-looking design + shipped history. Read before starting new work.

## Now / Next
- Station metadata refresh script (`scripts/refresh_stations.py`) — in progress, unblocks
  adding Gulf-coast stations.
- The planner currently ships with 12 curated NOAA stations (`src/tidepool/stations.py`).
- Next: confidence intervals on the window score (design sketch in NOTEBOOK, 2026-06-30
  entry) — surface score uncertainty when sunrise/sunset are near the low.

## Future directions
- Offline tide harmonics: compute predictions locally for cached stations, dropping the
  network dependency for repeat trips.
- iCal export of planned windows (feeds phone calendars; pairs with the CSV exporter).
- Wave/swell overlay: NDBC buoy data as a fourth scoring factor for exposed coastlines.

## Shipped history

### 2026-06-24 — Moon-phase scoring factor
Added `moon_phase_factor` to the planner: spring tides (new/full moon) expose more of the
intertidal zone, so windows near syzygy score higher. Piecewise-linear falloff toward the
quarters, floor at 0.0. 4 new unit tests.

### 2026-06-10 — Export subcommand wired into the CLI
`tidepool export <station> --out windows.csv` — the CSV exporter (shipped 2026-04-18) is now
reachable from the command line instead of only via the API. Argparse sub-parser, path
handling via `pathlib`.

### 2026-05-28 — Sunrise/sunset via astral
Replaced the hand-rolled solar-noon approximation with the `astral` package: `sun_events()`
in `plan.py` returns sunrise/sunset for the station's coordinates, and `moon_phase_days()`
wraps `astral.moon.phase`. Imports are function-local so the test suite stays
dependency-light.

### 2026-05-14 — Newport and The Battery added
Two Atlantic stations added to the curated registry after the Maine/Massachusetts pilot went
well. East-coast tidepooling windows differ enough (semidiurnal range, earlier lows) that
DOMAIN.md gained an East-vs-West note.

### 2026-05-02 — Planner v2: weighted three-factor scoring
Rewrote `score_window`: the v1 model weighted tide height 0.6 and daylight fit 0.4; v2 keeps
those two factors and the same weights while adding the plumbing for a third factor slot.
12 unit tests passing at ship time.

### 2026-04-18 — CSV export
`export_csv()` writes planned windows to disk for spreadsheet users. Seven columns: date,
window start/end, low-tide time, low-tide height, score, and station id. Returns the row
count for CLI reporting.

### 2026-04-05 — Hi/lo predictions client hardened
NOAA CO-OPS client (`tides.py`) gained a 30-second timeout, `raise_for_status`, and MLLW
datum pinning after a silent-failure field report from the Monterey trip. `low_tides()`
filter extracted for the planner.

### 2026-03-30 — Station metadata cache
Station metadata is now cached on disk in `cache.py` with a 24-hour TTL, cutting repeat
lookups from ~800 ms to instant. Cache directory under `~/.tidepool/cache`, one JSON file
per station.

### 2026-03-15 — Initial CLI
First working end-to-end flow: `stations` and `tides` subcommands, curated 8-station Pacific
registry, JSON parsing of the CO-OPS predictions payload. Packaging via `pyproject.toml`
console script.
