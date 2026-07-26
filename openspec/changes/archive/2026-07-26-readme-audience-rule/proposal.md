# readme-audience-rule — proposal

## Why

The public README had accumulated development-method minutiae (benchmark links, RED/GREEN
mechanics, "open lab notebook" framing) that confuse a fresh observer whose only question is
"what do these skills do and how do I install them." User directive 2026-07-26: README stays
potential-user-focused; workshop detail is confined to one labeled repo-layout paragraph —
and fixture projects (`harness/tidepool-fixture`, fictional TidePool) must be labeled as
test targets since they are publicly visible in the tree either way. The trim + the
RELEASING.md "README audience rule" already shipped (commit `995175d`); this change syncs
the rule into the `github-distribution` spec so the formal record matches.

## What Changes

- Tighten the `github-distribution` spec's "Public README at repo root" requirement: Why
  section is plain-language (no benchmark figures / internal evidence links), repo-layout
  paragraph is the *only* workshop mention and must label fixtures fictional, and the
  MUST-NOT list gains development/testing minutiae explicitly.
- No code, skill-text, or README changes — implementation already landed; this is a
  spec-sync change.

## Capabilities

### New Capabilities

*(none)*

### Modified Capabilities

- `github-distribution`: the public-README requirement gains the audience rule (user-focused
  only; workshop minutiae out; fixtures labeled fictional in the one repo-layout paragraph).

## Impact

- `openspec/specs/github-distribution/spec.md` (via archive sync). README.md and
  RELEASING.md already conform. Counterpart constraint (SKILL.md never simplified for human
  browsing) is recorded in RELEASING.md; it is a skill-authoring matter, out of this spec's
  distribution scope.
