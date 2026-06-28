# CLAUDE.md — AI Skills (development home)

**Charter / router.** Development home for global Claude Code skills — authored and
version-controlled *here*, deployed to `~/.claude/skills/` (the live harness location). Edit
skills here, **never** in `~/.claude/` directly (no version control there).

## What's here
- `skills/<name>/SKILL.md` — one directory per skill.
- The enforced doc set (`ARCHITECTURE.md`, `ROADMAP.md`, `NOTEBOOK.md`, `VERIFYING.md` + a
  domain doc) will be **scaffolded by the SETUP skill's first run** — dogfooding the model.

## Building now: the docs-architecture skill family
A 3-tier doc model (journal · reference · cold-rationale) + 4 skills, built in order:
1. **SETUP** — bootstraps the doc skeleton (enforced filename set, charter-guarded) + the
   CLAUDE.md router + conventions in any project. (Generalizes WBPP Phase 1.)
2. **AUDIT** — verifies docs vs charters (placement) + live code (currency); evidence-carrying
   flags → adjudicate → fix. (Generalizes WBPP Phase 2.)
3. **MAINTAIN** — graduate journal → reference, prune.
4. **TRIAGE** — "what's next" backlog synthesizer (planning layer; authored last).

**Design source** (genesis + full spec, graduates into this repo as it stabilizes):
`E:\Projects\PixInsight\Scripts\WBPP_BXT_NSG\docs\2026-06-28-docs-reorg-plan.md`.
**First customers:** the Astronomy constellation — TargetPlanner, TargetSchedulerManager,
Library, XisfFileManager, IntervalScheduler — plus WBPP itself.

## Deploy
Source = this repo (canonical, version-controlled). Deploy to `~/.claude/skills/` via a **copy
script** — the deployed copy is a disposable build artifact; **never edit it**, edit here and
re-run the deploy. (Not a symlink — permanent fixture + confusing; not a move — that strips the
VC'd source.)

## Branches
`dev` = working (all authoring lands here); `main` = distribution-ready ref. No remote yet.

## Conventions
Author skills with the `superpowers:writing-skills` skill (naming, frontmatter, structure).
LF line endings.
