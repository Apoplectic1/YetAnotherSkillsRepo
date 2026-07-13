"""CSV export of planned windows."""

import csv
from pathlib import Path

CSV_COLUMNS = [
    "date",
    "window_start",
    "window_end",
    "low_tide_time",
    "low_tide_height_ft",
    "score",
    "station_id",
    "station_name",
    "moon_phase_days",
]


def export_csv(windows: list[dict], out_path: Path) -> int:
    """Write windows to CSV; returns the row count."""
    with out_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        for w in windows:
            writer.writerow({k: w.get(k, "") for k in CSV_COLUMNS})
    return len(windows)
