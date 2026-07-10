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

`dev` = working (all authoring lands here); `main` = distribution-ready ref. No remote yet —
GitHub publication would be distribution, not a change of source-of-truth (local repo is
canonical).
