# main-specs-strict-clean: design

## Context

See `proposal.md` for the motivation and the measured state. The constraints that shape
the approach:

- The validator measures a requirement's description: the text between its
  `### Requirement:` line and its first `#### Scenario:`. It flags past 500 characters, and
  wants SHALL or MUST on the description's first line.
- A MODIFIED delta may not drop a scenario name the main spec still has
  (`.claude/rules/openspec.md`), so scenarios cannot move between requirements through a
  delta.
- Outside `openspec/`, no file cites a requirement by name (only the opsx command
  templates match the pattern), so a requirement's name can be kept or added freely. The
  archived changes cite the current names and are never edited.
- The main specs sit outside the doc set (`CLAUDE.md`'s exclusions), and nothing in the
  skills, scripts or deploy reads them. The change is to the specs' text alone.

## Goals / Non-Goals

**Goals:**

- `openspec validate --specs --strict` passes 5/5.
- Every behavior the specs state today is still stated, under a requirement whose name
  says what it is, with the scenarios that test it beneath it.
- A check, not a reading, shows that nothing was lost.

**Non-Goals:**

- Any change to what a skill does: no SKILL.md, script or fixture is touched.
- Rewording a requirement that already passes.
- Editing journal entries or archived changes that mention status notes.

## Decisions

- **D1: the eleven status notes, classified.** Each is test history (the RED result, why no
  skill text shipped, "encode it then"), which is not behavior. Nine hold nothing else and
  go: audit's "Worker evidence is disk-verified before adjudication", "Fan-out is
  right-sized to doc volume", "A journal's overflow directory is journal-tier", "The router
  sets the tier, not the directory or the name" and "Ancestor routers are convention
  sources"; setup's "Legacy-named domain doc is normalized into DOMAIN.md" and "A reference
  doc past its budget splits by topic into a directory named for it"; whats-next's
  "Audit-first is scoped, not unconditional" and "Open items are read from the live
  journal". (Five of the eleven sit after their scenarios, where the validator does not
  count them; the plan first counted only the six inside a description.) Two state behavior
  a RED cell showed correct. Setup's "Router lean on encounter" note
  carries four rules and maintain's "Graduations targeting a bloated doc are held, never
  applied into it" carries one; each rule becomes a requirement and the history goes. Under
  the owner's rule, this is what "contributes to behavior" means. Three of the five already
  stand as scenarios (setup's "A block a reference doc already holds" and "A halt bounds the
  plan" under the router-lean requirement, maintain's "A held promotion under a halt follows
  the halt's terms" under the bloated-target one; found at the apply), so each becomes a
  requirement in place with its scenario under it. The other two (a block at release cadence
  goes to ROADMAP; breadth at a container root counts every session beneath it) stand
  nowhere else, so they are ADDED deltas with a scenario taken from the cell that showed
  them.
- **D2: one behavior per requirement.** A behavior is one SHALL or MUST obligation with its
  trigger, its outcome and its own boundary or exception; a qualifier of that obligation
  stays with it. The parent keeps its name and its lead behavior; when its name names a
  behavior that moved away, it is renamed to what it still requires (decided at the apply:
  a name that points a grep at the wrong requirement is worse than a rename, and no file
  outside `openspec/` cites a requirement by name), the rename recorded in the ledger as
  `Renamed: "<old>" -> "<new>"`, which the check reads. Each other behavior
  becomes a requirement placed directly after its parent and named for what it requires (as
  the specs already name theirs: "Router lean on encounter", "Fix-or-delete discriminator
  on derivable claims"), SHALL on its first line. A scenario moves to the requirement whose
  behavior it tests; a scenario that tests two stays with the parent. A behavior no scenario
  tests gets one, written from the requirement's own text, never a new behavior. A
  requirement already under 500 characters is not touched, even when it bundles.
- **D3: prose that states no behavior goes.** Provenance (where a rule was derived, which
  fixture gated it), field cases and why-clauses are removed. What stays is anything that
  changes what a run does: a boundary, an exception, a name the run must use, a number it
  applies. A concrete example that is testable becomes a scenario (or part of one). The
  owner's rule names status notes; this applies the same test to the prose around them,
  since it is the same kind of text.
- **D4: the main specs are edited in place.** The alternative, MODIFIED deltas, cannot
  move a scenario: every scenario would stay under its trimmed parent, and each split-off
  requirement would need a duplicate. In place, a scenario sits under the requirement it
  tests, where a reader looks for it. The two rules D1 finds stated nowhere else are ADDED
  deltas, the change's only deltas, and land at the end of the setup spec at the archive. They stay there; their
  names say what they require and a grep finds them, so moving them beside their parent is
  not worth an edit outside the tracked tasks.
- **D5: the ledger and its check prove that nothing was lost.** `ledger.md` in the change
  directory lists every clause removed or reworded, by requirement, with its reason
  (status note, provenance, field case, why-clause, example moved to a named scenario) and,
  for a rewording, the new text. `check_specs.py` beside it reads each main spec at the
  commit the apply starts from and the spec on disk, splits each old description into
  clauses (at sentence ends and semicolons, line wraps normalized), and reports any clause
  found neither in the new spec nor in the ledger; any old requirement or scenario name
  missing; any requirement left without a scenario; and the strict validation result. The
  split moves whole clauses verbatim wherever it can, so the ledger holds removals and the
  few rewordings a split forces.
- **D6: the two Purposes** say in one or two sentences what each capability is for,
  following the three written ones: audit, verifying a project's reference docs against the
  code and their charters; setup, bootstrapping a project's docs into the convention.
- **D7: the convention for later work.** `DOMAIN.md`'s authoring conventions gain one line:
  a requirement whose candidate skill text no-failed its RED stands in the spec as a
  requirement with no note, and its test result lives in the change's design record. No doc
  stated the old habit, so without the line the next no-failed change would re-add a note.
- **D8: reader reps for meaning.** The check proves clauses were kept, not that a split
  kept their sense (a qualifier moved away from its obligation would pass it). Four reps,
  one per spec with a requirement cut (whats-next only loses two notes after its scenarios,
  which the check covers alone), each read the spec's old text and its new text (and, for
  setup, the ADDED delta) and list any behavior lost, added or changed, by requirement
  name. A finding is fixed and its rep rerun until it reports none.

## Risks / Trade-offs

- [A split changes a requirement's sense: a boundary left behind, an exception attached to
  the wrong obligation] -> D2's rule that a qualifier stays with its obligation, and D8's
  reps.
- [A sentence judged non-behavioral is a behavior] -> the ledger lists it with its reason,
  where the reps and the owner's review see it; restoring it is one line.
- [The specs grow: about 24 parents become perhaps 60 to 70 requirements, with new headings
  and some new scenarios] -> accepted: they are read rarely and by grep, and one obligation
  per requirement is what a grep should land on.
- [The two ADDED requirements sit at the end of the setup spec, away from their parent] ->
  accepted (D4).
- [A later archive appends a requirement past 500 characters] -> the validator flags it in
  the change's own delta before the archive, as it does today.

## Migration Plan

None. The specs are text no tool consumes, and nothing ships to a consumer. Rollback is a
revert of the change's commits.
