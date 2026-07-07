# Proposal — fix-skill-review-findings

## Why

A correctness + intent review (2026-07-06) of the four docs-architecture skills against their
canonical design (`E:\Projects\AI\Skills\docs\docs-architecture-design.md`) found **4 intent gaps**
(designed behavior missing from the shipped skills), **2 correctness bugs** (an internal
contradiction in AUDIT's action vocabulary; dangling rationale links in every deployed copy), and a
set of polish items. The family is about to run on its first real customers (TargetPlanner, Library,
XFM), so the shipped skills should match their validated design before those runs bake in the gaps.

## What Changes

- **SETUP** (`skills/docs-architecture-setup/SKILL.md`):
  - Add the **sub-project flag-and-skip** policy (root run never scaffolds into or restructures a
    nested own-`.git`/own-router project; flag + direct the user to run from the sub-project dir) —
    and scope the existing "coexist, never clobber / augment" rule so it cannot be read as license
    to augment a sub-project's CLAUDE.md.
  - Add the **design-heavy / code-light** project-shape rule (a large standalone design doc is a
    `DESIGN.md` slot that graduates into ARCHITECTURE/ROADMAP as code lands — never force-split).
  - Add `VERIFICATION.md` to the reference-tier bullet (currently omitted; design includes it).
  - Drop the development-era "prove the skill on a small project first" maturity note.
- **AUDIT** (`skills/docs-architecture-audit/SKILL.md`):
  - Add **cold-rationale (tier 3) handling**: cold docs get a decision-consistency check (not full
    currency), and lengthy+cold+evergreen reference sections are flagged as **extraction
    candidates** (new schema action) for user adjudication.
  - Resolve the **`graduate` report-only contradiction**: `graduate` is an apply-able doc edit after
    adjudication; the term "report-only" is reserved for `flag-code-bug` / `revisit-plan`.
  - Add a **disk-verify gate** to the merge/adjudicate machinery (orchestrator spot-checks worker
    evidence against disk before adjudication) — inherited by MAINTAIN and whats-next through their
    REQUIRED reuse of AUDIT's fan-out, so it is encoded once.
  - Align step-4 adjudication verbs with the schema's action vocabulary.
- **whats-next** (`skills/whats-next/SKILL.md`):
  - Clarify the ranking formula's risk semantics (risk-if-ignored ranks higher, not
    implementation risk).
  - Trim the frontmatter description to triggering conditions per the SDO rule (it currently
    summarizes outputs/process) and add the "Assumes the docs-architecture conventions" clause its
    siblings carry.
- **All four skills** (incl. MAINTAIN): replace the repo-relative footer links
  (`../../docs/...`) with absolute paths — the deployed copies under `~/.claude/skills/` currently
  resolve them to `~/docs/...`, which does not exist.
- **Design doc** (`docs/docs-architecture-design.md`): sync in the same commits — update the stale
  "needs a failing test before encoding (Iron Law)" gate notes (AUDIT already ships router-anchored
  scope + flag-and-skip) and record this fix batch's RED/GREEN outcomes.
- **Process guardrail**: every behavior-adding change (the four intent gaps) gets a RED scenario
  before the skill text is written and a GREEN re-run after, per the writing-skills Iron Law.
  Mechanical fixes (links, vocabulary alignment, contradiction resolution, description trim) ship
  without pressure scenarios but with a post-edit consistency re-read.

No breaking changes — the skills are guidance documents with a single consumer (this user's
harness); deployment is a wholesale copy from `main` via `deploy.sh`.

## Capabilities

### New Capabilities

No specs exist yet in `openspec/specs/`; each touched skill gets a capability spec scoped to the
requirements this change establishes (not a retroactive full spec of the skill).

- `docs-architecture-setup`: bootstrap-scope behavior — sub-project boundaries, design-heavy
  project shape, reference-tier completeness.
- `docs-architecture-audit`: audit behavior — tier-3 cold-rationale checks, action vocabulary and
  dispositions (graduate vs report-only), evidence disk-verification.
- `whats-next`: ranking semantics and trigger-scoped discovery description.

### Modified Capabilities

(none — no existing specs)

## Impact

- **Files**: `skills/docs-architecture-setup/SKILL.md`, `skills/docs-architecture-audit/SKILL.md`,
  `skills/whats-next/SKILL.md`, `skills/docs-architecture-maintain/SKILL.md` (footer link only),
  `docs/docs-architecture-design.md` — all in `E:\Projects\AI\Skills` (dev branch).
- **Testing**: RED/GREEN subagent harness (candidate SKILL.md text injected into test agents — the
  live Skill tool only sees deployed/main). Fixtures: `E:\Projects\AI\TargetPlanner` (reset
  contract `git reset --hard 9034e6f && git clean -fd`) plus small synthetic fixtures for the
  nested-sub-project and design-heavy shapes.
- **Deployment**: merge dev → main, run `./deploy.sh` — refreshes all four copies under
  `~/.claude/skills/`.
- **Out of scope**: this repo's own CLAUDE.md router drift and the benchmark doc's stale pending
  item (review option (b) — a separate docs-only pass); MAINTAIN behavior text (inherits the
  disk-verify gate by reference, per the family's single-sourcing rule).
