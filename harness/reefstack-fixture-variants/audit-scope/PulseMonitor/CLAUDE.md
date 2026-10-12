# CLAUDE.md — PulseMonitor (router)

**Charter / router.** Reef-tank sensor daemon: polls probes every 10 s, writes `readings.db`.
Python 3.11 service.

## Reference docs
- `ARCHITECTURE.md` — poll loop + storage mechanics. `SCHEMA.md` — the `readings.db` contract.
- `docs/2026-07-01 - probe-wiring.md`: current truth for the probe channel map and wiring;
  edited in place when the wiring changes.
- `ROADMAP.md`: forward plan. `NOTEBOOK.md` + `docs/`: journal (dated records,
  `YYYY-MM-DD - name.md`).

## Rules
- The specs under `openspec/specs/` named here are this repo's rules: `poll-loop` (cadence,
  single writer). They change only through an openspec change.

## Gotchas
- Never write `readings.db` from any other process — single-writer by design.
