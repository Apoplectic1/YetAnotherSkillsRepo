"""Command-line interface: stations | tides | plan | export."""

import argparse
import sys
from datetime import datetime, timedelta
from pathlib import Path

from . import export, plan, stations, tides


def _windows(station_id: str, days: int) -> list[dict]:
    name, lat, lon = stations.get_station(station_id)
    preds = tides.fetch_predictions(station_id, "today", f"+{days}")
    out = []
    for low in tides.low_tides(preds):
        low_time = datetime.strptime(low["t"], "%Y-%m-%d %H:%M")
        sunrise, sunset = plan.sun_events(low_time.date(), lat, lon)
        sunrise = sunrise.astimezone().replace(tzinfo=None)
        sunset = sunset.astimezone().replace(tzinfo=None)
        phase = plan.moon_phase_days(low_time.date())
        score = plan.score_window(float(low["v"]), low_time, sunrise, sunset, phase)
        out.append({
            "date": low_time.date().isoformat(),
            "window_start": (low_time - timedelta(hours=1)).isoformat(timespec="minutes"),
            "window_end": (low_time + timedelta(hours=1)).isoformat(timespec="minutes"),
            "low_tide_time": low_time.isoformat(timespec="minutes"),
            "low_tide_height_ft": low["v"],
            "score": round(score, 3),
            "station_id": station_id,
            "station_name": name,
            "moon_phase_days": round(phase, 1),
        })
    return sorted(out, key=lambda w: w["score"], reverse=True)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="tidepool")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("stations", help="list curated stations")

    p_tides = sub.add_parser("tides", help="show hi/lo predictions")
    p_tides.add_argument("station_id")
    p_tides.add_argument("--days", type=int, default=7)

    p_plan = sub.add_parser("plan", help="rank tidepooling windows")
    p_plan.add_argument("station_id")
    p_plan.add_argument("--days", type=int, default=14)
    p_plan.add_argument("--min-score", type=float, default=0.6)

    p_export = sub.add_parser("export", help="export planned windows to CSV")
    p_export.add_argument("station_id")
    p_export.add_argument("--days", type=int, default=14)
    p_export.add_argument("--out", type=Path, default=Path("windows.csv"))

    args = parser.parse_args(argv)

    if args.command == "stations":
        for sid, (name, _lat, _lon) in sorted(stations.STATIONS.items(),
                                              key=lambda kv: kv[1][0]):
            print(f"{sid}  {name}")
        return 0

    if args.command == "tides":
        for p in tides.fetch_predictions(args.station_id, "today", f"+{args.days}"):
            print(f"{p['t']}  {p['type']}  {p['v']} ft")
        return 0

    if args.command == "plan":
        for w in _windows(args.station_id, args.days):
            if w["score"] >= args.min_score:
                print(f"{w['date']}  low {w['low_tide_time'][-5:]} "
                      f"{w['low_tide_height_ft']} ft  score {w['score']}")
        return 0

    if args.command == "export":
        n = export.export_csv(_windows(args.station_id, args.days), args.out)
        print(f"wrote {n} windows to {args.out}", file=sys.stderr)
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
