# ROADMAP.md — forward plan

**Charter:** forward-looking design + a short Recently-shipped digest (shipped history →
`CHANGELOG.md` when it accrues; git backstops commits). The design doc's own open-items
section closed 2026-07-07 with nothing open.

## Open
- **AUDIT scaled-coverage mode** (2026-07-17 — gated, GREEN-only): one-round mode for small /
  low-drift doc sets. Refined shape, companion edits, and gate in NOTEBOOK 2026-07-17. Its
  informal "field R26" alias is stale — R26 was taken by the router-placement clause
  (shipped 2026-07-17); assign the next free number when it ships.
- **Portfolio-convention consumer adoption** (post-`b4-portfolio-domain`, shipped
  2026-07-26): in their own sessions — (a) Astronomy container: create the portfolio
  `DOMAIN.md` (cross-repo truth only), relocate the router's Data-flow-hubs detail per
  B4′/S7, keep readings-style owned contracts pointed down; (b) TSM + siblings: resolve
  the glossary loop to one-way pointers against the new portfolio DOMAIN.
- **MAINTAIN right-sizing candidates** (2026-07-26 — gated, from TSM's field feedback,
  NOTEBOOK same date): (a) skill `description` says "periodic journal-health sweep" —
  candidate rewording to trigger conditions (~10 archived changes / subsystem rewrite /
  journal visibly ahead); (b) **prune-teeth / anti-ratchet** — graduate:prune ran 12:1 in
  the field; candidate rule making prune candidates a first-class sweep output (or a
  graduation-count budget). Both iron-law gated (RED on a non-derived fixture; TSM is the
  deriving project). DOMAIN's When-to-reach guidance already updated (doc-side, ungated).
- **Deferred until a second skill family onboards** (decided 2026-07-10: flat `skills/` stays):
  restructure into per-family dirs (`skills/docs-architecture/…`) — requires deploy.sh
  two-level glob + prune re-verify, README/CLAUDE/ARCHITECTURE link updates, one commit.
  Trigger: onboarding `diagnose`/`graphify`/etc. into this repo.

## Recently shipped
- 2026-07-26 — **B4 portfolio DOMAIN shipped: SETUP B4′ + MAINTAIN M15** (change:
  `b4-portfolio-domain`; probe → user Option A → RED/GREEN on the new ReefStack container
  fixture). Container root = router + optional thin portfolio DOMAIN (cross-repo truth
  only) + optional thin status ROADMAP; owner rule; one-way pointers; M15
  portfolio-graduate targeting with flag-and-ask on M13 rails. Records:
  `docs/2026-07-26-b4-portfolio-probe.md`, `docs/2026-07-26-b4-red-green.md`.
- 2026-07-26 — **batch 2 shipped: AUDIT R28 + MAINTAIN M9′/M14** (changes:
  `derivability-discriminator`, `m9-hold-on-bloat`). R28: stale derivable rationale-free
  values get deletion-led fix proposals (stop re-caching greps). M9 hardened (apply-time
  content test; stuff-then-ask is the violation) + M14 hold procedure (report + one
  ROADMAP split-job line; promotions land post-split). RED/GREEN on TidePool DV/FA cells +
  generated fat-ARCH variant; record: `docs/2026-07-26-batch2-red-green.md`.
- 2026-07-26 — **code-bug persistence shipped: AUDIT R27 + MAINTAIN M12/M13** (change:
  `code-bug-persistence`; field RED from a MAINTAIN-on-TSM run). Report-only flags now
  persist to the target project's tiers before a run ends (dated `<skill>-report.md` +
  deduplicated ROADMAP open-lines; deferred → pointer line); MAINTAIN gains the in-schema
  `flag-code-bug` channel (code is the suspect; archived-design values and corroborated
  history are never contracts). RED/GREEN on TidePool + CB1–CB4 plants, two GREEN-round
  refactors, final wording micro-tested 2/2. Record:
  `docs/2026-07-26-code-bug-persistence-red-green.md`.
- 2026-07-26 — **openspec-archive awareness shipped: MAINTAIN M11 + AUDIT R14/R15 + SETUP B1**
  (change: `openspec-archive-awareness`). Archived `openspec/changes/archive/*/design.md` is
  now a first-class MAINTAIN source (graduate disposition pinned `cross-ref`-only; archive
  never edited; router's generic exclusion overridden), AUDIT never currency-audits the
  openspec archive and R15 suppresses tier-violations on cited archived design docs
  (consistency check only), SETUP's router exclusion wording carves the archive out. RED/GREEN
  on the TidePool fixture extended with planted archives (catalog O1–O4); RED failure mode =
  non-deterministic hedged sourcing + unpinned disposition, GREEN clean. Record in the design
  doc; supersedes half of the 2026-07-17 "no openspec integration" decision (in-flight/specs
  exclusions stand).
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
- 2026-07-11 — **README Agent-Skills portability shipped** (change:
  `openspec/changes/archive/2026-07-11-readme-portability/design.md`): README reframed as
  standard Agent Skills (agentskills.io), plus a "Beyond Claude Code" usage-notes section —
  marquee adopters, worker-model/fan-out degradation caveats, CLAUDE.md-vs-AGENTS.md
  adaptation note. *(Digest line added by the 2026-07-26 MAINTAIN sweep — the ship predates it.)*
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
