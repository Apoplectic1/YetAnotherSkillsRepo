# Always-on budget: RED/GREEN record (2026-10-12)

Change `always-on-budget` (the ROADMAP's "Always-on budget", queued 2026-09-26 after the
journal rollover). Fixtures: TidePool with the `fat-gotchas` overlay (a 10 KB pack of true
`tides.py`-only gotchas beside the router's three load-bearing ones), reefstack with the
`fat-chain` overlay (a 15 KB root router carrying a 12 KB PulseMonitor calibration pack, a 5 KB
DoseKeeper pump pack and a glossary; the chain from any sub-project 42 KB, 1.1x the budget),
and `harness/chain-fixture/` for the script. Cells in `harness/catalog-tidepool.md` (ST) and
`harness/catalog-reefstack.md` (CH, SC). Method: single-agent reps, report-only, Sonnet.
RED six through the Agent tool (effort inherited from the session, 137k to 203k tokens each);
GREEN six through a Workflow with `effort: 'high'` pinned (441k for six, about 73k each; the
owner's directive, now the standing path for reps). Every copy byte-untouched afterward.

## Cells and results

| Cell | Plant or probe | RED (current text) | GREEN (candidate) |
|---|---|---|---|
| ST1 | SETUP plan-only, "the router feels heavy": the CO-OPS pack | 2/2 S7's hybrid split: 22 bodies to ARCHITECTURE, 7 to 12 one-line guards kept always-on under an invented criterion ("forbids or requires something on a named symbol, fails silently") | 2/2 S8 cited: the pack, guards included, to `.claude/rules/` with `paths:` (fg4 as two files, client and exporter), one trigger line, "a guard only one activity needs is that activity's, however sharp" |
| ST2 | the three base gotchas | kept 2/2 | kept 2/2, each tested for breadth and stability |
| ST3 | the number vs the test | nothing measured; "feels heavy has no operational meaning", "no router budget exists" | 2/2 the chain estimated (about 2k tokens, under budget) and the pack moved anyway: "the number detects, the test decides" |
| CH1 | AUDIT from ReefDash under the fat root | 2/2 no chain row; the ancestor excluded by R12 and R16, "the text never mentions ancestors", its size an aside | 2/2 `chain_budget.py` run: 10,815 tokens against 10,000, the ancestor 15 KB and 206 lines named as the largest project-side item, "reported only, never flagged here", the owner's global file reported as the owner's |
| CH2 | ReefDash's thin router | unflagged 2/2 | unflagged 2/2, "passes breadth and stability on every block" |
| SC1 | AUDIT at the root: the two sub-project packs | 2/2 unflagged under R26's carve-out; "the call that most changes the result" | 2/2 one placement flag per pack citing R30 breadth (only a calibration or a pump session needs it) and stability (dated, bug-status lines), `move-to` a sub-project section, rule file or skill with a trigger line; fc8 projected the chain after the move (7,740 tokens, under) |
| SC2 | the vocabulary block | `move-to` a new portfolio DOMAIN (R26, B4) 2/2 | the same 2/2 |
| SC3 | the routing table and `scripts/` line | unflagged 2/2 | unflagged 2/2 |

## What RED taught

- **The content test was doing scope's job badly.** Both SETUP reps read each gotcha as a
  hybrid (trap plus mechanism), moved the mechanism by S7 and kept the trap lines, which is
  S7 working; what they could not say was which trap lines belong always-on, so each invented
  a criterion and named the gap ("load-bearing is never defined", "no end-state target,
  stopping rule or post-lean check"). S8 is that criterion.
- **An ancestor is invisible by rule.** Both ReefDash reps left the fat root out under R12 and
  R16 with a sentence of regret in the coverage note. Reading it was never the problem
  (2026-10-12's ancestor-router cells showed reps read ancestors unprompted); measuring it
  and saying so was.
- **R26's carve-out shields exactly the content the rule targets.** Both root reps saw 77
  percent of the file was two other projects' gotchas in a map whose charter sends per-repo
  specifics below, and left them because "never flag gotchas regardless of router size" gave
  no way through. The qualifier (content axis only) opens it; R30 walks through.
- **The fixture needed a second cut.** The first `fat-chain` root came in 38 tokens under
  budget, so the chain row would have had nothing to say; a DoseKeeper pack was added. A
  tripwire fixture has to trip.
- **A removal through a shell variable is refused by the harness's safety check**
  (`rm -rf "$d"` with `d` built from two variables). The GREEN copies were built without a
  removal step, under fresh names; a literal absolute path is the sanctioned form.

## What GREEN taught

- **The effort pin halved the cost at no visible loss.** RED reps at inherited effort ran
  137k to 203k tokens; GREEN reps pinned to high ran about 73k, found every plant, held every
  control, and wrote the same uncertainty lists.
- **The script was used as written.** Every AUDIT rep ran `chain_budget.py` from beside the
  skill text, quoted its row, and read the subtotals the way R30 asks (the owner's global as
  the owner's, the ancestor as its own audit's).
- **Two no-failure observations, recorded not encoded.** Rule-file granularity (one file per
  pack or one per module) and `paths:` precision are the author's call and the text is
  silent; both SETUP reps chose sensibly and asked. At a container root, "every session
  launched here" could be read as root sessions only, though the router loads into every
  sub-project session beneath it; both root reps still flagged the packs. If a run ever
  spares a container-root block on that reading, add the clause then.
- **Open questions the reps raised, not acted on:** `move-to` a doc that does not exist yet
  (the portfolio DOMAIN, twice); whether the three base gotchas are "every session" (each
  rep kept them and said the test has no threshold); the real ancestors above a scratch
  path (the fixture has none; a real run has them).

## Shipped

SETUP S8 (the scope test as the meaning of "load-bearing", the three on-demand homes, the
trigger line, the measure), B1's carve-out for a rule file the router names, the enforced-set
row, Procedure 3; AUDIT R30 (the chain measured and the row in the coverage note, the scope
test as a placement axis, an ancestor reported not flagged), R26 qualified to the content
axis, Procedure 1 and 3, R13's spec clause narrowed to `openspec/specs/`; `chain_budget.py`
beside the audit skill; the design doc's cost model and dated section; both specs. The
HlsLibrary pilot is queued in ROADMAP as consumer adoption from an HDL session.
