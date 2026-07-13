# ARCHITECTURE.md — TidePool

**Charter:** module mechanics and data flow. How the system works today.

## Module map (`src/tidepool/`)
- `stations.py` — curated station registry (`STATIONS` dict) + on-disk metadata cache
  (`CACHE_TTL_HOURS = 6`, one JSON file per station under `~/.tidepool/cache`).
- `tides.py` — NOAA CO-OPS client: hi/lo predictions, MLLW datum, english units, 30 s
  timeout; `low_tides()` filters the lows for the planner.
- `plan.py` — window scoring: three weighted factors (tide height 0.5, daylight fit 0.3,
  moon phase 0.2); `sun_events()` / `moon_phase_days()` wrap `astral` with function-local
  imports.
- `export.py` — CSV writer, nine columns (`CSV_COLUMNS`), returns row count.
- `cli.py` — argparse entry point; four subcommands: `stations`, `tides`, `plan`, `export`.

## Data flow
station id → `tides.fetch_predictions` (network, cached metadata) → `low_tides` →
per-low `plan.score_window` (needs `sun_events` + `moon_phase_days`) → ranked windows →
terminal table or `export.export_csv`.

## Design constraints
- Pure-math core: everything in `plan.py` except the astral wrappers is deterministic and
  unit-testable with no network or dependency footprint.
- The CLI never writes anywhere except an explicit `--out` path and the cache directory.
