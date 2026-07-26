# b4-portfolio-domain — design

## Context

B4's core survived the probe (2/2 no portfolio set; B3 clean) — the amendment is a scoped
carve-out, not a rewrite. The gap: *stable* cross-repo truth (shared glossary, store
disambiguations, cross-repo contracts) has no sanctioned home, so reps improvise
(→ root-ROADMAP charter mismatch, router fattening, cross-repo pointer loops). The user's
real container already runs a working exception (thin root ROADMAP for volatile
status/sequencing) that the amendment legalizes.

## Goals / Non-Goals

**Goals:** one sanctioned home per truth class at a container root; deterministic S7
destination when leaning a container router; loop-free cross-repo referencing; MAINTAIN
knows where portfolio graduates go.

**Non-Goals:**
- No full enforced set at container roots (B4's "portfolio-level set is noise" stands for
  ARCHITECTURE / NOTEBOOK / VERIFICATION / docs/ / CHANGELOG).
- No cross-repo audit machinery (audits stay router-anchored per repo; the portfolio DOMAIN
  is audited from the container root like any doc its router names).
- No migration of the Astronomy container in this change (consumer adoption afterward).

## Decisions

- **D1 — DOMAIN, not a new filename.** The portfolio home reuses the canonical `DOMAIN.md`
  name (S6 uniformity; the content class — glossary, domain conventions — is DOMAIN-shaped).
  Its charter line marks it portfolio-scoped: cross-repo truth only.
- **D2 — three truth classes, three homes.** Volatile status/sequencing → thin root
  ROADMAP (legalized); stable cross-repo truth nobody owns → portfolio DOMAIN; anything one
  repo defines → that repo's docs, referenced by name (owner-project rule).
- **D3 — one-way pointers, direction fixed.** Sub-projects point *up* only for shared
  terms; the portfolio DOMAIN points *down* by name only for owned detail. Mutual pointers
  are the loop mechanism — named as a violation.
- **D4 — MAINTAIN flag-and-ask fallback.** Where no portfolio DOMAIN exists (convention not
  adopted at that container), a portfolio-level graduate is flagged for the user, never
  improvised into a cross-repo pointer — ownership of portfolio truth is a user decision.
- **D5 — S7 destination table gains the container case.** Leaning a container router:
  cross-repo reference prose → portfolio DOMAIN (not per-project docs, not ROADMAP, not
  kept as "gotcha"). Genuine one-line disambiguation gotchas may stay in the router — the
  content test, not size, still governs.
- **D6 — new synthetic fixture, not TidePool.** A small fictional portfolio ("ReefStack"
  or similar: 2–3 routered sub-projects + shared glossary + a cross-store name collision +
  one owned contract + a planted mutual-pointer loop). TidePool is single-project shaped;
  the Astronomy container and TSM are deriving evidence and poisoned.

## Risks / Trade-offs

- [Portfolio DOMAIN becomes a dumping ground] → charter line restricts to cross-repo truth;
  owner-project rule diverts everything ownable; AUDIT R26/R10 placement machinery applies
  to it like any reference doc.
- [Reps create portfolio DOMAIN where unwarranted (single-project trees)] → GREEN control:
  a non-container fixture run must not produce one; the file stays *optional* — created
  when cross-repo truth exists, not scaffolded by default.
- [RED may partially no-fail on the MAINTAIN clause] → acceptable: the SETUP amendment
  carries probe-RED; the MAINTAIN clause has the TSM loop as field evidence and needs its
  own synthetic RED cell (a portfolio-level truth in a sub-project journal).
- [Word growth in B4] → target ≤ ~100 added words across both skills.

## Migration Plan

None in-skill (no back-compat). Consumer adoption (Astronomy container DOMAIN.md creation,
Data-flow-hubs relocation, TSM glossary-loop resolution to one-way pointers) happens after
deploy as normal doc work in those repos.

## Open Questions

None blocking — final wording after the fixture RED classifies the failure forms.
