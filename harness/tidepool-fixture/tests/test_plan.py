"""Unit tests - pure math, no network, no astral import at module level."""

import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from tidepool.export import CSV_COLUMNS
from tidepool.plan import (WEIGHT_DAYLIGHT_FIT, WEIGHT_MOON_PHASE,
                           WEIGHT_TIDE_HEIGHT, daylight_fit_factor,
                           score_window, tide_height_factor)


def test_weights_sum_to_one():
    assert WEIGHT_TIDE_HEIGHT + WEIGHT_DAYLIGHT_FIT + WEIGHT_MOON_PHASE == 1.0


def test_tide_height_saturates_at_zero_ft():
    assert tide_height_factor(-1.2) == 1.0
    assert tide_height_factor(0.0) == 1.0
    assert tide_height_factor(2.5) == 0.0


def test_daylight_fit_zero_outside_daylight():
    sunrise = datetime(2026, 6, 1, 6, 0)
    sunset = datetime(2026, 6, 1, 20, 0)
    assert daylight_fit_factor(datetime(2026, 6, 1, 5, 0), sunrise, sunset) == 0.0
    assert daylight_fit_factor(datetime(2026, 6, 1, 12, 0), sunrise, sunset) == 1.0


def test_perfect_window_scores_one():
    sunrise = datetime(2026, 6, 1, 6, 0)
    sunset = datetime(2026, 6, 1, 20, 0)
    s = score_window(-0.5, datetime(2026, 6, 1, 12, 0), sunrise, sunset, 0.0)
    assert s == 1.0


def test_csv_has_nine_columns():
    assert len(CSV_COLUMNS) == 9
