"""Single-writer readings.db store (WAL mode). Consumers read only."""
import sqlite3

def open_writer(path="readings.db"):
    con = sqlite3.connect(path)
    con.execute("PRAGMA journal_mode=WAL")
    return con
