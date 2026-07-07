# docs-architecture-audit — delta (fix-skill-review-round2)

## ADDED Requirements

### Requirement: Fan-out is right-sized to doc volume
The fan-out SHALL scale with the audited doc set's volume. On a thin doc set (few, small,
recently-written reference docs) the run SHALL NOT deploy machinery disproportionate to the
content — per-doc workers plus the cross-reference pass suffice as the opening round;
per-section splitting, replicate rounds, and model diversity engage as volume and dry-round
results warrant. Loop-until-dry remains the terminator in all cases.

#### Scenario: Thin fresh set gets a small opening round
- **WHEN** an audit runs on a project with a handful of small, recently-written reference docs
- **THEN** the opening round is per-doc (not per-section × multiple models), the cross-ref
  pass still runs, and the run stops when a round is dry

#### Scenario: Large doc set still gets the full machinery
- **WHEN** an audit runs on a project with large multi-section reference docs
- **THEN** per-section workers, loop-until-dry, and model diversity apply as currently
  specified

**Status note (2026-07-07):** satisfied by baseline behavior, not by skill text. RED 2/2 passed —
on a 5-thin-doc fixture both reps planned a proportionate opening round (6 workers; explicit
"per-section collapses to per-doc" volume reasoning), kept round 3 conditional on a wet round 2,
and preserved loop-until-dry as the terminator. Per the no-failure gate no scale sentence was
added; if a future run deploys machinery grossly over volume, encode then. Record: design doc,
review-round-2 RED/GREEN entry.
