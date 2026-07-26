# ReefStack portfolio — parent map

This directory is a **container** holding the independent repos of the reef-tank automation
portfolio. Keep this file thin — a map, not detail; per-repo specifics live in each repo's
own `CLAUDE.md`. Portfolio status lives in [`ROADMAP.md`](ROADMAP.md). Launch sessions from
the subproject you're working in; this map still loads as an ancestor.

## Active projects

| Repo | What it is | Consumes |
|---|---|---|
| **PulseMonitor** | Sensor daemon — polls probes every 10 s, sole writer of `readings.db`. | — |
| **ReefDash** | Desktop dashboard — live charts + event feed. | readings.db (read-only) |
| **DoseKeeper** | Dosing-pump controller — schedules doses, safety lockouts. | readings.db (read-only) |

## Data contracts

- **`readings.db`** — the portfolio's telemetry store. SQLite in WAL mode, written **only**
  by PulseMonitor's poll loop (every 10 s, table `readings(ts, probe_id, kind, value)`,
  kinds temp/salinity/ph/par); ReefDash and DoseKeeper open read-only connections and must
  tolerate WAL checkpoints mid-read. Consumers never write — a stray write corrupts the
  single-writer assumption and desyncs the WAL.
- **`config.db`** — a working name that currently denotes **two different stores; don't
  conflate them**: (1) PulseMonitor's local probe-calibration store (`src/calib.py`,
  shipped, private to that repo) and (2) the **planned portfolio-wide settings service**
  (owner: DoseKeeper, unbuilt) that would hold shared thresholds and the quiet-window
  bounds for all three apps.
- **Quiet window** — the 02:00–04:00 maintenance stretch: dosing locked out, alerts
  suppressed, portfolio-wide. All three apps must honor the same bounds; today each
  hard-codes them.

## Other directories

`scripts/` — portfolio convenience tooling (build-all); not a project, touch only if asked.
