# ROADMAP.md — forward plan

**Charter:** forward-looking design + a short Recently-shipped digest (shipped history →
`CHANGELOG.md` when it accrues; git backstops commits). The design doc's own open-items
section closed 2026-07-07 with nothing open.

## Open
- **AUDIT scaled-coverage mode** (2026-07-17 — gated, GREEN-only): one-round mode for small /
  low-drift doc sets. Refined shape, companion edits, and gate in NOTEBOOK 2026-07-17. Its
  informal "field R26" alias is stale — R26 was taken by the router-placement clause
  (shipped 2026-07-17); assign the next free number when it ships.
- **B4 portfolio probe** (2026-07-13): B4 portfolio-DOMAIN amendment — cheap observational
  SETUP probe at the Astronomy container first (expected router-only per B4; old projects get
  B3 flag-and-skip lines). Refined in NOTEBOOK 2026-07-13. *(Split out 2026-07-17: the
  fat-router-lean half shipped as SETUP S7 + AUDIT R26.)*
- **Deferred until a second skill family onboards** (decided 2026-07-10: flat `skills/` stays):
  restructure into per-family dirs (`skills/docs-architecture/…`) — requires deploy.sh
  two-level glob + prune re-verify, README/CLAUDE/ARCHITECTURE link updates, one commit.
  Trigger: onboarding `diagnose`/`graphify`/etc. into this repo.

## Recently shipped
- 2026-07-17 — **fat-router-lean shipped: SETUP S7 + AUDIT R26** (change: `fat-router-lean`).
  Router lean on encounter (content test, perform via S1 move, B2 carve-out) + router
  placement-audited (one structural flag per block, currency orthogonal). RED reproduced only
  at scale (real 24 KB TP router, 2/2; small synthetic 0/3) — mechanism: B2 misread as
  forbidding the trim. GREEN 4/4 disk-verified. Fixture catalog: `harness/catalog-fat-router.md`.
- 2026-07-13 — **hybrid-rulebook family shipped + CHANGELOG convention** (change:
  `apply-hybrid-rewrite`): all four SKILL.md replaced with the RED/GREEN-validated hybrid
  candidates (rule IDs, −21% words, portable GitHub-URL footers); SETUP A2′ + AUDIT
  R25/R14/R21 encode shipped-history→`CHANGELOG.md`; deployed + pushed. Validation:
  `docs/2026-07-13-round3-red-green-results.md`. TidePool fixture promoted to `harness/`.
- 2026-07-10 — **GitHub mirror renamed** `docs-architecture` → `YetAnotherSkillsRepo`
  (redirects live); README reframed as skills home (flagship: docs-architecture family);
  `github-distribution` spec Purpose filled + URL updated; RELEASING's stale "No remote
  yet" replaced with the mirror section (missed at publication).
- 2026-07-10 — **published to GitHub** (`github.com/Apoplectic1/docs-architecture`, MIT):
  fresh public README (OpenSpec-style Why / Updating / Usage Notes backbone), LICENSE,
  `origin` wired, `main` pushed — `dev` stays local (change: `publish-to-github`).
- 2026-07-10 — **AUDIT worker-death hardening** (field RED from TSM's live audit run — a
  section worker died on an API 5xx and vanished silently; synthetic RED→GREEN on a
  non-derived fixture, GREEN 2/2): fan-out step 1 gains retry-a-dead-worker-once, step 3 a
  coverage note naming lost spans + their fallback coverage. On `dev`; deploys with the next
  `main` merge.
- 2026-07-10 — **first self-audit** (4 rounds, 3 models, 36 findings; lessons in NOTEBOOK):
  design-doc running-commentary staleness fixed (SETUP-spec survey stamped as a 2026-06-28
  derivation snapshot), `README.md` dissolved into `DOMAIN.md`/`ARCHITECTURE.md` (the
  publish-to-GitHub candidate retired with it — a public README would be rewritten fresh at
  publish time), `deploy.sh` now marker-stamps deployed skills and prunes family-stale
  dirs, VERIFICATION gains the downstream-state method rule.
- 2026-07-07 — review round 2, behavioral batch (RED→GREEN, archived): SETUP gains the
  non-git recovery net + container-root router-only rules (both GREEN 2/2); legacy-domain
  rename, scoped audit-first, and AUDIT right-sizing all passed RED (no-failure gate —
  status-noted in specs, no text). Deployed.
- 2026-07-07 — family review round 2, mechanical half: MAINTAIN SDO description, README tier
  line gains VERIFICATION, whats-next `flag-code-bug` term, design-doc reconciliations,
  benchmark catalog addendum (C19/C20/C21).
- 2026-07-07 — doc set scaffolded by SETUP's first run here (dogfooding); domain doc always
  named `DOMAIN.md` (dropped the elicited-name model).
- 2026-07-06/07 — `fix-skill-review-findings` batch (openspec change, archived): review
  fixes across SETUP / AUDIT / whats-next specs.
- 2026-06-28/29 — all four skills built + deployed; AUDIT worker-model benchmark
  (`docs/2026-06-29-audit-model-benchmark.md`).
