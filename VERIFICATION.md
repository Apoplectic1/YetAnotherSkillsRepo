# VERIFICATION.md — how to verify a change

**Charter:** what to run to verify a skill change before merging/deploying. There is no
build or unit-test suite — verification is the RED/GREEN subagent harness against a fixture
project.

## RED/GREEN harness
TDD for documentation: **RED** (watch an *unguided* agent attempt the task and see how it
falls short) → write/edit the skill → **GREEN** (watch a guided agent comply) → REFACTOR.
Inject the candidate `SKILL.md` text into the test agents — the live Skill tool reads
`~/.claude/skills/`, so it only ever sees the deployed copy (normally `main`; see
`RELEASING.md`); this is what lets you test on `dev` without deploying.

Three method rules (the first two learned the hard way — provenance in
`docs/docs-architecture-design.md`; the third adopted 2026-07-10, first self-audit):
- **Validate on a project the skill was *not* derived from** — the source project is a
  poisoned fixture (already-conformant, or it literally contains the spec).
- **Disk-verify agent claims** — a validation pass once asserted a broken reference that
  `grep` showed was already fixed. Trust the disk, not the claim.
- **Downstream project state is never validation evidence** — consumer projects are the
  skills' *outputs*, not oracles: their existence/commits are checkable facts, their
  conformance is not. Field findings enter the spec only via RED→GREEN on a non-derived
  fixture.

## Test fixture — create on demand
There is **no standing fixture**; create one when testing. (The original RED/GREEN rounds
used a pristine TargetPlanner copy at `E:\Projects\AI\TargetPlanner`, since deleted.)

Recipe: copy a **pristine, skills-unmodified** project — close-to-worst-case is best
(missing/scattered docs, no router, drift) — to a scratch location, and commit an empty
marker commit ("SKILLS-TEST BASELINE") to name the baseline.

**Reset contract** — restore baseline after every test run that mutated the tree:
```
git reset --hard <baseline-marker> && git clean -fd
```
**Gotcha:** the marker only *names* the baseline — `reset --hard` rewinds tracked files but
leaves behind any **untracked** files a skill dropped in, so the `git clean -fd` is
mandatory, not optional.
