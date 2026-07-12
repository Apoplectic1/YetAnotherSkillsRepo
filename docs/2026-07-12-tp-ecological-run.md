# 2026-07-12 — TargetPlanner ecological run: hybrid SETUP + AUDIT vs the old skill set's real output

**What this is / when to read:** record of the ecological check — the hybrid candidates run
end-to-end on a container copy of the restored pre-skills TargetPlanner backup (baseline
`9034e6f`), compared against the real TargetPlanner's docs (old-skill SETUP + adjudicated
old-skill AUDIT, applied 2026-07-07, untouched since). Read alongside the two arm results docs;
this is the final validation evidence before the apply. The full AUDIT adjudication list is
appended — the user adjudicates it (or treats it as evidence only; nothing has been applied).

## SETUP stage — convergent, with two hybrid-side improvements
On the messy backup (24 KB router, 125 KB ROADMAP, no NOTEBOOK/VERIFICATION/DOMAIN), the hybrid
SETUP made 6 small commits (196+/11−, 1 rename), and its moves converged with the old skill's
real-world output almost one for one: created exactly the three missing files, all charter'd;
added a Docs-map router section (by-name / by-convention / exclusions); left `docs/design/`,
`archive/`, `reference-material/` intact; and independently performed the *identical* journal
normalization (`docs/code-quality-audit.md` → `docs/2026-05-19-code-quality-audit.md`) the old
run made on the real tree. Hybrid-only improvements: it repaired CLAUDE.md's stranded
"Build / run" section (empty heading, content under the wrong header) by relocating build/test
guidance verbatim into VERIFICATION.md, and synced README's doc index. Neither generation
leaned the fat router (see field findings).

## AUDIT stage — 34 workers, ~130–140 unique flags, discipline held
Zero dead workers; schema + evidence on every flag; sibling-Library claims correctly marked
`unverifiable → ask user` (the copy stands alone); journal/R15 scoping correct; code findings
report-only. One process deviation, disclosed by the orchestrator itself: it **skipped the R21
model-diversification round**, arguing cross-worker convergence = dry (see field finding 2).

## The comparison — hybrid audit (on the untouched snapshot) vs old audit (applied to the real tree)
Grep-verified against the real TargetPlanner's staged docs:

**Independently rediscovered — the old audit had caught and fixed these (convergence):**
ChartEvaluation 1-field→3-field (real CLAUDE.md carries the corrected text) · dead
Begin/FinishChartBuildProgress purged from ARCHITECTURE · CheckboxTintPresenter/presenter split
present · moon-sweep cadence corrected to per-minute · MoonSample→MoonSweepSample rename ·
filter-defaults two-bucket claim gone · AnyCPU configs removed · Velopack 0.0.1589 · dangling
screenshot reference removed.

**Still stale in the real tree today — the hybrid audit found these; the old audit missed or
deferred them:**
- README's sort-options claim ("name, RA, declination, or transit time" — actual: Name /
  Transit / Rise / Longest / Highest), present twice in the real README.
- The installer-name contradiction (README `TargetPlanner-win-Setup.exe` vs RELEASING.md
  `Setup.exe`) — flagged `unverifiable → ask user`, correctly.
- ROADMAP's "Last updated 2026-05-28" banner vs its own 2026-06-11 entries.
- (Worth a look) README's two remaining "M31" mentions.

**Verdict:** on the same project, the hybrid audit reproduced the old audit's fix set and
surfaced real defects that persist in the production docs — the per-model/per-run ceiling story
in action (different runs find different subsets; the union needed both). No evidence of
regression anywhere in the ecological run; evidence of strictly-added value at three points.

## Disclosures
- Sub-agents can see this session's connected-folder project instructions, which include the
  *real* TargetPlanner's current (post-audit, corrected) CLAUDE.md. Workers explicitly treated
  it as non-authoritative and verified against disk; all flags carry code evidence. Note the
  three hybrid-only finds above are NOT present in that leaked router — they are clean.
- The backup's git history is a synthetic single baseline, so ROADMAP's ~20 commit-hash
  citations were treated as systemically unverifiable rather than per-entry defects (correct).

## Field findings → candidate skill adjustments (each needs RED→GREEN before any text ships)
1. **Fat-router lean is a shared gap, not a regression.** Both skill generations scaffold and
   route but leave an existing oversized CLAUDE.md fat (old: 24→26 KB; hybrid: net-flat). The
   enforced-set table says "kept thin"; no rule compels moving glossary/contract prose down on
   encounter. Decide whether SETUP should perform (or at least propose) an always-on lean; if
   yes → new S-rule via synthetic RED→GREEN.
2. **R21 skip-rationalization.** The ecological orchestrator concluded "dry" from *same-model*
   cross-worker convergence and skipped the model switch — precisely the plateau the 2026-06-29
   benchmark refutes (a dry Sonnet round still missed ~4-of-25 that Opus caught). Candidate
   hardening: R21's why-clause gains "same-model convergence is agreement, not completeness."
   Single occurrence; per the no-failure gate, record now, encode after a RED reproduces it.
3. **Dated shipped-history inside ROADMAP.** TP's ROADMAP embeds a huge dated changelog; the
   audit currency-flags symbol drift inside those historical entries (the old audit largely left
   them). The tier model's real answer is A2 (git-is-changelog + short digest — a SETUP/MAINTAIN
   split job), not per-entry currency fixes. Candidate guidance question: should AUDIT treat
   dated ROADMAP history entries as journal-tier (R14) once flagged for digest-extraction?
   User's call before any rule change.
4. **(From arm 2, restated)** Nested orchestrators must collect worker results with a
   self-contained mechanism — notification-waiting stalls. Mitigated in the ecological run via
   prompt guidance; candidate one-line hardening for AUDIT step 1 if it recurs.

## Status
- SETUP applied on the fixture copy (6 commits, reviewable). AUDIT flag list below — nothing
  applied, per the skill: user approves / amends / defers.
- whats-next / MAINTAIN ecological stages: optional — both are synthetically GREEN 2/2 and the
  comparison goal (old-vs-new equivalence) is answered at the flag level above.

---

# Appendix — the AUDIT adjudication report (verbatim agent deliverable)

The complete adjudication-ready report from the ecological AUDIT run follows in the companion
file `2026-07-12-tp-audit-adjudication.md` (top-40 schema'd flags + ~90–100 remainder by theme +
coverage note).
