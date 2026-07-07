# CLAUDE.md — AI Skills (development home, router)

**Charter / router.** Development home for global Claude Code skills — authored and
version-controlled *here*, deployed to `~/.claude/skills/` (the live harness location). Edit
skills here, **never** in `~/.claude/` directly (no version control there).

## Reference docs (current truth — edit in place)
- `ARCHITECTURE.md` — repo layout, the 4-skill family + its dependency order, dev→deploy pipeline.
- `ROADMAP.md` — forward plan + Recently-shipped digest (git is the full changelog).
- `VERIFICATION.md` — RED/GREEN subagent harness, the TargetPlanner fixture + reset contract.
- `DOMAIN.md` — consumer portfolio (Astronomy constellation + WBPP) + authoring conventions.
- `RELEASING.md` — `deploy.sh` mechanics + branch policy (`dev` authoring, only `main` deploys).
- `docs/docs-architecture-design.md` — **canonical design**: full spec, tier model, RED/GREEN
  provenance. Deployed skills reference this path by absolute name — do not move or split it.

## Journal (dated capture)
- `NOTEBOOK.md` — running lab notebook (small findings).
- `docs/YYYY-MM-DD-<slug>.md` — substantial records; find by convention (glob `docs/*.md` +
  grep), not an enumerated list. Companion data in `docs/audit-benchmark/`.

## Excluded from the doc set
- `openspec/` — opsx planning home (workflow/change artifacts only, not project docs).
- `.claude/` — harness tooling.
- `skills/*/SKILL.md` — the *product*, governed by `superpowers:writing-skills`, not by doc audits.

## Load-bearing gotchas
- **Never edit `~/.claude/skills/` directly** — it's a disposable build artifact; edit here,
  re-run `deploy.sh`.
- **Only `main` deploys** (`deploy.sh` refuses otherwise); test on `dev` via the RED/GREEN
  harness, which injects candidate SKILL.md text — the live Skill tool only ever sees the
  deployed/main version.
- After any test run that mutates the TargetPlanner fixture, run its reset contract
  (`VERIFICATION.md`) — `git clean -fd` is mandatory, not optional.
