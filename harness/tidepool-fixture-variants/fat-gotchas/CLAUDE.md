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

## Load-bearing gotchas
- The NOAA API is unauthenticated but rate-limited — never loop station fetches without the
  cache check (`stations.cache_fresh`).
- Tide heights are MLLW feet everywhere; never mix datums.
- `astral` imports stay function-local (`plan.py`) so `pytest` runs without it installed.

## Gotchas (the CO-OPS client and the exporter, learned on the export rewrite, 2026-06)

Everything that bit while `tides.py` and `export.py` were rewritten. Each one cost a trip or
a day; none is obvious from the API docs.

- **`begin_date` and `end_date` take `yyyymmdd` or `yyyymmdd HH:mm`, and the `+N`/`today`
  shorthands are a separate parameter pair.** Passing `today` as `begin_date` with
  `end_date=+7` works; passing `+7` as `begin_date` returns a 400 whose body is an HTML page,
  not JSON, so `resp.json()` raises `JSONDecodeError` before `raise_for_status` sees anything
  (the status is 200 for the HTML error page). Check `content-type` before parsing.
- **The datagetter returns `{"error": {"message": ...}}` with HTTP 200 for a bad station.**
  `raise_for_status()` passes; the `predictions` key is absent and the client raises
  `KeyError`. Test for the `error` key first and raise a clean `StationError`; the message
  text is the only place the station id appears.
- **`interval=hilo` caps the range at 31 days per request.** A 45-day plan needs two
  requests; the second must start the day after the first ends, not the same day, or the
  boundary day's lows appear twice and the planner scores them twice (the midnight-straddle
  duplicate in the June notebook was this, not a scoring bug).
- **`time_zone=lst_ldt` is station-local *with* DST; `lst` is without; `gmt` is UTC.** The
  planner compares low times to `astral`'s sunrise/sunset, which come back in UTC and are
  converted with `.astimezone()` to the *machine's* zone. For a station in another zone the
  comparison is off by the zone difference. Convert both to the station's zone, from the
  station's `timezone` metadata field, before comparing.
- **Station ids are strings with a leading digit that can be zero-padded in the metadata
  API and not in the datagetter.** The MDAPI lists `08418150`; the datagetter wants
  `8418150`. Strip the leading zero when a station id comes from MDAPI; the registry stores
  the datagetter form.
- **Subordinate stations return `type` but no `v` for some lows.** A subordinate station
  (one whose predictions are offsets from a reference station) occasionally returns a hilo
  row with the height missing; `float(low["v"])` raises. Skip the row and log it; do not
  substitute zero, which would score as a perfect window.
- **The `H`/`L` type values are upper case in `hilo` and lower case in the 6-minute
  product.** `low_tides()` tests `== "L"`; a client switched to the 6-minute product for a
  finer curve gets no lows at all and the plan is silently empty.
- **The API rate limit is per source IP, not per key (there is no key).** A planning session
  on a shared network trips 429s that the client's `raise_for_status` reports as
  `HTTPError: 429`. Back off 30 s and retry once; a second 429 means the day is done for
  that network. The metadata cache exists so station lookups do not spend requests.
- **`datum=MLLW` is unavailable at a few Great Lakes and river stations.** Those return the
  `error` dict ("datum not available"). The registry is curated to tidal stations for this
  reason; an added station must be checked for MLLW before it is admitted (the station
  curation checklist).
- **`units=english` returns feet; `metric` returns meters; the planner's thresholds are in
  feet.** A client call with `units` omitted defaults to metric on some endpoints and english
  on others. Always pass it. `GOOD_TIDE_FT` is feet; a metric response makes every low look
  exceptional.
- **A 30 s timeout is not optional.** The Monterey trip's silent hang was a request with no
  timeout against a server that accepted the connection and never answered; `requests` waits
  forever by default. Every call carries `timeout=30` and `raise_for_status`. (Contract, see
  NOTEBOOK 2026-07-04.)
- **`application=tidepool` is required by NOAA's terms, and some responses include it in
  the error text.** Omit it and the request still works today; NOAA reserves the right to
  block unidentified clients. Keep it.
- **The DST changeover day returns 23 or 25 hours of predictions in `lst_ldt`.** A low at
  01:30 on the spring-forward day does not exist in local time; the API returns it anyway
  with the pre-change offset. `strptime` parses it; `astral` comparisons for that hour are
  off by one. Treat the changeover day's pre-dawn low as unplannable.
- **The exporter's `csv.DictWriter` needs `newline=""` on Windows or every row gets a blank
  line after it.** Spreadsheet users on Windows reported doubled rows; the fix is the
  `open(..., newline="")` the exporter now uses. Any new writer must do the same.
- **`--out` is a `pathlib.Path`; a relative path resolves against the current directory, not
  the repo.** The CLI run from a cron job writes `windows.csv` into cron's working
  directory. Document the absolute path in any scheduled use; the exporter does not resolve
  it.
- **The export columns are the dict keys of `_windows()`; adding a column there without
  adding it to `CSV_COLUMNS` drops it silently.** `DictWriter` writes only the listed
  fieldnames and ignores extra keys. The nine-column test asserts the list, not the dict; a
  new field needs both.
- **`moon_phase_days` is a float with the astral scale (0 to about 28), and the CSV rounds it
  to one decimal.** Round in `_windows()` not in the exporter, so the terminal table and the
  CSV agree; a spreadsheet formula on the column expects one decimal.
- **The score column must be rounded to three decimals before export or the CSV carries
  float noise (0.7000000000000001).** `_windows()` rounds; the exporter must not re-round or
  the two tables disagree on ties.
- **Sorting by score descending with Python's `sorted` is stable; ties keep date order.**
  The exporter relies on that for the "best window first, then earliest" order the docs
  promise. A sort key that adds the date reverses it. Do not touch the sort.
- **The hilo product has no `datum` field in the response; the datum is whatever you
  asked for.** A reader checking the response's datum finds none and must trust the
  request. Log the request parameters with every fetch so a wrong datum is visible after the
  fact.
- **MDAPI's station metadata is a different host and a different JSON shape.** The
  `stations.py` cache stores the MDAPI response; the datagetter never reads it. Mixing the
  two in one client class was the June rewrite's first mistake. Keep them in separate
  modules.
- **An empty predictions list is a valid response for a station with no lows in range.**
  A one-day request on a diurnal station can return a single high and no low. The planner
  must handle an empty list without raising; the CLI prints "no windows" and exits 0.
