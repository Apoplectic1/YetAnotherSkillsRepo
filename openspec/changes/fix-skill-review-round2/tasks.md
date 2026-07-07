# Tasks — fix-skill-review-round2

Iron Law throughout: RED first with **current** skill text (candidate-text injection, Sonnet
workers, 2 reps, disk-verify claims); encode only what fails; GREEN with the candidate text;
no-failure → no text, add a disk-verify-style status note to the delta spec instead. Reset
fixtures per `VERIFICATION.md` after every mutating run.

## 1. Fixtures (synthetic — see design.md D1/D3)

- [x] 1.1 Build the legacy-domain fixture: git repo, router + ARCHITECTURE/ROADMAP + populated
  `OBSERVING.md`, no DOMAIN.md; `SKILLS-TEST BASELINE` marker commit *(baseline commit; per-rep
  fresh copies replace the reset contract — equivalent for synthetic fixtures)*
- [x] 1.2 Build the non-git fixture: same shape, no `.git`, docs messy enough to force a
  restructure apply *(fat CLAUDE.md + `Design Notes.md` (space) + journal-ish notes.md)*
- [x] 1.3 Build the container-root fixture: two sub-projects (own `.git` + router each) +
  `.claude/`, no first-party content (GREEN-only — live RED banked 2026-07-07)
- [x] 1.4 Build the fresh-docs backlog fixture: freshly-SETUP project, current docs, visible
  backlog sources (TODOs, ROADMAP Next, open journal items)
- [x] 1.5 Build the small-set fixture: 5–6 thin charter'd docs, ~10-file code base, 2 planted
  drifts *(ARCHITECTURE names `AltCalc.Compute`, code has `Evaluate`; router gotcha cites
  missing `docs/setup-notes.md`)*

## 2. Item 1 — SETUP legacy-named domain doc

- [x] 2.1 RED ×2 on fixture 1.1 with current SETUP text; verdict per design D3 (duplicate home
  / no normalization = fail); disk-verify end state *(RED 2/2 PASS — both reps `git mv`
  OBSERVING.md → DOMAIN.md, content preserved, router updated, zero duplicate homes;
  disk-verified. No-failure gate → no text change)*
- [ ] 2.2 If failed: encode the rename/merge sentence in SETUP step 2; align the design doc's
  "Domain-doc name fixed" paragraph; GREEN ×2; record in design doc
- [x] 2.3 If passed: status-note the delta spec (no-failure gate); record the pass *(done —
  status note added to the setup delta spec)*

## 3. Item 2 — SETUP non-git recovery net

- [x] 3.1 RED ×2 on fixture 1.2; verdict: restructure with no net offered = fail (mention-only
  counts as fail per design open-question lean) *(RED 2/2 FAIL — both reps merged-then-DELETED
  `Design Notes.md`/`notes.md`/fat router with no git init and no snapshot; rep 1 rationalized
  "out of scope", rep 2 noticed the missing net, "compensated" with self-review, deleted anyway
  — disk-verified originals gone. Rep 2 partially confounded by harness wording ("leave tree
  uncommitted" read as no-git-ops); rep 1 clean → failure stands, encode)*
- [x] 3.2 If failed: encode the non-git branch in SETUP Safety; GREEN ×2; record *(encoded
  "Not a git repo? Create the net first" + pure-scaffold exception; GREEN 2/2 disk-verified —
  both reps `git init` + committed the originals verbatim BEFORE restructuring (baselines
  4951de5 / e5be05c hold all original files); 3.3 n/a)*
- [ ] 3.3 If passed: status-note + record

## 4. Item 3 — SETUP container root (live RED banked)

- [x] 4.1 Encode router-only-at-container guidance in SETUP; GREEN ×2 on fixture 1.3
  (router-only + redirects, no full set); record with the live-RED citation *(encoded in
  Coexist section; GREEN 2/2 disk-verified — router-only at root, both sub-projects untouched
  (clean git trees), redirects delivered, .claude/ excluded; both reps also correctly invoked
  the new pure-scaffold non-git exception — the two new rules compose)*

## 5. Item 4 — whats-next scoped audit-first

- [x] 5.1 RED ×2 on fixture 1.4; verdict per design D3 observable (blocks on / performs an
  audit despite fresh docs = fail) *(RED 2/2 PASS — both reps proceeded straight to backlog +
  manifest, no audit demanded or performed; absence of audit output handled as an honest
  manifest row; both caught the fixture's accidental ROADMAP↔NOTEBOOK cross-ref mismatch as
  doc-debt. No-failure gate → no text change)*
- [ ] 5.2 If failed: reword When-to-use + Common-mistakes bullet; GREEN ×2; record
- [x] 5.3 If passed: status-note + record *(done — status note added to the whats-next delta
  spec; 5.2 n/a)*

## 6. Item 5 — AUDIT small-set right-sizing

- [x] 6.1 Resolve design open question (disproportion test) before running; RED ×2 on
  fixture 1.5 *(question resolved in design.md pre-run: judge the stated plan. RED 2/2 PASS —
  both reps planned 6 workers for 5 thin docs with explicit volume reasoning ("per-section
  collapses to per-doc"), conditional round 3, loop-until-dry intact; both caught the two
  planted drifts + two accidental ones, zero cry-wolf, one textbook flag-code-bug. No-failure
  gate → no text change)*
- [ ] 6.2 If failed: encode the one-sentence scale rule in AUDIT step 1 (compress per the
  word-count REFACTOR precedent); GREEN ×2; record
- [x] 6.3 If passed: status-note + record (expected — loop-until-dry self-terminates) *(done —
  status note added to the audit delta spec; 6.2 n/a)*

## 7. Close out

- [x] 7.1 Append the consolidated RED/GREEN record to `docs/docs-architecture-design.md`
  (per-item verdicts, what shipped vs no-failure) *(done — "Round-2 behavioral batch" entry)*
- [x] 7.2 Word-count check on SETUP/AUDIT/whats-next; compress if additions landed *(SETUP
  927→970 words, only skill changed — within precedent, no compression)*
- [x] 7.3 Commit on dev; merge → main; `deploy.sh` (SKILL.md changes only take effect after
  deploy); sync delta specs to main specs; archive the change *(order adjusted: archive first
  so the whole batch lands as one commit → merge → deploy; `openspec archive` performs the
  main-spec sync)*
