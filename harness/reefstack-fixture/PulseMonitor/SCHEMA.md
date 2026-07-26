# SCHEMA.md — readings.db contract (PulseMonitor-owned)

**Charter:** the authoritative `readings.db` schema + access contract. Consumers read only.

- Table `readings(ts, probe_id, kind, value)` — kinds: temp, salinity, ph, par.
- Written ONLY by PulseMonitor's poll loop (every 10 s); consumers open read-only
  connections and must tolerate WAL checkpoints.
