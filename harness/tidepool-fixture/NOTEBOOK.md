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
