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

Four method rules (the first two learned the hard way — provenance in
`docs/docs-architecture-design.md`; the third adopted 2026-07-10, first self-audit; the
fourth a recurring disclosure across the 2026-07-12/13 validation runs):
- **Validate on a project the skill was *not* derived from** — the source project is a
  poisoned fixture (already-conformant, or it literally contains the spec).
- **Disk-verify agent claims** — a validation pass once asserted a broken reference that
  `grep` showed was already fixed. Trust the disk, not the claim.
- **Downstream project state is never validation evidence** — consumer projects are the
  skills' *outputs*, not oracles: their existence/commits are checkable facts, their
  conformance is not. Field findings enter the spec only via RED→GREEN on a non-derived
  fixture.
- **Disclose the orchestrator-context leak** — the orchestrating session's own CLAUDE.md /
  router context leaks into every nested test agent's prompt. The bias is conservative for
  the GREEN-delta claim (RED gets convention vocabulary for free), so it doesn't invalidate
  results — but disclose it per run (per-run bias-direction analyses live in the dated
  arm/ecological/round-3 results docs).

## Test fixture — harness source + create-on-demand recipe
A **standing fixture source** lives at `harness/tidepool-fixture/` (round-3 synthetic:
cataloged planted defects + verified genuine drift; ground truth in
`harness/catalog-tidepool.md`, usage + derivation caveats in `harness/README.md`). Per-run
copies are still disposable: copy to scratch, `git init`, baseline marker commit.

For tests the standing fixture can't serve (derivation caveat, or a different project
shape), create one on demand: copy a **pristine, skills-unmodified** project —
close-to-worst-case is best (missing/scattered docs, no router, drift) — to a scratch
location, and commit an empty marker commit ("SKILLS-TEST BASELINE") to name the baseline.
(The original rounds used a pristine TargetPlanner copy, since deleted; arms 1–2 used
FermCtl/TrailKit, which died with the Cowork container.)

A third source for at-scale tests: `TestProjects/` — copies of real projects (e.g. the 24 KB
TP router behind fat-router-lean), **untracked by design and never `git add`ed**: the copies
carry nested `.git` dirs (a plain add records only a contentless gitlink stub), and committing
real content would publish private project source through the public mirror on the next `main`
push. Hidden locally via `.git/info/exclude`; lifecycle + keep-until rationale: NOTEBOOK
2026-07-13/17.

**Reset contract** — restore baseline after every test run that mutated the tree:
```
git reset --hard <baseline-marker> && git clean -fd
```
**Gotcha:** the marker only *names* the baseline — `reset --hard` rewinds tracked files but
leaves behind any **untracked** files a skill dropped in, so the `git clean -fd` is
mandatory, not optional.
