# audit-scope-from-routers: design

## Context

Both items come from the HDL tree's audits. The ATML audit (2026-09-24) found repositories
citing an umbrella rule that had moved to the other umbrella, and restating rules the HDL
router already carries as an ancestor; the maintain sweep (2026-09-26) found 12 false SHALL
claims in router-named specs that no default sweep reads, and a dated reference doc in
`docs/` that R14's wholesale exclusion would skip while R12 names it. The ROADMAP carried
them as "Ancestor-router conventions" and "Scope precedence; router-named specs".

## Decisions

- **D1: the router sets the tier, not the directory or the name.** The owner's global rule
  dates every new `docs/` file, reference docs included (ATML's `2026-09-06 - LAB-KIT.md` is
  routed as current truth), so a dated-vs-undated test would misfire across the portfolio.
  A doc the router routes as current truth is reference-tier wherever it sits; R13 and R14
  exclude what the router does not route that way.
- **D2: a router-named spec is reference for currency and never an edit target.** A spec
  changes only through a change (the project's own rule, and the openspec validator's). A
  stale claim in one is the new report-only action `spec-change`, naming the change that
  would correct it; R27 persists it with the other report-only flags. R7's code-is-suspect
  reading holds only while the spec stands uncontradicted: when code, router and reference
  docs agree against the spec, the spec is the stale party.
- **D3: ancestor routers are convention sources, read and never edited.** Every `CLAUDE.md`
  above the project root loads in each session there. An upward pointer resolves against
  the ancestor's current text; a convention the ancestor scopes to the repositories beneath
  it is a contract in each (R7 across the ancestor line); a restatement is `cross-ref+delete`.
  The ancestor's own defects belong to its own audit (R16).
- **D4: the iron law decides what ships as text.** Six RED reps on the reefstack variant:
  every ancestor cell (AR1 to AR6, cited and uncited) and the routed-doc cell (SP1) passed on
  the current text, each rep reading the parent unprompted and applying R7 across it, while
  listing "the skill does not say" for both. The router-named-spec cell (SS1) failed 2/2:
  the stale SHALL went out as `flag-code-bug` by R7's letter, the reps saying the schema had
  no action for a spec that needs a change. So D2 ships as skill text (R4, R13, the schema);
  D1 and D3 ship as spec requirements with status notes, their candidate text held in this
  change's record (the owner's call, 2026-10-12: status notes only).
- **D5: the cells must not lead the reader to the ancestor.** The first four RED reps ran
  on ReefDash, whose router points up twice; that alone could explain the parent being read.
  AR5 and AR6 were added on DoseKeeper, whose router never points up, and passed the same
  way. A fixture for an "unprompted" behavior needs a target that gives no prompt.

## Verification

Single-agent audit reps (one round, report-only, R18 to R23 and R27 waived), Sonnet:
RED six reps (ReefDash 2, PulseMonitor 2, DoseKeeper 2) on the current text, GREEN two reps on
PulseMonitor with the candidate. Every copy byte-untouched after each rep. Record:
`docs/2026-10-12 - audit-scope-red-green.md`.
