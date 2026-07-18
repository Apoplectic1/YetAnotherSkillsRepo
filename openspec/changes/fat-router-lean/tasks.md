# fat-router-lean — tasks

## 1. Fixture prep (RED prerequisites)

- [x] 1.1 Copy `harness/tidepool-fixture` to scratch; `git init` + "SKILLS-TEST BASELINE"
  marker commit (per VERIFICATION.md recipe)
- [x] 1.2 Author the **fat-router variant**: inject into the copy's CLAUDE.md a planted
  glossary block, a contract-prose block, and one hybrid block (gotcha line wrapped in
  contract prose, per design D6/risks); commit as a second marker
- [x] 1.3 Author the **lean-router control** state: fixture CLAUDE.md with routing +
  gotchas only (baseline may already serve; verify and mark the commit)
- [x] 1.4 Catalog the planted blocks + expected destinations (glossary → DOMAIN.md, etc.)
  in `harness/` (extend `catalog-tidepool.md` or add a sibling catalog file)

## 2. RED (current skill text must fail)

- [x] 2.1 SETUP RED ×2 on the fat-router variant with the **current** SKILL.md text
  injected: confirm the fat stays in place (expected per field finding 1); reset fixture
  after each rep — **OUTCOME: failed to reproduce, 0/2 — both reps leaned correctly**
- [x] 2.2 AUDIT RED ×1 on the fat-router variant: confirm no placement flag is emitted for
  the router; reset after rep — **OUTCOME: failed to reproduce — router placement-flagged
  under existing R10+R12**
- [x] 2.3 Record RED outcomes in NOTEBOOK (dated entry; reps, what fell short) — includes
  scale-RED ×2 on the real TP router (2/2 reproduced; B2 rule-collision mechanism captured)

## 3. Write the rules (candidate text)

- [x] 3.1 SETUP: add **S7** (router lean on encounter — content test; perform via S1 move;
  report moves; size as italic rationale only; hybrid-block split guidance; explicit B2
  carve-out countering the captured scale-RED rationalization) and cross-ref the
  enforced-set CLAUDE.md row ("kept thin — enforced by S7")
- [x] 3.2 AUDIT: add **R26** (router placement-audited; one structural `move-to` flag per
  block; currency flags inside the block stay legitimate — reference-tier, unlike R25;
  routing + gotchas never placement-flagged, regardless of size)
- [x] 3.3 Review both edits with `superpowers:writing-skills` conventions (wording, rule
  style, no instance-overfit) — form-matched to failure type (conditional + rationalization
  counter, not prohibition)

## 4. GREEN (candidate text must pass)

- [x] 4.1 SETUP GREEN ×2 — run on the **real TP router** (where RED reproduced), not the
  small variant: 24 KB → 3.5/4.3 KB routers, all blocks to charter homes, hybrid splits
  correct, moves named in reports — **2/2 PASS**
- [x] 4.2 SETUP control ×1 on the lean-router state: no lean action taken or reported —
  **PASS** (only the legitimate A2 history move)
- [x] 4.3 AUDIT GREEN ×1 on the fat-router variant: one structural placement flag per block
  citing R26, currency flags inside blocks preserved (amended two-axis design), no flags on
  routing/gotchas, tree untouched — **PASS**
- [x] 4.4 Disk-verify all GREEN claims (grep the fixture tree — trust disk, not agent
  claims); record GREEN outcomes in NOTEBOOK — verified: residual-fat greps clean,
  distinctive-phrase preservation checks pass (incl. verbatim perf-budget sentence in both
  ARCHITECTUREs)

## 5. Docs + ship

- [ ] 5.1 Update ROADMAP (close the fat-router-lean Open item; B4 probe + R26
  scaled-coverage remain open), NOTEBOOK (gate outcome + R26-alias renumber note), and
  CHANGELOG — same commit as the skill text per doc convention
- [ ] 5.2 Commit on `dev`; merge to `main`; run `deploy.sh` (only `main` deploys); verify
  deployed copies match repo
- [ ] 5.3 Final fixture reset/cleanup of scratch copies
