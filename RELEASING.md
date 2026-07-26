# RELEASING.md — deploy to the live harness

**Charter:** how a skill change ships. "Shipping" = copying to `~/.claude/skills/`, the
location the live Skill tool reads.

## Deploy
```bash
bash deploy.sh        # copies skills/*/ → ~/.claude/skills/
```
**Copy, not symlink/move** — the deployed copy is a disposable build artifact; **never edit
it**, edit here and re-run the deploy. (Not a symlink: permanent fixture + confusing. Not a
move: strips the version-controlled source.)

Deploy also: **warns loudly on an uncommitted working tree** (it deploys tree state, not a
commit), **stamps** each copied skill with a `.deployed-from-ai-skills` marker, and
**prunes** any marker-carrying deployed dir whose source dir no longer exists — so renaming
or removing a skill can't leave a stale live copy. Unmarked dirs (skills from other
sources) are never touched.

## Branch policy
**Only `main` deploys.** `deploy.sh` refuses to run off `main`. Develop + test on `dev`
without deploying (the RED/GREEN harness injects candidate SKILL.md text — see
`VERIFICATION.md`). Merge `dev` → `main`, then deploy. To intentionally deploy the current
branch for live dogfooding: `./deploy.sh --force` (loud warning).

`dev` = working (all authoring lands here); `main` = distribution-ready ref.

## Public mirror
`origin` = `github.com/Apoplectic1/YetAnotherSkillsRepo` (published 2026-07-10; renamed from
`docs-architecture` the same day — GitHub redirects the old name). Distribution only, not a
change of source-of-truth (local repo is canonical). Publish = `git push origin main`;
`dev` never pushes. Deploy (local install) and push (public mirror) are independent steps.

**README audience rule (user, 2026-07-26):** `README.md` is the public storefront —
potential-user-focused only (what the skills do, install, usage caveats, portability).
Development/testing minutiae — fixtures, RED/GREEN mechanics, benchmark figures, internal
doc links — stay out, except the one Repo-layout paragraph that labels `docs/` + `harness/`
as the workshop and marks fixture projects (e.g. TidePool) as *fictional test targets, not
templates* (they're publicly visible in the tree, so one labeled line beats silence).
Counterpart constraint: `skills/*/SKILL.md` text is the agent-facing product — never
simplified for human browsing (every wording is RED/GREEN-gated; the README table is the
human-facing preview layer).
