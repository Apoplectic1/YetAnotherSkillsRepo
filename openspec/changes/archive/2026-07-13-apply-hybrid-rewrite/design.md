# Design: apply-hybrid-rewrite

## Context

The candidate texts are already final and validated — this change is an *apply*, not an
authoring exercise. Sources of truth: `docs/2026-07-13-hybrid-candidates-round3.md` (SETUP,
AUDIT — the round-3 GREEN payloads) and `docs/2026-07-11-hybrid-rewrite-candidates.md`
(MAINTAIN, whats-next — arm-2 GREEN, unchanged in round 3). The harness only ever tested
injected text; the live Skill tool reads `~/.claude/skills/`, deployed from `main` by
`deploy.sh` (RELEASING.md). Authoring happens on `dev`.

## Goals / Non-Goals

**Goals:**
- `skills/*/SKILL.md` byte-match the validated candidate bodies (frontmatter + body exactly
  as tested; the only permissible divergence is none).
- Repo-side truth (README line, root CLAUDE.md gotcha, design-doc paragraph) matches the
  shipped texts, so a doc audit of this repo finds no self-contradiction.
- Spec deltas record the three requirement-level changes.

**Non-Goals:**
- No re-editing or "improving" candidate wording during apply (superpowers:writing-skills
  governs future edits; this apply ships the tested text verbatim).
- No consumer migration of existing projects' embedded histories (house no-back-compat rule;
  the skills themselves perform relocation when next run on a consumer).
- No README restructure beyond the one line (README is governed by `github-distribution`).

## Decisions

1. **Extract candidate bodies mechanically from the journal docs** (the ````markdown fenced
   blocks), not retyped — eliminates transcription drift; verify with a fence-extraction
   diff after writing (same method used to word-count them).
2. **Frontmatter**: candidates carry their own `name`/`description` frontmatter — shipped
   as-is (descriptions unchanged from shipped skills except where the candidates changed
   them; the harness tested the full file).
3. **Design-doc edit scope**: replace only the "Shipped history / changelog" paragraph
   (lines ~191–197) with the adopted convention, citing the decision doc — the design doc
   is otherwise treated as canonical/stable (root CLAUDE.md: "move or split neither" — the
   file stays put; only the gotcha's *reference form* line changes).
4. **Spec deltas over full-spec rewrites**: `openspec/specs/` stays sparse by choice
   (design doc); each modified capability gets a delta with the new requirements only.
5. **Deploy path**: commit on `dev` → merge `main` → `bash deploy.sh` from `main`
   (script refuses elsewhere). No `--force`.

## Risks / Trade-offs

- [Transcription drift between journal candidate and shipped file] → mechanical extraction +
  post-write `diff` against the extracted fence block; zero-diff required.
- [Repo-side lines drift from shipped footers] → the verify step greps deployed text for the
  GitHub URL and greps README/CLAUDE.md for the updated phrasing.
- [Old A2 text lingering in specs/archive references] → specs are deltas; archived changes
  are journal-tier (never retconned) — acceptable, by convention.
- [Deploy propagates to live harness mid-session] → deploy last, after all repo commits.

## Migration Plan

Repo-only; no data migration. Rollback = `git revert` on `dev`/`main` + re-run `deploy.sh`
(deploy stamps markers and prunes, so re-running is always safe).

## Open Questions

(none — all decisions were adjudicated in the journal record: form Option C, Q1–Q8
portability, CHANGELOG convention, ID-stability rule.)
