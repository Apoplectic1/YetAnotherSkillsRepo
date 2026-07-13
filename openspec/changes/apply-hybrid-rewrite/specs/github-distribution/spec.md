# Delta: github-distribution — apply-hybrid-rewrite

## ADDED Requirements

### Requirement: Skill footers cite provenance by public GitHub URL
Each shipped `skills/*/SKILL.md` SHALL end with a single provenance link — the public GitHub
URL of the canonical design doc (`docs/docs-architecture-design.md` on `main`) — so deployed
copies are self-contained for public consumers. Skill text SHALL NOT cite evidence docs by
author-local absolute path, and benchmark figures ride in skill text as uncited claims (the
benchmark doc is not referenced by name from skill text). Repo-side descriptions of the
citation form (README lab-notebook line, root CLAUDE.md gotcha) SHALL match this convention.

#### Scenario: Deployed skill is self-contained
- **WHEN** a public consumer reads a deployed SKILL.md outside this machine
- **THEN** its only provenance reference is the resolvable GitHub URL of the design doc
  (no `E:\...` or other author-local paths anywhere in the text)

#### Scenario: Design doc stays at its published path
- **WHEN** repo maintenance considers moving or splitting `docs/docs-architecture-design.md`
- **THEN** the root CLAUDE.md gotcha blocks it — the published URL in every deployed skill
  footer must remain valid on `main`
