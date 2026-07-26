# docs-architecture-maintain — delta: b4-portfolio-domain

## ADDED Requirements

### Requirement: Portfolio-level graduates target the portfolio DOMAIN or flag-and-ask
The MAINTAIN skill SHALL route a graduate whose standing truth is portfolio-level — it
spans repos, or no reference doc in the current repo's charter set can own it — to the
container's portfolio `DOMAIN.md` when the convention provides one (pointer discipline per
the SETUP amendment: one-way only). When no portfolio DOMAIN exists, the skill SHALL
flag-and-ask — present the graduate with its portfolio-level classification for the user
to place — and SHALL NOT improvise a cross-repo pointer into another project's docs
(two repos improvising produces ownerless cross-ref loops). Gated on RED→GREEN per the
iron law on a synthetic container fixture; the TSM glossary loop is deriving field
evidence (poisoned for validation).

#### Scenario: Portfolio truth with a portfolio DOMAIN available
- **WHEN** a sweep classifies a journal truth as standing and portfolio-level, and the
  container provides a portfolio DOMAIN
- **THEN** the graduate targets that DOMAIN (subject to M9/M14 as usual), and the source
  repo keeps a one-line upward pointer per the normal disposition rules

#### Scenario: Portfolio truth, no portfolio DOMAIN
- **WHEN** the same class of truth surfaces and no portfolio DOMAIN exists
- **THEN** the run flags it for the user (report + adjudication) instead of writing a
  pointer into a sibling repo's docs — no cross-repo improvisation

#### Scenario: Mutual pointer never created
- **WHEN** resolving where a shared term lives
- **THEN** the outcome never leaves two repos pointing at each other for the same truth
