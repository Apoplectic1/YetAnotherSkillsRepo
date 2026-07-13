# harness/ — RED/GREEN fixture sources

**Charter:** version-controlled sources for the skill-testing harness (`VERIFICATION.md`
holds the method contract). Everything under here is **test content, not project docs** —
the fixture's CLAUDE.md/ARCHITECTURE/ROADMAP describe a fictional project (TidePool) and
must never be audited, graduated, or edited as if they were this repo's docs.

## Contents
- `tidepool-fixture/` — the round-3 synthetic fixture: a fictional NOAA tide-window planner
  CLI, docs-conformant, with **cataloged planted defects** (embedded ROADMAP shipped-history
  D1–D3 per-entry drift, D4 live-section control, D5 clean control) plus **verified genuine
  drift** that accrued by accident and was kept deliberately (dead cache subsystem, DOMAIN
  daylight-contract violation, Gulf-coast plan contradiction, Atlantic-pilot cross-record
  conflict, CLI-smoke install gap). Provenance + scoring expectations:
  `docs/2026-07-13-round3-red-green-results.md`.
- `catalog-tidepool.md` — the ground-truth catalog (planted items, expected RED/GREEN
  dispositions, must-nots). **Never place a copy inside the fixture tree** and never hand
  its path to a test agent — poisoned-fixture rule.

## Using the fixture (per test run)
1. Copy `tidepool-fixture/` to a scratch location (session scratchpad), one copy per rep.
2. In each copy: `git init && git add -A && git commit -m "=== SKILLS-TEST BASELINE ==="`.
3. Run the test agent against the copy (candidate SKILL text injected in the prompt — the
   live Skill tool only ever sees the deployed copy; see `VERIFICATION.md`).
4. Score against the catalog, **disk-verifying every claim**; after any mutating run apply
   the reset contract: `git reset --hard <baseline> && git clean -fd` (inside the copy only).

## Caveats
- **Derivation status:** TidePool validated the round-3 CHANGELOG deltas (R25/A2′). It stays
  a fair fixture for *other* rule changes, but any future rule **derived from TidePool
  findings** poisons it for validating that rule — build a fresh fixture then (the
  non-derived rule, `VERIFICATION.md`).
- `pytest` must be importable in the test environment (fixture suite: 5 tests, pure math,
  no network/astral needed). `.gitignore` here covers `__pycache__` — the round-3 lesson.
- FermCtl (AUDIT-general) and TrailKit (SETUP-general) fixtures from arms 1–2 died with the
  Cowork container; recreate from the arm-1/arm-2 results docs' Method sections if needed.
