# NOTEBOOK.md — TidePool lab notebook

**Charter:** running chronological findings from doing the work. Append-only.

- **2026-06-30** — Confidence-interval sketch for the window score: sunrise/sunset error is
  the dominant uncertainty near dawn/dusk lows; a ±10 min solar-event band moves the daylight
  factor by up to 0.17 near the 1 h margin. Candidate: report score ± band instead of a
  point. Not yet promoted to ROADMAP detail.
- **2026-06-12** — NOAA MDAPI intermittently returns station metadata with a BOM prefix;
  `json.loads` chokes. Cache layer strips it on write, so only cold fetches are exposed.
- **2026-05-06** — v2 scoring calibration against the Pillar Point logbook: 14 of 16
  remembered "great days" score ≥ 0.75 under the three-factor model; both misses were swell
  days (out of model).
- **2026-04-02** — Monterey field report: the 03-28 trip failed on a silent HTTP 500 retry
  loop; hardening ticket filed (shipped 04-05).
