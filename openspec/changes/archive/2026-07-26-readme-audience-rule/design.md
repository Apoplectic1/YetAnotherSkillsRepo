# readme-audience-rule — design

## Context

README.md is the public storefront (excluded from the audited doc set by the router). The
2026-07-26 trim removed method minutiae; RELEASING.md § Public mirror now carries the
"README audience rule". The github-distribution spec's README requirement predates the trim
("evidence-backed" Why section, "lab notebook" framing) and must be brought to the new
target state.

## Goals / Non-Goals

**Goals:** spec text matches the shipped README shape and encodes the audience rule so
future README edits are judged against it.

**Non-Goals:** no README/skill edits (already conformant); no new tracking artifacts; the
SKILL.md-never-simplified counterpart stays in RELEASING.md (authoring concern, not
distribution).

## Decisions

- **D1 — one MODIFIED requirement, not a new one.** The audience rule is a property of the
  existing "Public README at repo root" requirement; a second requirement would split one
  contract across two headings.
- **D2 — fixture labeling is REQUIRED, not forbidden-mention.** `harness/` is publicly
  visible; one labeled sentence ("fictional test targets, not templates") in the repo-layout
  paragraph prevents the confusion that total silence would invite.

## Risks / Trade-offs

- [Spec drifts again after future README restyling] → the requirement pins content *roles*,
  not exact prose, so restyling within the audience rule needs no spec change.

## Migration Plan

None — spec-sync only (no back-compat by policy).

## Open Questions

None.
