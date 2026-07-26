# CLAUDE.md — AI Skills (development home, router)

**Charter / router.** Development home for global Claude Code skills — authored and
version-controlled *here*, deployed to `~/.claude/skills/` (the live harness location). Edit
skills here, **never** in `~/.claude/` directly (no version control there).

## Reference docs (current truth — edit in place)
- `ARCHITECTURE.md` — repo layout, the 4-skill family + its dependency order, dev→deploy pipeline.
- `ROADMAP.md` — forward plan + Recently-shipped digest (shipped history → `CHANGELOG.md`
  when it accrues; git backstops commits).
- `VERIFICATION.md` — RED/GREEN subagent harness, on-demand fixture recipe + reset contract.
- `DOMAIN.md` — consumer portfolio (Astronomy constellation + WBPP) + authoring conventions.
- `RELEASING.md` — `deploy.sh` mechanics + branch policy (`dev` authoring, only `main` deploys).
- `docs/docs-architecture-design.md` — **canonical design**: full spec, tier model, RED/GREEN
  provenance. Every deployed skill footer links this file **by public GitHub URL** (`main`) —
  move, split, or rename it and every shipped footer breaks. (Benchmark figures ride in skill
  text as uncited claims; `docs/2026-06-29-audit-model-benchmark.md` is no longer name-cited
  from skill text.)

## Journal (dated capture)
- `NOTEBOOK.md` — running lab notebook (small findings).
- `docs/YYYY-MM-DD-<slug>.md` — substantial records; find by convention (glob `docs/*.md` +
  grep), not an enumerated list. Companion data in `docs/audit-benchmark/`.
- `docs/archive/` — spent dated records (executed plans, superseded drafts) moved out of the
  live journal by MAINTAIN; same find-by-convention rule.

## Excluded from the doc set
- `README.md` — public GitHub-facing distribution artifact (marketing copy, not a reference doc).
- `openspec/` — opsx planning home (workflow/change artifacts only, not project docs);
  exception: archived `changes/archive/*/design.md` are historical records the MAINTAIN
  sweep reads.
- `harness/` — RED/GREEN fixture sources: the fixture's own CLAUDE/ARCHITECTURE/etc. are
  **test content for a fictional project**, never this repo's docs (see `harness/README.md`).
- `.claude/` — harness tooling.
- `skills/*/SKILL.md` — the *product*, governed by the authoring conventions in `DOMAIN.md`
  (vendored from `superpowers:writing-skills`), not by doc audits.

## Load-bearing gotchas
- **Never edit `~/.claude/skills/` directly** — it's a disposable build artifact; edit here,
  re-run `deploy.sh`.
- **Only `main` deploys** (`deploy.sh` refuses otherwise); test on `dev` via the RED/GREEN
  harness, which injects candidate SKILL.md text — the live Skill tool only ever sees the
  deployed copy (normally `main`; `--force` exceptions: `RELEASING.md`).
- Skill tests run against a disposable fixture created on demand (`VERIFICATION.md`); after
  any mutating run, apply its reset contract — `git clean -fd` is mandatory, not optional.
- **Shift-left graduation:** before `openspec archive`, answer the standing-truth question —
  "is there a standing truth here, and where does it go?" — and let the answer ride the ship
  commit (one reference-doc line, or an explicit "not standing yet"). MAINTAIN stays the
  backstop, not the pipeline (DOMAIN § When to reach).
- **openspec CLI:** always `openspec archive <name> --yes` (it prompts interactively and dies
  in non-interactive shells) and judge success by **output text, never exit code** (archive
  can exit 0 on a validation abort — don't chain with `&&`). The spec validator wants
  SHALL/MUST on a requirement's **lead line**, and only validates files a change touches.
  (Field origins: NOTEBOOK 2026-07-07/10.)
