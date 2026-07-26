# NOTEBOOK.md — lab notebook

**Charter:** chronological empirical findings from working on the skills — small
observations that don't warrant a standalone dated note. Newest at the top. Substantial
records go to `docs/YYYY-MM-DD-<slug>.md` (existing example: the 2026-06-29 audit
worker-model benchmark).

- 2026-07-26 — **Field signal #2 for B4 (same TSM maintain run): cross-project glossary
  loop.** The sweep surfaced a cross-ref cycle around glossary content shared across the
  Astronomy constellation — the per-repo convention gives portfolio-level truth no owner, so
  each repo's locally-correct "single-source it there, point up" produces A→B and B→A with
  nobody holding the content. Interim discipline (pre-B4): ownership follows the code that
  defines the term (shared concepts → Library; scheduler terms → TSM); pointers one-way
  only; MAINTAIN must flag-and-ask on cross-project ownership, never improvise cross-repo
  pointers (rule candidate, gated). Bumps the B4 portfolio probe — now hit in the wild
  twice. Specific loop details pending from the TSM session.
- 2026-07-26 — **Field RED (TSM maintain run): M9 stuff-then-ask.** The rep graduated into
  a 37.6→38.6 KB ARCHITECTURE.md three times in one sweep, *then* asked "split it?" — knew
  the rule (quoted "split before you stuff" in its own closing) and inverted M9's required
  order under finish-the-graduate pressure. Failure class: knows-rule-skips-under-pressure →
  fix form is prohibition + rationalization red-flags (DOMAIN table), unlike this week's
  REQUIRED-slot fixes. Target behavior sketch: bloated target → HOLD its graduations
  (record in the M13 report + a ROADMAP line naming the pending split job), split is a
  separately-adjudicated job, promotions land in the split homes. Gate: RED→GREEN on a
  fat-reference-doc fixture variant (fat-router family precedent; new plant class).
- 2026-07-26 — **Field finding (same TSM run): a "dry" round from an overloaded worker is
  not evidence.** Worker holding 16 records skimmed (found 2); re-partitioning the same set
  four ways found 2 more; the dedicated dry-check emptied at round 3 while a critic worker
  kept finding. Hole in loop-until-dry semantics (M10/R20): dryness only means exhaustion if
  partition size stays small enough to force depth — candidate: partition-size cap or
  re-partition-before-dry clause. Natural batch-mate for the AUDIT scaled-coverage backlog
  item (both touch round/coverage mechanics). Ungated; needs synthetic RED.
  `derivability-discriminator`.** User question ("are we documenting what's better derived
  from code?") exposed the gap: on stale derivable trivia (counts, versions, column lists —
  rationale-free, one grep from truth), AUDIT's reps consistently propose `fix-doc`
  re-caching the grep (observed: every TidePool rep corrected 12→18 rather than questioning
  the count's presence), when the durable fix is often deleting/de-valuing the claim — a
  drift-prone cache re-primed is drift deferred, not cured. Discriminator sketch: claim is
  cheaply derivable AND carries no rationale/contract/gotcha → propose removal or reword
  without the perishable value; otherwise fix normally. Iron-law gated; fixture note: D4's
  catalog expectation (fix-doc on the station count) will need a GREEN-text variant
  (deletion/reword acceptable) without weakening its live-section-control role.
  fail-closed→fail-soft contract violations (doc guarantees "hard 0"/abort, code ships a
  ramp/fallback) deserve top severity — graceful degradation converts a loud, fixable
  violation into plausible wrong answers (rhymes with the user's global fail-fast rule).
  Companion insight: a test suite often inherits the code's misconception (TidePool tests
  check the low instant because the code does; TSM's SyncMarksTests keyed by Id because
  TsInboundDiff did) — green tests measure code-fixture agreement, not contract conformance,
  which is the argument for docs-vs-code audit as a separate pass. No RED evidence yet that
  reps *misrank* these; iron-law gate before any severity-rule text ships. TidePool's
  daylight two-defect decomposition (catalog annotation, same date) is the worked example.
- 2026-07-26 — **Field finding → shipped same day: code-bug flags had no persistence path
  (MAINTAIN-on-TSM).** Full decision + RED/GREEN record:
  `docs/2026-07-26-code-bug-persistence-red-green.md` (+ design-doc provenance entry);
  shipped as AUDIT R27 + MAINTAIN M12/M13. Unique note: the TSM run's own findings were
  saved manually in that session — this repo's fix is forward-looking only.
- 2026-07-26 — **superpowers plugin retired; writing-skills conventions vendored** → single
  source: DOMAIN.md § Authoring conventions (v6.2.0 frozen digest). Unique notes: deployed
  skills never referenced superpowers → zero runtime impact; historical superpowers mentions
  in dated docs / opsx archive left as record.
- 2026-07-26 — **Openspec-archive RED failure mode: non-determinism, not absence** → full
  provenance: design doc § Openspec-archive awareness (M11 pins scope + disposition
  vocabulary). Unique note: TidePool fixture now carries `openspec/changes/archive/` plants
  (catalog O1–O4) — reusable for future archive-related rules, but any rule *derived from*
  these plants poisons them (non-derived rule stands).
- 2026-07-20 — **Repo relocated to `E:\Projects\AI\Skills\doc-architecture`** (was
  `E:\Projects\AI\Skills` root). deploy.sh needed no change (self-locates via `dirname "$0"`);
  skill footers unaffected (GitHub URL, remote unchanged). Updated the live absolute paths:
  design-doc header + the two `docs/audit-benchmark/score*.py` `DOCS` constants. Old paths in
  dated docs / openspec archive left as historical record.
- 2026-07-17 — **TestProjects/ hidden via `.git/info/exclude`** (local-only, untracked file —
  nothing reaches the mirror): still on disk, still per the 2026-07-13 keep-until-B4-probe
  decision; it just no longer shows in `git status`.
- 2026-07-17 — **fat-router-lean GREEN 4/4 — S7 + R26 ship.** Candidate text (SETUP S7 lean
  rule with explicit B2 carve-out; AUDIT R26 router-placement clause): SETUP GREEN 2/2 on the
  real TP router — 24 KB → 3.5/4.3 KB, every off-charter block to its charter home
  (glossary/conventions→DOMAIN, mechanics/contracts→ARCHITECTURE, build/run→VERIFICATION),
  hybrid gotchas split one-liner-stays+pointer, disk-verified content-preserving (verbatim
  phrase checks incl. the perf-budget sentence); lean-router control 1/1 no-trigger (no
  cry-wolf); AUDIT GREEN 1/1 — one structural `move-to` flag per block citing R26, currency
  flags inside blocks correctly preserved (two-axis), routing/gotchas untouched. GREEN ran
  where RED reproduced (TP), not the small fixture that passed under current text — plan
  amended mid-run. **R26 number now taken** by the router-placement clause: the 2026-07-17
  scaled-coverage backlog item's informal "field R26" alias needs a new number when it ships
  (its ROADMAP entry updated). Ground truth: `harness/catalog-fat-router.md`.
  0/3 on the small synthetic.** Small tidepool fat-router variant (3 planted blocks, ~3.5 KB
  router): SETUP 0/2 — both reps leaned perfectly unprompted (F1→DOMAIN, contracts→ARCH,
  hybrid split correct); AUDIT 0/1 — router placement-flagged under existing R10+R12. Real
  24 KB TP router (`TestProjects/` copies): SETUP 2/2 reproduced — both did the A2 history
  move + scaffolding but left glossary/conventions/contract in the router and **grew** it
  (24.3→26.1 KB and 24.3→25.9 KB; the ecological 24→26 KB replay). Mechanism captured by rep
  2 verbatim: it *saw* the fat, then read **B2 "coexist, never clobber" as forbidding the
  trim** — a rule collision, not inattention; S7 wording must explicitly carve moves out of
  B2. Also: probe currency-flagged stale claims *inside* a misplaced router block — correct
  per the two-axis frame; R26 must suppress only per-fact *placement* flags, not currency
  (unlike R25, router fat is reference-tier, not journal-tier). Fixture evidence in
  scratchpad reps; ground truth `harness/catalog-fat-router.md`.
  gated.** Added mid-session from another (small) project straight into the skill text — repo
  copy *and* live deployed copy, bypassing dev→main→deploy.sh — reviewed and reverted same day
  (live copy restored to main's state). Concept accepted, wording deferred. Target shape from
  review: predicate = **small doc set AND low expected drift** (not source-file count); mode =
  one per-section round + the R19 cross-reference pass, **pinned to the R22 default tier**
  (else R22's "first sweep only" cheap-tier allowance legally covers the whole audit), no loop
  / no model switch; coverage note announces the mode + what a full run would add; full loop
  stays default for large/drift-prone sets and on request. Companion edits found mandatory:
  Procedure step 3 gains the branch (else the unconditional loop-until-dry checklist wins),
  R18 gains a sanctioned-exception clause (its "never any fixed N" contradicts the rule),
  italic rationale marks it a **user-set cost tradeoff, not an empirical ceiling**, provenance
  date goes to the design doc (whose coverage section still mandates the unconditional loop —
  needs a dated addendum), and the "~12–15 workers" instance-overfit count drops (count falls
  out of section count). Gate: GREEN-only — preference rule, no failure to reproduce (cf.
  2026-07-07 "AUDIT right-sizing" passed RED no-failure): TidePool scaled-branch reps + one
  not-small control that must NOT trigger, + a catalog entry. Est. ~150–200k subagent tokens;
  natural batch-mate for the fat-router-lean AUDIT clause (same fixture family, one deploy).
  Open sub-question: audit-only or family-wide (MAINTAIN / whats-next also mandate
  loop-until-dry)?
- 2026-07-13 — **TestProjects/ stays untracked — decided, don't re-propose.** Nested `.git`
  means a plain add records only a contentless gitlink stub, and committing real content
  would publish the user's TargetPlanner source through the public mirror on the next
  `main` push. Backup, if ever wanted, = push the fixture's own nested repo to a private
  remote. Keep until fat-router-lean + the B4 portfolio probe ship (it holds the real 24 KB
  router those need); recreatable-with-effort from real TP history after that.
- 2026-07-13 — **fat-router-lean backlog item refined** (disposition of the user's held
  q1.txt question, now deleted; source: ecological field finding 1 — both skill generations
  left a 24 KB router's glossary/contract weight in place, and the audit didn't placement-flag
  it). Two linked pieces, both gated on RED→GREEN: **(a) lean rule** — SETUP relocates
  off-charter router weight to charter-selected reference docs on encounter (glossary →
  DOMAIN.md; abbreviations-for-CLI-use are an authoring convention, squarely DOMAIN charter),
  plus one AUDIT clarifying clause making the router itself explicitly placement-audited.
  Leaning: content test ("reference content vs routing/gotchas") over a numeric size
  threshold, with the ~40 KB perf line as the *why*. Est. ~450–500k subagent tokens
  (SETUP 2+2 reps + narrow AUDIT probe; `harness/tidepool-fixture` + fat-router variant —
  not poisoned: rule derives from the TP ecological run, not TidePool). **(b) B4 amendment**
  — portfolio-shared DOMAIN.md at a container root (user's Astronomy-portfolio glossary
  idea): collides with shipped B4 ("router only; portfolio-level set is noise"), so it's a
  rule change with a single-sourcing design question (per-project DOMAIN.md cross-refs up?).
  Cheap probe first: run SETUP at `E:\Projects\VisualStudio\Astronomy` and observe (expected:
  router-only per B4; old non-portfolio projects get B3 flag-and-skip lines — not a blocker).
- 2026-07-10 — **openspec archive prompts interactively** (third CLI gotcha, joins the
  2026-07-07 pair): `archive` asks "Proceed with spec updates?" and dies in a
  non-interactive shell ("User force closed the prompt", exit 1 — *after* printing
  "Task status: ✓ Complete"). Run `openspec archive <name> --yes`; keep judging by output
  text, never exit code.
- 2026-07-10 — **AUDIT worker-death hardening** → full provenance (field workflow ID, dead
  span, JSON-parsing-vs-schema-API mechanism, GREEN 2/2 detail): design doc § AUDIT
  worker-death hardening — 2026-07-10. Shipped: step 1 retry-once, step 3 coverage note, one
  mistakes bullet.
- 2026-07-10 — **first self-audit** (AUDIT on this repo: 4 rounds, 16 workers,
  Sonnet→Opus→Fable; 36 findings, zero code-contract violations). Lessons: (a)
  **running-commentary tense is the dominant staleness class** (17 of 18 design-doc flags) —
  "awaits / in-flight / queued" rots within days; write past-tense immediately or stamp a
  date. Systemic cure: the SETUP-spec survey is now an explicit dated derivation snapshot.
  (b) **Model diversity beat same-model reps**, exactly as the 2026-06-29 benchmark
  predicted — 17/9/10 new finds per tier, each catching what the prior tier's dry rounds
  missed. (c) **Mid-audit edits ripple** — adding VERIFICATION's third method rule made
  README's "two lessons" stale within the hour (caught by the loop, round 3). (d) `deploy.sh`
  was add/refresh-only — a renamed skill would have left a stale live copy; now
  marker-stamps + prunes.
- 2026-07-07 — **openspec CLI gotchas** (hit during the round-2 archive): (a) the spec
  validator requires SHALL/MUST on a requirement's **lead line** — put the normative verb in
  the first sentence, not after a "When…" clause; a requirement only gets validated when its
  file is *updated*, so offenders can hide in specs created by an earlier change. (b)
  `openspec archive` **exits 0 on validation abort** — check the output text, never the exit
  code, and don't chain it with `&&`.
