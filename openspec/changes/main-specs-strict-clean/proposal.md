# Proposal: main-specs-strict-clean

## Why

`openspec validate --specs --strict` fails four of the five main specs, so a strict run
cannot serve as a whole-repository check. The failures are warnings: 26 requirements whose
description passes 500 characters, and a placeholder Purpose in the audit and setup specs.
The owner asked on 2026-11-10 for all of them fixed, and for status notes to be removed
unless they contribute to behavior.

## What the specs hold today (measured 2026-11-10)

| Spec | Requirements | Past 500 characters | Status notes | Purpose |
|---|---|---|---|---|
| `docs-architecture-audit` | 21 | 10 | 5 | placeholder |
| `docs-architecture-maintain` | 8 | 6 | 1 | written |
| `docs-architecture-setup` | 19 | 8 | 3 | placeholder |
| `github-distribution` | 6 | 2 | 0 | written |
| `whats-next` | 4 | 0 | 2 | written (passes strict) |

Of the eleven status notes, six sit inside a requirement's description and five after its
scenarios, where the validator does not count them (the count of eleven was corrected at the
apply, 2026-11-10; the proposal first counted only the six). Removing them clears two of the
26 long requirements: the other 24 are long because each
bundles several behaviors, often with rationale or provenance beside them (the router-lean
requirement holds a content test, a scope test, the homes and their triggers, the naming
rule, the per-file line and the chain measurement in 2,007 characters).

## What Changes

- **Status notes removed.** Nine record test history only (design D1 lists them) and go,
  `whats-next`'s two included. Two also
  state behavior, which stays as requirements of its own (the owner's rule): setup's
  router-lean note carries four rules RED showed correct (a block a reference doc already
  holds is dropped with a cross-reference; a block at release cadence goes to ROADMAP; a halt
  the ROADMAP states bounds the plan; breadth at a container root counts every session
  beneath it), and maintain's bloated-target note carries one (a held promotion under a halt
  follows the halt's own terms). Three of the five already stand in the specs as scenarios
  (found at the apply: setup's "A block a reference doc already holds" and "A halt bounds
  the plan", maintain's "A held promotion under a halt follows the halt's terms"); they
  become requirements in place with those scenarios under them. The other two stand nowhere
  but in the note, so they are the change's only spec-level additions, written as ADDED
  deltas to setup.
- **One behavior per requirement.** Each requirement still past 500 characters is cut to
  its lead behavior under its own name; every other behavior it bundles becomes a
  requirement named for that behavior. Scenarios move with the behavior they test, so every
  scenario sits under the requirement it checks; a behavior no scenario tests gets one,
  written from the requirement's own text. A parent keeps its name unless the name names a
  behavior that moved away (design D2); no file outside `openspec/` cites a requirement by
  name.
- **Prose that states no behavior is removed with the notes**: provenance ("gated on
  RED/GREEN on a non-derived fixture"), field cases and why-clauses. A testable example
  moves into a scenario. Every removed sentence is recorded in the change's ledger with the
  reason, and a check confirms that every sentence of the old text is either in the new
  spec or in the ledger.
- **The two placeholder Purposes are written**, each one or two sentences on what the
  capability is for.
- **The convention changes for later work**: a requirement whose candidate skill text
  no-failed its RED stands in the spec as a requirement with no note; its test result lives
  in the change's design record. One line in `DOMAIN.md`'s authoring conventions says so,
  since no doc stated the old habit.
- **Reference docs that describe the specs as carrying status notes** are corrected: the
  design doc's Always-on budget part and Scope-from-the-routers part, and the latter's index
  line. Journal entries (CHANGELOG, NOTEBOOK, dated records) and archived changes stay as
  written.

## Decided (2026-11-10, by what lets an agent find a fact fastest)

- **The main specs are edited in place, not through MODIFIED deltas.** A MODIFIED block may
  not drop a scenario name the main spec still has, so a delta-only split would leave every
  scenario under the trimmed parent and need a duplicate under each split-off requirement.
  Edited in place, a scenario sits under the requirement it tests, which is where a reader
  looks for it. The two behaviors the specs state nowhere are ADDED deltas, the change's
  only deltas.
- **Removed prose goes, not elsewhere.** The status notes' test results are already in the
  archived changes' design records and dated records; the spec is a behavior contract, and
  git backs up the old text.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `docs-architecture-setup`: two behaviors from the router-lean status note added as
  requirements; in place: one behavior per requirement, the status notes gone, the Purpose
  written.

`docs-architecture-audit` (with its Purpose), `docs-architecture-maintain`,
`github-distribution` and `whats-next` are restructured in place with no behavior added, so
they carry no delta.

## Impact

- **Specs**: the four failing main specs under `openspec/specs/`. No skill text, script or
  fixture changes; nothing deploys differently.
- **Docs**: `DOMAIN.md` (one convention line), the design doc's two parts and one index
  line, `CHANGELOG.md`, the ROADMAP digest.
- **Checks**: strict validation 5/5; the ledger check (every old sentence kept or recorded,
  every old scenario and requirement name present); four reader reps at Sonnet/high, one per
  spec, each comparing the old spec with the new for behavior lost, added or changed.
