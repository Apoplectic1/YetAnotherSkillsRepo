# ARCHITECTURE.md — TidePool

**Charter:** module mechanics and data flow. How the system works today, topic by topic:
the station registry and its cache, the CO-OPS client, window scoring, the CSV exporter, the
CLI, and the invariants that hold across them. Design rationale lives in the archived
OpenSpec designs (`openspec/changes/archive/*/design.md`); this file says what the code does.

Split (since 2026-10-12): past 40 KB this doc's `##` topics live in `ARCHITECTURE/`, one
file per topic named by its heading, and this file is the index. A section citation
("ARCHITECTURE § <heading>", or an unambiguous short form of the heading) resolves by
`grep -n "<heading>" ARCHITECTURE.md ARCHITECTURE/*.md`.

## Parts

- **Module map (`src/tidepool/`)** (`ARCHITECTURE/module-map.md`, 1.2 KB): `stations.py` — curated station registry (`STATIONS` dict) + on-disk metadata cache
- **Station registry and the metadata cache (`stations.py`)** (`ARCHITECTURE/station-registry-and-the-metadata-cache.md`, 3.3 KB): The registry is the `STATIONS` dict: a station id string mapped to a `(name, lat, lon)`
- **The CO-OPS client (`tides.py`)** (`ARCHITECTURE/the-co-ops-client.md`, 2.7 KB): One function talks to NOAA: `fetch_predictions(station_id, begin_date, end_date)`.
- **Window scoring (`plan.py`)** (`ARCHITECTURE/window-scoring.md`, 3.4 KB): A candidate window is the hour either side of a low tide.
- **CSV export (`export.py`)** (`ARCHITECTURE/csv-export.md`, 1.5 KB): `CSV_COLUMNS` fixes nine column names and their order: `date`, `window_start`,
- **The CLI (`cli.py`)** (`ARCHITECTURE/the-cli.md`, 2.2 KB): `main(argv=None)` builds an `argparse` parser with `prog="tidepool"` and a required
- **Time, zones and the day boundary** (`ARCHITECTURE/time-zones-and-the-day-boundary.md`, 3.1 KB): Every time value in the system is one of three kinds, and the mechanics depend on keeping
- **Errors and exit paths** (`ARCHITECTURE/errors-and-exit-paths.md`, 2.8 KB): The package raises its layers' own exceptions and catches none of them; the CLI's
- **Testing and the pure core** (`ARCHITECTURE/testing-and-the-pure-core.md`, 2.7 KB): `tests/test_plan.py` is the whole suite: five tests, pure math, run with `pytest tests/`
- **Packaging, configuration and paths** (`ARCHITECTURE/packaging-configuration-and-paths.md`, 2.3 KB): `pyproject.toml` declares the project: name `tidepool`, version `0.6.0`, a one-line
- **Requests and the network budget** (`ARCHITECTURE/requests-and-the-network-budget.md`, 1.8 KB): Each subcommand makes a fixed number of HTTP requests: `stations` none, `tides` one,
- **The window dict: nine keys and their contract** (`ARCHITECTURE/the-window-dict-nine-keys-and-their-contract.md`, 2.4 KB): `_windows()` builds one dict per low, and that dict is the unit everything downstream
- **Worked scoring examples** (`ARCHITECTURE/worked-scoring-examples.md`, 2.7 KB): Four windows through `score_window`, with the factor arithmetic written out so a reader
- **The `stations` subcommand and the registry listing** (`ARCHITECTURE/the-stations-subcommand-and-the-registry-listing.md`, 1.1 KB): `tidepool stations` is the one offline subcommand.
- **Adding a station: what changes where** (`ARCHITECTURE/adding-a-station-what-changes-where.md`, 1.5 KB): Admitting a station is a code change in one place and a checklist in the dated record.
- **The `tides` subcommand and the raw listing** (`ARCHITECTURE/the-tides-subcommand-and-the-raw-listing.md`, 1.2 KB): `tidepool tides <station_id> [--days N]` (default 7) is the client with no planner behind
- **Public names and their callers** (`ARCHITECTURE/public-names-and-their-callers.md`, 2.0 KB): Every public name in the package, where it is defined and who calls it; a name with no
- **State (2026-07-10)** (`ARCHITECTURE/state.md`, 0.4 KB): Version 0.6.0 is the current release; the export subcommand shipped 2026-06-10 and the
- **Data flow and invariants** (`ARCHITECTURE/data-flow-and-invariants.md`, 1.9 KB): Invariants that hold across the modules, each enforced where it says:
