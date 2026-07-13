# Proposal: apply-hybrid-rewrite

## Why

The four-skill docs-architecture family has been rewritten into the hybrid-rulebook form
(portable, rule-ID'd, −23% words with zero rule drops) and fully validated: arms 1–2 GREEN
8/8 (`docs/2026-07-12-hybrid-red-green-arm1-results.md`, `…arm2-results.md`), ecological run
convergent-plus (`docs/2026-07-12-tp-ecological-run.md`), and round 3 GREEN on the
CHANGELOG-convention deltas (`docs/2026-07-13-round3-red-green-results.md`). The validated
candidate texts sit in journal docs; the shipped `skills/` still carry the old form and the
superseded "git is the changelog / no CHANGELOG.md" rule. This change ships the candidates.

## What Changes

- Replace all four `skills/*/SKILL.md` bodies with the validated candidates:
  - `docs-architecture-setup`, `docs-architecture-audit` — round-3 texts
    (`docs/2026-07-13-hybrid-candidates-round3.md`): CHANGELOG.md conditional row + A2
    rewritten + T1 three-way journal split; R25 structural placement rule (appended ID,
    no renumbering) + R14 journal list gains CHANGELOG.md + R21 hardened why-clause.
  - `docs-architecture-maintain`, `whats-next` — 07-11 hybrid texts
    (`docs/2026-07-11-hybrid-rewrite-candidates.md`), no rule changes.
  - **BREAKING** (convention level): shipped history now routes to `CHANGELOG.md`
    (journal tier); the 2026-06-28 "no CHANGELOG.md" rule is superseded
    (`docs/2026-07-12-changelog-convention-adopted.md`). No consumer migration is shipped
    (house rule: no back-compat; consumers get the new behavior on next skill run).
- Skill footers become a single public GitHub URL to the design doc (portability decision,
  Q1–Q8) — repo-side Class-E lines updated to match:
  - `README.md` lab-notebook line: footers cite by GitHub URL, not "the author's local path".
  - Root `CLAUDE.md` gotcha: deployed skills reference the design doc **by public GitHub
    URL** (benchmark doc no longer referenced by name from skill text; benchmark numbers ride
    as uncited claims).
- Design doc `docs/docs-architecture-design.md` "Shipped history / changelog" paragraph
  rewritten to the adopted CHANGELOG.md convention (owner-sanctioned edit per the 00:00
  decision doc; the old paragraph's rationale is preserved in the decision doc, not deleted).

## Capabilities

### New Capabilities
(none)

### Modified Capabilities
- `docs-architecture-setup`: shipped-history routing requirement changes — history accrues in
  `CHANGELOG.md` (append-only journal tier, conditional file); ROADMAP keeps digest +
  pointer; relocation of an embedded history is content-preserving; three-way journal split.
- `docs-architecture-audit`: new structural-placement requirement — a reference doc embedding
  a growing dated shipped-history yields exactly ONE `move-to CHANGELOG.md` placement flag
  with entries not individually currency-flagged; `CHANGELOG.md` joins the never-currency-
  audited journal set; model-diversification requirement hardened (same-model cross-worker
  convergence is agreement, not completeness).
- `github-distribution`: skill texts cite provenance by public GitHub URL (single design-doc
  link per skill footer), keeping deployed copies self-contained for public consumers.

## Impact

- `skills/*/SKILL.md` ×4 (the product; deployed via `deploy.sh` from `main` only).
- `README.md` (one line), root `CLAUDE.md` (one gotcha), `docs/docs-architecture-design.md`
  (one paragraph — otherwise append-only-by-convention; this edit is owner-sanctioned).
- `openspec/specs/` deltas for the three capabilities above.
- Post-apply: `dev`→`main` merge + `bash deploy.sh` (RELEASING.md branch policy).
