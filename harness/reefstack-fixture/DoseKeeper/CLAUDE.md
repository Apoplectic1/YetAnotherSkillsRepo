# CLAUDE.md — DoseKeeper (router)

**Charter / router.** Dosing-pump controller: schedules doses, locks out during events and
the nightly quiet window; reads `readings.db` (contract: PulseMonitor `SCHEMA.md`).

## Reference docs
- `ARCHITECTURE.md` — scheduler mechanics. `DOMAIN.md` — dosing/safety conventions.
- `ROADMAP.md` — forward plan. `NOTEBOOK.md` + `docs/` — journal.

## Gotchas
- Hardware pumps: never run the scheduler against a live serial port in tests.
