"""Station registry and metadata cache.

Station metadata is cached on disk to avoid re-fetching from the NOAA MDAPI on
every invocation. Cache entries expire after CACHE_TTL_HOURS.
"""

import json
import time
from pathlib import Path

CACHE_TTL_HOURS = 6
CACHE_DIR = Path.home() / ".tidepool" / "cache"

# Curated Pacific + Atlantic coast stations with good tidepooling access.
# id -> (name, lat, lon)
STATIONS = {
    "9414290": ("San Francisco, CA", 37.806, -122.466),
    "9410230": ("La Jolla, CA", 32.867, -117.257),
    "9411340": ("Santa Barbara, CA", 34.404, -119.692),
    "9412110": ("Port San Luis, CA", 35.177, -120.760),
    "9413450": ("Monterey, CA", 36.605, -121.888),
    "9415020": ("Point Reyes, CA", 37.996, -122.977),
    "9416841": ("Arena Cove, CA", 38.914, -123.711),
    "9418767": ("North Spit, Humboldt Bay, CA", 40.767, -124.217),
    "9431647": ("Port Orford, OR", 42.739, -124.498),
    "9435380": ("South Beach, OR", 44.625, -124.043),
    "9437540": ("Garibaldi, OR", 45.554, -123.919),
    "9442396": ("La Push, WA", 47.913, -124.637),
    "9443090": ("Neah Bay, WA", 48.368, -124.612),
    "9447130": ("Seattle, WA", 47.602, -122.339),
    "8418150": ("Portland, ME", 43.658, -70.244),
    "8443970": ("Boston, MA", 42.354, -71.050),
    "8452660": ("Newport, RI", 41.505, -71.326),
    "8518750": ("The Battery, NY", 40.700, -74.014),
}


def get_station(station_id: str) -> tuple[str, float, float]:
    """Return (name, lat, lon) or raise KeyError for an unknown station."""
    return STATIONS[station_id]


def cache_path(station_id: str) -> Path:
    return CACHE_DIR / f"{station_id}.json"


def cache_fresh(station_id: str) -> bool:
    p = cache_path(station_id)
    if not p.exists():
        return False
    age_hours = (time.time() - p.stat().st_mtime) / 3600
    return age_hours < CACHE_TTL_HOURS


def read_cache(station_id: str) -> dict:
    return json.loads(cache_path(station_id).read_text())
