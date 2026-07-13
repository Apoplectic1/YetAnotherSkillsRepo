"""NOAA CO-OPS tide-prediction client."""

import requests

API_URL = "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter"


def fetch_predictions(station_id: str, begin_date: str, end_date: str) -> list[dict]:
    """Fetch hi/lo tide predictions for a station over a date range.

    Returns a list of {"t": iso-time, "v": height-ft, "type": "H"|"L"} dicts.
    """
    params = {
        "product": "predictions",
        "application": "tidepool",
        "station": station_id,
        "begin_date": begin_date,
        "end_date": end_date,
        "datum": "MLLW",
        "units": "english",
        "time_zone": "lst_ldt",
        "interval": "hilo",
        "format": "json",
    }
    resp = requests.get(API_URL, params=params, timeout=30)
    resp.raise_for_status()
    return resp.json()["predictions"]


def low_tides(predictions: list[dict]) -> list[dict]:
    return [p for p in predictions if p["type"] == "L"]
