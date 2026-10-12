# s8-field-fixes: design

## Context

S8 shipped on the morning of 2026-10-12 (`always-on-budget`) and met three real
repositories that afternoon (`docs/2026-10-12 - hdl-pilot.md`). The budget it stated could
not be met from inside any of them, two of its three homes had load triggers it did not
state and B1 forbade one of them, and a third of each router's gotchas already lived in a
reference doc. Every finding came from the tree, so every clause was RED/GREEN'd on the
TidePool `s8-field` variant and the reefstack `fat-chain` root, and only a clause a rep
failed there ships (the record: `docs/2026-10-12 - s8-field-fixes-red-green.md`).

## Decisions

- **D1: the budget is per file.** Every file that loads at launch has 200 lines (the
  harness's own guidance, about 20 KB, about 5k tokens): the number a unit can act on. The
  chain's 5 percent stays the row's tripwire, met when every level meets its own; the
  ancestors' and the owner's shares are reported for their own leans and never chased from
  below. The owner's global file is 6.8k tokens on this machine; no unit's chain meets 10k
  while it loads, and the old text told the rep to fix it (RED 3/3). The alternative, a
  per-project share of the chain, was rejected: it makes a project's budget depend on files
  it does not own.
- **D2: each home states its load trigger.** A path-scoped rule file loads on a matching
  file's first touch, so it fits a need keyed to files in this repository and nothing else:
  a session that only runs a command touches no file (a build, a bench run), and a glob
  cannot name a sibling repository's files. A skill loads on invocation, for an activity. A
  section is read by heading, for prose. A guard keyed to neither keeps one router line. The
  old text named the homes without the triggers, and two of three reps wrote a rule file
  that never fires.
- **D3: B1 lets S8 write a skill.** The only things written under `.claude/` are what S8
  moves a block to, a rule file or a skill, each named by the router. The old B1 allowed a
  rule file only; all three RED reps named the contradiction.
- **D4: stability reads "changes less often than a release".** The old "audit cadence" is
  a term no project defines. A wording clarification, not a rule: the State-block cell was
  no-failure under either.
- **D5: what did not ship.** Five clauses drafted from the pilot were no-failure on the
  fixtures and are status notes in the specs: a block a reference doc already holds is
  dropped with a cross-reference (both reps did it as S1's merge); a status block goes to
  ROADMAP (both); a halt bounds the plan to documentation (the rep read the halt); breadth
  at a container root counts the sessions beneath it (the root rep counted them; the
  pilot's AtmlBoards rep, which did not, stands as the evidence that a run can misread it);
  a held promotion under a halt stays held (the MAINTAIN rep read the halt's terms, which
  admit documentation, and sequenced a docs landing after the split: right for that halt,
  and the drafted clause would have been wrong there). B4 for an umbrella with first-party
  content and a row for a project's reference docs outside the set were not probed and wait
  for a cell.
- **D6: the tools.** `chain_budget.py` lists the files over their own line in the summary,
  each with whose it is. `split_doc.py --reindex` rewrites a split index's Parts list from
  the parts (sizes, first sentences) in the index's order, bodies untouched: the design
  doc's always-on part was edited twice today and the index's sizes went stale each time.

## Verification

RED on the current texts: SF1 fail 3/3, SF2 fail 3/3, SF3 fail 1/2; SF4, SF5, SF6, CR1
no failure; SM1 moot (the fixture's halt admits documentation), SM2 no failure. GREEN on
the candidate: SF1, SF2, SF3 pass 2/2. Script-level: the chain fixture's expected output
and the split fixture's index and dry run reproduce byte for byte; `--reindex` on an
unedited split leaves the index byte-identical and, after a part is edited, changes that
part's line alone.
