# Tasks — fix-skill-review-findings

Work on `dev` in `E:\Projects\AI\Skills`. Behavior-adding edits (groups 3–4) follow the Iron Law:
RED first; if a baseline does not fail, drop that guidance and record the outcome (design
Decision 6). Skill edit + design-doc sync land in the same commit.

## 1. Mechanical fixes (no pressure scenarios; one commit)

- [x] 1.1 Replace repo-relative footer links with absolute paths (`E:\Projects\AI\Skills\docs\...`) in all four SKILL.md files (setup, audit, maintain, whats-next; audit has two links)
- [x] 1.2 AUDIT: resolve the `graduate` contradiction — modality section's "two report-only exceptions" → "two non-stale statuses"; keep report-only = exactly `flag-code-bug` + `revisit-plan` (writes-docs-only section + step 5 unchanged)
- [x] 1.3 AUDIT: align step-4 adjudication wording with the schema's action vocabulary (per-flag call = approve / amend / defer the flag's proposed schema action; no free-floating verb list)
- [x] 1.4 SETUP: add VERIFICATION to the reference-tier bullet in "Tiers & routing"
- [x] 1.5 SETUP: remove the "prove the skill on a small project first" maturity note from Safety
- [x] 1.6 whats-next: clarify ranking risk term = exposure-if-deferred (raises rank); implementation riskiness alone does not
- [x] 1.7 whats-next: trim frontmatter description to triggers only (keep "what should I work on next?" / backlog phrases) + add "Assumes the docs-architecture conventions."
- [x] 1.8 Family-wide consistency re-read (cross-refs, vocabulary, wc -w per skill) and design-doc sync for group-1 items; commit

## 2. Fixtures for RED/GREEN

- [x] 2.1 Reset TP fixture (`git reset --hard 9034e6f && git clean -fd` in `E:\Projects\AI\TargetPlanner`), then plant: nested mini-project (own `git init` + own CLAUDE.md + one unconventionally-named doc)
- [x] 2.2 Plant cold-rationale material in TP: a dated rationale note containing one drifted code-coupled fact, cited from a reference doc; plus one lengthy+cold+evergreen section inside a reference doc
- [x] 2.3 Build synthetic design-heavy fixture in the session scratchpad (2–3 source files + one large standalone design doc, no other docs)
- [x] 2.4 Author the seeded disk-verify input: a merged flag list with one plausible-but-false flag (fabricated `file:line` evidence) against the TP fixture

## 3. RED baselines (current skill text injected; 2 reps per scenario; record behavior verbatim)

- [x] 3.1 RED sub-project: SETUP on the TP+nested fixture — does it scaffold into / augment the sub-project?
- [x] 3.2 RED design-heavy: SETUP on the synthetic fixture — does it force-split the design doc?
- [x] 3.3 RED cold-rationale: AUDIT on TP — is the cold doc skipped entirely ("not the journal") and the extraction candidate unflagged?
- [x] 3.4 RED disk-verify: orchestrator-role agent with the seeded false flag — is it rubber-stamped into adjudication?
- [x] 3.5 Gate check: for any scenario where the baseline did NOT fail, drop that guidance from scope and record the no-failure outcome in `docs-architecture-design.md`

## 4. GREEN — write minimal guidance per failing scenario, re-run, commit each

- [x] 4.1 SETUP: sub-project flag-and-skip (mirror AUDIT's scope wording) + scope the "coexist, never clobber" rule to root-project files; re-run 3.1 scenario → complies; commit with design-doc record
- [x] 4.2 SETUP: design-heavy `DESIGN.md`-slot rule (preserve whole; charter'd-thin ARCHITECTURE/ROADMAP alongside); re-run 3.2 → complies; commit with design-doc record
- [x] 4.3 AUDIT: cold-rationale tier scope (decision-consistency check; code-coupled-fact-in-cold-doc = misplacement flag) + `extract-cold` schema action; re-run 3.3 → complies, no cry-wolf on sound reasoning; commit with design-doc record
- [x] 4.4 AUDIT: disk-verify gate in merge/adjudicate steps (spot-check cited evidence; failed evidence corrected/dropped, never presented as verified); re-run 3.4 → catches the seeded flag; commit with design-doc record
- [x] 4.5 REFACTOR: close any new rationalizations from GREEN runs; enforce the word-count guard (AUDIT ≤ ~1250 words — trim step-1/step-3 bold stacking if over)

## 5. Finalize

- [x] 5.1 Reset TP fixture (mandatory reset contract); delete scratchpad fixture
- [x] 5.2 Full-family final re-read: schema/vocabulary/cross-skill consistency, footer links, frontmatter (verify whats-next description passes the SDO check)
- [x] 5.3 Update `docs-architecture-design.md`: stale "needs a failing test before encoding" gate notes (AUDIT already ships router-anchored scope + flag-and-skip) + this batch's RED/GREEN outcomes; include in the relevant commits
- [x] 5.4 Merge `dev` → `main`; run `./deploy.sh`
- [x] 5.5 Verify deployment: deployed copies byte-identical to repo; footer links resolve from `~/.claude/skills/<name>/`
