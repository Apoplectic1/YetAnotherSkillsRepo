# always-on-budget: design

## Context

The family budgets one file (40 KB, the harness's per-file warning) and never the chain a
session actually pays: the owner's global file, every ancestor router, the project's router,
the memory index. Measured 2026-10-12 on the HDL tree: 83 KB (about 21k tokens, a tenth of
the window) for a session under HlsLibrary or the Arty; this repo 36 KB. S7 leans a router by
content and keeps gotchas "regardless of router size", so HlsLibrary's 39.9 KB router (16.2 KB
of HLS synthesis gotchas, 12.6 KB of element maps the class READMEs already hold) is S7-clean.
The owner's question (2026-09-26): the gate is brute force, is there a better way?

## Decisions

- **D1: always-on is a scope, not a size.** An item loads at launch only if it passes breadth
  (every session launched here needs it) and stability (it changes less often than the audit
  cadence). S7's content test says where a thing lives; this test says whether it loads every
  time, and it is the definition "load-bearing" lacked: RED's SETUP reps each invented a
  criterion ("forbids or requires something on a named symbol; fails silently") because the
  text offered none.
- **D2: three on-demand homes, keyed to the need.** A path-scoped rule file
  (`.claude/rules/<name>.md` with `paths:`) for a file-keyed need: the harness loads it when a
  matching file is read, written or edited (verified against the Claude Code docs
  2026-10-12). A skill for an activity-keyed need: its body loads on invocation. A
  reference-doc section read by heading for prose. Not `@import`: imports expand at launch
  and cost the same as inline text. A rules file without `paths:` loads at launch and counts.
- **D3: the number detects, the test decides.** `chain_budget.py` reports the chain against
  5 percent of a 200k window (10k tokens; the router may state its own share). The budget is
  a tripwire that prompts the test, never a trigger that moves content; a router under budget
  still moves a block that fails. The default was the owner's call (5 percent: every HDL
  session trips it today, which is the finding; this repo does not).
- **D4: the chain is reported whole, the test applied to what the project controls.** The
  row shows the owner's global file (26.7 KB, a third of every chain on the machine) as the
  owner's and an ancestor's weight as its own audit's; the project's own part is subtotaled.
  A sub-project's audit does not flag its ancestor; the root's audit does.
- **D5: R26 keeps its content-axis carve-out.** "Never flag routing lines or gotchas,
  regardless of router size" stays true for content; the scope test is a second axis. RED
  showed the carve-out shielding 11.9 KB of per-repo gotchas in a container root whose own
  charter says per-repo specifics live below: both root reps named it "the call that most
  changes the result".
- **D6: lines, too.** The harness warns at 200 lines per CLAUDE.md; the script marks files
  over it so the family's tripwire and the harness's agree. HlsLibrary's router is 397 lines,
  the Arty's 346, so that warning is live there today.
- **D7: the pilot is consumer work.** HlsLibrary's router (element maps to the class READMEs,
  the HLS gotchas to a path-scoped rule file or a skill), the ATML DOMAIN read by section, the
  Arty's router: from an HDL session after the ship, queued in ROADMAP. The owner's call.

## What RED showed (2026-10-12)

Six single-agent reps on the current texts. SETUP, plan-only on the `fat-gotchas` router (a
10 KB pack of true `tides.py`-only gotchas): both reps split the pack by S7's hybrid rule
(bodies to ARCHITECTURE) and kept 7 to 12 one-line guards always-on under an invented
criterion, measured nothing, and listed "load-bearing is never defined" and "feels heavy has
no operational meaning" among what the text did not decide. AUDIT from `ReefDash` under a
15 KB root: both reps excluded the ancestor by R12 and R16, measured nothing, and noted its
size as an aside. AUDIT at the root: both reps left the two sub-project packs (77 percent of
the file) unflagged under R26's carve-out and said so; the vocabulary block went to a new
portfolio DOMAIN (R26, B4) and the routing table stayed, as the controls expected. Every
copy byte-untouched.

## Verification

Script-level: `gen_chain_fixture.py` writes a tree with exact sizes; `chain_budget.py`'s
output byte-matches `chain.expected.txt`. Reps: RED six through the Agent tool (effort
inherited), GREEN six through a Workflow with `model: 'sonnet', effort: 'high'` pinned (the
owner's directive, now the standing path for reps). Record:
`docs/2026-10-12 - always-on-budget-red-green.md`.
