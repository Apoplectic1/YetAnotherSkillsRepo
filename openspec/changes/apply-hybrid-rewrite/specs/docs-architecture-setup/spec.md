# Delta: docs-architecture-setup — apply-hybrid-rewrite

## ADDED Requirements

### Requirement: Shipped history routes to CHANGELOG.md
The SETUP skill SHALL teach that shipped history lives in `CHANGELOG.md` — journal tier:
append-only, dated, newest first — created conditionally when history accrues (like README).
`ROADMAP.md` SHALL keep only a short "Recently shipped" digest plus a one-line pointer;
a long dated history embedded in ROADMAP is non-conformant. Shipped history SHALL never be
routed into `archive/`; git remains the commit-level backstop. Relocating an embedded
history SHALL be a content-preserving move (safety rule S1).

#### Scenario: Embedded ROADMAP history is relocated, content-preserved
- **WHEN** a SETUP-guided agent standardizes a project whose ROADMAP embeds a long dated
  shipped-history
- **THEN** it creates a charter'd `CHANGELOG.md` holding every entry verbatim (newest
  first), reduces ROADMAP to a short digest + pointer, and updates the router — with zero
  entries dropped or reworded (disk-verifiable against the pre-change tree)

#### Scenario: No history accrued, no CHANGELOG forced
- **WHEN** the target project has no shipped history to speak of
- **THEN** no `CHANGELOG.md` is created (conditional file — don't force content)

### Requirement: Router teaches the three-way journal split
The router/tier guidance SHALL define the journal tier as `docs/YYYY-MM-DD-*.md` +
`NOTEBOOK.md` + `CHANGELOG.md`, split three ways: small finding from doing the work →
NOTEBOOK; shipped unit → CHANGELOG; substantial standalone record → `docs/`.

#### Scenario: CLAUDE.md written by SETUP names the three-way split
- **WHEN** SETUP writes or aligns a project's CLAUDE.md router
- **THEN** the journal tier it teaches includes `CHANGELOG.md` with the shipped-unit
  routing, alongside NOTEBOOK and dated docs/
