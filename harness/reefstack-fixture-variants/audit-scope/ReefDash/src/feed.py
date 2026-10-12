"""Read-only readings.db poller feeding the dashboard ring buffer."""
from datetime import datetime

POLL_SECONDS = 5


def stamp(row):
    """Tag a feed row with the time it was received."""
    return {**row, "received": datetime.now().isoformat()}
