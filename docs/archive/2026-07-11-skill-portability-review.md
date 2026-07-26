# 2026-07-11 — Skill portability review: dependency inventory + consolidation questions

**What this is / when to read:** pre-change review of the four shipped skills (SETUP · AUDIT ·
MAINTAIN · whats-next) ahead of a portability/consolidation pass — verified purpose + mechanics
per skill, a classed inventory of every external-project / author-local dependency in the shipped
text, compression estimates at constant behavior, and the open questions to adjudicate before any
edit. Read before proposing that change. Review only — no skill or doc text was modified.

**Method.** Full read of `skills/*/SKILL.md` (×4), `README.md`, the root reference docs
(`CLAUDE` / `ARCHITECTURE` / `DOMAIN` / `VERIFICATION` / `ROADMAP` / `NOTEBOOK` / `RELEASING`),
`docs/docs-architecture-design.md`, and the three synced openspec specs. Token inventory
grep-verified against the four SKILL.md files; word counts by `wc -w`.

## 1. Verified: what each skill is, and how it works

**Key portability finding up front: the external-project dependency is textual, not mechanical.**
No step in any skill reads a test project, the design doc, or the benchmark note at runtime. The
skills are data-driven against the *target* project (its router, charters, code, journal). What
binds the text to the author's environment is (a) footer citations by absolute `E:\` path,
(b) Astronomy-constellation tokens used as inline exemplars, and (c) benchmark-derived numbers
whose provenance is repo-local. All three are rewritable without touching mechanics.

### docs-architecture-setup (970 words)
Bootstraps the convention the other three assume: one always-loaded `CLAUDE.md` **router** plus
the enforced, charter-guarded doc set (`ARCHITECTURE` / `ROADMAP` / `NOTEBOOK` / `VERIFICATION` /
`DOMAIN` / `docs/` journal; `README` / `RELEASING` conditional). Mechanics: survey → create/align
the set (charter-guarded, never blank; carry the set as a rule, never infer it from siblings) →
write the router (reference docs by name, journal by convention, exclusions noted) → don't force
content. Guard rails, each RED- or incident-derived: restructure-never-destroy (merge/move/archive,
never delete; clean git tree or a non-git recovery net first; diff before commit); hard
scope-exclusions (vendored / generated / tooling); sub-project flag-and-skip + run-from-its-own-dir
redirect; container root ⇒ router-only; design-heavy/code-light ⇒ DESIGN slot kept whole; legacy
domain doc ⇒ normalized into `DOMAIN.md`, never re-minted.

### docs-architecture-audit (1,382 words)
Verifies the reference tier on two axes — **placement** (section vs its doc's charter) and
**currency** (claim vs live code) — and exists because a single careful pass finds only ~half the
real issues, non-deterministically. Mechanics: fan out per-section workers + one cross-reference
pass (inbound refs / rename-orphans) → merge + dedup on a fixed flag schema → **loop-until-dry**,
then **switch worker model** (a dry round is that model's ceiling, not truth) → adjudicate each
flag (approve / amend / defer) → apply approved doc fixes + re-verify. Discipline rules:
conservative evidence (`file:line` or the literal `unverifiable → ask user`; never guess stale);
classify modality first (descriptive ⇒ code wins ⇒ `fix-doc` — except an asserted contract the
code violates ⇒ `flag-code-bug`, report-only; prescriptive ⇒ plan wins ⇒ `graduate` /
`revisit-plan`); AUDIT edits docs only, never code; router-anchored scope; dead workers retried
once, then named in a coverage note.

### docs-architecture-maintain (630 words)
The journal→reference promotion sweep. Classifies each journal item (graduate / keep / archive /
prune-only); the linchpin is that every `graduate` carries both a charter-chosen target and a
REQUIRED source-disposition (stub / cross-ref / archive) — blocking the two failure modes,
graduate-without-prune (duplication) and prune-by-deletion (lost why/when). Reuses AUDIT's fan-out
machinery by name (workers → schema'd flags → merge → loop-until-dry → adjudicate → apply).

### whats-next (684 words)
The planning layer. Sweeps a nine-row source checklist (git state, ROADMAP, gotchas, journal,
code TODO/FIXME ownership, change-tool state, audit findings, cross-repo blockers, tests) →
separates **live-actionable** from **accepted-constraint** (live marker required; default to
accepted) → buckets + ranks (value × 1/effort × exposure-if-deferred) → top-N with a recommended
sequence. Two REQUIRED outputs the RED baseline omitted: the **coverage manifest** (swept /
not-reached, per row) and the **accepted-constraints list**. Reuses AUDIT's fan-out.

### Family coupling (intentional — keep)
SETUP must run first (the other three assume the conventions); MAINTAIN and whats-next invoke
"the fan-out from docs-architecture-audit" by skill name; whats-next consumes AUDIT's
`flag-code-bug` output. Intra-family references are portable so long as the family ships together
(it does — one repo, one deploy).

## 2. Dependency inventory (grep-verified against the four SKILL.md files)

### Class A — author-local absolute paths (hard break for any other consumer)
| Where | Reference |
|---|---|
| all four footers | `E:\Projects\AI\Skills\docs\docs-architecture-design.md` |
| AUDIT footer, 2nd citation | `E:\Projects\AI\Skills\docs\2026-06-29-audit-model-benchmark.md` |

Deliberate at the time (2026-07-06 fix batch: repo-relative `../../docs/…` links dangled from
deployed copies in `~/.claude/skills/`), and asserted in repo governance — root `CLAUDE.md`:
"referenced … by absolute name — move or split neither." For anyone without `E:\Projects\AI\Skills`
these are dangling, Windows-shaped paths. Runtime impact of removal: none — pure provenance
pointers; no procedure step reads them.

### Class B — constellation tokens as inline exemplars (soft break: noise or misdirection outside the Astronomy constellation)
| Token | Skill(s) | Teaches (the class is the rule) | Generic candidate |
|---|---|---|---|
| `PCL/`, `nsg-v8-fork/`, `*/3rdparty/` | SETUP, AUDIT | vendored / forked third-party trees | `vendor/`, `third_party/`, a forked upstream tree |
| `bin`/`obj`, `BenchmarkDotNet.Artifacts` | SETUP, AUDIT | generated / build output | `bin/`, `obj/`, `dist/`, `target/`, benchmark artifacts |
| `.superpowers/` | SETUP | tooling dirs | drop or swap for a second generic tooling example |
| `dotnet test` (×2) | SETUP | honest thin-verification charter | "the project's test command (`dotnet test`, `npm test`, …)" |
| `OBSERVING.md` | SETUP | legacy content-specific domain-doc name | "a legacy content-specific name" |
| `nsg-v8-fork/NOTICE.md` | AUDIT | a router-named leaf *inside* an excluded vendored tree is still in scope | "a router-named playbook leaf inside a vendored tree" |
| `.xaml`/`.cs` | AUDIT | code/UI files as inbound doc referrers | "source and UI files" |
| OpenSpec `changes/` row | whats-next | change-tool state as a backlog source | "planning/change-tool state (e.g. `openspec/changes/`, issue tracker)" |

Every token is a category exemplar; none is load-bearing as a literal — the rules key on the
class. Nuance: the openspec specs' scenarios cite the specific names (`OBSERVING.md` etc.); specs
are repo-internal, so they can stay, but the rewritten class descriptions must remain crisp enough
that the same scenario behavior still follows from the text.

### Class C — benchmark-derived numbers woven into rule text (portable as claims; provenance repo-local)
AUDIT: "~half the real issues" (per-pass recall) · "three replicate passes still missed real
flags / ground truth ~30% larger" · "two models' ~20-of-25 unions shared only ~16" · "medium's
cumulative ceiling runs ~3 real issues below high" · Sonnet-at-high default, Haiku/medium
first-sweep-only. whats-next overview: the clean-fixture RED finding (unguided runs omit the
manifest + accepted-constraints list). These are calibration, not decoration — they justify the
fan-out, loop-until-dry, model-diversity, and effort rules *to the executing agent*. The numbers
are facts about a benchmark, not about a project, so they survive genericizing intact; the open
question is precision (keep / round to qualitative) and where provenance points (Q1/Q2).

### Class D — harness/vendor assumptions (documented degradations, not defects)
Claude worker-model tiers + effort levels; parallel-subagent orchestration for the fan-out;
`CLAUDE.md` as the auto-loaded router filename; `~/.claude/skills/` as the deploy target (deploy.sh
and repo docs, not skill text). README's "Beyond Claude Code" already names the first three and
their graceful degradations. Decision needed only on how vendor-explicit the *skill text* stays (Q3).

### Class E — repo-side text that must move in the same change (else the next self-audit flags the contradiction)
- `README.md` "Repo layout": "cited in skill footers by the author's local path; in this repo they
  live under `docs/`."
- Root `CLAUDE.md` gotcha: "Deployed skills reference this file … by absolute name — move or split
  neither."
- Note: the README itself names no test project — its external-project dependency is transitive
  (links into `docs/`, whose design/benchmark records are constellation-heavy) plus the
  footer-path acknowledgment above. The design doc and benchmark note themselves stay as-is:
  journal tier, dated historical record, never retconned.

## 3. The functional floor any rewrite must hold
- Every behavioral rule in the four texts traces to a RED failure, a field incident, or a recorded
  user directive (design doc, Phase-3 records onward). "Maintain functionality" ⇒ zero rule drops;
  compression targets wording and provenance asides, not rules.
- The openspec specs are the testable contract. Three requirements carry **no-failure-gate status
  notes** (disk-verify gate, fan-out right-sizing, legacy-domain rename, audit-first scoping) that
  deliberately keep text *out* of the skills — the rewrite must not accidentally add it back.
- Frontmatter descriptions stay SDO-scoped (trigger conditions + the assumes-conventions clause; no
  process summary) — the round-1 rule, applied family-wide.
- Fixed vocabulary that rewording must not blur: report-only = exactly {`flag-code-bug`,
  `revisit-plan`}; `disposition` REQUIRED on every `graduate`; the literal `unverifiable → ask
  user`; whats-next's two REQUIRED outputs; the flag schemas themselves (they are what makes
  fan-outs mergeable).

## 4. Compression map (constant behavior)
Where the words are: (a) provenance asides — "in testing…", benchmark parentheticals, RED/GREEN
references — the largest safe cut; (b) Common-mistakes sections that restate rules ~1:1 (AUDIT's
nine bullets are all restatements — compressible to a line each or folded into their rules);
(c) micro-examples duplicated between a rule and its mistake bullet; (d) the Class-A footers.
Rough floors at zero behavioral change:

| Skill | Now (words) | Est. floor | Main savings |
|---|---|---|---|
| AUDIT | 1,382 | ~900–1,000 | provenance asides, mistakes dedup, footer |
| SETUP | 970 | ~700–750 | exemplar tightening, mistakes dedup |
| MAINTAIN | 630 | ~500–550 | already lean; phrasing only |
| whats-next | 684 | ~550–600 | overview RED framing, mistakes dedup |

≈30% family-wide. Materially smaller than that means dropping tested rules or the Class-C
calibrations — possible, but each cut should be adjudicated per-flag, not assumed under
"consolidation."

## 5. Open questions (Q1–Q4 asked interactively in-session; Q5–Q8 proposed defaults, veto-able)
- **Q1 — footers:** remove entirely · swap to GitHub blob URLs · repo-relative (repo-relative
  re-opens the exact 2026-07-06 dangling-link bug on deployed copies).
- **Q2 — benchmark numbers:** keep verbatim, uncited · qualitative only · keep + GitHub citation.
- **Q3 — worker-model guidance:** Claude tiers as-is · dual-form (generic rule, Claude example) ·
  fully generic.
- **Q4 — re-validation:** diff review only · GREEN spot-checks per `VERIFICATION.md` on a
  non-derived synthetic fixture · full RED→GREEN.
- **Q5 — scope (default: yes):** one change covering the four SKILL.md + the two Class-E lines
  (README, root CLAUDE.md gotcha), so the repo stays self-consistent.
- **Q6 — "consolidation" reading (default: compress-in-place):** four skills stay four; merging
  would blur the SDO trigger descriptions and the per-lifecycle-moment invocation. The by-name
  fan-out reuse is already the DRY seam; no shared-machinery extraction proposed.
- **Q7 — compression appetite (default: constant behavior):** §4 floors; rule-dropping only as
  explicitly adjudicated cuts.
- **Q8 — whats-next OpenSpec row (default: genericize):** "planning/change-tool state," keeping
  `openspec/changes/` as one example among others.

## 6. Process recommendation (when the edit is approved)
Run as one openspec change (house workflow): proposal → apply across the four skills + Class-E
lines → re-validation per Q4 → `dev` → `main` → `deploy.sh`. No spec requirement changes expected
(behavior constant); the change record becomes the provenance for the portability pass itself —
and the retired footer targets remain reachable through the repo/README for anyone who wants the
full rationale.

## 7. Decisions — adjudicated in-session, 2026-07-11
- **Q1 footers** → GitHub blob URLs (`github.com/Apoplectic1/YetAnotherSkillsRepo`).
- **Q2 benchmark numbers** → keep verbatim, uncited (calibration claims stay; local citations go).
- **Q3 model guidance** → dual-form: generic rule (strong fast tier at high effort default; cheap
  tier first-sweep only; diversify once dry) with Claude tiers as the parenthetical example.
- **Q4 re-validation** → **full RED→GREEN**, under the house method rules (non-derived synthetic
  fixture, candidate-text injection, disk-verified claims).
- **Scope** → **portability + constant-behavior compression** (§4 floors; zero rule drops).
  Size finding that recalibrated the goal: portability alone is word-neutral (~70 footer words
  family-wide; token swaps net zero) — the length lives in the tested rules, so "much smaller"
  was retargeted to the ≈30% constant-behavior floor; the aggressive-cut option was declined.
- **Q5** repo-side lines (README "author's local path" note + root `CLAUDE.md` "by absolute
  name" gotcha) confirmed in-scope of the same change. **Q6** compress-in-place, four skills stay
  four. **Q7** constant behavior. **Q8** whats-next's OpenSpec row genericized — defaults accepted.
- **Next step agreed:** draft the AUDIT rewrite first as the calibration before/after, review,
  then the remaining three; execute as one openspec change with RED→GREEN before merge/deploy.
