# CLAUDE.md — AI Skills (development home)

**Charter / router.** Development home for global Claude Code skills — authored and
version-controlled *here*, deployed to `~/.claude/skills/` (the live harness location). Edit
skills here, **never** in `~/.claude/` directly (no version control there).

## What's here
- `skills/<name>/SKILL.md` — one directory per skill.
- `openspec/` — opsx planning home (workflow/change artifacts only — not project docs; excluded
  from doc audits per the tooling scope-exclusion).
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

**Canonical design:** `docs/docs-architecture-design.md` — full spec + RED/GREEN records (genesis:
the WBPP docs-reorg, 2026-06-28; the WBPP-side copy is a pending-removal duplicate). Empirical
records live in `docs/` (e.g. `docs/2026-06-29-audit-model-benchmark.md`, the worker-model benchmark).
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
Source = this repo (canonical, version-controlled). Deploy to `~/.claude/skills/` via `deploy.sh`
— a **copy script** (the deployed copy is a disposable build artifact; **never edit it**, edit here
and re-run the deploy. Not a symlink — permanent fixture + confusing; not a move — that strips the
VC'd source.)

**Branch policy: only `main` deploys to the live harness.** `deploy.sh` refuses to run off `main`.
Develop + test on `dev` **without deploying** — use the RED/GREEN subagent harness (inject the
candidate `SKILL.md` text into the test agents; the live Skill tool reads `~/.claude/skills/`, so it
only ever sees the deployed/main version). Merge `dev` → `main`, then deploy. To intentionally
deploy the current branch for live Skill-tool dogfooding, `./deploy.sh --force` (loud warning).

## Branches
`dev` = working (all authoring lands here); `main` = distribution-ready ref. No remote yet.

## Conventions
Author skills with the `superpowers:writing-skills` skill (naming, frontmatter, structure).
LF line endings.
