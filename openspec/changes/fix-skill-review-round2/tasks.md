# Tasks — fix-skill-review-round2

Iron Law throughout: RED first with **current** skill text (candidate-text injection, Sonnet
workers, 2 reps, disk-verify claims); encode only what fails; GREEN with the candidate text;
no-failure → no text, add a disk-verify-style status note to the delta spec instead. Reset
fixtures per `VERIFICATION.md` after every mutating run.

## 1. Fixtures (synthetic — see design.md D1/D3)

- [ ] 1.1 Build the legacy-domain fixture: git repo, router + ARCHITECTURE/ROADMAP + populated
  `OBSERVING.md`, no DOMAIN.md; `SKILLS-TEST BASELINE` marker commit
- [ ] 1.2 Build the non-git fixture: same shape, no `.git`, docs messy enough to force a
  restructure apply
- [ ] 1.3 Build the container-root fixture: two sub-projects (own `.git` + router each) +
  `.claude/`, no first-party content (GREEN-only — live RED banked 2026-07-07)
- [ ] 1.4 Build the fresh-docs backlog fixture: freshly-SETUP project, current docs, visible
  backlog sources (TODOs, ROADMAP Next, open journal items)
- [ ] 1.5 Build the small-set fixture: 5–6 thin charter'd docs, ~10-file code base, 2 planted
  drifts

## 2. Item 1 — SETUP legacy-named domain doc

- [ ] 2.1 RED ×2 on fixture 1.1 with current SETUP text; verdict per design D3 (duplicate home
  / no normalization = fail); disk-verify end state
- [ ] 2.2 If failed: encode the rename/merge sentence in SETUP step 2; align the design doc's
  "Domain-doc name fixed" paragraph; GREEN ×2; record in design doc
- [ ] 2.3 If passed: status-note the delta spec (no-failure gate); record the pass

## 3. Item 2 — SETUP non-git recovery net

- [ ] 3.1 RED ×2 on fixture 1.2; verdict: restructure with no net offered = fail (mention-only
  counts as fail per design open-question lean)
- [ ] 3.2 If failed: encode the non-git branch in SETUP Safety; GREEN ×2; record
- [ ] 3.3 If passed: status-note + record

## 4. Item 3 — SETUP container root (live RED banked)

- [ ] 4.1 Encode router-only-at-container guidance in SETUP; GREEN ×2 on fixture 1.3
  (router-only + redirects, no full set); record with the live-RED citation

## 5. Item 4 — whats-next scoped audit-first

- [ ] 5.1 RED ×2 on fixture 1.4; verdict per design D3 observable (blocks on / performs an
  audit despite fresh docs = fail)
- [ ] 5.2 If failed: reword When-to-use + Common-mistakes bullet; GREEN ×2; record
- [ ] 5.3 If passed: status-note + record

## 6. Item 5 — AUDIT small-set right-sizing

- [ ] 6.1 Resolve design open question (disproportion test) before running; RED ×2 on
  fixture 1.5
- [ ] 6.2 If failed: encode the one-sentence scale rule in AUDIT step 1 (compress per the
  word-count REFACTOR precedent); GREEN ×2; record
- [ ] 6.3 If passed: status-note + record (expected — loop-until-dry self-terminates)

## 7. Close out

- [ ] 7.1 Append the consolidated RED/GREEN record to `docs/docs-architecture-design.md`
  (per-item verdicts, what shipped vs no-failure)
- [ ] 7.2 Word-count check on SETUP/AUDIT/whats-next; compress if additions landed
- [ ] 7.3 Commit on dev; merge → main; `deploy.sh` (SKILL.md changes only take effect after
  deploy); sync delta specs to main specs; archive the change
