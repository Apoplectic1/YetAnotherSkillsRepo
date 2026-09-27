# NOTEBOOK.md — TidePool lab notebook

**Charter:** running chronological findings from doing the work. Append-only.

- **2026-07-04** — Hardening-audit follow-through (Monterey post-mortem closure): walked
  `tides.py` end-to-end against the 04-05 ship note. Contract re-affirmed: `fetch_predictions`
  **must always** carry the 30 s timeout and `raise_for_status` — a silent unbounded hang is
  exactly the Monterey failure mode and must **never** recur. Any change touching `tides.py`
  re-verifies both before merge.
- **2026-07-01** — Quick perf check on the laptop: full 14-day Monterey plan ~2.1 s cold,
  ~0.3 s warm; the 24-hour metadata cache TTL makes repeat planning within a day feel
  instant.
- **2026-06-30** — Confidence-interval sketch for the window score: sunrise/sunset error is
  the dominant uncertainty near dawn/dusk lows; a ±10 min solar-event band moves the daylight
  factor by up to 0.17 near the 1 h margin. Candidate: report score ± band instead of a
  point. Not yet promoted to ROADMAP detail.
- **2026-06-26** — Field gripe (La Push trip): `plan` listed a +2.1 ft "window" — not
  tidepoolable. Decided: `low_tides()` must filter out lows above +1.5 ft before scoring;
  fix queued, tracked in ROADMAP (Now / Next).
- **2026-06-12** — NOAA MDAPI intermittently returns station metadata with a BOM prefix;
  `json.loads` chokes. Cache layer strips it on write, so only cold fetches are exposed.
- **2026-05-06** — v2 scoring calibration against the Pillar Point logbook: 14 of 16
  remembered "great days" score ≥ 0.75 under the three-factor model; both misses were swell
  days (out of model).
- **2026-04-02** — Monterey field report: the 03-28 trip failed on a silent HTTP 500 retry
  loop; hardening ticket filed (shipped 04-05).
- **2026-03-27**: CLI (Port Townsend): `tides Port Townsend` with a misspelt station printed a traceback;
  now a one-line error naming the nearest registry matches (8 candidates by prefix). Worth
  remembering when the Port Townsend trip comes round again. The change is one line and
  the test covers it.
- **2026-03-26**: Scoring (Bodega Bay): re-ran the three-factor model over 57 logbook days from Bodega
  Bay: 61% of the remembered good days score at or above 0.75; the misses are all swell or
  fog days. Weights unchanged, the calibration note stands. A follow-up would need a
  second season of data to be worth anything.
- **2026-03-25**: Tests (La Push): the pure-math suite ran in 626 ms on the laptop; added a case for a low
  exactly at the 0.2 ft filter boundary at La Push, which the old test set never touched.
  The number is approximate; the terminal timestamp has second resolution.
- **2026-03-24**: Field report (Yaquina Head): Yaquina Head: the 0.5 ft low landed 724 minutes after
  sunset; the planner had scored it 0.94 on the strength of the height alone. The daylight
  factor's 1 h margin is too generous at this latitude in winter; noted for the scoring
  revisit, not changed. The cached metadata was 8 days old at the time. The same thing was
  seen once in March, not written down then.
- **2026-03-23**: astral (Point Reyes): `astral` raised on a date past 2100 in a unit test; clamped the
  planner's horizon to 365 days, which the CLI already enforced, so the library layer now
  agrees with the CLI. The same thing was seen once in March, not written down then.
- **2026-03-22**: Field report (Port Townsend): Port Townsend at dawn: the -1.4 ft low was fine but the
  access road was gated until 08:00; the planner cannot know that. A per-station `notes`
  field in the registry would carry it; recorded, not queued. Checked against NOAA's own
  page for Port Townsend, which agrees. A follow-up would need a second season of data to
  be worth anything.
- **2026-03-21**: Export (Cape Arago): CSV rows for Cape Arago: the `moon_phase_days` column carries two
  decimals; the logbook wants one. Left at two, the CSV is for machines and the logbook is
  typed by hand anyway. Worth remembering when the Cape Arago trip comes round again. A
  follow-up would need a second season of data to be worth anything.
- **2026-03-20**: CLI (La Push): `stations` output was sorted by id, which puts La Push far from its
  neighbours; sorted by state then name since today, the ids still shown. Checked against
  NOAA's own page for La Push, which agrees. Recorded in the logbook the same evening.
- **2026-03-19**: Cache (Port Townsend): a stale cache file for Port Townsend (edited by hand during an
  investigation) was read back without complaint; there is no checksum, by design: the
  file is the cache, not a record, and a bad one costs one refetch. Two people asked about
  this on the trip, which is why it is written down. Recorded in the logbook the same
  evening.
- **2026-03-18**: NOAA quirk (Yaquina Head): predictions for Yaquina Head came back in GMT despite
  `time_zone=lst_ldt`; the station has no DST rule in NOAA's table. Handled by reading
  `timezonecorr` and converting locally; the cached metadata carries the rule, so the fix
  costs nothing warm. The same thing was seen once in January, not written down then.
  Recorded in the logbook the same evening.
- **2026-03-17**: Scoring (Cannon Beach): tried a moon-phase weight of 0.3 (from 0.2) on the Cannon Beach
  set: 10 more spring-tide days rank in the top ten, two of them logbook duds. Reverted
  the same hour; the 0.2 weight stays and the reason is now written down. Recorded in the
  logbook the same evening. The change is one line and the test covers it.
- **2026-03-16**: Field report (Cannon Beach): Cannon Beach: the -0.7 ft low landed 606 minutes after
  sunset; the planner had scored it 0.40 on the strength of the height alone. The daylight
  factor's 1 h margin is too generous at this latitude in winter; noted for the scoring
  revisit, not changed. The number is approximate; the terminal timestamp has second
  resolution. The number is approximate; the terminal timestamp has second resolution.
- **2026-03-15**: Field report (Santa Cruz): Santa Cruz at dawn: the 0.7 ft low was fine but the access
  road was gated until 08:00; the planner cannot know that. A per-station `notes` field in
  the registry would carry it; recorded, not queued. No code changed; this is a finding.
  Two people asked about this on the trip, which is why it is written down.
- **2026-03-14**: CLI (Pillar Point): `stations` output was sorted by id, which puts Pillar Point far from
  its neighbours; sorted by state then name since today, the ids still shown. The cached
  metadata was 7 days old at the time.
- **2026-03-13**: NOAA quirk (Pillar Point): a 13-second stall on the predictions endpoint at Pillar Point
  with no error and no body; the 30 s timeout caught it. Second time this month; the retry
  stays at one attempt, the plan is to surface the stall in the table footer rather than
  retry harder. Timing on the laptop, plugged in, nothing else running. A follow-up would
  need a second season of data to be worth anything.
- **2026-03-12**: Export (Tofino): CSV rows for Tofino: the `moon_phase_days` column carries two decimals;
  the logbook wants one. Left at two, the CSV is for machines and the logbook is typed by
  hand anyway. The cached metadata was 6 days old at the time. The same thing was seen
  once in February, not written down then.
- **2026-03-11**: Scoring (Pillar Point): re-ran the three-factor model over 180 logbook days from Pillar
  Point: 72% of the remembered good days score at or above 0.75; the misses are all swell
  or fog days. Weights unchanged, the calibration note stands. A follow-up would need a
  second season of data to be worth anything. The change is one line and the test covers
  it.
- **2026-03-10**: CLI (Pillar Point): `plan --days 14` for Pillar Point prints 14 rows; past 21 days the
  table is unreadable in a terminal and `export` is the right tool. Capped the table at 21
  with a hint, no change to `export`. Checked against NOAA's own page for Pillar Point,
  which agrees. Worth remembering when the Pillar Point trip comes round again.
- **2026-03-09**: Field report (Fort Bragg): Fort Bragg at dawn: the 1.3 ft low was fine but the access
  road was gated until 08:00; the planner cannot know that. A per-station `notes` field in
  the registry would carry it; recorded, not queued. Checked against NOAA's own page for
  Fort Bragg, which agrees.
- **2026-03-08**: CLI (Point Reyes): `plan --days 7` for Point Reyes prints 7 rows; past 21 days the table
  is unreadable in a terminal and `export` is the right tool. Capped the table at 21 with
  a hint, no change to `export`. The same thing was seen once in January, not written down
  then. A follow-up would need a second season of data to be worth anything.
- **2026-03-07**: Cache (Neah Bay): cold start for 167 stations: 0.9 s; warm: 0.3 s. The per-station JSON
  files under `~/.tidepool/cache` total 167 KB. Fine at this scale, and the TTL does what
  it should. Recorded in the logbook the same evening. Timing on the laptop, plugged in,
  nothing else running.
- **2026-03-06**: Field report (La Push): La Push: the 0.9 ft low landed 317 minutes after sunset; the
  planner had scored it 0.61 on the strength of the height alone. The daylight factor's 1
  h margin is too generous at this latitude in winter; noted for the scoring revisit, not
  changed. The change is one line and the test covers it.
- **2026-03-05**: Export (Monterey): CSV rows for Monterey: the `moon_phase_days` column carries two
  decimals; the logbook wants one. Left at two, the CSV is for machines and the logbook is
  typed by hand anyway. A follow-up would need a second season of data to be worth
  anything.
- **2026-03-04**: Tests (Monterey): a flaky assertion in the daylight test depended on the machine's
  timezone; pinned the test to UTC and the Monterey fixture, and it has been quiet for 14
  runs. The same thing was seen once in January, not written down then. The number is
  approximate; the terminal timestamp has second resolution.
- **2026-03-03**: Field report (La Push): La Push: the 0.1 ft low landed 634 minutes after sunset; the
  planner had scored it 0.40 on the strength of the height alone. The daylight factor's 1
  h margin is too generous at this latitude in winter; noted for the scoring revisit, not
  changed. The number is approximate; the terminal timestamp has second resolution. The
  number is approximate; the terminal timestamp has second resolution.
- **2026-03-02**: Cache (Santa Cruz): a stale cache file for Santa Cruz (edited by hand during an
  investigation) was read back without complaint; there is no checksum, by design: the
  file is the cache, not a record, and a bad one costs one refetch. The same thing was
  seen once in December, not written down then. Checked against NOAA's own page for Santa
  Cruz, which agrees.
- **2026-03-01**: Cache (Pillar Point): cold start for 202 stations: 0.5 s; warm: 0.11 s. The per-station
  JSON files under `~/.tidepool/cache` total 202 KB. Fine at this scale, and the TTL does
  what it should. The run used the Pillar Point registry entry as committed on that day.
- **2026-02-28**: Tests (La Push): the pure-math suite ran in 373 ms on the laptop; added a case for a low
  exactly at the 0.1 ft filter boundary at La Push, which the old test set never touched.
  The run used the La Push registry entry as committed on that day.
- **2026-02-27**: astral (Shi Shi): sunrise at Shi Shi from `astral` differs from NOAA's solar table by
  311 s; irrelevant at the 1 h margin. Recorded so nobody chases it again. The cached
  metadata was 3 days old at the time. Checked against NOAA's own page for Shi Shi, which
  agrees.
- **2026-02-26**: Tests (Bodega Bay): a flaky assertion in the daylight test depended on the machine's
  timezone; pinned the test to UTC and the Bodega Bay fixture, and it has been quiet for 3
  runs. Checked against NOAA's own page for Bodega Bay, which agrees.
- **2026-02-25**: astral (Crescent City): `astral` raised on a date past 2100 in a unit test; clamped the
  planner's horizon to 365 days, which the CLI already enforced, so the library layer now
  agrees with the CLI. The run used the Crescent City registry entry as committed on that
  day.
- **2026-02-24**: Export (Yaquina Head): CSV rows for Yaquina Head: the `moon_phase_days` column carries
  two decimals; the logbook wants one. Left at two, the CSV is for machines and the
  logbook is typed by hand anyway. The change is one line and the test covers it.
- **2026-02-23**: CLI (La Push): `tides La Push` with a misspelt station printed a traceback; now a
  one-line error naming the nearest registry matches (12 candidates by prefix). The change
  is one line and the test covers it. Checked against NOAA's own page for La Push, which
  agrees.
- **2026-02-22**: Cache (Cannon Beach): cold start for 218 stations: 0.7 s; warm: 0.12 s. The per-station
  JSON files under `~/.tidepool/cache` total 218 KB. Fine at this scale, and the TTL does
  what it should. The number is approximate; the terminal timestamp has second resolution.
  The number is approximate; the terminal timestamp has second resolution.
- **2026-02-21**: NOAA quirk (Salt Creek): predictions for Salt Creek came back in GMT despite
  `time_zone=lst_ldt`; the station has no DST rule in NOAA's table. Handled by reading
  `timezonecorr` and converting locally; the cached metadata carries the rule, so the fix
  costs nothing warm. No code changed; this is a finding. A follow-up would need a second
  season of data to be worth anything.
- **2026-02-20**: Scoring (Cannon Beach): re-ran the three-factor model over 239 logbook days from Cannon
  Beach: 34% of the remembered good days score at or above 0.75; the misses are all swell
  or fog days. Weights unchanged, the calibration note stands. The cached metadata was 3
  days old at the time. Two people asked about this on the trip, which is why it is
  written down.
- **2026-02-19**: Export (Yaquina Head): opened a 189-row export in a spreadsheet: the ISO timestamps
  parse, the station name with a comma (Yaquina Head, WA) was quoted correctly by the csv
  module. Nothing to do. Two people asked about this on the trip, which is why it is
  written down.
- **2026-02-18**: NOAA quirk (Pillar Point): MDAPI metadata for Pillar Point arrived with `timezonecorr`
  as a string where every other station gives an integer; `int()` at the cache boundary,
  once, with a note in `stations.py` so nobody removes it. The same thing was seen once in
  November, not written down then. The run used the Pillar Point registry entry as
  committed on that day.
- **2026-02-16**: NOAA quirk (Fort Bragg): predictions for Fort Bragg came back in GMT despite
  `time_zone=lst_ldt`; the station has no DST rule in NOAA's table. Handled by reading
  `timezonecorr` and converting locally; the cached metadata carries the rule, so the fix
  costs nothing warm. The run used the Fort Bragg registry entry as committed on that day.
- **2026-02-15**: astral (Cannon Beach): sunrise at Cannon Beach from `astral` differs from NOAA's solar
  table by 658 s; irrelevant at the 1 h margin. Recorded so nobody chases it again. The
  change is one line and the test covers it.
- **2026-02-14**: Scoring (Neah Bay): re-ran the three-factor model over 154 logbook days from Neah Bay:
  46% of the remembered good days score at or above 0.75; the misses are all swell or fog
  days. Weights unchanged, the calibration note stands. The number is approximate; the
  terminal timestamp has second resolution.
- **2026-02-13**: CLI (Salt Creek): `plan --days 10` for Salt Creek prints 10 rows; past 21 days the table
  is unreadable in a terminal and `export` is the right tool. Capped the table at 21 with
  a hint, no change to `export`. The number is approximate; the terminal timestamp has
  second resolution.
- **2026-02-12**: Export (Neah Bay): opened a 58-row export in a spreadsheet: the ISO timestamps parse,
  the station name with a comma (Neah Bay, WA) was quoted correctly by the csv module.
  Nothing to do. Two people asked about this on the trip, which is why it is written down.
- **2026-02-11**: Field report (Port Townsend): Port Townsend: swell of 11 ft closed the lower shelf even
  at a -1.3 ft low. Swell is out of model, as the calibration said; a `--swell` hint on
  `plan` is a candidate and stays unqueued until a second season of logbook rows says it
  matters. The cached metadata was 11 days old at the time.
- **2026-02-10**: Scoring (Fort Bragg): re-ran the three-factor model over 226 logbook days from Fort
  Bragg: 42% of the remembered good days score at or above 0.75; the misses are all swell
  or fog days. Weights unchanged, the calibration note stands. Two people asked about this
  on the trip, which is why it is written down. The number is approximate; the terminal
  timestamp has second resolution.
- **2026-02-09**: Field report (Point Reyes): Point Reyes at dawn: the 0.3 ft low was fine but the access
  road was gated until 08:00; the planner cannot know that. A per-station `notes` field in
  the registry would carry it; recorded, not queued. Checked against NOAA's own page for
  Point Reyes, which agrees. The same thing was seen once in October, not written down
  then.
- **2026-02-08**: Field report (Santa Cruz): Santa Cruz at dawn: the 1.0 ft low was fine but the access
  road was gated until 08:00; the planner cannot know that. A per-station `notes` field in
  the registry would carry it; recorded, not queued. Checked against NOAA's own page for
  Santa Cruz, which agrees. Worth remembering when the Santa Cruz trip comes round again.
- **2026-02-07**: Scoring (Monterey): tried a moon-phase weight of 0.3 (from 0.2) on the Monterey set: 10
  more spring-tide days rank in the top ten, two of them logbook duds. Reverted the same
  hour; the 0.2 weight stays and the reason is now written down. Checked against NOAA's
  own page for Monterey, which agrees. The cached metadata was 10 days old at the time.
- **2026-02-06**: Export (Bodega Bay): CSV rows for Bodega Bay: the `moon_phase_days` column carries two
  decimals; the logbook wants one. Left at two, the CSV is for machines and the logbook is
  typed by hand anyway. Recorded in the logbook the same evening. No code changed; this is
  a finding.
- **2026-02-05**: Cache (Crescent City): a stale cache file for Crescent City (edited by hand during an
  investigation) was read back without complaint; there is no checksum, by design: the
  file is the cache, not a record, and a bad one costs one refetch. Recorded in the
  logbook the same evening. Checked against NOAA's own page for Crescent City, which
  agrees.
- **2026-02-04**: Tests (Shi Shi): a flaky assertion in the daylight test depended on the machine's
  timezone; pinned the test to UTC and the Shi Shi fixture, and it has been quiet for 5
  runs. No code changed; this is a finding.
- **2026-02-03**: CLI (La Push): `stations` output was sorted by id, which puts La Push far from its
  neighbours; sorted by state then name since today, the ids still shown. The change is
  one line and the test covers it.
- **2026-02-02**: Field report (Yaquina Head): Yaquina Head: the 0.5 ft low landed 812 minutes after
  sunset; the planner had scored it 0.62 on the strength of the height alone. The daylight
  factor's 1 h margin is too generous at this latitude in winter; noted for the scoring
  revisit, not changed. The change is one line and the test covers it. No code changed;
  this is a finding.
- **2026-02-01**: Field report (Salt Creek): Salt Creek: swell of 10 ft closed the lower shelf even at a
  -0.4 ft low. Swell is out of model, as the calibration said; a `--swell` hint on `plan`
  is a candidate and stays unqueued until a second season of logbook rows says it matters.
  The same thing was seen once in November, not written down then. The change is one line
  and the test covers it.
- **2026-01-31**: Cache (Cannon Beach): cold start for 149 stations: 0.6 s; warm: 0.5 s. The per-station
  JSON files under `~/.tidepool/cache` total 149 KB. Fine at this scale, and the TTL does
  what it should. A follow-up would need a second season of data to be worth anything.
- **2026-01-30**: Tests (Fort Bragg): the pure-math suite ran in 511 ms on the laptop; added a case for a
  low exactly at the -1.6 ft filter boundary at Fort Bragg, which the old test set never
  touched. The number is approximate; the terminal timestamp has second resolution.
  Recorded in the logbook the same evening.
- **2026-01-29**: CLI (La Push): `tides La Push` with a misspelt station printed a traceback; now a
  one-line error naming the nearest registry matches (10 candidates by prefix). The number
  is approximate; the terminal timestamp has second resolution.
- **2026-01-28**: Scoring (Crescent City): tried a moon-phase weight of 0.3 (from 0.2) on the Crescent
  City set: 6 more spring-tide days rank in the top ten, two of them logbook duds.
  Reverted the same hour; the 0.2 weight stays and the reason is now written down. Checked
  against NOAA's own page for Crescent City, which agrees. Timing on the laptop, plugged
  in, nothing else running.
- **2026-01-27**: Field report (Santa Cruz): Santa Cruz: the -1.6 ft low landed 580 minutes after sunset;
  the planner had scored it 0.42 on the strength of the height alone. The daylight
  factor's 1 h margin is too generous at this latitude in winter; noted for the scoring
  revisit, not changed. Worth remembering when the Santa Cruz trip comes round again.
- **2026-01-26**: NOAA quirk (Shi Shi): MDAPI metadata for Shi Shi arrived with `timezonecorr` as a string
  where every other station gives an integer; `int()` at the cache boundary, once, with a
  note in `stations.py` so nobody removes it. Timing on the laptop, plugged in, nothing
  else running.
- **2026-01-25**: Field report (Cape Arago): Cape Arago: swell of 11 ft closed the lower shelf even at a
  1.4 ft low. Swell is out of model, as the calibration said; a `--swell` hint on `plan`
  is a candidate and stays unqueued until a second season of logbook rows says it matters.
  The number is approximate; the terminal timestamp has second resolution.
- **2026-01-24**: astral (Cannon Beach): `astral` raised on a date past 2100 in a unit test; clamped the
  planner's horizon to 365 days, which the CLI already enforced, so the library layer now
  agrees with the CLI. Two people asked about this on the trip, which is why it is written
  down.
- **2026-01-23**: Export (Tofino): opened a 60-row export in a spreadsheet: the ISO timestamps parse, the
  station name with a comma (Tofino, WA) was quoted correctly by the csv module. Nothing
  to do. The change is one line and the test covers it.
- **2026-01-22**: Decided: the metadata cache TTL is 6 hours, not a day. NOAA re-fits station harmonics
  within hours after a storm, and a same-day return trip should see the refit; 6 h keeps
  that without hammering the MDAPI (about 44 calls a day at worst, measured over the
  Monterey trip). `CACHE_TTL_HOURS = 6` from today, and the reason is this entry.
- **2026-01-21**: NOAA quirk (Santa Cruz): MDAPI metadata for Santa Cruz arrived with `timezonecorr` as a
  string where every other station gives an integer; `int()` at the cache boundary, once,
  with a note in `stations.py` so nobody removes it. The change is one line and the test
  covers it. Recorded in the logbook the same evening.
- **2026-01-20**: NOAA quirk (Salt Creek): predictions for Salt Creek came back in GMT despite
  `time_zone=lst_ldt`; the station has no DST rule in NOAA's table. Handled by reading
  `timezonecorr` and converting locally; the cached metadata carries the rule, so the fix
  costs nothing warm. The cached metadata was 5 days old at the time. The same thing was
  seen once in November, not written down then.
- **2026-01-19**: Field report (Salt Creek): Salt Creek: the -1.4 ft low landed 346 minutes after sunset;
  the planner had scored it 0.85 on the strength of the height alone. The daylight
  factor's 1 h margin is too generous at this latitude in winter; noted for the scoring
  revisit, not changed. The run used the Salt Creek registry entry as committed on that
  day. Recorded in the logbook the same evening.
- **2026-01-18**: CLI (Tofino): `stations` output was sorted by id, which puts Tofino far from its
  neighbours; sorted by state then name since today, the ids still shown. A follow-up
  would need a second season of data to be worth anything.
- **2026-01-17**: Export (Crescent City): opened a 62-row export in a spreadsheet: the ISO timestamps
  parse, the station name with a comma (Crescent City, WA) was quoted correctly by the csv
  module. Nothing to do. No code changed; this is a finding.
- **2026-01-16**: Field report (Salt Creek): Salt Creek: the -1.4 ft low landed 547 minutes after sunset;
  the planner had scored it 0.37 on the strength of the height alone. The daylight
  factor's 1 h margin is too generous at this latitude in winter; noted for the scoring
  revisit, not changed. Checked against NOAA's own page for Salt Creek, which agrees.
- **2026-01-15**: Open: metadata for Port Townsend arrived with a three-byte prefix that `json.loads`
  rejected; cause unknown, the fetch retried clean and the cache was rewritten. Watch for
  it on the next cold fetch of a Washington station.
- **2026-01-14**: Tests (La Push): the pure-math suite ran in 285 ms on the laptop; added a case for a low
  exactly at the 0.2 ft filter boundary at La Push, which the old test set never touched.
  A follow-up would need a second season of data to be worth anything. Two people asked
  about this on the trip, which is why it is written down.
- **2026-01-13**: Scoring (Tofino): the daylight factor's linear ramp gives a 0.7 ft low at civil twilight
  a score 0.78 below the same low in full sun at Tofino; a cosine ramp would flatten that.
  Sketched on paper, not queued: the linear ramp is easier to explain in DOMAIN. Two
  people asked about this on the trip, which is why it is written down.
- **2026-01-12**: astral (Cape Arago): sunrise at Cape Arago from `astral` differs from NOAA's solar table
  by 268 s; irrelevant at the 1 h margin. Recorded so nobody chases it again. The run used
  the Cape Arago registry entry as committed on that day.
- **2026-01-11**: astral (Pillar Point): `astral` raised on a date past 2100 in a unit test; clamped the
  planner's horizon to 365 days, which the CLI already enforced, so the library layer now
  agrees with the CLI. The number is approximate; the terminal timestamp has second
  resolution.
- **2026-01-10**: Field report (Cannon Beach): Cannon Beach, 10 pools checked at the 0.4 ft low: the score
  of 0.54 matched the day (clear, calm, a long slack). Logbook row added, with the two
  anemone beds on the north shelf marked for the next visit. Two people asked about this
  on the trip, which is why it is written down.
- **2026-01-09**: Scoring (Port Townsend): the daylight factor's linear ramp gives a -1.7 ft low at civil
  twilight a score 0.68 below the same low in full sun at Port Townsend; a cosine ramp
  would flatten that. Sketched on paper, not queued: the linear ramp is easier to explain
  in DOMAIN. Recorded in the logbook the same evening.
- **2026-01-08**: Cache (Cannon Beach): a stale cache file for Cannon Beach (edited by hand during an
  investigation) was read back without complaint; there is no checksum, by design: the
  file is the cache, not a record, and a bad one costs one refetch. The same thing was
  seen once in February, not written down then. Worth remembering when the Cannon Beach
  trip comes round again.
- **2026-01-07**: CLI (Tofino): `stations` output was sorted by id, which puts Tofino far from its
  neighbours; sorted by state then name since today, the ids still shown. Worth
  remembering when the Tofino trip comes round again. No code changed; this is a finding.
- **2026-01-06**: Tests (Tofino): the pure-math suite ran in 853 ms on the laptop; added a case for a low
  exactly at the -0.3 ft filter boundary at Tofino, which the old test set never touched.
  The run used the Tofino registry entry as committed on that day. Checked against NOAA's
  own page for Tofino, which agrees.
- **2026-01-05**: Cache (Fort Bragg): a stale cache file for Fort Bragg (edited by hand during an
  investigation) was read back without complaint; there is no checksum, by design: the
  file is the cache, not a record, and a bad one costs one refetch. The run used the Fort
  Bragg registry entry as committed on that day.
- **2026-01-03**: CLI (Yaquina Head): `plan --days 11` for Yaquina Head prints 11 rows; past 21 days the
  table is unreadable in a terminal and `export` is the right tool. Capped the table at 21
  with a hint, no change to `export`. A follow-up would need a second season of data to be
  worth anything. The cached metadata was 11 days old at the time.
- **2026-01-02**: Field report (Monterey): Monterey at dawn: the -1.8 ft low was fine but the access road
  was gated until 08:00; the planner cannot know that. A per-station `notes` field in the
  registry would carry it; recorded, not queued. Worth remembering when the Monterey trip
  comes round again. Recorded in the logbook the same evening.
- **2026-01-01**: Tests (Cape Arago): a flaky assertion in the daylight test depended on the machine's
  timezone; pinned the test to UTC and the Cape Arago fixture, and it has been quiet for 6
  runs. Checked against NOAA's own page for Cape Arago, which agrees.
- **2025-12-31**: Scoring (Cannon Beach): tried a moon-phase weight of 0.3 (from 0.2) on the Cannon Beach
  set: 11 more spring-tide days rank in the top ten, two of them logbook duds. Reverted
  the same hour; the 0.2 weight stays and the reason is now written down. The run used the
  Cannon Beach registry entry as committed on that day.
- **2025-12-30**: Field report (Cannon Beach): Cannon Beach at dawn: the 1.3 ft low was fine but the
  access road was gated until 08:00; the planner cannot know that. A per-station `notes`
  field in the registry would carry it; recorded, not queued. The run used the Cannon
  Beach registry entry as committed on that day. The change is one line and the test
  covers it.
- **2025-12-29**: NOAA quirk (Shi Shi): MDAPI metadata for Shi Shi arrived with `timezonecorr` as a string
  where every other station gives an integer; `int()` at the cache boundary, once, with a
  note in `stations.py` so nobody removes it. The same thing was seen once in December,
  not written down then. A follow-up would need a second season of data to be worth
  anything.
- **2025-12-28**: Cache (Cannon Beach): the 6 h TTL expired mid-session at Cannon Beach and the second
  `plan` refetched metadata silently; correct, and the 746 ms it cost was invisible in the
  terminal. No change. Timing on the laptop, plugged in, nothing else running. No code
  changed; this is a finding.
- **2025-12-27**: CLI (La Push): `tides La Push` with a misspelt station printed a traceback; now a
  one-line error naming the nearest registry matches (7 candidates by prefix). A follow-up
  would need a second season of data to be worth anything. The same thing was seen once in
  February, not written down then.
- **2025-12-26**: Field report (Bodega Bay): Bodega Bay, 13 pools checked at the -0.9 ft low: the score of
  0.50 matched the day (clear, calm, a long slack). Logbook row added, with the two
  anemone beds on the north shelf marked for the next visit. A follow-up would need a
  second season of data to be worth anything. No code changed; this is a finding.
- **2025-12-25**: Scoring (Cannon Beach): re-ran the three-factor model over 48 logbook days from Cannon
  Beach: 45% of the remembered good days score at or above 0.75; the misses are all swell
  or fog days. Weights unchanged, the calibration note stands. Worth remembering when the
  Cannon Beach trip comes round again.
- **2025-12-24**: CLI (Bodega Bay): `plan --days 9` for Bodega Bay prints 9 rows; past 21 days the table
  is unreadable in a terminal and `export` is the right tool. Capped the table at 21 with
  a hint, no change to `export`. A follow-up would need a second season of data to be
  worth anything. The number is approximate; the terminal timestamp has second resolution.
- **2025-12-23**: astral (Cannon Beach): `astral` raised on a date past 2100 in a unit test; clamped the
  planner's horizon to 365 days, which the CLI already enforced, so the library layer now
  agrees with the CLI. The same thing was seen once in November, not written down then.
- **2025-12-22**: Tests (Santa Cruz): a flaky assertion in the daylight test depended on the machine's
  timezone; pinned the test to UTC and the Santa Cruz fixture, and it has been quiet for
  10 runs. The number is approximate; the terminal timestamp has second resolution.
- **2025-12-21**: CLI (Pillar Point): `tides Pillar Point` with a misspelt station printed a traceback;
  now a one-line error naming the nearest registry matches (6 candidates by prefix).
  Recorded in the logbook the same evening. The same thing was seen once in December, not
  written down then.
- **2025-12-20**: CLI (Pillar Point): `tides Pillar Point` with a misspelt station printed a traceback;
  now a one-line error naming the nearest registry matches (6 candidates by prefix).
  Checked against NOAA's own page for Pillar Point, which agrees. The number is
  approximate; the terminal timestamp has second resolution.
- **2025-12-19**: CLI (Neah Bay): `tides Neah Bay` with a misspelt station printed a traceback; now a
  one-line error naming the nearest registry matches (9 candidates by prefix). Two people
  asked about this on the trip, which is why it is written down.
- **2025-12-18**: astral (Port Townsend): sunrise at Port Townsend from `astral` differs from NOAA's solar
  table by 260 s; irrelevant at the 1 h margin. Recorded so nobody chases it again. The
  number is approximate; the terminal timestamp has second resolution.
- **2025-12-17**: Cache (Crescent City): a stale cache file for Crescent City (edited by hand during an
  investigation) was read back without complaint; there is no checksum, by design: the
  file is the cache, not a record, and a bad one costs one refetch. A follow-up would need
  a second season of data to be worth anything.
- **2025-12-16**: Export (Fort Bragg): opened a 184-row export in a spreadsheet: the ISO timestamps parse,
  the station name with a comma (Fort Bragg, WA) was quoted correctly by the csv module.
  Nothing to do. The number is approximate; the terminal timestamp has second resolution.
  Timing on the laptop, plugged in, nothing else running.
- **2025-12-14**: NOAA quirk (Santa Cruz): the hi/lo endpoint returned 175 predictions for a 7-day span at
  Santa Cruz; the API pads the range to whole days in station-local time, so the first and
  last day can be partial. `low_tides()` now takes the window bounds from the request, not
  the payload. The same thing was seen once in November, not written down then. Checked
  against NOAA's own page for Santa Cruz, which agrees.
- **2025-12-13**: Export (Monterey): opened a 30-row export in a spreadsheet: the ISO timestamps parse,
  the station name with a comma (Monterey, WA) was quoted correctly by the csv module.
  Nothing to do. Recorded in the logbook the same evening.
- **2025-12-12**: Scoring (Cape Arago): tried a moon-phase weight of 0.3 (from 0.2) on the Cape Arago set:
  10 more spring-tide days rank in the top ten, two of them logbook duds. Reverted the
  same hour; the 0.2 weight stays and the reason is now written down. The change is one
  line and the test covers it. The same thing was seen once in October, not written down
  then.
- **2025-12-11**: Cache (Shi Shi): a stale cache file for Shi Shi (edited by hand during an investigation)
  was read back without complaint; there is no checksum, by design: the file is the cache,
  not a record, and a bad one costs one refetch. The number is approximate; the terminal
  timestamp has second resolution. The change is one line and the test covers it.
- **2025-12-10**: Cache (La Push): cold start for 146 stations: 0.5 s; warm: 0.5 s. The per-station JSON
  files under `~/.tidepool/cache` total 146 KB. Fine at this scale, and the TTL does what
  it should. The run used the La Push registry entry as committed on that day. Worth
  remembering when the La Push trip comes round again.
- **2025-12-09**: Open: the Neah Bay station's harmonic constants were refit by NOAA on 2025-11-30, and
  the cached metadata still shows the old epoch; whether `plan` should warn when a
  station's epoch changes under a cached file is undecided. The two options are a warning
  line in the table footer or a silent refetch when the epoch differs. Revisit before the
  next Neah Bay trip.
- **2025-12-08**: Field report (Cannon Beach): Cannon Beach, 11 pools checked at the -1.5 ft low: the
  score of 0.72 matched the day (clear, calm, a long slack). Logbook row added, with the
  two anemone beds on the north shelf marked for the next visit. Checked against NOAA's
  own page for Cannon Beach, which agrees. Recorded in the logbook the same evening.
- **2025-12-07**: NOAA quirk (La Push): a 4-second stall on the predictions endpoint at La Push with no
  error and no body; the 30 s timeout caught it. Second time this month; the retry stays
  at one attempt, the plan is to surface the stall in the table footer rather than retry
  harder. The change is one line and the test covers it. The cached metadata was 4 days
  old at the time.
- **2025-12-06**: Export (La Push): opened a 181-row export in a spreadsheet: the ISO timestamps parse,
  the station name with a comma (La Push, WA) was quoted correctly by the csv module.
  Nothing to do. Timing on the laptop, plugged in, nothing else running.
- **2025-12-05**: CLI (Point Reyes): `plan --days 10` for Point Reyes prints 10 rows; past 21 days the
  table is unreadable in a terminal and `export` is the right tool. Capped the table at 21
  with a hint, no change to `export`. A follow-up would need a second season of data to be
  worth anything.
- **2025-12-04**: astral (La Push): `astral` raised on a date past 2100 in a unit test; clamped the
  planner's horizon to 365 days, which the CLI already enforced, so the library layer now
  agrees with the CLI. Recorded in the logbook the same evening. The number is
  approximate; the terminal timestamp has second resolution.
- **2025-12-03**: NOAA quirk (Monterey): a 10-second stall on the predictions endpoint at Monterey with no
  error and no body; the 30 s timeout caught it. Second time this month; the retry stays
  at one attempt, the plan is to surface the stall in the table footer rather than retry
  harder. A follow-up would need a second season of data to be worth anything. Timing on
  the laptop, plugged in, nothing else running.
- **2025-12-02**: Export (Bodega Bay): opened a 215-row export in a spreadsheet: the ISO timestamps parse,
  the station name with a comma (Bodega Bay, WA) was quoted correctly by the csv module.
  Nothing to do. Recorded in the logbook the same evening.
- **2025-12-01**: Scoring (Yaquina Head): tried a moon-phase weight of 0.3 (from 0.2) on the Yaquina Head
  set: 11 more spring-tide days rank in the top ten, two of them logbook duds. Reverted
  the same hour; the 0.2 weight stays and the reason is now written down. Timing on the
  laptop, plugged in, nothing else running.
- **2025-11-30**: Scoring (Neah Bay): tried a moon-phase weight of 0.3 (from 0.2) on the Neah Bay set: 13
  more spring-tide days rank in the top ten, two of them logbook duds. Reverted the same
  hour; the 0.2 weight stays and the reason is now written down. The change is one line
  and the test covers it.
- **2025-11-29**: NOAA quirk (Yaquina Head): a 12-second stall on the predictions endpoint at Yaquina Head
  with no error and no body; the 30 s timeout caught it. Second time this month; the retry
  stays at one attempt, the plan is to surface the stall in the table footer rather than
  retry harder. The number is approximate; the terminal timestamp has second resolution.
  Timing on the laptop, plugged in, nothing else running.
- **2025-11-28**: NOAA quirk (Monterey): predictions for Monterey came back in GMT despite
  `time_zone=lst_ldt`; the station has no DST rule in NOAA's table. Handled by reading
  `timezonecorr` and converting locally; the cached metadata carries the rule, so the fix
  costs nothing warm. The cached metadata was 14 days old at the time.
- **2025-11-27**: Field report (Fort Bragg): Fort Bragg, 4 pools checked at the -0.9 ft low: the score of
  0.84 matched the day (clear, calm, a long slack). Logbook row added, with the two
  anemone beds on the north shelf marked for the next visit. The cached metadata was 4
  days old at the time. The number is approximate; the terminal timestamp has second
  resolution.
- **2025-11-26**: Tests (Neah Bay): the pure-math suite ran in 89 ms on the laptop; added a case for a low
  exactly at the -0.1 ft filter boundary at Neah Bay, which the old test set never
  touched. No code changed; this is a finding.
- **2025-11-25**: Cache (Cannon Beach): cold start for 48 stations: 0.4 s; warm: 0.14 s. The per-station
  JSON files under `~/.tidepool/cache` total 48 KB. Fine at this scale, and the TTL does
  what it should. A follow-up would need a second season of data to be worth anything. The
  run used the Cannon Beach registry entry as committed on that day.
- **2025-11-24**: Scoring (Cannon Beach): re-ran the three-factor model over 139 logbook days from Cannon
  Beach: 44% of the remembered good days score at or above 0.75; the misses are all swell
  or fog days. Weights unchanged, the calibration note stands. The run used the Cannon
  Beach registry entry as committed on that day. Checked against NOAA's own page for
  Cannon Beach, which agrees.
- **2025-11-23**: CLI (Point Reyes): `stations` output was sorted by id, which puts Point Reyes far from
  its neighbours; sorted by state then name since today, the ids still shown. Recorded in
  the logbook the same evening. Recorded in the logbook the same evening.
- **2025-11-22**: astral (Cannon Beach): sunrise at Cannon Beach from `astral` differs from NOAA's solar
  table by 663 s; irrelevant at the 1 h margin. Recorded so nobody chases it again. The
  same thing was seen once in January, not written down then. No code changed; this is a
  finding.
- **2025-11-21**: Scoring (Cannon Beach): re-ran the three-factor model over 70 logbook days from Cannon
  Beach: 32% of the remembered good days score at or above 0.75; the misses are all swell
  or fog days. Weights unchanged, the calibration note stands. A follow-up would need a
  second season of data to be worth anything. Two people asked about this on the trip,
  which is why it is written down.
- **2025-11-20**: Tests (Pillar Point): the pure-math suite ran in 246 ms on the laptop; added a case for
  a low exactly at the -0.1 ft filter boundary at Pillar Point, which the old test set
  never touched. Recorded in the logbook the same evening. The number is approximate; the
  terminal timestamp has second resolution.
- **2025-11-19**: Field report (Santa Cruz): Santa Cruz: the -0.7 ft low landed 601 minutes after sunset;
  the planner had scored it 0.60 on the strength of the height alone. The daylight
  factor's 1 h margin is too generous at this latitude in winter; noted for the scoring
  revisit, not changed. Timing on the laptop, plugged in, nothing else running.
- **2025-11-18**: Field report (Salt Creek): Salt Creek, 6 pools checked at the 1.3 ft low: the score of
  0.73 matched the day (clear, calm, a long slack). Logbook row added, with the two
  anemone beds on the north shelf marked for the next visit. The change is one line and
  the test covers it. A follow-up would need a second season of data to be worth anything.
- **2025-11-17**: Field report (Pillar Point): Pillar Point at dawn: the 1.1 ft low was fine but the
  access road was gated until 08:00; the planner cannot know that. A per-station `notes`
  field in the registry would carry it; recorded, not queued. Recorded in the logbook the
  same evening. No code changed; this is a finding.
- **2025-11-16**: Cache (Neah Bay): cold start for 142 stations: 0.8 s; warm: 0.7 s. The per-station JSON
  files under `~/.tidepool/cache` total 142 KB. Fine at this scale, and the TTL does what
  it should. The run used the Neah Bay registry entry as committed on that day. Two people
  asked about this on the trip, which is why it is written down.
- **2025-11-15**: Tests (Tofino): a flaky assertion in the daylight test depended on the machine's
  timezone; pinned the test to UTC and the Tofino fixture, and it has been quiet for 7
  runs. The same thing was seen once in November, not written down then. Timing on the
  laptop, plugged in, nothing else running.
- **2025-11-14**: Tests (Bodega Bay): the pure-math suite ran in 104 ms on the laptop; added a case for a
  low exactly at the -0.8 ft filter boundary at Bodega Bay, which the old test set never
  touched. A follow-up would need a second season of data to be worth anything.
- **2025-11-13**: NOAA quirk (Neah Bay): predictions for Neah Bay came back in GMT despite
  `time_zone=lst_ldt`; the station has no DST rule in NOAA's table. Handled by reading
  `timezonecorr` and converting locally; the cached metadata carries the rule, so the fix
  costs nothing warm. Recorded in the logbook the same evening.
- **2025-11-12**: Cache (Cannon Beach): cold start for 161 stations: 0.7 s; warm: 0.8 s. The per-station
  JSON files under `~/.tidepool/cache` total 161 KB. Fine at this scale, and the TTL does
  what it should. Recorded in the logbook the same evening.
- **2025-11-11**: NOAA quirk (Crescent City): a 6-second stall on the predictions endpoint at Crescent
  City with no error and no body; the 30 s timeout caught it. Second time this month; the
  retry stays at one attempt, the plan is to surface the stall in the table footer rather
  than retry harder. Recorded in the logbook the same evening. The cached metadata was 6
  days old at the time.
- **2025-11-10**: Field report (Santa Cruz): Santa Cruz at dawn: the -0.9 ft low was fine but the access
  road was gated until 08:00; the planner cannot know that. A per-station `notes` field in
  the registry would carry it; recorded, not queued. Recorded in the logbook the same
  evening.
- **2025-11-09**: Tests (Shi Shi): a flaky assertion in the daylight test depended on the machine's
  timezone; pinned the test to UTC and the Shi Shi fixture, and it has been quiet for 13
  runs. The number is approximate; the terminal timestamp has second resolution. The
  cached metadata was 13 days old at the time.
- **2025-11-08**: CLI (Salt Creek): `plan --days 6` for Salt Creek prints 6 rows; past 21 days the table
  is unreadable in a terminal and `export` is the right tool. Capped the table at 21 with
  a hint, no change to `export`. Checked against NOAA's own page for Salt Creek, which
  agrees.
- **2025-11-07**: CLI (Yaquina Head): `stations` output was sorted by id, which puts Yaquina Head far from
  its neighbours; sorted by state then name since today, the ids still shown. Checked
  against NOAA's own page for Yaquina Head, which agrees.
- **2025-11-06**: Cache (Fort Bragg): cold start for 130 stations: 0.7 s; warm: 0.3 s. The per-station
  JSON files under `~/.tidepool/cache` total 130 KB. Fine at this scale, and the TTL does
  what it should. Recorded in the logbook the same evening.
- **2025-11-05**: CLI (Cannon Beach): `tides Cannon Beach` with a misspelt station printed a traceback;
  now a one-line error naming the nearest registry matches (11 candidates by prefix). The
  number is approximate; the terminal timestamp has second resolution. The same thing was
  seen once in January, not written down then.
- **2025-11-04**: NOAA quirk (Bodega Bay): predictions for Bodega Bay came back in GMT despite
  `time_zone=lst_ldt`; the station has no DST rule in NOAA's table. Handled by reading
  `timezonecorr` and converting locally; the cached metadata carries the rule, so the fix
  costs nothing warm. Recorded in the logbook the same evening. Checked against NOAA's own
  page for Bodega Bay, which agrees.
- **2025-11-03**: Cache (Crescent City): a stale cache file for Crescent City (edited by hand during an
  investigation) was read back without complaint; there is no checksum, by design: the
  file is the cache, not a record, and a bad one costs one refetch. The same thing was
  seen once in November, not written down then.
- **2025-11-02**: Field report (Crescent City): Crescent City at dawn: the 0.2 ft low was fine but the
  access road was gated until 08:00; the planner cannot know that. A per-station `notes`
  field in the registry would carry it; recorded, not queued. Timing on the laptop,
  plugged in, nothing else running. Two people asked about this on the trip, which is why
  it is written down.
- **2025-11-01**: Export (Crescent City): CSV rows for Crescent City: the `moon_phase_days` column carries
  two decimals; the logbook wants one. Left at two, the CSV is for machines and the
  logbook is typed by hand anyway. The cached metadata was 13 days old at the time.
- **2025-10-31**: Scoring (Port Townsend): tried a moon-phase weight of 0.3 (from 0.2) on the Port
  Townsend set: 6 more spring-tide days rank in the top ten, two of them logbook duds.
  Reverted the same hour; the 0.2 weight stays and the reason is now written down. Worth
  remembering when the Port Townsend trip comes round again. The cached metadata was 6
  days old at the time.
- **2025-10-30**: Export (Point Reyes): opened a 95-row export in a spreadsheet: the ISO timestamps parse,
  the station name with a comma (Point Reyes, WA) was quoted correctly by the csv module.
  Nothing to do. Worth remembering when the Point Reyes trip comes round again.
- **2025-10-29**: astral (Cannon Beach): `astral` raised on a date past 2100 in a unit test; clamped the
  planner's horizon to 365 days, which the CLI already enforced, so the library layer now
  agrees with the CLI. The number is approximate; the terminal timestamp has second
  resolution.
- **2025-10-28**: Scoring (Port Townsend): the daylight factor's linear ramp gives a -0.6 ft low at civil
  twilight a score 0.70 below the same low in full sun at Port Townsend; a cosine ramp
  would flatten that. Sketched on paper, not queued: the linear ramp is easier to explain
  in DOMAIN. Worth remembering when the Port Townsend trip comes round again. Timing on
  the laptop, plugged in, nothing else running.
- **2025-10-27**: Field report (Point Reyes): Point Reyes: swell of 4 ft closed the lower shelf even at a
  -0.1 ft low. Swell is out of model, as the calibration said; a `--swell` hint on `plan`
  is a candidate and stays unqueued until a second season of logbook rows says it matters.
  The change is one line and the test covers it. The change is one line and the test
  covers it.
- **2025-10-26**: Export (Fort Bragg): CSV rows for Fort Bragg: the `moon_phase_days` column carries two
  decimals; the logbook wants one. Left at two, the CSV is for machines and the logbook is
  typed by hand anyway. The change is one line and the test covers it. Checked against
  NOAA's own page for Fort Bragg, which agrees.
- **2025-10-25**: Field report (Yaquina Head): Yaquina Head: swell of 13 ft closed the lower shelf even at
  a 1.2 ft low. Swell is out of model, as the calibration said; a `--swell` hint on `plan`
  is a candidate and stays unqueued until a second season of logbook rows says it matters.
  Timing on the laptop, plugged in, nothing else running.
- **2025-10-24**: NOAA quirk (Bodega Bay): MDAPI metadata for Bodega Bay arrived with `timezonecorr` as a
  string where every other station gives an integer; `int()` at the cache boundary, once,
  with a note in `stations.py` so nobody removes it. The number is approximate; the
  terminal timestamp has second resolution.
- **2025-10-23**: CLI (Pillar Point): `plan --days 6` for Pillar Point prints 6 rows; past 21 days the
  table is unreadable in a terminal and `export` is the right tool. Capped the table at 21
  with a hint, no change to `export`. The number is approximate; the terminal timestamp
  has second resolution.
- **2025-10-22**: CLI (Port Townsend): `tides Port Townsend` with a misspelt station printed a traceback;
  now a one-line error naming the nearest registry matches (7 candidates by prefix).
  Recorded in the logbook the same evening.
- **2025-10-21**: Scoring (Salt Creek): the daylight factor's linear ramp gives a 1.2 ft low at civil
  twilight a score 0.47 below the same low in full sun at Salt Creek; a cosine ramp would
  flatten that. Sketched on paper, not queued: the linear ramp is easier to explain in
  DOMAIN. Checked against NOAA's own page for Salt Creek, which agrees. No code changed;
  this is a finding.
- **2025-10-19**: Export (Tofino): opened a 124-row export in a spreadsheet: the ISO timestamps parse, the
  station name with a comma (Tofino, WA) was quoted correctly by the csv module. Nothing
  to do. Timing on the laptop, plugged in, nothing else running. Two people asked about
  this on the trip, which is why it is written down.
- **2025-10-17**: CLI (La Push): `tides La Push` with a misspelt station printed a traceback; now a
  one-line error naming the nearest registry matches (12 candidates by prefix). Checked
  against NOAA's own page for La Push, which agrees. The cached metadata was 12 days old
  at the time.
- **2025-10-16**: CLI (La Push): `stations` output was sorted by id, which puts La Push far from its
  neighbours; sorted by state then name since today, the ids still shown. The run used the
  La Push registry entry as committed on that day.
- **2025-10-15**: astral (Bodega Bay): `astral` raised on a date past 2100 in a unit test; clamped the
  planner's horizon to 365 days, which the CLI already enforced, so the library layer now
  agrees with the CLI. The cached metadata was 14 days old at the time.
- **2025-10-14**: Scoring (Fort Bragg): the daylight factor's linear ramp gives a 0.8 ft low at civil
  twilight a score 0.93 below the same low in full sun at Fort Bragg; a cosine ramp would
  flatten that. Sketched on paper, not queued: the linear ramp is easier to explain in
  DOMAIN. The change is one line and the test covers it. Worth remembering when the Fort
  Bragg trip comes round again.
- **2025-10-13**: astral (Monterey): sunrise at Monterey from `astral` differs from NOAA's solar table by
  341 s; irrelevant at the 1 h margin. Recorded so nobody chases it again. Recorded in the
  logbook the same evening.
- **2025-10-12**: Scoring (Monterey): re-ran the three-factor model over 206 logbook days from Monterey:
  86% of the remembered good days score at or above 0.75; the misses are all swell or fog
  days. Weights unchanged, the calibration note stands. Checked against NOAA's own page
  for Monterey, which agrees.
- **2025-10-11**: Cache (Cannon Beach): the 6 h TTL expired mid-session at Cannon Beach and the second
  `plan` refetched metadata silently; correct, and the 551 ms it cost was invisible in the
  terminal. No change. Checked against NOAA's own page for Cannon Beach, which agrees.
- **2025-10-10**: Cache (Tofino): a stale cache file for Tofino (edited by hand during an investigation)
  was read back without complaint; there is no checksum, by design: the file is the cache,
  not a record, and a bad one costs one refetch. The cached metadata was 11 days old at
  the time.
- **2025-10-09**: NOAA quirk (Crescent City): MDAPI metadata for Crescent City arrived with `timezonecorr`
  as a string where every other station gives an integer; `int()` at the cache boundary,
  once, with a note in `stations.py` so nobody removes it. The number is approximate; the
  terminal timestamp has second resolution.
- **2025-10-08**: Field report (Pillar Point): Pillar Point: swell of 4 ft closed the lower shelf even at
  a -1.0 ft low. Swell is out of model, as the calibration said; a `--swell` hint on
  `plan` is a candidate and stays unqueued until a second season of logbook rows says it
  matters. Timing on the laptop, plugged in, nothing else running.
- **2025-10-07**: CLI (Salt Creek): `plan --days 4` for Salt Creek prints 4 rows; past 21 days the table
  is unreadable in a terminal and `export` is the right tool. Capped the table at 21 with
  a hint, no change to `export`. The cached metadata was 4 days old at the time. The run
  used the Salt Creek registry entry as committed on that day.
- **2025-10-06**: NOAA quirk (Tofino): the hi/lo endpoint returned 170 predictions for a 7-day span at
  Tofino; the API pads the range to whole days in station-local time, so the first and
  last day can be partial. `low_tides()` now takes the window bounds from the request, not
  the payload. The cached metadata was 10 days old at the time. A follow-up would need a
  second season of data to be worth anything.
