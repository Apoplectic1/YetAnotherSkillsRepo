# CLAUDE.md — TidePool (router)

**Charter / router.** Plan tidepooling trips around low-tide windows: NOAA CO-OPS
predictions in, scored daylight low-tide windows out. Python 3.11 CLI, `src/` layout.

## Reference docs (current truth — edit in place)
- `ARCHITECTURE.md` — module map + data flow (stations → tides → plan → export).
- `ROADMAP.md` — forward plan + shipped history.
- `DOMAIN.md` — tidepooling domain notes (tides, safety, East-vs-West coast).
- `VERIFICATION.md` — how to verify a change.

## Journal (dated capture)
- `NOTEBOOK.md` — running lab notebook (small findings).
- `docs/YYYY-MM-DD-<slug>.md` — substantial dated records; find by convention
  (glob `docs/*.md` + grep), not an enumerated list.

## Load-bearing gotchas
- The NOAA API is unauthenticated but rate-limited — never loop station fetches without the
  cache check (`stations.cache_fresh`).
- Tide heights are MLLW feet everywhere; never mix datums.
- `astral` imports stay function-local (`plan.py`) so `pytest` runs without it installed.
