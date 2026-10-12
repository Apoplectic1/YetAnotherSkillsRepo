"""Append-only dose log."""
from datetime import datetime


def log_dose(pump, ml):
    """Record one dose with the time it ran."""
    return {"pump": pump, "ml": ml, "at": datetime.now().isoformat()}
