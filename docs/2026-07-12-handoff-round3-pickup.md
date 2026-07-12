# 2026-07-12 — Session handoff: Cowork-crash recovery → round-3 pickup

**What this is / when to read:** state-save written at the user's request when the 2026-07-12
recovery session had to end mid-pickup. A fresh agent (or the resumed session) starts HERE:
this doc holds the verified state, the decisions already made, the open decisions, and the
execution plan. All substance lives in the eight journal docs committed alongside — this doc
only routes; do not re-derive what they already record.

## 1. What happened (one paragraph)

A Claude Cowork desktop session ran the hybrid skill-rewrite program (2026-07-11 → past
midnight), wedged (blank window), and was force-killed while executing **"round 3"** — the
RED→GREEN validation of revised hybrid candidate texts. Everything up to round 3 survived on
disk and is recorded in the journal docs below. Round 3's execution (and the container-only
copy of the ecological SETUP result, 6 commits) died with the app; nothing else was lost. The
recovery session verified all of this against disk, then was ended by the user before round 3
could be re-run.

## 2. The record — read in this order

| Doc (`docs/`) | Holds |
|---|---|
| `2026-07-11-skill-portability-review.md` | goal + Q1–Q8 decisions (§7) — portability + constant-behavior compression |
| `2026-07-11-audit-rewrite-draft.md` | conservative AUDIT draft + form-factor options (A–D) |
| `2026-07-11-hybrid-rewrite-candidates.md` | **the four hybrid candidate SKILL texts (Option C) — base texts for round 3** |
| `2026-07-12-hybrid-red-green-arm1-results.md` | AUDIT + SETUP synthetic validation — GREEN 2/2 each |
| `2026-07-12-hybrid-red-green-arm2-results.md` | MAINTAIN + whats-next — GREEN 2/2 each; family 8/8 |
| `2026-07-12-tp-ecological-run.md` | hybrid vs old skills on real-world TargetPlanner copy — convergent + 3 hybrid-only finds, no regressions; 4 field findings |
| `2026-07-12-tp-audit-adjudication.md` | the 34-worker audit's full flag report (top-40 + ~90–100 remainder) — **standing open queue** |
| `2026-07-12-changelog-convention-adopted.md` | **the 00:00 decision doc: CHANGELOG.md convention + candidate skill-text deltas + the round-3 test plan. Round 3's spec lives here.** |

Note: the four docs named `2026-07-12` with pre-midnight content were written 07-11 evening
(session dateline); cross-references between docs are consistent as-is. User has not asked to
rename — leave unless they do.

## 3. Verified state (checked against disk 2026-07-12, not assumed)

- **This repo** (`E:\Projects\AI\Skills`, `dev` @ `89d7ee4` pre-handoff): `skills/` untouched;
  deployed `~/.claude/skills/` untouched; the 8 docs + this handoff committed by the recovery
  session (user instruction "save state"; undo = `git reset --soft HEAD~1` if unwanted).
- **Fixture** `TestProjects/TargetPlanner/` — own nested `.git`, clean at baseline `9034e6f`
  ("SKILLS-TEST BASELINE"). This is the user's restored "standard messy baseline" for
  ecological testing; the ecological run mutated only a container *copy*, never this tree.
  Stays untracked in the Skills repo (nested `.git`; user declined a gitignore entry).
  Restore contract: `git reset --hard 9034e6f && git clean -fd` **run inside that directory**.
- **Real TargetPlanner** (`E:\Projects\VisualStudio\Astronomy\TargetPlanner`, `dev`, last
  commit `f3b19bc` 2026-07-07 = old-skill audit output): **working tree deliberately dirty,
  decision pending** — uncommitted layer written by Cowork via the bridge during the user's
  adjudication walk-through: 20 approved doc fixes (CLAUDE ×3, ARCHITECTURE ×9, README ×4,
  ROADMAP banner, RELEASING ×3) **plus** the ROADMAP→CHANGELOG relocation (1,178 lines out of
  ROADMAP.md; `CHANGELOG.md` 1,182 lines, charter'd; shape-verified content-preserving; one
  stray relocated preamble line at CHANGELOG.md ~line 8 to smooth before any commit).
  **Do not restore/clean/commit this tree without the user's verdict (open decision #1).**
- **Deleted (user-approved):** `TestProjects/_to_delete/` (git-less seed tarball + stale lock).

## 4. Decisions already made (this session — do not re-ask)

1. **Round 3: re-derive the revised texts + re-run here** (fresh; no salvage from the app chat
   needed).
2. **Audit remainder** (rest of top-40 + ~90–100 themed flags): **standing open queue**; input
   is the adjudication doc. Backlog item, not now.
3. `_to_delete/` deleted; journal docs committed; TestProjects stays untracked, un-ignored.

## 5. Open decisions (ask the user, in this order)

1. **Real-TP uncommitted layer** — verify→commit on TP `dev` (recommended: the fixes are
   user-approved and the CHANGELOG convention is already *decided*; round 3 tests only whether
   the skill TEXT induces the behavior — its outcome cannot un-decide the convention) · or
   discard back to pure 07-07 state · or hold. The two-layer explanation was already given to
   the user; they only owe the verdict.
2. (Minor) Rename the four misdated docs? Default: leave as-is.

## 6. Execution plan — round 3 (spec: `2026-07-12-changelog-convention-adopted.md` §"RED→GREEN plan")

Read `VERIFICATION.md` (harness contract) before running anything. Arm-doc precedent
(`…arm1/arm2-results.md` §Method) governs protocol: Sonnet test agents, candidate text
injected in the task prompt, disk-verify every scored claim, judge by output text, fresh
disposable copy per rep, report-only for AUDIT reps.

1. **Re-derive the revised candidate texts** → new dated doc (`hybrid-candidates-round3`).
   Base = candidates doc; deltas = 00:00 doc §"Candidate skill-text deltas":
   - SETUP: enforced-set table + conditional `CHANGELOG.md` row; **A2 rewritten** (spec text in
     the 00:00 doc); **T1** teaches the three-way journal split (finding → NOTEBOOK · shipped
     unit → CHANGELOG · substantial record → docs/).
   - AUDIT: **R14** journal list gains `CHANGELOG.md`; **new structural placement rule** — a
     reference doc embedding a growing dated shipped-history = ONE placement flag
     `move-to CHANGELOG.md`, embedded entries NOT currency-flagged individually; **R21**
     why-clause gains "same-model cross-worker convergence is agreement, not completeness."
   - MAINTAIN / whats-next: **no rule changes** (bundle notes only).
   - **ID-stability rule decided in-session: never renumber existing rule IDs** (journal docs
     cite R14/R21/R22/R23). Add the structural rule under a fresh appended ID (e.g. R25 placed
     in the Placement section), not by inserting/shifting.
2. **Build the synthetic fixture** (non-derived: invent a fresh small project — not
   FermCtl/TrailKit, not TargetPlanner): docs-conformant tree whose ROADMAP embeds ~8–10 dated
   history entries; plant 3 per-entry drifts (RED bait), 1 genuine live-section currency defect
   (control — must be flagged in BOTH arms), 1 clean history entry (control); ground-truth
   catalog OUTSIDE the tree; baseline marker commit; per-rep copies in the session scratchpad.
3. **Run** (2 RED + 2 GREEN per test; **RED here = the 07-11 candidate text, not unguided** —
   this round is A/B current-vs-revised):
   - t1 AUDIT structural: RED expect per-entry currency flags on embedded history; GREEN expect
     exactly one `move-to CHANGELOG.md` structural flag, entries untouched, live-defect control
     still flagged.
   - t2 SETUP A2′: RED record current disposition (old A2 forbids CHANGELOG); GREEN expect
     content-preserving relocation + digest + pointer.
   - t3 AUDIT R21: hand the orchestrator a converged same-model flag set (2 rounds dry, heavy
     cross-worker convergence); RED — does it rationalize skipping the model switch (the
     ecological field finding 2); GREEN — switches or explicitly justifies against the hardened
     clause. No filesystem fixture needed; it's a judgment probe.
   Cost expectation from arm precedent: ~0.5–1.5M subagent tokens.
4. **Write the results doc** (arm-doc format). If GREEN across the board → **the openspec
   change**: apply all four candidates to `skills/`, update the two Class-E lines (README
   "author's local path" note; root CLAUDE.md "by absolute name" gotcha), edit the design doc's
   "Shipped history" paragraph (owner-sanctioned per the 00:00 doc), `dev` → `main`,
   `deploy.sh` (see `RELEASING.md`; only `main` deploys).
5. **Backlog (later):** TP-side commit per open decision #1 · audit-queue remainder · harness
   promotion (recreate FermCtl/TrailKit + catalogs → permanent `harness/` home, arm-2 §Next) ·
   fat-router lean + nested-orchestrator collection hardening (ecological field findings 1 & 4,
   no-failure gate applies).

## 7. Gotchas (load-bearing)

- `git clean -fd` is part of the fixture reset contract — run it **only inside the fixture
  dir**, never at the Skills-repo root.
- Never edit `skills/` outside the openspec change; never edit `~/.claude/skills/` at all
  (build artifact). Candidate texts are tested by **injection**, not deployment.
- The real-TP tree is dirty **on purpose** (open decision #1) — don't "helpfully" clean it.
- Round-3 RED ≠ unguided baseline (see §6.3).
- Journal docs are append-only history — never retcon them to match later decisions.

## 8. Suggested skills for the next session

- `superpowers:verification-before-completion` — before declaring any round-3 arm GREEN.
- `superpowers:dispatching-parallel-agents` / `superpowers:subagent-driven-development` — the
  RED/GREEN rep fan-outs.
- `openspec-propose` (or `opsx:propose`) then `openspec-apply-change` — the apply change in §6.4
  (house workflow; the change record is the provenance for the portability pass).
- `superpowers:writing-skills` — governs the actual `skills/*/SKILL.md` edits when applying.
- `whats-next` — if direction is unclear after round 3, it will sweep this journal + the
  standing audit queue correctly.
