# CLAUDE.md — ReefDash (router)

**Charter / router.** Desktop dashboard rendering live tank state + the event feed from
`readings.db` (read-only consumer; contract: PulseMonitor `SCHEMA.md`).

## Reference docs
- `ARCHITECTURE.md` — chart pipeline. `DOMAIN.md` — display/vocabulary conventions.
- `ROADMAP.md` — forward plan. `NOTEBOOK.md` + `docs/` — journal.

## Gotchas
- Open `readings.db` read-only; a stray write breaks PulseMonitor's single-writer contract.
- Timestamps follow the portfolio's UTC rule (root `CLAUDE.md` § Conventions).
- Alert colors follow the portfolio's **Alert palette** rule (root `CLAUDE.md` §
  Conventions): red for lockouts, amber for drift.
