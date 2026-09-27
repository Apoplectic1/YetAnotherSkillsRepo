# ROADMAP.md — forward plan

**Charter:** forward-looking design + a short Recently-shipped digest (shipped history →
`CHANGELOG.md` when it accrues; git backstops commits). The design doc's own open-items
section closed 2026-07-07 with nothing open.

## Open
- **Ancestor-router conventions** (2026-09-24, from the HDL tree's ATML audit): make the AUDIT
  sweep check a repository against its ancestor routers' conventions, not only its own
  charter, so an umbrella rule (the HDL tree's Zynq IRQ-wrapper check, its LF rule) is
  audited in every repository beneath it. Seen there: a rule moved between umbrellas left
  the repositories that cite it pointing at a router that no longer carries it.
- **Journal rollover and the overflow directory** (2026-09-26, from the HDL tree's ATML maintain
  sweep; the owner chose chronological rollover and the subdirectory). The journals outgrow one
  file: the ATML umbrella's NOTEBOOK reached 138 KB in 20 days, the Arty's 311 KB in 33, and a
  sweep needed three workers for one file. Decided: a journal rolls over chronologically, and
  its closed periods live in a directory named for the file (`NOTEBOOK/` beside
  `NOTEBOOK.md`), so rollover files never clutter the root; `NOTEBOOK.md` stays the live file
  every router, charter and skill names. Proposed, to settle in the change: (a) the trigger is
  size, not the calendar (the live file past a budget, about 40 KB, rolls whole closed entries
  out oldest first; a busy month here is 300 KB, too big for one file); (b) a rollover file is
  named by the first date it holds (`NOTEBOOK/2026-09-06.md`, up to the next file's date), so a
  dated citation ("NOTEBOOK 2026-09-16") resolves by one grep over `NOTEBOOK.md NOTEBOOK/` and
  no pointer changes; (c) open threads never roll out (an entry with a live item stays, or the
  item is carried into the live file's open list first, so `whats-next` still finds it);
  (d) one rule for every overflow: a file's overflow lives in a directory of its own name, a
  journal split by date (NOTEBOOK, CHANGELOG), a bloated reference doc split by topic with the
  parent as its index (`ARCHITECTURE/`), which gives MAINTAIN's M14 split job its target
  shape; (e) MAINTAIN's M3 archive disposition then applies to dated `docs/` records only,
  never to NOTEBOOK entries, which move by date, not by judgment. Touches SETUP (the layout
  and the charter line), MAINTAIN (M3, M14, the rollover as a sweep step or its own trigger),
  AUDIT (R14's journal set includes the directory), `whats-next` (open items across the live
  file only). **Piloted and applied 2026-09-26** across the HDL tree (the ATML umbrella's
  NOTEBOOK entry of that day records it): seven journals past 40 KB rolled (the ATML
  umbrella's, the Arty's, HlsLibrary's, the KR260's, EthernetLibrary's and TxnContractLibrary's
  NOTEBOOKs, the Arty's CHANGELOG), by a script that moves entries byte for byte and checks it.
  Findings for the change: (a) and (b) hold; whole days stay in one file so a date names one
  file; the live file is cut to half the budget (about 20 KB) so it does not roll again the
  next day; a newest-first CHANGELOG rolls from its oldest end; an undated `##` section (an
  Open threads list) stays live after the charter; a carried open thread gets an "Open threads
  (carried at a rollover)" section. **A prerequisite:** an umbrella over repositories that
  ignores `/*/` silently drops the overflow directory (and a kit copied from what is committed
  loses it); the owner's rule is that a directory created in a repository is tracked, so such
  an umbrella ignores its nested repositories by name, each reason on its own line (git reads a
  comment only on a line of its own; a trailing one makes the pattern literal). The three
  HDL-side umbrellas were inverted; the root and Astronomy still carry `/*/`, and the root's
  list must also name its foreign areas (WSL disks, sync metadata). A manifest that enumerates
  files (the ATML lab kit) is a consumer the rollover must update. SETUP should create an
  umbrella's ignore file by name, never by wildcard. **The index** (added the same day, backfilled in all seven overflow directories):
  `<JOURNAL>/INDEX.md`, one section per rolled file (date span, size), one line per entry (date,
  title); the rolled files are frozen, so the index is regenerated at each rollover without
  changing its existing lines. The same property gives MAINTAIN a watermark: a sweep records
  the last rolled file it covered and the next reads only the live file and newer rollovers.
  The scripts: `docs/2026-09-26 - journal-rollover/` (`rollover.py`, `journal_index.py`).
- **Always-on budget** (2026-09-26, queued after journal rollover; the owner's question:
  the 40 KB gate is brute force, is there a better way?). Measured that day (NOTEBOOK
  2026-09-26): a session under the HDL tree loads 52 to 79 KB of routers before its first
  question (the owner's global file 22.5 KB, then three to four ancestor routers), and no rule
  counts the chain: the 40 KB line is the harness's per-file warning, about 10k tokens, about
  5 percent of a 200k window, the right budget at the wrong scope. The cost model: context
  room (linear in tokens), interference (scales with the count of directives the session does
  not need, not with bytes; an activity's gotcha misapplied elsewhere) and staleness (scales
  with volatility). The rule: an item is always-on only if it passes breadth (every session
  launched here needs it) and stability (it changes less often than the audit cadence); S7's
  content test gains that scope half (12.8 KB of HLS synthesis gotchas pass S7 today and fail
  breadth). Failed items go on demand behind a one-line always-on trigger: a skill whose body
  loads on invocation (the owner's rule 17 pattern; an activity's gotcha pack as a skill), or a
  path-scoped rule file if the harness has them (verify first); reference docs are read by
  section (topic-named headings, `grep -n "^## "` then the span). The tripwire: one number on
  the chain in tokens (the global file, every ancestor router, the memory index), its threshold
  derived from the accepted share of the window, measured per launch directory by a script and
  reported by AUDIT as a coverage row; the number detects, the test decides. Touches SETUP
  (S7's scope half, the trigger-line pattern), AUDIT (R26 gains the scope test, the chain row),
  the design doc (the cost model). Pilot: HlsLibrary's router (32.6 KB: element maps to the
  class READMEs that already hold them, gotchas to a skill, about 9 KB left), the ATML
  umbrella's DOMAIN (40 KB, four headings) for section reads, then the Arty's 27 KB router.
  Non-derived RED/GREEN: TidePool's fat-router variant plus a fat-chain container variant.
- **The split job's owner** (2026-09-26): M9 and M14 hold promotions "until the split,
  setup/audit territory", and no skill describes the split; three HDL docs past 40 KB hold ten
  promotions (the ATML umbrella's `docs/2026-09-26 - maintain-report.md`). Candidate: the
  overflow rule's other half, a bloated reference doc split by topic into a directory named for
  it (`ARCHITECTURE/`), the parent left as the index with one line per part. Unpiloted: pilot
  the Arty's ARCHITECTURE (72 KB, a halted board, low risk), then codify the procedure in SETUP
  with MAINTAIN's M14 naming the shape. Sequenced after always-on budget: a split is worth it
  only where section reads are not enough.
- **Release-close currency lens** (2026-09-26): after a milestone the reference tier goes stale
  in predictable phrases ("waits for", "not yet", "until", "today", a version, a count). The HDL
  sweep's best worker was one such lens over the reference tier, 188k tokens for 13
  corrections, against about 2.6M for the full sweep (NOTEBOOK 2026-09-26). A named cheap
  mode: that lens plus AUDIT's cross-reference pass, run at release close, shift-left for
  currency as the family already shifts graduation left. Owner to decide: an AUDIT scoped mode
  (with the scaled-coverage item below) or a MAINTAIN round-2 lens. RED on TidePool with
  post-release phrasing plants.
- **Scope precedence; router-named specs** (2026-09-26): (a) R14 excludes `docs/` wholesale
  while R13 puts a router-named leaf in scope, and a project that keeps undated reference docs
  in `docs/` (the HDL tree's toolchain record, where a pointer check found stale pointers) has
  both apply: state that R13 wins. (b) `openspec/specs` is workflow-only by the design doc, but
  a project whose routers cite its specs by name as its rules has them as reference tier; the
  HDL sweep's spec lens found 12 false SHALL claims no default sweep reaches. Class:
  router-named specs are reference-tier for AUDIT's currency pass, never edited by it (a spec
  changes through a change), the finding a flag naming the cleanup change. (c) The family's
  `YYYY-MM-DD-<slug>` and B2's normalization collide with the owner's global rule
  (`YYYY-MM-DD - name`): folded into journal-rollover as the project's stated pattern.
- **AUDIT scaled-coverage mode** (2026-07-17 — gated, GREEN-only): one-round mode for small /
  low-drift doc sets. Refined shape, companion edits, and gate in NOTEBOOK 2026-07-17. Its
  informal "field R26" alias is stale — R26 was taken by the router-placement clause
  (shipped 2026-07-17); assign the next free number when it ships.
- **Portfolio-convention consumer adoption** (post-`b4-portfolio-domain`, shipped
  2026-07-26): in their own sessions — (a) Astronomy container: create the portfolio
  `DOMAIN.md` (cross-repo truth only), relocate the router's Data-flow-hubs detail per
  B4′/S7, keep readings-style owned contracts pointed down; (b) TSM + siblings: resolve
  the glossary loop to one-way pointers against the new portfolio DOMAIN.
- **Deferred until a second skill family onboards** (decided 2026-07-10: flat `skills/` stays):
  restructure into per-family dirs (`skills/docs-architecture/…`) — requires deploy.sh
  two-level glob + prune re-verify, README/CLAUDE/ARCHITECTURE link updates, one commit.
  Trigger: onboarding `diagnose`/`graphify`/etc. into this repo.

## Recently shipped
- 2026-07-26 — **maintain right-sizing shipped: MAINTAIN M16** (change:
  `maintain-right-sizing`): the dated report now ends with a REQUIRED accounting slot —
  prune/archive candidates (or explicit "none found") + one-line net reference-tier delta,
  making the add:remove ratchet visible per run. Two proposed halves no-failed and shipped
  no text (description rewording; forced prune pass) — status-noted in the spec. Record:
  `docs/2026-07-26-right-sizing-red-green.md`.
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
