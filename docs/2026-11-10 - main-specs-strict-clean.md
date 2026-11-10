# Main specs strict-clean: record (2026-11-10)

Change `main-specs-strict-clean` (the owner, 2026-11-10: fix every strict warning, and remove
the status notes unless they contribute to behavior). The five main specs under
`openspec/specs/` were restructured in place to one behavior per requirement. The record
covers the result, the two checks that show nothing was lost, and the reader reps.

## Result

| Spec | Requirements before -> after | Status notes removed | Strict before -> after |
|---|---|---|---|
| `docs-architecture-audit` | 21 -> 35 | 5 | fails (10 long, Purpose a placeholder) -> passes |
| `docs-architecture-maintain` | 8 -> 24 | 1 | fails (6 long) -> passes |
| `docs-architecture-setup` | 19 -> 39, plus 2 ADDED at the archive | 3 | fails (8 long, Purpose a placeholder) -> passes |
| `github-distribution` | 6 -> 13 | 0 | fails (2 long) -> passes |
| `whats-next` | 4 -> 4 | 2 | passes -> passes |

`openspec validate --specs --strict`: 1 passed and 4 failed at the base commit (`6edbf67`),
5 passed after. No skill text, script or fixture changed.

Of the eleven status notes, nine held test history only. Two also stated behavior a RED had
shown correct: setup's router-lean note (four rules) and maintain's bloated-target note (one).
Three of those five rules already stood as scenarios and became requirements in place
(setup's "A router block a reference doc already holds is dropped with a cross-reference" and
"A halt the ROADMAP states bounds the plan to docs-only moves", maintain's "A held promotion
under a halt follows the halt's terms"). The other two stood nowhere else and are the change's
ADDED requirements in setup ("A router block at release cadence goes to ROADMAP", "Breadth at
a container root counts every session beneath it").

Prose that states no behavior went with the notes: provenance ("Gated on RED/GREEN..."),
field cases, why-clauses and two cross-skill analogies. Each removal and each rewording a
split forced is quoted in the change's `ledger.md` with its reason.

## The clause check

`check_specs.py` (in the change directory) reads each spec at the base commit and on disk,
splits each old description into clauses at sentence ends and semicolons, and reports a clause
found neither in the new spec nor in the ledger, an old requirement or scenario name missing
(a rename needs a `Renamed:` ledger line; there is one, audit's chain requirement), a changed
scenario body, a requirement without a scenario, and any status note left. Final run: 0 faults
on all five specs, no status note, strict 5/5. The check caught, during the apply, a clause
that had been dropped instead of moved (maintain's "mirroring AUDIT R4/R7 semantics", then
removed on purpose as an analogy and ledgered) and two ledger quotes abbreviated with "...".

## The reader reps

One Workflow, four reps at Sonnet/high (`rep:<spec> [sonnet/high]`), one per spec with a
requirement cut; whats-next lost only two notes after its scenarios, which the clause check
covers alone. Each rep read the old spec, the new spec, the ledger's section for it and (for
setup) the ADDED delta, and listed behavior lost, changed, added, removed by misjudgment, or
misplaced.

| Spec | First read | Fix | Rerun |
|---|---|---|---|
| audit | 44 requirements compared, no finding | none | not needed |
| maintain | 35 compared, no finding | none | not needed |
| setup | 45 compared, one finding (below) | the creation rule moved into the parent | 52 compared, no finding |
| github-distribution | 12 compared, no finding, one point noted but not reported (below) | the pointer named | 13 compared, no finding |

- **Setup, misplacement.** The portfolio DOMAIN's creation rule ("created when cross-repo
  truth exists, never by default") had moved to the requirement "Cross-repo prose from a
  leaned container router goes to the portfolio DOMAIN", while its test, the scenario "No
  portfolio set beyond the sanctioned pair", stayed under the parent "Container roots support
  a thin portfolio DOMAIN for cross-repo truth". Fixed by stating the condition in the parent's
  own sentence (in place of its "optionally"), the lean requirement keeping "creating it thin
  if absent" from its scenario.
- **github-distribution, noted.** "Repo-side descriptions of the citation form match the footer
  convention" said "SHALL match this convention" with the convention now in the requirement
  before it. Fixed by naming that requirement.

Tokens: 303k for the four reps, 150k for the two reruns, 454k in all.

## Reference docs corrected

`DOMAIN.md` (The iron law) gained the convention: a requirement whose candidate skill text
no-failed its RED stands in the spec as a requirement with no note, its result in the change's
design record and its dated RED/GREEN record. The design doc's Always-on budget and
Scope-from-the-routers parts no longer say the specs carry status notes, the latter's index
line with them (`split_doc.py --reindex` kept the lines and listed that part for review;
`--check` clean). The Journal-rollover part's "status-noted" now says "in the change's delta".
Two past-tense mentions in The phased arc describe archived deltas, which keep their notes, and
stand as written.
