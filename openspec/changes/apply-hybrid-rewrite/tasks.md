# Tasks: apply-hybrid-rewrite

## 1. Apply candidate texts to skills/ (verbatim)
- [x] 1.1 Extract the two round-3 fenced candidate bodies from
      `docs/2026-07-13-hybrid-candidates-round3.md` → write
      `skills/docs-architecture-setup/SKILL.md`, `skills/docs-architecture-audit/SKILL.md`.
- [x] 1.2 Extract the MAINTAIN + whats-next fenced bodies from
      `docs/2026-07-11-hybrid-rewrite-candidates.md` → write
      `skills/docs-architecture-maintain/SKILL.md`, `skills/whats-next/SKILL.md`.
- [x] 1.3 Verify zero transcription drift: re-extract each fence to a temp file and `diff`
      against the written SKILL.md (4× identical required).

## 2. Repo-side Class-E lines + design-doc paragraph
- [x] 2.1 `README.md` lab-notebook line: footers cite by public GitHub URL (drop
      "the author's local path" phrasing).
- [x] 2.2 Root `CLAUDE.md` design-doc gotcha: referenced **by public GitHub URL** from
      deployed skill footers (benchmark doc no longer name-referenced from skill text);
      keep the move-neither constraint.
- [x] 2.3 `docs/docs-architecture-design.md` "Shipped history / changelog" paragraph:
      rewrite to the CHANGELOG.md convention, citing
      `docs/2026-07-12-changelog-convention-adopted.md` as the superseding decision.

## 3. Verify
- [x] 3.1 Grep all four `skills/*/SKILL.md`: no local paths, footer URL present, R25/A2′
      text present where expected; word counts ≈ candidates doc table.
- [x] 3.2 Grep repo docs for stale "git is the changelog / no CHANGELOG.md" statements in
      reference-tier docs (journal/archived docs exempt — never retconned); fix any found
      (`CLAUDE.md` ROADMAP router line says "git is the full changelog" — align).
- [x] 3.3 `openspec validate` passes for the change artifacts (if available).

## 4. Ship
- [ ] 4.1 Commit on `dev` (skills + repo lines + design-doc edit + openspec artifacts,
      one commit).
- [ ] 4.2 Merge `dev` → `main`.
- [ ] 4.3 `bash deploy.sh` from `main`; confirm deployed `~/.claude/skills/*/SKILL.md`
      match `skills/` (deploy output + spot diff).
- [ ] 4.4 Push `main` to origin (distribution channel publishes main only).
