# ARCHITECTURE.md — TidePool

**Charter:** module mechanics and data flow. How the system works today.

## Module map (`src/tidepool/`)
- `stations.py` — curated station registry (`STATIONS` dict) + on-disk metadata cache
  (`CACHE_TTL_HOURS = 6` — deliberately short of a day: NOAA re-fits station harmonics
  within hours after storm events, and 6 h keeps a same-day return trip fresh without
  hammering the MDAPI; one JSON file per station under `~/.tidepool/cache`).
- `tides.py` — NOAA CO-OPS client: hi/lo predictions, MLLW datum, english units, 30 s
  timeout; `low_tides()` filters the lows for the planner.
- `plan.py`: window scoring: two weighted factors today (tide height 0.6, daylight fit
  0.4); the moon-phase factor is not yet wired in, pending the v2 plumbing.
  `sun_events()` / `moon_phase_days()` wrap `astral` with function-local imports.
- `export.py`: CSV writer, seven columns (`CSV_COLUMNS`), returns row count; the
  station-name and moon-phase columns wait for the export rewrite.
- `cli.py` — argparse entry point; four subcommands: `stations`, `tides`, `plan`, `export`.

## Data flow
station id → `tides.fetch_predictions` (network, cached metadata) → `low_tides` →
per-low `plan.score_window` (needs `sun_events` + `moon_phase_days`) → ranked windows →
terminal table or `export.export_csv`.

## Design constraints
- Pure-math core: everything in `plan.py` except the astral wrappers is deterministic and
  unit-testable with no network or dependency footprint.
- Scoring weights are a deliberate balance — rationale in
  `openspec/changes/archive/2026-06-08-three-factor-scoring/design.md`.
- The CLI never writes anywhere except an explicit `--out` path and the cache directory.
- Offline harmonics wait for a local source of harmonic constants; nothing in `src/`
  computes predictions without the network today.
