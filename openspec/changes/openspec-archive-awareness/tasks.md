# Tasks: openspec-archive-awareness

## 1. Candidate skill text (authored on dev, per RELEASING branch policy)

- [x] 1.1 Draft maintain edit: new source-class rule in
      `skills/docs-architecture-maintain/SKILL.md` — archived
      `openspec/changes/archive/*/design.md` as a journal source, disposition pinned to
      `cross-ref`-only (pointer lives in the reference doc; archive never edited), plus the
      override clause: a router's generic `openspec/` exclusion does not exempt this source.
      Keep it to one rule; follow `superpowers:writing-skills` conventions.
- [x] 1.2 Draft audit edits in `skills/docs-architecture-audit/SKILL.md`: R14 gains explicit
      `openspec/changes/archive/`; R15 gains the carve-out (decision-consistency only,
      tier-violation flags suppressed, never edited).
- [x] 1.3 Draft setup edit in `skills/docs-architecture-setup/SKILL.md`: B1 exclusion-wording
      clause (archived design.md = historical records the maintain sweep reads; no scaffolding
      change, no T1 change).

## 2. RED/GREEN harness (behavior-bearing edits only, per design D5)

- [x] 2.1 Extend the on-demand fixture (`VERIFICATION.md` recipe) with an
      `openspec/changes/archive/<id>/design.md` carrying (a) graduable rationale absent from
      the reference tier and (b) code-coupled facts that have drifted, plus an
      ARCHITECTURE.md citation into it. The fixture router keeps the OLD blanket
      "`openspec/` — excluded, tooling" wording, so the runs exercise the override clause.
- [x] 2.2 RED maintain: run current skill text against the fixture — assert the miss (source
      not swept, or a `stub`/`archive` disposition touching the archive). Record verbatim.
- [x] 2.3 GREEN maintain: run candidate 1.1 text — assert graduate-with-cross-ref and a
      byte-identical archive. Apply the no-failure gate: if RED already passes, drop the
      corresponding candidate text and record why.
- [x] 2.4 RED audit: run current skill text — assert tier-violation flags fire on the cited
      archived design.md. Record verbatim.
- [x] 2.5 GREEN audit: run candidate 1.2 text — assert consistency-check-only, zero
      tier-violation flags, archive untouched. Same no-failure gate.
- [x] 2.6 After every mutating fixture run, apply the reset contract (`git clean -fd` —
      mandatory).

## 3. Docs (same commit as the skill edits, not separate)

- [x] 3.1 Record rationale + RED/GREEN results in `docs/docs-architecture-design.md` (edit in
      place — footer-linked by URL, never rename/move).
- [x] 3.2 Update `ARCHITECTURE.md` (skill-family behavior summary) and `ROADMAP.md`
      (Recently shipped) as warranted; note the run in `NOTEBOOK.md`.
- [x] 3.3 Update this repo's own `CLAUDE.md` router exclusion note per the setup carve-out
      wording (dogfood the new convention here).

## 4. Verify, sync, ship

- [ ] 4.1 `openspec validate --change openspec-archive-awareness`; run `/opsx:verify` against
      the delta specs.
- [ ] 4.2 Sync delta specs to main specs (`/opsx:sync`), archive the change
      (`/opsx:archive`).
- [ ] 4.3 Merge `dev` → `main`; deploy via `deploy.sh` (only `main` deploys); confirm
      `~/.claude/skills/` copies match.
