# docs-architecture-audit: delta for spec-wording-2026-10-12

## MODIFIED Requirements

### Requirement: Ancestor routers are convention sources
Every `CLAUDE.md` above the audited project's root (each loads in every session launched
there) SHALL be read as a convention source and never edited: the cross-reference pass SHALL
resolve each upward pointer against the ancestor's current text, a convention the ancestor
scopes to the repositories beneath it SHALL be checked as a contract (code violating it →
`flag-code-bug` citing the ancestor line, R7; a repo doc agreeing with that code is not
evidence against the convention), and a repo doc restating an ancestor's rule SHALL be a
placement flag `cross-ref+delete`. The ancestor's own defects belong to its own audit (R16).

**Status note (2026-10-12):** satisfied by baseline behavior, not by skill text. RED 6/6 on
the reefstack `audit-scope` variant: on ReefDash (whose router points up twice) both reps
resolved the dangling "Alert palette" pointer, raised `flag-code-bug` for naive local time
against the root's UTC rule, and `cross-ref+delete` for the restated TOML rule (AR1 to AR3),
leaving the valid pointer alone (AR4); on DoseKeeper (whose router never points up) both
reps read the parent "as an ancestor, auto-loaded" unprompted and raised `flag-code-bug` for
both violated conventions (AR5, AR6). Every rep listed "the skill does not say whether an
ancestor router counts" among its uncertainties. Per the no-failure gate no ancestor-router
rule was added to the skill; the candidate text (labeled R29 in that change's design record,
a number the scoped-modes rule has since taken) is held there and takes the next free number
if it ever ships. The field case (the ATML audit, 2026-09-24, a Sonnet fan-out over a 27 KB
router) remains the evidence that a real run can miss it; if one does again, encode it then.

#### Scenario: An uncited ancestor convention is checked
- **WHEN** an ancestor router states a convention for every repository beneath it, the
  audited repo's router never cites it, and the repo's code violates it with its doc agreeing
- **THEN** a `flag-code-bug` is raised citing the ancestor line, and the doc is not fixed
  toward the code

#### Scenario: A pointer to a rule the ancestor no longer carries
- **WHEN** the audited repo's router cites a named rule in an ancestor's section and that
  section does not hold it
- **THEN** the cross-reference pass reports the pointer as dangling

#### Scenario: A restated ancestor rule
- **WHEN** a repo reference doc restates, unattributed, a rule the ancestor router carries
- **THEN** one placement flag proposes `cross-ref+delete`
