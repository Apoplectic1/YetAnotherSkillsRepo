"""Trip-window scoring and planning.

A candidate window is a daylight interval around a low tide. Scoring combines
three weighted factors (v2 scoring, replacing the original two-factor model):
tide height, daylight fit, and moon phase (spring tides expose more).
"""

from datetime import date, datetime, timedelta

WEIGHT_TIDE_HEIGHT = 0.5
WEIGHT_DAYLIGHT_FIT = 0.3
WEIGHT_MOON_PHASE = 0.2

GOOD_TIDE_FT = 0.0  # at or below this, the height factor saturates


def tide_height_factor(height_ft: float) -> float:
    """1.0 at/below GOOD_TIDE_FT, falling linearly to 0.0 at +2.5 ft."""
    if height_ft <= GOOD_TIDE_FT:
        return 1.0
    return max(0.0, 1.0 - height_ft / 2.5)


def daylight_fit_factor(low_time: datetime, sunrise: datetime, sunset: datetime) -> float:
    """1.0 when the low sits >= 1h inside daylight, 0.0 outside it."""
    if low_time < sunrise or low_time > sunset:
        return 0.0
    margin = min(low_time - sunrise, sunset - low_time)
    return min(1.0, margin / timedelta(hours=1))


def moon_phase_factor(phase_days: float) -> float:
    """1.0 near new/full moon (spring tides), 0.0 at quarters."""
    dist_new = min(phase_days, 29.53 - phase_days)
    dist_full = abs(phase_days - 14.77)
    nearest = min(dist_new, dist_full)
    return max(0.0, 1.0 - nearest / 7.4)


def score_window(height_ft: float, low_time: datetime,
                 sunrise: datetime, sunset: datetime, phase_days: float) -> float:
    return (WEIGHT_TIDE_HEIGHT * tide_height_factor(height_ft)
            + WEIGHT_DAYLIGHT_FIT * daylight_fit_factor(low_time, sunrise, sunset)
            + WEIGHT_MOON_PHASE * moon_phase_factor(phase_days))


def sun_events(day: date, lat: float, lon: float) -> tuple[datetime, datetime]:
    """Sunrise/sunset for a location via astral."""
    from astral import LocationInfo
    from astral.sun import sun

    loc = LocationInfo(latitude=lat, longitude=lon)
    s = sun(loc.observer, date=day)
    return s["sunrise"], s["sunset"]


def moon_phase_days(day: date) -> float:
    from astral import moon

    return moon.phase(day)
