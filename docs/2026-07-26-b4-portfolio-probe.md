# 2026-07-26 — B4 portfolio probe (Astronomy container, observational)

**Charter:** dated record of the B4 probe — 2 read-only SETUP reps (plan-only, Explore
agents, Sonnet-high) against the real `E:\Projects\VisualStudio\Astronomy` container.
Nothing applied; the container was not modified. Run `wf_b7f6a8da-f22`. Context: B4
amendment backlog item (NOTEBOOK 2026-07-13) + two same-day field signals (TSM glossary
cross-ref loop; this probe).

## What held (B4's core is right)
- **B4 predicate: 2/2 confirmed** on a real container that strains it (root ROADMAP.md +
  build-all.ps1 present). Both reps reasoned it cleanly — one cited the root `.gitignore`'s
  `/*/` pattern as the structural enforcement of container semantics.
- **No portfolio-level enforced set:** 2/2 declined to scaffold ARCHITECTURE / DOMAIN /
  NOTEBOOK / VERIFICATION / docs/ at the root — "per-project docs are the truth" survived
  contact with a real, doc-rich portfolio.
- **B3 flag-and-skip: 2/2 across all four sub-project classes** (routered repos,
  router-less git repos, read-only clones incl. the nested-clone gotcha, non-git utility
  dirs).

## The gap (found exactly where predicted)
Both reps hit the **S7 ↔ B4 collision** on the root router's Data-flow-hubs block (genuine
cross-repo contract prose: schedulerdb ownership, the two-stores-named-Catalog.db trap) —
S7 says move it to a charter home; B4 forbids creating one — and **resolved it
differently**:
- Rep 1: split — gotcha + pointer stays in the router, mechanics detail merged into the
  root **ROADMAP** ("the closest legitimate structural analog") — charter-questionable
  (mechanics in a status board).
- Rep 2: no move — reclassified the block as a "load-bearing disambiguation gotcha" and
  kept it in the **router** — router-fattening pressure, the exact S7 failure mode one
  level up.
Both explicitly acknowledged content that "no single sub-project owns" / "literally cannot
live in any one sub-project's own docs." Neither invented a portfolio DOMAIN (B4 held), so
the truth had nowhere sanctioned to go: **non-determinism from an unpinned rule** — the
same signature as every RED this week, and the same root cause as the TSM glossary loop
(portfolio truth has no owner, so each repo's locally-correct move produces cross-repo
cycles).
- Rep 2 also flagged its own B4 tension on the root ROADMAP's existence ("a literal
  reading a stricter reviewer could contest") — the field tree already runs a working
  exception to B4's letter.

## Bonus real-tree finding
Root `CLAUDE.md` § Other directories lists `AutoIntegrate` — no such directory exists in
the tree (rep 2, verified by listing + search). One stale token; user's call to strike.

## Adjudication → the B4 amendment decision (user's call, per the 2026-07-13 note)
The probe converts the backlog question into three concrete options:
- **A (recommended): sanction a thin portfolio `DOMAIN.md`** at container roots, chartered
  *cross-repo truth only* — shared glossary terms, cross-store disambiguations, cross-repo
  contracts (by pointer where a sub-project owns the detail). Pair with an
  **owner-project rule** (anything one project's code defines lives in that project's docs;
  the portfolio doc holds only what no single project owns) and **one-way pointers**
  (sub-projects point up; the portfolio doc points down by name; never mutual) — which is
  what breaks the TSM glossary loop. B4 amended: router + optional thin DOMAIN + optional
  thin status ROADMAP; never the rest of the set.
- **B: owner-project rule only** — no portfolio docs; every shared term gets a forced
  owner. Cheapest, but the probe shows real "nobody owns it" content exists; it would keep
  leaking into routers/status docs as improvisation.
- **C: pin the status quo** — allow root ROADMAP as the sequencing home and router gotchas
  for disambiguations. Legalizes today's tree but leaves the collision unpinned →
  non-determinism persists.
Whatever is chosen ships as a SETUP B4 amendment (+ likely a MAINTAIN targeting clause for
portfolio-truth graduates), iron-law gated: RED exists (this probe's 1/1-vs-1/1 divergence
+ the TSM loop), GREEN on a synthetic container fixture (this container is now the deriving
evidence — poisoned for validating the rule).
