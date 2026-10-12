# ARCHITECTURE.md — TidePool

**Charter:** module mechanics and data flow. How the system works today, topic by topic:
the station registry and its cache, the CO-OPS client, window scoring, the CSV exporter, the
CLI, and the invariants that hold across them. Design rationale lives in the archived
OpenSpec designs (`openspec/changes/archive/*/design.md`); this file says what the code does.

## Module map (`src/tidepool/`)
- `stations.py` — curated station registry (`STATIONS` dict) + on-disk metadata cache
  (`CACHE_TTL_HOURS = 6` — deliberately short of a day: NOAA re-fits station harmonics
  within hours after storm events, and 6 h keeps a same-day return trip fresh without
  hammering the MDAPI; one JSON file per station under `~/.tidepool/cache`).
- `tides.py` — NOAA CO-OPS client: hi/lo predictions, MLLW datum, english units, 30 s
  timeout; `low_tides()` filters the lows for the planner.
- `plan.py` — window scoring: three weighted factors (tide height 0.5, daylight fit 0.3,
  moon phase 0.2); `sun_events()` / `moon_phase_days()` wrap `astral` with function-local
  imports.
- `export.py` — CSV writer, nine columns (`CSV_COLUMNS`), returns row count.
- `cli.py` — argparse entry point; four subcommands: `stations`, `tides`, `plan`, `export`.

The modules form a straight pipeline with no back edges: the registry answers "where", the
client answers "when", the scorer answers "how good", the exporter and the CLI answer "show
me". Each topic below describes one of them in the order the data flows (see § Data flow and
invariants for the whole path and the rules that hold across modules).

## Station registry and the metadata cache (`stations.py`)

The registry is the `STATIONS` dict: a station id string mapped to a `(name, lat, lon)`
tuple. Ids are the CO-OPS datagetter form (seven digits, no leading zero); names are the
NOAA station names with their state; coordinates are decimal degrees, west negative. The
dict is hand-curated and ordered geographically: fourteen Pacific stations from San Francisco
(`9414290`) south to La Jolla and north through Monterey, Point Reyes, Arena Cove, Humboldt
Bay, Port Orford, South Beach, Garibaldi, La Push, Neah Bay and Seattle, then four Atlantic
stations added after the Maine and Massachusetts pilot: Portland ME (`8418150`), Boston,
Newport RI and The Battery NY. Admission is by the curation checklist (tidal station, MLLW
available, public shore access within a short walk of the gauge), never by an API sync; the
archived station-curation design records the decision and the reasons.

`get_station(station_id)` returns the tuple or raises `KeyError` for an unknown id. The CLI
calls it first in `_windows()` so an unknown station fails before any network call; the
error text is the bare id, which the CLI prints as the traceback (a friendlier message is a
ROADMAP item, not a mechanism). Nothing else in the package reads `STATIONS` directly except
the `stations` subcommand, which sorts the dict by name for display (see § The CLI).

The metadata cache holds the MDAPI's station record (datums, time zone, the harmonic refit
date) as one JSON file per station under `CACHE_DIR`, which is `~/.tidepool/cache`
(`Path.home() / ".tidepool" / "cache"`). Three helpers implement the read side:

- `cache_path(station_id)` returns `CACHE_DIR / f"{station_id}.json"`; it never creates the
  directory.
- `cache_fresh(station_id)` returns `False` when the file does not exist, otherwise compares
  the file's `st_mtime` age in hours against `CACHE_TTL_HOURS` (6) and returns whether the
  age is under it. The age is wall-clock since the last write, not since the record's own
  refit date: a record written at 09:00 is stale at 15:00 whatever NOAA did in between,
  which is the behavior the short TTL is for.
- `read_cache(station_id)` parses the file with `json.loads` and returns the dict; it does
  not check freshness, so callers call `cache_fresh` first.

The write side is not in the package today: no function fetches the MDAPI record or writes
the file, and nothing calls `cache_fresh` or `read_cache`. The helpers are the read-side
contract the refresh script (ROADMAP, in progress) will write against; until it lands, the
cache directory is empty and the client (see § The CO-OPS client) fetches predictions with
no metadata at all, taking the station's coordinates from the registry tuple. The router's
gotcha ("never loop station fetches without the cache check") is the rule for that script,
stated ahead of it so the first draft honors it.

Two consequences follow for the rest of the system. The time zone used for sunrise and
sunset is the machine's, not the station's, because the station's zone lives in the
metadata record the cache would hold (see § Window scoring for the conversion and its
limit). And the registry's coordinates are the only station facts the planner can rely on,
so a station admitted without accurate coordinates mis-places every sunrise by minutes per
tenth of a degree; the checklist's coordinate check exists for this.

## The CO-OPS client (`tides.py`)

One function talks to NOAA: `fetch_predictions(station_id, begin_date, end_date)`. It
builds the datagetter request from a fixed parameter dict and returns the `predictions`
list of the JSON response, each item a dict with `t` (the local time string,
`YYYY-MM-DD HH:MM`), `v` (the height in feet as a string) and `type` (`H` or `L`). The
parameters, all literal except the three arguments:

| Parameter | Value | Why |
|---|---|---|
| `product` | `predictions` | the hi/lo prediction product, not observed water levels |
| `application` | `tidepool` | NOAA asks clients to identify themselves |
| `station` | the id | the datagetter form, seven digits |
| `begin_date`, `end_date` | the arguments | the CLI passes `today` and `+N` (see § The CLI) |
| `datum` | `MLLW` | every height in the system is MLLW feet (router gotcha) |
| `units` | `english` | feet, matching `GOOD_TIDE_FT` and the DOMAIN thresholds |
| `time_zone` | `lst_ldt` | station-local time with daylight saving applied |
| `interval` | `hilo` | only the highs and lows, which is all the planner uses |
| `format` | `json` | the parser is `resp.json()` |

`API_URL` is the production datagetter endpoint
(`https://api.tidesandcurrents.noaa.gov/api/prod/datagetter`). The call is
`requests.get(API_URL, params=params)` followed by `resp.raise_for_status()`, so an HTTP
error status raises `requests.HTTPError` before parsing; the 30 s timeout bounds the wait
on a server that accepts the connection and never answers (the Monterey failure mode the
hardening pass closed). The function then indexes `resp.json()["predictions"]`, so a 200
response without that key (the datagetter's error shape) raises `KeyError` at the index;
the CLI lets it propagate.

`low_tides(predictions)` is a list comprehension keeping the items whose `type == "L"`. It
does no height filtering: every low in the range comes through, including lows well above
the planner's useful band, and the scorer's height factor is what pushes those down (see
§ Window scoring); the La Push field report's request for a height cut in `low_tides()`
itself is the ROADMAP's known bug. The function takes the raw list and returns a new list;
it never mutates the response.

Range semantics belong to the caller. The CLI always asks for `today` as the begin and
`+days` as the end, which the datagetter reads as a relative range from the station's local
midnight; the hi/lo product caps one request at 31 days, so a `--days` past that returns
an error status and `raise_for_status` raises. Nothing in the client retries, backs off or
caches a response: a plan that runs twice fetches twice, and the rate limit NOAA applies per
source address is the reason the router warns against looping station fetches.

## Window scoring (`plan.py`)

A candidate window is the hour either side of a low tide. Its score is a weighted sum of
three factors, each in `[0, 1]`:

```
score = 0.5 * tide_height_factor(height_ft)
      + 0.3 * daylight_fit_factor(low_time, sunrise, sunset)
      + 0.2 * moon_phase_factor(phase_days)
```

The weights are the module constants `WEIGHT_TIDE_HEIGHT`, `WEIGHT_DAYLIGHT_FIT` and
`WEIGHT_MOON_PHASE`; they sum to 1.0 so a perfect window scores 1.0 and the CLI's default
`--min-score` of 0.6 reads as a fraction of perfect. Their balance is a design decision with
its rationale in the archived three-factor-scoring design; this section says only what each
factor computes.

**Tide height.** `tide_height_factor(height_ft)` returns 1.0 at or below `GOOD_TIDE_FT`
(0.0 ft MLLW: the DOMAIN's "good window" line) and falls linearly to 0.0 at +2.5 ft:
`max(0.0, 1.0 - height_ft / 2.5)`. A minus tide (below 0.0) earns no extra credit; the
factor saturates, which is why the DOMAIN calls a minus tide "exceptional" without the
scorer preferring it. The +2.5 ft zero is the point past which a low is not a tidepooling low
on any curated coast; it is a constant, not a per-station value, which is the limit the
Gulf-coast rejection (dated record, 2026-05-20) ran into.

**Daylight fit.** `daylight_fit_factor(low_time, sunrise, sunset)` returns 0.0 when the low
falls outside `[sunrise, sunset]`, otherwise the smaller of the two margins (low to sunrise,
sunset to low) divided by one hour and capped at 1.0. A low one hour or more inside daylight
scores 1.0; a low ten minutes after sunrise scores one sixth. The test is on the low's
instant, not on the window's ends; the DOMAIN's "never plan a window that ends after sunset"
is enforced by the factor's zero outside daylight and the min-score gate together, not by a
check on `window_end`, and the two are not the same thing when a low sits inside the last
hour before sunset (an open point the field reports have not yet raised).

**Moon phase.** `moon_phase_factor(phase_days)` takes the phase in days since new moon on
a 29.53-day cycle, measures the distance to the nearest syzygy (new at 0 or 29.53, full at
14.77), and returns `max(0.0, 1.0 - nearest / 7.4)`: 1.0 at new or full moon, 0.0 at the
quarters (7.4 days away). The 7.4-day falloff makes the factor a triangle wave, which is a
crude model of the spring-neap cycle that the archived design accepted over a cosine for
being obviously right at the four anchor points.

**The astral wrappers.** `sun_events(day, lat, lon)` builds an `astral.LocationInfo` from
the coordinates, calls `astral.sun.sun(loc.observer, date=day)` and returns the
`sunrise` and `sunset` entries, which are timezone-aware UTC datetimes. `moon_phase_days(day)`
returns `astral.moon.phase(day)`. Both import `astral` inside the function body, so
`import tidepool.plan` succeeds without `astral` installed and the pure-math tests run
dependency-free (router gotcha). The caller converts the UTC datetimes with
`.astimezone().replace(tzinfo=None)`, which lands them in the machine's local zone as naive
values comparable to the naive `t` strings the client returns in station-local time; for a
station in the machine's zone the two agree, and for a station elsewhere they differ by the
zone offset, the limit § Station registry and the metadata cache notes.

`score_window(height_ft, low_time, sunrise, sunset, phase_days)` is the only function the
CLI calls; it is pure, deterministic, and the thing the test suite pins.

## CSV export (`export.py`)

`CSV_COLUMNS` fixes nine column names and their order: `date`, `window_start`,
`window_end`, `low_tide_time`, `low_tide_height_ft`, `score`, `station_id`, `station_name`,
`moon_phase_days`. `export_csv(windows, out_path)` opens the path for writing with
`newline=""` (so `csv` controls the line terminator and Windows does not double it), writes a
header row from `CSV_COLUMNS`, then one row per window with `{k: w.get(k, "") for k in
CSV_COLUMNS}`: a window dict missing a column writes an empty cell, and a window dict with
extra keys drops them silently, because `DictWriter` writes only the listed fieldnames. The
function returns `len(windows)` for the CLI's count message and never prints.

The row values are whatever `_windows()` built (see § The CLI): the date as ISO, the three
times as ISO to the minute, the height as the string NOAA returned, the score rounded to
three decimals, the phase rounded to one. The exporter does no formatting of its own, which
keeps the terminal table and the CSV in agreement; a column that needs a different
rendering is changed in `_windows()`, and `CSV_COLUMNS` gains the key in the same change
or the column never appears.

The path is the caller's: a relative `--out` resolves against the process's working
directory, not the repository, and the exporter overwrites an existing file without asking.
Nothing else is written anywhere; the design constraint in § Data flow and invariants is
enforced by there being no other `open(..., "w")` in the package.

## The CLI (`cli.py`)

`main(argv=None)` builds an `argparse` parser with `prog="tidepool"` and a required
subcommand, parses `argv` (the real `sys.argv` when `None`), dispatches, and returns 0; the
module's `__main__` block calls `sys.exit(main())`. Four subcommands:

- `stations` lists the registry, one line per station, `id  name`, sorted by name. Offline.
- `tides <station_id> [--days N]` (default 7) prints every hi/lo prediction in the range as
  `t  type  v ft`, straight from the client. Needs the network.
- `plan <station_id> [--days N] [--min-score S]` (defaults 14 and 0.6) prints the ranked
  windows whose score is at or above the threshold: `date  low HH:MM  height ft  score`.
- `export <station_id> [--days N] [--out PATH]` (defaults 14 and `windows.csv`, a
  `pathlib.Path`) writes every window (no threshold) and prints `wrote N windows to PATH`
  on stderr.

`_windows(station_id, days)` is the planner's driver and the one place the modules meet.
It looks the station up (`stations.get_station`, which raises for an unknown id before any
request), fetches predictions for `today` to `+days`, and for each low from
`tides.low_tides`: parses `t` with `"%Y-%m-%d %H:%M"`; gets sunrise and sunset for that date
and the station's coordinates, converted to naive local as § Window scoring describes; gets
the moon phase for the date; scores the window; and appends a dict with the nine
`CSV_COLUMNS` keys, the window running from one hour before the low to one hour after
(`isoformat(timespec="minutes")`), the score rounded to three decimals, the phase to one.
The list is returned sorted by score descending; Python's sort is stable, so equal scores
keep the fetch order, which is date order. `plan` filters by `--min-score` after the sort;
`export` takes the whole list.

Errors propagate: an unknown station raises `KeyError`, an HTTP error raises
`requests.HTTPError`, a response without `predictions` raises `KeyError`, and `astral`
missing at `plan` or `export` time raises `ImportError` from inside the wrapper. The CLI
catches none of them, by design: the tracebacks name the layer, and a wrapper that turned
them into messages would hide which layer failed. Exit status is 0 on every handled path.

## Time, zones and the day boundary

Every time value in the system is one of three kinds, and the mechanics depend on keeping
them apart. The client's `t` strings are station-local wall-clock time with daylight saving
applied (`time_zone=lst_ldt`), formatted `YYYY-MM-DD HH:MM` with no zone marker; `_windows()`
parses them with `datetime.strptime(low["t"], "%Y-%m-%d %H:%M")` into naive datetimes. The
astral wrappers return timezone-aware UTC datetimes; `_windows()` converts each with
`.astimezone()` (to the machine's local zone) and then `.replace(tzinfo=None)` (to naive).
The scorer compares the two naive values directly in `daylight_fit_factor`, so the comparison
is exact when the machine's zone is the station's and off by the zone difference otherwise.
For the curated registry that means a planner run on the West Coast scores Pacific stations
exactly and Atlantic stations three hours early: a Boston low at 09:00 Eastern is compared
against a sunrise expressed in Pacific time, which reads as 06:00-ish, and the daylight
margin is overstated by the offset. The fix needs the station's zone, which is in the MDAPI
metadata record the cache will hold (see § Station registry and the metadata cache); until
the refresh script lands, the limit stands and is documented here rather than hidden.

The day boundary is the datagetter's. A `begin_date` of `today` means the station's local
midnight today, and `+N` means N days from it, so a run late in the evening on the West
Coast asks an Atlantic station for a range that started three hours earlier in that
station's day; the lows returned are complete for the station's days, and the planner never
splits a window across the boundary because a window is defined around one low (the hour
either side), never across two. A low at 23:50 gives a window ending at 00:50 the next day,
and `window_end` carries the next day's date in its ISO string; the `date` column stays the
low's date. The CSV column pair (`date`, `window_end`) is how a reader sees the straddle.

Daylight saving changes inside a range are the datagetter's to handle, and it does: the
`lst_ldt` times step with the change, so a low at 01:30 on the spring-forward day appears
with its post-change clock time. The astral conversion follows the machine's rules, so on
the change day the two clocks can disagree by an hour for the hour around the change; the
planner does not special-case it. A window's duration is always two hours of wall-clock
arithmetic on the naive low time (`timedelta(hours=1)` each side), so a window across the
change is two clock hours, not two elapsed hours; no consumer has cared yet.

`moon_phase_days(day)` takes a `date`, not a datetime, and returns the phase at that
calendar day; the phase moves about 0.9 days per day, so the time of day within the low's
date changes the factor by at most a few hundredths. The scorer rounds nothing; the CLI
rounds the phase to one decimal for display and export and the score to three, after the
sort, so two windows whose scores differ in the fourth decimal keep their true order and
print as a tie. There is no tie-break rule beyond the stable sort's date order.

## Errors and exit paths

The package raises its layers' own exceptions and catches none of them; the CLI's
`main()` returns 0 on every path it handles and lets everything else propagate as a
traceback. The complete set, by layer, and what a reader of the traceback learns:

- `KeyError: '<station id>'` from `stations.get_station`: the id is not in the registry.
  Raised before any network call because `_windows()` looks the station up first. The
  `tides` subcommand does not look the station up, so an unknown id there reaches NOAA and
  comes back as the datagetter's error shape (next item).
- `KeyError: 'predictions'` from `tides.fetch_predictions`: the datagetter answered 200
  with an error body (`{"error": {"message": ...}}`), which it does for an unknown station, an
  unavailable datum, or a malformed date. `raise_for_status` passes on a 200; the index on
  `predictions` is what fails. The message text, which names the cause, is in the body the
  client discarded; reproducing the request by hand is the way to read it.
- `requests.HTTPError` from `raise_for_status`: a 4xx or 5xx. A 429 is the rate limit
  (per source address; wait and retry by hand, the client does not); a 500-class is NOAA's.
  A range past the hi/lo product's 31-day cap is a 400 with an HTML body, which raises here
  before any JSON parsing.
- `requests.exceptions.JSONDecodeError` from `resp.json()`: a 200 whose body is not JSON,
  which NOAA serves for some malformed requests as an HTML page. Rare; the parameters are
  fixed and only the dates vary.
- `requests.exceptions.Timeout` after 30 s: the server accepted the connection and did not
  answer in time. This is the one the hardening pass added; before it the process hung.
- `ImportError: No module named 'astral'` from inside `sun_events` or `moon_phase_days`: the
  dependency is missing at `plan` or `export` time. `stations` and `tides` never import it,
  and the test suite never imports it, which is the reason the imports are function-local.
- `OSError` (typically `PermissionError` or `FileNotFoundError` for a missing parent
  directory) from `export_csv`'s `open(out_path, "w")`: the `--out` path is not writable.
  The exporter creates no directories.
- `ValueError` from `strptime`: a `t` string not in `YYYY-MM-DD HH:MM`. Never seen from the
  hi/lo product; a client switched to another product (the six-minute predictions carry
  seconds) would raise here.

The exit status is 0 when `main()` returns and the interpreter's 1 on an uncaught exception.
`export` prints its count to stderr so a shell pipeline reading the CSV from stdout is not
polluted; the other subcommands print to stdout. No subcommand reads stdin, no subcommand
takes a configuration file, and there is no `--verbose` or logging: the tracebacks are the
diagnostics, and § Testing and the pure core says what the offline checks can tell before a
network call is made.

## Testing and the pure core

`tests/test_plan.py` is the whole suite: five tests, pure math, run with `pytest tests/`
from the repository root. The file inserts `src/` at the front of `sys.path` so the package
imports without installation, then imports `CSV_COLUMNS` from the exporter and the three
weights plus `daylight_fit_factor`, `score_window` and `tide_height_factor` from the scorer.
Nothing in it imports `requests`, `astral` or the CLI, so the suite runs on a machine with
neither dependency installed and with no network, which is the property the router's
function-local-import gotcha protects.

What the five tests pin:

- The three weights sum to 1.0 exactly. A weight change that breaks the sum fails here
  before any score is wrong by a scale factor.
- `tide_height_factor` saturates: 1.0 at -1.2 ft and at 0.0 ft, 0.0 at 2.5 ft. The zero
  point and the saturation point are the two constants the DOMAIN's thresholds depend on.
- `daylight_fit_factor` is 0.0 for a low an hour before a 06:00 sunrise and 1.0 for a low at
  noon between 06:00 and 20:00. The ramp between them is untested; a change to the one-hour
  margin would pass.
- A perfect window scores 1.0: a -0.5 ft low at noon on a new moon (`phase_days=0.0`).
  This is the regression anchor for the whole formula; any factor or weight change that
  moves a perfect window off 1.0 fails here.
- `CSV_COLUMNS` has nine entries. A column added to `_windows()` without the list, or
  removed from the list, fails here; the names and order are not pinned.

What the suite cannot tell: anything about the client (no network in tests), the astral
wrappers (not imported), the CLI's argument parsing and dispatch (not imported), the
exporter's file writing (only the column count is checked), and the moon-phase factor's
shape (not imported, though `score_window` calls it with 0.0). The CLI smoke in
VERIFICATION covers the first and the third against the live service. Adding a test follows
the file's shape: import from `tidepool.<module>` after the path insert, construct naive
datetimes by hand, assert on the pure function; a test that needs `astral` or the network
does not belong in this file and there is no second file for it yet (the scoring-regression
practice the notebook records as decided is not yet in VERIFICATION).

`score_window` is pure in the strict sense: five scalar arguments, one float, no reads of
module state beyond the constants, no I/O. `tide_height_factor`, `daylight_fit_factor` and
`moon_phase_factor` are pure likewise. The two wrappers are the only impure functions in
`plan.py`, and they are impure only in depending on `astral`'s ephemeris; given a date and
coordinates they are deterministic too, which is why a recorded sunrise could stand in for
them in a future offline CLI test.

## Packaging, configuration and paths

`pyproject.toml` declares the project: name `tidepool`, version `0.6.0`, a one-line
description, `requires-python = ">=3.11"`, and two dependencies, `requests>=2.31` and
`astral>=3.2`. The console script `tidepool = "tidepool.cli:main"` installs the command;
`python -m tidepool.cli` runs the same entry point without installation, which is how
VERIFICATION's smoke commands invoke it. The layout is `src/tidepool/` with five modules and
an `__init__.py` carrying `__version__ = "0.6.0"`; the version is stated twice and nothing
checks that the two agree. There is no lock file, no build backend pinned beyond the
default, and no optional dependency groups: `astral` is required for `plan` and `export`
even though the test suite does not need it.

Configuration is by constants, not files. The scorer's weights and thresholds are module
constants in `plan.py`; the cache TTL and directory are constants in `stations.py`; the
datagetter parameters are a literal dict in `tides.py`; the subcommand defaults (`--days` 7
or 14, `--min-score` 0.6, `--out windows.csv`) are argparse defaults in `cli.py`. No
environment variable is read anywhere, no `config.toml` or `.tidepoolrc` exists, and the
only user-specific path is the cache directory, `Path.home() / ".tidepool" / "cache"`,
resolved at import time of `stations.py` from the home directory of the process's user.
Changing any of these is a code change and a release, which is deliberate for a tool whose
numbers encode safety rules (see DOMAIN) rather than preferences.

Paths the package touches, in full: the cache directory (read by the helpers, written by
nothing yet); the `--out` path of `export`, relative paths resolving against the process's
working directory; and nothing else. It does not write a log, a history, a lock, or a
temporary file. The CO-OPS endpoint is the one `API_URL` constant; the MDAPI endpoint the
refresh script will use is not yet named in the package.

Installation for development is `pip install -e .` from the repository root (it pulls both
dependencies) or, for the offline path the tests use, no installation at all: `pytest tests/`
works from a bare checkout with `pytest` importable, because the test file adds `src/` to
the path itself. A release is a version bump in both places and a tag; there is no
RELEASING.md because nothing is published to an index.

## Requests and the network budget

Each subcommand makes a fixed number of HTTP requests: `stations` none, `tides` one,
`plan` one, `export` one. There is no per-station metadata request today (the cache's write
side is pending) and no second prediction request for a range under the 31-day cap. A
planning session that runs `plan` for three stations makes three requests; a script that
loops `plan` over the registry's eighteen stations makes eighteen in quick succession, which
is the pattern the router's gotcha forbids without a cache check, because NOAA's limit is per
source address and a burst of that size has drawn a 429 on a shared network.

The request is small (a GET with nine query parameters) and the response for a 14-day hilo
range is about 4 KB of JSON, two to four hi/lo rows per day; parsing is immediate. The cost
of a run is dominated by the round trip to NOAA, typically 300 to 800 ms, and by `astral`'s
first import, which loads its ephemeris tables once per process (about 200 ms); a `plan` run
is well under two seconds cold on a laptop and the second run in the same process would be
faster, but each CLI invocation is its own process, so every run is cold. The metadata
cache, when its writer lands, removes the one request that would otherwise be repeated per
station per run (the MDAPI record), not the prediction request, which is always live:
predictions for a future range cannot be cached usefully because the planner asks for "from
today".

Timeouts and retries: one 30 s timeout per request, no retries. The notebook records a
decided resilience policy (one retry with a 2 s backoff on a 5xx, never on a 4xx) that is not
yet in the client; until it is, a transient 5xx ends the run with the traceback and the user
runs it again. The policy, when implemented, belongs in `fetch_predictions` and nowhere
else, since it is the only network call.

## The window dict: nine keys and their contract

`_windows()` builds one dict per low, and that dict is the unit everything downstream
consumes: the terminal table reads four of its keys, the exporter writes all nine in
`CSV_COLUMNS` order. The keys, their Python types at construction, and what each means:

| Key | Type | Value |
|---|---|---|
| `date` | `str` | the low's calendar date, `date.isoformat()`, `YYYY-MM-DD` |
| `window_start` | `str` | the low time minus one hour, `isoformat(timespec="minutes")` |
| `window_end` | `str` | the low time plus one hour, same format; may carry the next date |
| `low_tide_time` | `str` | the low time itself, same format, `YYYY-MM-DDTHH:MM` |
| `low_tide_height_ft` | `str` | NOAA's `v` as received, a decimal string in feet, unconverted |
| `score` | `float` | `round(score_window(...), 3)` |
| `station_id` | `str` | the registry id, as given on the command line |
| `station_name` | `str` | the registry name, with state |
| `moon_phase_days` | `float` | `round(phase, 1)`, days since new moon on astral's scale |

Three details carry weight. The height stays a string: `float(low["v"])` is computed for
the scorer and discarded, and the dict keeps NOAA's text, so the CSV shows exactly what NOAA
sent (including a trailing zero NOAA may or may not include) and a reader comparing against
the NOAA site sees the same digits. The three time strings use the `T` separator of
`isoformat`, which spreadsheets parse as a datetime, while `date` has none; a consumer that
wants the low's time of day takes `low_tide_time[-5:]`, which is what the `plan` table does.
And the dict is built with exactly the nine keys, in `CSV_COLUMNS` order, by construction:
there is no later enrichment, so a reader of the CSV has the full record.

The sort key is `score` descending over the list; ties keep fetch order, which is date
order ascending, because Python's `sorted` is stable. A consumer that re-sorts by date gets
the planner's own order back for the ties. The dict is not a class on purpose: it is what
`csv.DictWriter` and `print` consume with no adapter, and a dataclass would add a conversion
in both directions for no reader.

The dict's only contract outside the package is the CSV; a change to a key's name, type or
rounding is a change to every spreadsheet built on an exported file, so a key is added or
changed by a change whose proposal names the CSV consumers (the station-selection record
lists the two known ones).

## Worked scoring examples

Four windows through `score_window`, with the factor arithmetic written out so a reader
can check a change against them (sunrise 06:00 and sunset 20:00 unless stated, weights
0.5, 0.3, 0.2):

**A perfect window** (the test suite's anchor): a -0.5 ft low at 12:00, new moon
(`phase_days` 0.0). Height: -0.5 is at or below 0.0, factor 1.0, contributes 0.5. Daylight:
the low is six hours inside each edge, the margin ratio caps at 1.0, contributes 0.3. Moon:
distance to new is 0.0, factor 1.0, contributes 0.2. Score 1.0; printed by `plan` at any
threshold.

**A marginal dawn low**: a +1.0 ft low at 07:00 with sunrise at 06:30, first quarter
(`phase_days` 7.4). Height: `1.0 - 1.0 / 2.5` = 0.6, contributes 0.30. Daylight: the smaller
margin is 30 minutes, ratio 0.5, contributes 0.15. Moon: distance to new is 7.4, distance to
full is `|7.4 - 14.77|` = 7.37, nearest 7.37, factor `1.0 - 7.37 / 7.4` = 0.004,
contributes 0.0008. Score 0.4508, rounded 0.451; below the 0.6 default, so `plan` omits it
and `export` writes it.

**A minus tide before dawn**: a -1.5 ft low at 05:30, full moon (`phase_days` 14.77).
Height: saturated, 0.5. Daylight: the low precedes sunrise, factor 0.0, contributes 0.0.
Moon: distance to full is 0.0, factor 1.0, contributes 0.2. Score 0.7; above the default
threshold, so `plan` prints it although the window runs 04:30 to 06:30, half of it before
sunrise. This is the case § Window scoring notes: the daylight factor is a weighted term,
not a gate, and the DOMAIN's "never plan a window that ends after sunset" (or before
sunrise) is only approximately enforced by the threshold. A reader who wants the gate raises
`--min-score` above 0.7, which also drops every daytime window with a poor height.

**A high low at noon**: a +2.5 ft low at 12:00, new moon. Height: `1.0 - 2.5 / 2.5` = 0.0,
contributes 0.0. Daylight: 0.3. Moon: 0.2. Score 0.5; omitted by `plan`. Above +2.5 ft the
height factor is clamped at 0.0 by `max`, so a +4 ft low scores the same 0.5: the planner
does not distinguish bad lows from very bad ones, which is the reason the ROADMAP's known
bug asks for a height cut in `low_tides()` so they do not reach the table at all.

Two properties the examples show. The maximum score for a window outside daylight is 0.7
(height and moon saturated), and the minimum for a daytime window at a good height is 0.8
(moon at a quarter); the two bands overlap between 0.7 and 0.8 only when a daytime window
has a poor height and a good moon, which is the region where the default threshold's
behavior is least intuitive. And no single factor can carry a window over the default
threshold alone: 0.5 is the largest contribution, so a printed window always has at least
two factors partly satisfied.

## The `stations` subcommand and the registry listing

`tidepool stations` is the one offline subcommand. It iterates `stations.STATIONS.items()`
sorted by the name in the tuple (`key=lambda kv: kv[1][0]`), so the listing is
alphabetical by station name, not by id or by coast: "Arena Cove, CA" first, "The Battery,
NY" last. Each line is `f"{sid}  {name}"`, two spaces between, no header, no coordinates;
the coordinates are in the registry for the planner and not shown because a user chooses by
name. The listing is eighteen lines today and grows by one per admitted station.

The subcommand makes no network call and imports nothing beyond the registry, so it is the
first thing VERIFICATION's smoke runs: a clean checkout that prints eighteen lines has a
working package, a working console script and a readable registry. It returns 0. A station
id a user then passes to `plan` must match the first column exactly; there is no name
lookup, no prefix match and no fuzzy search, which keeps the id the single key through the
whole pipeline (registry, request, window dict, CSV).

## Adding a station: what changes where

Admitting a station is a code change in one place and a checklist in the dated record. The
code change is one line in `STATIONS`: the datagetter id as a seven-digit string key, and a
`(name, lat, lon)` tuple with the NOAA station name and state and decimal-degree
coordinates to three places. The line goes in the registry's geographic order (Pacific
south to north, then Atlantic), which nothing enforces but which keeps a diff readable.

The checklist the curation design records, applied before the line is added: the station is
a tidal station with an MLLW datum (a request with `datum=MLLW` returns predictions, not the
error shape); the hi/lo product returns lows for it (a subordinate station without `v`
values is excluded); the coordinates place sunrise and sunset within a minute of the
station's published times; and there is public shore access near the gauge, which is the
domain judgment and the reason the registry is curated by hand rather than synced. A Gulf
Coast station fails on the scorer's height model, not on the checklist (the dated record).

After the line: `tidepool stations` shows nineteen lines; `tidepool plan <id> --days 3`
prints or omits windows without raising; the CSV from `export` has nine columns with the new
name in the eighth. No test changes, because the suite does not pin the registry's size or
contents; the ROADMAP's station count line is the one doc that goes stale, which is why it
is better written without the number.

## The `tides` subcommand and the raw listing

`tidepool tides <station_id> [--days N]` (default 7) is the client with no planner behind
it: it calls `fetch_predictions(station_id, "today", f"+{days}")` and prints every
prediction in the range as `f"{p['t']}  {p['type']}  {p['v']} ft"`, highs and lows alike, in
the order NOAA returns them, which is chronological. It does not look the station up in the
registry, so it works for any CO-OPS station id, curated or not, and it is the way to check
a candidate station's datum and hi/lo availability before adding it (see § Adding a station:
what changes where): an unknown or non-tidal id surfaces as the datagetter's error shape
(`KeyError: 'predictions'`, see § Errors and exit paths) rather than as a registry miss.

The listing is the only place the highs appear anywhere in the system; the planner discards
them in `low_tides` and never prints them. It is also the quickest check that a `plan` run
that printed nothing is a threshold effect and not an empty response: `tides` for the same
range shows the lows the planner scored below `--min-score`. The subcommand returns 0 and
prints to stdout; with `--days` past 31 the datagetter's cap returns a 400 and
`raise_for_status` raises before anything prints.

## Public names and their callers

Every public name in the package, where it is defined and who calls it; a name with no
caller is noted, since those are the ones a reader is most likely to misjudge as live.

| Name | Defined in | Called by |
|---|---|---|
| `STATIONS` | `stations.py` | `get_station`; `cli.main` (the `stations` listing) |
| `CACHE_TTL_HOURS`, `CACHE_DIR` | `stations.py` | `cache_fresh`, `cache_path` |
| `get_station` | `stations.py` | `cli._windows` |
| `cache_path` | `stations.py` | `cache_fresh`, `read_cache` |
| `cache_fresh`, `read_cache` | `stations.py` | nothing yet (the refresh script's contract) |
| `API_URL` | `tides.py` | `fetch_predictions` |
| `fetch_predictions` | `tides.py` | `cli._windows`; `cli.main` (the `tides` listing) |
| `low_tides` | `tides.py` | `cli._windows` |
| `WEIGHT_TIDE_HEIGHT`, `WEIGHT_DAYLIGHT_FIT`, `WEIGHT_MOON_PHASE` | `plan.py` | `score_window`; the test suite |
| `GOOD_TIDE_FT` | `plan.py` | `tide_height_factor` |
| `tide_height_factor`, `daylight_fit_factor`, `moon_phase_factor` | `plan.py` | `score_window`; the first two by the test suite |
| `score_window` | `plan.py` | `cli._windows`; the test suite |
| `sun_events`, `moon_phase_days` | `plan.py` | `cli._windows` |
| `CSV_COLUMNS` | `export.py` | `export_csv`; the test suite |
| `export_csv` | `export.py` | `cli.main` (the `export` subcommand) |
| `_windows` | `cli.py` | `cli.main` (`plan` and `export`) |
| `main` | `cli.py` | the console script; `python -m tidepool.cli` |

The table is the dependency graph in another form: `cli` depends on all four modules,
`export` and `plan` depend on nothing in the package, `tides` depends on `requests` only, and
`stations` on the standard library only. No module imports `cli`, and `plan` and `export`
import neither `requests` nor `astral` at module level, which is what lets the test suite
import them bare. A new public name is added to this table in the same change that adds
it; a name that leaves the table leaves the code.

## Data flow and invariants

```
station id ─▶ stations.get_station (registry; KeyError for an unknown id)
           ─▶ tides.fetch_predictions("today", "+N")   (network, no cache, MLLW feet, hilo)
           ─▶ tides.low_tides                           (type == "L", no height cut)
           ─▶ per low: plan.sun_events + plan.moon_phase_days (astral, function-local)
                       plan.score_window                (0.5 / 0.3 / 0.2, pure)
           ─▶ ranked window dicts (nine keys)           (cli._windows, sorted by score)
           ─▶ terminal table (plan, --min-score)  or  export.export_csv (every window)
```

Invariants that hold across the modules, each enforced where it says:

- **Heights are MLLW feet everywhere.** The client pins `datum=MLLW` and `units=english`;
  the scorer's constants are feet; the DOMAIN's thresholds are feet. A second datum enters
  nowhere.
- **The core is pure.** Everything in `plan.py` except the two astral wrappers is
  deterministic over its arguments, with no I/O; the test suite exercises it without the
  network and without `astral`.
- **One writer of files.** The package writes only the `--out` path of `export`; the cache
  directory has no writer until the refresh script lands (§ Station registry and the
  metadata cache).
- **Lows are not pre-filtered.** `low_tides` passes every low; the score and the threshold
  do the selecting. The known bug (ROADMAP) proposes a cut at +1.5 ft inside `low_tides`;
  until it ships, a high low scores low rather than disappearing.
- **The CLI formats, the modules compute.** Rounding happens once, in `_windows()`; the
  exporter and the table print what they are given.
- **Scoring weights are a deliberate balance**: rationale in
  `openspec/changes/archive/2026-06-08-three-factor-scoring/design.md`.
- **The CLI never writes anywhere except an explicit `--out` path and the cache directory.**
