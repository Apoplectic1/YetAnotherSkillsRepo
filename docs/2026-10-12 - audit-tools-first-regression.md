# audit-tools-first: regression record (2026-10-12)

**Charter:** the dated record of the regression that gated the AUDIT trim: what ran, what
each family's cells showed with the trimmed text, the one clause restored, and what the reps
named. The design is `openspec/changes/archive/2026-10-12-audit-tools-first/design.md`; the
standing truth is the design doc's "Tools over prose" part and AUDIT's text.

## The gate

As for SETUP: no RED, one report-only single-agent rep per fixture family (R18 to R23 and
R27 waived), Sonnet at high through one Workflow (five reps, 344k tokens, 114 s), then one
re-run after the restore (one rep). The text under test: AUDIT at 10.1 KB and 147 lines
(from 13.4 KB and 182), each rule its action plus one boundary, the procedure opening with
`scope.py` beside it (its own check: byte-exact output on three baselined fixture copies,
`harness/scope-fixture/`). The orchestrator-context leak is disclosed as always.

## The families

| Rep | Launch dir | Cells | Result |
|---|---|---|---|
| tp | the base TidePool | t1, O1, CB1, CB4, DV2 | PASS. One structural flag on the shipped history, `move-to CHANGELOG.md`, the nine entries not flagged one by one (the seed's `cache.py` folded into it); D4 flagged with the R28 lead ("a curated station registry"); D5 clean; the cited archived design kept on a consistency check with its drifted values noted and no edit; the timeout contract `flag-code-bug` by corroboration (R7); the known bug `keep`. Also the DOMAIN daylight contract as `flag-code-bug` and the dead cache helpers as `unverifiable → ask user` (R8). |
| pm | `audit-scope`, from `PulseMonitor/` | SS1, SS2, SP1, SP2 | PASS. The router-named spec's "every 5 seconds" → `spec-change`, the spec untouched, R7's code-is-suspect set aside because code, router, SCHEMA and the ancestor agree on 10 s; the unnamed spec unflagged; the routed dated wiring doc audited (`fix-doc`, the swapped channels) with the R28 lead (point at `CHANNELS`); the unrouted bring-up record left out. The rep overrode the scope script, which had listed the routed doc as unrouted: a spaced dated name (`docs/2026-07-01 - probe-wiring.md`) was not read as a path. Fixed in the script the same hour; the expected output regenerated. |
| fcr | the `fat-chain` root | SC1, SC2, SC3 | PASS. One placement flag per sub-project gotcha pack, each `move-to` an on-demand home in its sub-project with a trigger line (breadth and stability failed, the dated narrative named); the vocabulary `move-to` a portfolio DOMAIN (R26), the sub-projects' mutual salinity-event pointers noticed; the routing table and the `scripts/` line unflagged; the `readings.db` contract prose `cross-ref+delete` against the owner's SCHEMA. |
| rd | `ReefDash/` under the fat root | CH1, CH2 | PASS. The coverage note carries the row: 10,815 tokens over by 815, the overage "entirely the ancestors' and the owner's, reported, not flagged", the ancestor router the only file over its line, the largest items named; no flag on ReefDash's own router. The mutual DOMAIN pointers found as two `fix-doc` flags, the sibling's report-only. |
| rl | `release-lens`, "A release just closed; run the audit cheaply." | RL1 to RL6, RC1 to RC3, SM2 | RL1 to RL6 all flagged (`fix-doc`, the R28 lead where the value is derivable), RC1 to RC3 held, the timeout `flag-code-bug` by corroboration. SM2 FAILED: the rep did not name the mode: "R29 says a scoped mode is invoked by the user and never chosen by the run. I treated the request as a plain audit ... and did not use `--lens release`." The trim had dropped R29's second sentence, "The user names one, or asks for one round or a cheap run and the run names which fits and says so", and the rep read what was left literally. |
| rl2 | the same, with the sentence restored | SM2 | PASS. "Mode: `release-close` (R29). The user asked for a cheap run right after a release, so I chose the mode and am saying so." `--lens release` run (21 lines), RL1 to RL6 flagged, RC1 to RC3 held, the coverage note naming the mode and what a full run would add; the timeout and the daylight contract found outside the lens and flagged as code bugs, with the rep asking whether a lens run should stay inside its lines. 81k tokens. |

## The clause restored

R29 regains "The user names one, or asks for one round or a cheap run and the run names
which fits and says so" (26 words). It is the only sentence the regression restored: the
rule's first sentence states the principle, the second maps a user's wording to a mode, and
a rep given only the principle refused the inference. Shortest form that passes: the
original sentence; nothing shorter was tried, since the sentence is the mapping itself.

## What the reps named (none a failure of a cell)

- R25 against a ROADMAP charter that lists "shipped history" (tp, rl): flagged anyway, the
  charter conflict noted; a fixture artifact of the base charter line.
- An uncited archived design used as evidence for a `revisit-plan` (tp): R15 governs the
  cited one; the rep asked whether an uncited archive may carry evidence.
- A move whose target is inside a sub-project (fcr): `move-to` with the sub-project side as
  a handoff (R16, R3).
- A parent router as a canonical home for a term the children point at each other for
  (rd); a sibling treated as a sub-project by analogy (R16).
- A bare filename that resolves only through a sibling (rd): the script says "under the
  ancestor"; the rep counted it resolved.
- Whether every `unverifiable → ask user` claim is worth a flag on a small set (pm, rd).

## Verdict

Four families clean on the first run, one clause restored and re-run to a pass, the scope
script corrected on a rep's finding. The trim ships at 10.2 KB (10,243 bytes, 149 lines).
The cost of the gate: 425k tokens over six reps.
