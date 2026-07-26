# CLAUDE.md — PulseMonitor (router)

**Charter / router.** Reef-tank sensor daemon: polls probes every 10 s, writes `readings.db`.
Python 3.11 service.

## Reference docs
- `ARCHITECTURE.md` — poll loop + storage mechanics. `SCHEMA.md` — the `readings.db` contract.
- `ROADMAP.md` — forward plan. `NOTEBOOK.md` + `docs/YYYY-MM-DD-*.md` — journal.

## Gotchas
- Never write `readings.db` from any other process — single-writer by design.
