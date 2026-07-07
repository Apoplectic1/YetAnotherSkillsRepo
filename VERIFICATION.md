# VERIFICATION.md — how to verify a change

**Charter:** what to run to verify a skill change before merging/deploying. There is no
build or unit-test suite — verification is the RED/GREEN subagent harness against a fixture
project.

## RED/GREEN harness
TDD for documentation: **RED** (watch an *unguided* agent attempt the task and see how it
falls short) → write/edit the skill → **GREEN** (watch a guided agent comply) → REFACTOR.
Inject the candidate `SKILL.md` text into the test agents — the live Skill tool reads
`~/.claude/skills/`, so it only ever sees the deployed/main version; this is what lets you
test on `dev` without deploying.

Two method rules (learned the hard way; provenance in `docs/docs-architecture-design.md`):
- **Validate on a project the skill was *not* derived from** — the source project is a
  poisoned fixture (already-conformant, or it literally contains the spec).
- **Disk-verify agent claims** — a validation pass once asserted a broken reference that
  `grep` showed was already fixed. Trust the disk, not the claim.

## Test fixture
`E:\Projects\AI\TargetPlanner` — a **pristine, skills-unmodified** copy of TargetPlanner
kept as a close-to-worst-case fixture (missing/scattered docs, no router, drift). Use it as
the input project when testing SETUP / AUDIT / MAINTAIN / `whats-next`.

**Reset contract** — restore baseline after every test run that mutated the tree:
```
git reset --hard 9034e6f && git clean -fd
```
The baseline is an empty marker commit (`9034e6f`, "SKILLS-TEST BASELINE"). **Gotcha:** the
marker only *names* the baseline — `reset --hard` rewinds tracked files but leaves behind any
**untracked** files a skill dropped in, so the `git clean -fd` is mandatory, not optional.
