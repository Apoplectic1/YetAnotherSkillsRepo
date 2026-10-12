# CLAUDE.md — TidePool (router)

**Charter / router.** Plan tidepooling trips around low-tide windows: NOAA CO-OPS
predictions in, scored daylight low-tide windows out. Python 3.11 CLI, `src/` layout.

## Reference docs (current truth — edit in place)
- `ARCHITECTURE.md` — module map + data flow (stations → tides → plan → export).
- `ROADMAP.md` — forward plan + shipped history.
- `DOMAIN.md` — tidepooling domain notes (tides, safety, East-vs-West coast).
- `VERIFICATION.md` — how to verify a change.

## Journal (dated capture)
- `NOTEBOOK.md` — running lab notebook (small findings).
- `docs/YYYY-MM-DD-<slug>.md` — substantial dated records; find by convention
  (glob `docs/*.md` + grep), not an enumerated list.

## Excluded from the doc set
- `openspec/` — opsx planning home (workflow/change artifacts only, not project docs).

## How a plan run moves data (the mechanics, for quick reference)

`tidepool plan <station> --days N` is a single pass. `cli._windows()` looks the station up
in `stations.STATIONS` (a `KeyError` for an unknown id, before any network call), asks
`tides.fetch_predictions(station, "today", f"+{N}")` for the hi/lo rows (one GET against the
datagetter with `product=predictions`, `datum=MLLW`, `units=english`, `time_zone=lst_ldt`,
`interval=hilo`, `format=json`; `raise_for_status`, then the `predictions` key), keeps the
lows with `tides.low_tides` (`type == "L"`, no height cut), and for each low parses `t` with
`%Y-%m-%d %H:%M`, gets sunrise and sunset from `plan.sun_events(day, lat, lon)` (astral,
imported inside the function; the UTC result converted with `.astimezone()` and
`.replace(tzinfo=None)` to the machine's local zone), gets the phase from
`plan.moon_phase_days(day)`, and scores with `plan.score_window(height, low_time, sunrise,
sunset, phase)`: `0.5 * tide_height_factor + 0.3 * daylight_fit_factor + 0.2 *
moon_phase_factor`, where the height factor is 1.0 at or below 0.0 ft falling to 0.0 at
+2.5 ft, the daylight factor is 0.0 outside sunrise to sunset and the smaller margin over
one hour capped at 1.0 inside, and the moon factor is 1.0 at new or full moon falling to 0.0
at the quarters over 7.4 days. Each low becomes a dict with the nine `CSV_COLUMNS` keys
(`date`, `window_start`, `window_end` at plus or minus one hour of the low, `low_tide_time`,
`low_tide_height_ft` as NOAA's string, `score` rounded to three decimals, `station_id`,
`station_name`, `moon_phase_days` rounded to one); the list is sorted by score descending,
stable, so ties keep date order; `plan` prints the rows at or above `--min-score` (0.6 by
default) as `date  low HH:MM  height ft  score`, and `export` writes every row through
`export.export_csv(windows, out_path)` (a `DictWriter` over `CSV_COLUMNS`, `newline=""`,
missing keys as empty cells, extra keys dropped) and reports `wrote N windows to PATH` on
stderr. Nothing is cached: `stations.cache_fresh` and `read_cache` exist for the metadata
refresh script that has not landed, and no code calls them; a second `plan` fetches again.
Errors propagate as their layer's own exception (`KeyError` for the station or the missing
`predictions` key, `requests.HTTPError` for a 4xx or 5xx including the 429 rate limit,
`requests.exceptions.Timeout` after 30 s, `ImportError` for a missing `astral` at `plan` or
`export` time, `OSError` for an unwritable `--out`); `main()` returns 0 on every handled
path and catches nothing.

The two listing subcommands share nothing with the planner. `tidepool stations` iterates
`STATIONS.items()` sorted by the name in the tuple and prints `id  name` per line, eighteen
lines today, offline, which is why VERIFICATION's smoke runs it first on a clean checkout.
`tidepool tides <station> --days N` (default 7) calls `fetch_predictions` with the same
`today`/`+N` range and prints every hi/lo row as `t  type  v ft` in NOAA's order, highs
included; it does not look the station up in the registry, so it is the way to check a
candidate station's datum and hi/lo availability before admitting it. With `--days` past
31 the datagetter's cap returns a 400 and `raise_for_status` raises before anything prints.
The test suite (`tests/test_plan.py`, five tests, `pytest tests/` from the root) imports the
weights, two factors, `score_window` and `CSV_COLUMNS` after inserting `src/` on `sys.path`;
it never imports `requests`, `astral` or the CLI, so it runs with neither dependency
installed and no network. What it pins: the weights sum to 1.0; the height factor saturates
at 0.0 ft and reaches 0.0 at 2.5 ft; the daylight factor is 0.0 before sunrise and 1.0 at
noon; a perfect window scores 1.0; `CSV_COLUMNS` has nine entries.

## Load-bearing gotchas
- The NOAA API is unauthenticated but rate-limited — never loop station fetches without the
  cache check (`stations.cache_fresh`).
- Tide heights are MLLW feet everywhere; never mix datums.
- `astral` imports stay function-local (`plan.py`) so `pytest` runs without it installed.
