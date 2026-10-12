# poll-loop Specification

## Purpose
The poll loop's cadence and its single-writer access to `readings.db`.

## Requirements

### Requirement: Poll cadence
The poll loop SHALL write one row per probe to `readings.db` every 5 seconds.

#### Scenario: One tick
- **WHEN** a poll tick completes
- **THEN** `readings` holds one new row per probe, stamped with the tick's time

### Requirement: Single writer
The poll loop SHALL be the only process that opens `readings.db` for writing.

#### Scenario: A consumer opens the store
- **WHEN** ReefDash or DoseKeeper opens `readings.db`
- **THEN** the connection is read-only
