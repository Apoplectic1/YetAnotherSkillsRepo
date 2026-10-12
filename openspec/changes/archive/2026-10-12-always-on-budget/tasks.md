# Tasks

## 1. The script and the fixtures
- [x] 1.1 `skills/docs-architecture-audit/chain_budget.py`: the chain in load order (the owner's global file and always-on global rules, every ancestor router, the project's router and always-on rules, the memory index), bytes, lines, estimated tokens, the 200-line mark, the budget as a share of the window, the project's part subtotaled; `--root` for byte-exact fixture output
- [x] 1.2 `harness/chain-fixture/`: `gen_chain_fixture.py` and `chain.expected.txt`; the script's output on the generated tree matches it
- [x] 1.3 `harness/reefstack-fixture-variants/fat-chain/CLAUDE.md` (a 12 KB PulseMonitor-only gotcha pack and a vocabulary in the root router) and `harness/tidepool-fixture-variants/fat-gotchas/CLAUDE.md` (a 10 KB `tides.py`-only pack beside the three load-bearing gotchas); cells in both catalogs; `harness/README.md` names all three

## 2. RED
- [x] 2.1 AUDIT, current text: two reps from `fat-chain/ReefDash` (CH1 fail 2/2: no chain row, the ancestor excluded by R12 and R16; CH2 held), two from the root (SC1 fail 2/2: both packs shielded by R26's carve-out, "the call that most changes the result"; SC2, SC3 held)
- [x] 2.2 SETUP, current text: two plan-only reps on `fat-gotchas` (ST1 fail 2/2: S7's split kept 7 to 12 activity guards always-on under an invented criterion, nothing measured; ST2 held)

## 3. The skill text
- [x] 3.1 SETUP: S8 beside S7 (breadth, stability as the meaning of load-bearing, the three homes, the trigger line, the measure); the enforced-set row; B1's carve-out for a rule file the router names; Procedure 3
- [x] 3.2 AUDIT: R30 (the chain measured and the row in the coverage note, the scope test as a placement axis, an ancestor reported not flagged); R26 qualified to the content axis; Procedure 1 and 3; R13's spec clause narrowed to `openspec/specs/` (a RED rep read it wider)
- [x] 3.3 The design doc: the cost model, the harness facts, the dated section and the principle-1 sentence; no DOMAIN line needed (the router test is the skills' own)

## 4. GREEN
- [x] 4.1 The same six reps with the candidate texts, through a Workflow at Sonnet/high (the owner's directive): ST1 to ST3, CH1, CH2, SC1 to SC3 all 2/2; 441k tokens for six

## 5. The reference tier and the record
- [x] 5.1 The setup and audit specs: MODIFIED lean requirement (scenario names kept), ADDED chain requirement, MODIFIED router-placement requirement
- [x] 5.2 `docs/2026-10-12 - always-on-budget-red-green.md`; ROADMAP: the item to Recently shipped, the HlsLibrary pilot queued as consumer adoption, the split item unblocked; NOTEBOOK entry; `VERIFICATION.md` names the chain fixture
- [x] 5.3 `openspec validate always-on-budget --strict`; archive with `--yes`, judged by output text; `main` fast-forwarded; `deploy.sh`
