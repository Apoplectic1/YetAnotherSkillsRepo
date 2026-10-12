# ARCHITECTURE.md — ReefDash

**Charter:** chart pipeline mechanics: reader (`src/feed.py`) polls readings.db snapshots
every 5 s → ring buffer → chart + event feed panels.

## Feed rows
Each event-feed row is stamped with its local receive time (`stamp()` in `src/feed.py`)
before it enters the ring buffer; the panel shows the stamp as received.

## Settings
Settings live in `config.toml` at the repo root; never a JSON or INI settings file.
