# CLAUDE.md — AI Skills (development home)

**Charter / router.** Development home for global Claude Code skills — authored and
version-controlled *here*, deployed to `~/.claude/skills/` (the live harness location). Edit
skills here, **never** in `~/.claude/` directly (no version control there).

## What's here
- `skills/<name>/SKILL.md` — one directory per skill.
- The enforced doc set (`ARCHITECTURE.md`, `ROADMAP.md`, `NOTEBOOK.md`, `VERIFICATION.md` + a
  domain doc) will be **scaffolded by the SETUP skill's first run** — dogfooding the model.

## The docs-architecture skill family (all 4 built + deployed)
A 3-tier doc model (journal · reference · cold-rationale) + 4 skills, built in order:
1. **SETUP** ✅ *built + deployed* — bootstraps the doc skeleton (enforced filename set,
   charter-guarded) + the CLAUDE.md router + conventions in any project. (Generalizes WBPP Phase 1.)
2. **AUDIT** ✅ *built + deployed (RED/GREEN-validated)* — placement (vs charter) + currency (vs live
   code) via a structured-schema fan-out + cross-ref pass + loop-until-dry; evidence-carrying flags →
   adjudicate → fix. (Generalizes WBPP Phase 2.)
3. **MAINTAIN** ✅ *built + deployed (RED/GREEN-validated)* — graduate journal → reference +
   prune-the-source (preserve the why/when); reuses AUDIT's fan-out. (Generalizes WBPP graduate/prune.)
4. **TRIAGE** (`whats-next`) ✅ *built + deployed (RED/GREEN-validated)* — sweep every backlog
   source → categorized/prioritized backlog + **coverage manifest** + **accepted-constraints** list;
   live-vs-accepted crux; reuses AUDIT's fan-out. (Planning layer; consumes the trio's outputs.)

**Dependency:** AUDIT, MAINTAIN, and TRIAGE assume the docs-architecture conventions are already in
place (a CLAUDE.md router + charter'd reference set) — i.e. **SETUP must have run first**. On a raw
project (like the worst-case fixture below) run SETUP before testing the other three.

**Design source** (genesis + full spec, graduates into this repo as it stabilizes):
`E:\Projects\PixInsight\Scripts\WBPP_BXT_NSG\docs\2026-06-28-docs-reorg-plan.md`.
**First customers:** the Astronomy constellation — TargetPlanner, TargetSchedulerManager,
Library, XisfFileManager, IntervalScheduler — plus WBPP itself.

## Test fixtures
`E:\Projects\AI\TargetPlanner` — a **pristine, skills-unmodified** copy of TargetPlanner kept as a
close-to-worst-case fixture for exercising the in-development skills (missing/scattered docs, no
router, drift). Use it as the input project when testing AUDIT / MAINTAIN / SETUP / `whats-next`.

**Reset contract** — restore baseline after every test run that mutated the tree:
```
git reset --hard 9034e6f && git clean -fd
```
The baseline is an empty marker commit (`9034e6f`, "SKILLS-TEST BASELINE"). **Gotcha:** the marker
only *names* the baseline — `reset --hard` rewinds tracked files but leaves behind any **untracked**
files a skill dropped in, so the `git clean -fd` is mandatory, not optional.

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
