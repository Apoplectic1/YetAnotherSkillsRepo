# Design — fix-skill-review-findings

## Context

A 2026-07-06 correctness + intent review compared the four deployed docs-architecture skills
against their canonical design (`E:\Projects\AI\Skills\docs\docs-architecture-design.md`) and the
worker-model benchmark. Findings split into three classes: intent gaps (designed behavior absent
from skills), correctness bugs (internal contradiction; dangling deployed links), and polish.
Constraints: the repo's branch policy (author on `dev`, only `main` deploys via `deploy.sh`), the
writing-skills Iron Law (no behavior-adding skill edit without a failing test first), and the
family's own single-sourcing principle (encode a rule once; siblings inherit by reference).

## Goals / Non-Goals

**Goals:**
- Close the four intent gaps with RED/GREEN-validated guidance (or record honestly when a baseline
  doesn't fail — see Decisions).
- Fix the two correctness bugs and the polish items mechanically.
- Keep the skills lean (they already exceed the rubric's word target) — additions offset by trims.
- Sync `docs-architecture-design.md` in the same commits as the skill edits.

**Non-Goals:**
- This repo's own CLAUDE.md router drift and the benchmark doc's stale pending item (review
  option (b), a separate docs-only pass).
- Behavior text in MAINTAIN (it inherits the disk-verify gate through its REQUIRED reuse of
  AUDIT's machinery; only its footer link changes).
- Re-running the worker-model benchmark or retro-speccing entire skills.

## Decisions

1. **Footer links become absolute paths** (`E:\Projects\AI\Skills\docs\...`).
   Deployed copies at `~/.claude/skills/<name>/` resolve `../../docs/...` to `~/docs/...`
   (verified absent). Alternatives: (a) deploy.sh rewrites links at copy time — rejected, turns a
   deliberately dumb copy script into a build step; (b) prose-only pointer ("in the AI Skills
   repo") — rejected, loses direct navigability. Absolute paths are honest on a solo machine;
   accepted trade-off: they rot if the repo ever moves (cheap to fix then).

2. **`graduate` resolves to apply-able-after-adjudication; "report-only" is reserved for
   `flag-code-bug` + `revisit-plan`.** Graduating a satisfied plan into "Recently shipped" is a
   doc-only edit — squarely inside AUDIT's "writes docs only" boundary — and the Phase-2 worked
   example applied such relocations after adjudication. The two report-only actions are precisely
   the ones whose targets AUDIT does not own (code, plan intent). The modality section's "two
   report-only exceptions" phrasing becomes "two non-stale statuses" (they are exceptions to
   *flagging staleness*, not to applying).

3. **Disk-verify gate is encoded once, in AUDIT's merge/adjudicate steps.** MAINTAIN and
   whats-next REQUIRED-reuse AUDIT's fan-out, so they inherit it — the family's own
   single-sourcing rule applied to itself. Alternative (repeat the rule in each skill) rejected:
   that is the duplication-drift pattern the family exists to prevent. Wording: orchestrator
   spot-checks each merged flag's cited evidence (grep/read the `file:line`) before adjudication;
   evidence that fails is corrected or dropped with a note.

4. **Cold-rationale handling enters AUDIT as (a) a tier-scope line + (b) one schema action.**
   Cold docs get decision-consistency checks only; a code-coupled fact in a cold doc is a
   misplacement flag; `extract-cold` joins the schema's action list for lengthy+cold+evergreen
   reference sections. Keeping it schema-shaped preserves mergeability across the fan-out. The
   "not the journal" exclusion gets scoped: the *journal* is not currency-audited, but
   cold-rationale docs (journal-resident, reference-cited) get the consistency check.

5. **SETUP's sub-project text mirrors AUDIT's existing scope wording** (own router / own `.git` →
   flag-and-skip; run from the sub-project's dir), and the "coexist, never clobber" rule gains the
   scoping clause (applies to the root project's own files). Consistent wording across the two
   skills prevents the next drift.

6. **Iron Law discipline, honestly applied.** The four behavior-adding changes each get a RED
   scenario with the *current* skill text first. **If a baseline does not fail, the guidance is
   not added** (writing-skills: no failure → nothing to fix); the outcome is recorded in the design
   doc instead. Mechanical fixes (links, vocabulary, contradiction resolution, description trim,
   tier bullet, maturity-note removal) ship without pressure scenarios but with a post-edit
   family-wide consistency re-read. The contradiction fix is included in the cold-rationale /
   disk-verify GREEN runs' prompts, so its new wording gets incidental behavioral coverage.

7. **Test harness = candidate-text injection into subagents** (per repo CLAUDE.md): the live Skill
   tool reads `~/.claude/skills/` (main-deployed), so dev-branch candidates are injected as prompt
   text. Reps: 2 per scenario per phase, matching the family's prior RED/GREEN validation depth.
   Fixtures:
   - **Sub-project**: TP fixture + a planted nested mini-project (own `.git` init, own CLAUDE.md,
     one stray doc with an unconventional name).
   - **Design-heavy**: small synthetic fixture in the session scratchpad (2–3 source files + one
     ~50 KB+ design doc + no other docs) — TP is code-rich and cannot exercise this shape.
   - **Cold-rationale**: TP fixture + a planted dated rationale note (containing one drifted
     code-coupled fact) cited by a reference doc, plus one genuinely lengthy+cold+evergreen section
     planted in a reference doc.
   - **Disk-verify**: orchestrator-role agent given a merged flag list seeded with one
     plausible-but-false flag (fabricated `file:line` evidence) against the TP fixture.
   - TP reset contract after every mutating run: `git reset --hard 9034e6f && git clean -fd`.

8. **Word-count guard.** AUDIT gains two behaviors; offset by trimming the bold-caveat stacking in
   its steps 1/3 where possible and by the SETUP maturity-note removal. Soft ceiling: AUDIT stays
   ≤ ~1250 words; net family growth ≤ ~10%.

## Risks / Trade-offs

- [A RED baseline doesn't fail → temptation to add the guidance anyway] → Decision 6's gate:
  record, don't encode. This is the same discipline the design doc already applies ("needs a
  failing test before encoding").
- [AUDIT bloat degrades scanability] → word-count guard (Decision 8); detail belongs in the
  design doc behind the now-working footer link.
- [Synthetic fixtures too clean to be representative] → keep them minimal but real (actual
  `git init`, actual router lines); the TP fixture carries the realistic-mess load for the other
  scenarios.
- [Fixture contamination across scenarios] → reset TP between scenarios; scratchpad fixture is
  session-local and disposable.
- [`extract-cold` action overlaps MAINTAIN's classify vocabulary] → it doesn't: extraction is
  reference → cold (AUDIT's placement axis); MAINTAIN graduates journal → reference. Noted in the
  skill text only if GREEN runs show confusion.
- [Deployed skills drift from dev during the work] → no deploy until merge; injection harness
  keeps live behavior unchanged throughout.

## Migration Plan

1. All edits on `dev`; each validated behavior lands as one commit (skill text + design-doc
   RED/GREEN record together, per collaboration rule #4).
2. Merge `dev` → `main`; run `./deploy.sh`.
3. Verify: deployed copies byte-identical to repo; footer links resolve from
   `~/.claude/skills/<name>/`.
4. Rollback: `git revert` on main + re-run `./deploy.sh` (deploy is a wholesale copy; no state).

## Open Questions

- None blocking. If the sub-project or design-heavy RED baselines *pass* (agents already behave),
  the corresponding SETUP additions are dropped per Decision 6 and the design doc records the
  no-failure outcome — that path needs no further input.
