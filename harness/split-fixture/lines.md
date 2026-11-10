# Written lines for the TidePool `fat-topics` ARCHITECTURE (split_doc.py --lines)

## Module map (`src/tidepool/`)
The five modules and what each owns: `stations.py` (registry, `CACHE_TTL_HOURS = 6` and why), `tides.py`, `plan.py` (the three weights 0.5, 0.3, 0.2), `export.py` (nine columns), `cli.py` (four subcommands); the pipeline order with no back edges.

## Station registry and the metadata cache (`stations.py`)
The `STATIONS` dict (an id mapped to `(name, lat, lon)`, Pacific then Atlantic, admitted by checklist), `get_station` raising `KeyError`, the cache helpers `cache_path`, `cache_fresh` (age by file mtime against the 6-hour TTL) and `read_cache`, and the missing write side with its consequences.

## The CO-OPS client (`tides.py`)
`fetch_predictions` and its fixed datagetter parameters (`MLLW`, `english`, `lst_ldt`, `hilo`) with the reason for each, `API_URL`, how an HTTP error or a 200 without `predictions` fails, `low_tides` (no height cut), the 31-day cap, and no retry or caching.

## Window scoring (`plan.py`)
The score formula and its weight constants, each factor's arithmetic (`tide_height_factor` saturating at `GOOD_TIDE_FT`, `daylight_fit_factor`'s one-hour margins, `moon_phase_factor`'s 7.4-day triangle), the astral wrappers `sun_events` and `moon_phase_days`, and the UTC-to-local conversion.

## CSV export (`export.py`)
`CSV_COLUMNS` (the nine names in order), `export_csv` writing with `newline=""` and `DictWriter` (missing keys empty, extra keys dropped), the row values taken unformatted from `_windows()`, and the `--out` path: relative to the working directory, overwritten without asking.

## The CLI (`cli.py`)
`main` and the four subcommands with their arguments, defaults and output formats (`stations`, `tides`, `plan`, `export`), `_windows` as the driver where the modules meet (lookup, fetch, score, the nine-key dict, sort by score), and the errors it lets propagate.

## Time, zones and the day boundary
The three kinds of time value (station-local `t` strings, astral's UTC, naive local), why stations outside the machine's zone score off by the offset, the datagetter's day boundary and a window straddling midnight, daylight-saving days, and rounding after the sort.

## Errors and exit paths
Every exception a run can end with and its layer: `KeyError` for an unknown station or a 200 error body, `requests.HTTPError` (429, the 31-day 400), `JSONDecodeError`, `Timeout`, `ImportError` for astral, `OSError` on `--out`, `ValueError` from `strptime`; exit status and stdout versus stderr.

## Testing and the pure core
`tests/test_plan.py`: what its five tests pin (the weights' sum, height saturation, two daylight points, the perfect window, the nine columns), what the suite cannot tell (client, wrappers, CLI, the daylight ramp), how to add a test, and which functions are pure.

## Packaging, configuration and paths
`pyproject.toml` (version `0.6.0` stated twice and unchecked, `requires-python`, two dependencies, the console script), configuration by module constants only with no environment variables or config file, every path the package touches, and how to install and release.

## Requests and the network budget
HTTP requests per subcommand, why looping `plan` over the registry draws a 429, the size and timing of a run (the NOAA round trip, astral's first import), what the metadata cache will and will not save, and the decided retry policy not yet in `fetch_predictions`.

## The window dict: nine keys and their contract
The table of the nine keys with their types and values, why the height stays NOAA's string, the `T` separator in the three time strings, the sort and its tie order, why the dict is not a class, and the CSV as its only outside contract.

## Worked scoring examples
Four windows through `score_window` with the factor arithmetic written out (a perfect window, a marginal dawn low, a minus tide before dawn, a +2.5 ft low at noon), the score bands they imply, and why no single factor clears the 0.6 default.

## The `stations` subcommand and the registry listing
What `tidepool stations` prints (alphabetical by station name, two spaces between id and name, no header or coordinates), why it is the first smoke check, and why an id must match exactly with no name lookup.

## Adding a station: what changes where
The one-line change to `STATIONS` (an id key, a `(name, lat, lon)` tuple, geographic order), the curation checklist applied first (MLLW, hi/lo lows, coordinates, shore access), and the checks after the line goes in.

## The `tides` subcommand and the raw listing
What `tidepool tides` prints (every high and low in NOAA's order), that it skips the registry so any CO-OPS id works, its use for vetting a candidate station and for telling a threshold effect from an empty response, and the 31-day cap.

## Public names and their callers
A table of every public name with the module defining it and its callers, the names with no caller yet (`cache_fresh`, `read_cache`), and the dependency graph it implies (`cli` on all four modules, `plan` and `export` importing neither `requests` nor `astral` at module level).

## State (2026-07-10)
Version 0.6.0 as the current release, the dates the export subcommand and the moon-phase factor shipped, the refresh script in progress, and where the shipped history and the archived rationale live.

## Data flow and invariants
The pipeline diagram from station id to table or CSV, and the invariants that hold across modules: MLLW feet everywhere, a pure core, one writer of files, lows not pre-filtered, rounding only in `_windows()`, the weights' rationale.
