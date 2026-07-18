# fat-router-lean — proposal

## Why

The 2026-07-12 TargetPlanner ecological run (field finding 1) showed both skill generations
scaffold and route correctly but leave an existing oversized CLAUDE.md router fat (24→26 KB old,
net-flat hybrid): the enforced-set table says "kept thin," yet no SETUP rule compels relocating
glossary/contract prose on encounter, and AUDIT never placement-flagged the router itself. An
over-40-KB router degrades harness performance, and off-charter reference content in the router
escapes the tier model entirely.

## What Changes

- **SETUP gains a lean rule**: on encountering a router carrying off-charter reference content,
  SETUP *performs* a content-preserving relocation (S1 move semantics) of that weight to
  charter-selected reference docs (e.g. glossary / abbreviations-for-CLI-use → DOMAIN.md, an
  authoring convention squarely in DOMAIN's charter). Trigger is a **content test** — "reference
  content vs routing/gotchas" — not a numeric size threshold; the ~40 KB perf line is cited as
  the *why*, never the trigger. Moves are reported in the run summary.
- **AUDIT gains one clarifying clause**: the CLAUDE.md router is itself explicitly
  placement-audited — off-charter reference content in the router is a structural placement flag
  (move-to the charter-owning reference doc), same family as R25.
- Both rule texts are **gated RED→GREEN** before deploy: SETUP 2+2 reps on
  `harness/tidepool-fixture` + a fat-router variant, plus a narrow AUDIT probe. (Fixture not
  poisoned: the rule derives from the TP ecological run, not TidePool.)

Out of scope (tracked separately): the B4 portfolio-DOMAIN amendment (starts with an
observational probe at the Astronomy container) and the AUDIT scaled-coverage mode (field
"R26", independently gated).

## Capabilities

### New Capabilities

(none)

### Modified Capabilities

- `docs-architecture-setup`: new requirement — SETUP relocates off-charter router weight to
  charter-selected reference docs on encounter (content-test trigger, perform not propose,
  content-preserving, reported).
- `docs-architecture-audit`: new requirement — the router is placement-audited; off-charter
  reference content in CLAUDE.md yields a structural move-to flag.

## Impact

- `skills/docs-architecture-setup/SKILL.md` — new S-rule (lean rule) + likely one-line touch to
  the enforced-set "kept thin" wording so the rule is discoverable.
- `skills/docs-architecture-audit/SKILL.md` — one clarifying clause in the Scope/Rules section.
- `harness/` — fat-router fixture variant for RED→GREEN; catalog entry.
- Deploy via `deploy.sh` from `main` after GREEN (RELEASING.md policy).
- Docs: ROADMAP Open item closes; NOTEBOOK gate outcome entry; CHANGELOG on ship.
