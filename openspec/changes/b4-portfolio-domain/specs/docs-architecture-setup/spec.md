# docs-architecture-setup — delta: b4-portfolio-domain

## ADDED Requirements

### Requirement: Container roots support a thin portfolio DOMAIN for cross-repo truth
The SETUP skill SHALL treat a container root as router-plus-portfolio-tier: the `CLAUDE.md`
router (B4's core, unchanged), optionally a thin portfolio `DOMAIN.md` chartered
*cross-repo truth only* (shared glossary terms, cross-store disambiguations, cross-repo
contracts by pointer where a sub-project owns the detail), and optionally a thin
status/sequencing `ROADMAP.md` — and SHALL NOT scaffold the rest of the enforced set at a
container root. The portfolio DOMAIN is created when cross-repo truth exists (e.g. found
while leaning the container router per S7), never by default. Companion rules: content one
project's code defines lives in that project's docs (owner-project rule); sub-projects
point *up* to the portfolio DOMAIN for shared terms and the portfolio DOMAIN points *down*
by name for owned detail — mutual cross-repo pointers are a violation (loop breaker).
Leaning a container router routes cross-repo reference prose to the portfolio DOMAIN — not
into ROADMAP, not retained as router "gotchas" (one-line genuine disambiguations may stay;
the content test governs). Gated on RED→GREEN per the iron law on a synthetic container
fixture (the Astronomy container and TSM are deriving evidence — poisoned).

#### Scenario: Container router leaned with cross-repo prose present
- **WHEN** SETUP runs at a container root whose router embeds cross-repo contract/glossary
  prose (S7 content test positive)
- **THEN** the prose moves to the portfolio `DOMAIN.md` (created thin if absent, chartered
  cross-repo-only) with a router pointer — not into ROADMAP, not left in the router

#### Scenario: No portfolio set beyond the sanctioned pair
- **WHEN** SETUP runs at a container root
- **THEN** no portfolio-level ARCHITECTURE / NOTEBOOK / VERIFICATION / docs/ / CHANGELOG is
  scaffolded, and a portfolio DOMAIN is not created when no cross-repo truth exists

#### Scenario: Owner-project rule diverts ownable content
- **WHEN** candidate portfolio-DOMAIN content is defined by a single sub-project's code
  (e.g. a store schema one repo manages)
- **THEN** it lives in that sub-project's docs and the portfolio DOMAIN carries at most a
  one-line pointer down by name

#### Scenario: Single-project tree control
- **WHEN** SETUP runs on an ordinary (non-container) project
- **THEN** no portfolio DOMAIN appears — the amendment changes container behavior only
