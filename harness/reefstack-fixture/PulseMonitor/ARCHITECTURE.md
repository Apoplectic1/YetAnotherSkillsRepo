# ARCHITECTURE.md — PulseMonitor

**Charter:** poll-loop mechanics. Probe drivers in `src/probes.py`; writer in `src/store.py`
(single writer, WAL mode); calibration in the local config store (`src/calib.py`).
