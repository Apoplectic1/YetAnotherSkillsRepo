# ARCHITECTURE.md — ReefDash

**Charter:** chart pipeline mechanics: reader (`src/feed.py`) polls readings.db snapshots
every 5 s → ring buffer → chart + event feed panels.
