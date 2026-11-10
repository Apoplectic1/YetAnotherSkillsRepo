# docs-architecture-setup: delta for main-specs-strict-clean

## ADDED Requirements

### Requirement: A router block a reference doc already holds is dropped with a cross-reference
The SETUP skill SHALL drop a router block whose content a reference doc already holds,
leaving a cross-reference to that doc (S1's merge), rather than move a second copy of it into
the reference doc.

#### Scenario: A duplicated module map
- **WHEN** the router carries a copy of the module map that ARCHITECTURE already holds
- **THEN** the plan deletes the router's copy and leaves a cross-reference to ARCHITECTURE,
  and ARCHITECTURE gains nothing

### Requirement: A router block at release cadence goes to ROADMAP
The SETUP skill SHALL move a router block whose content changes at release cadence, such as
a status block naming the current release and the work in progress, to ROADMAP, since it
fails the stability test.

#### Scenario: A State block in the router
- **WHEN** the router carries a "State" block naming the release and what is in progress
- **THEN** the plan moves the block to ROADMAP for failing stability

### Requirement: A halt the ROADMAP states bounds the plan
The SETUP skill SHALL bound its plan to what a halt stated in the project's ROADMAP permits,
and say so; under a halt that admits only documentation, the plan's moves are documentation
moves.

#### Scenario: A documentation-only halt
- **WHEN** ROADMAP states that only documentation changes until the halt lifts
- **THEN** the plan proposes documentation moves only and names the halt as its bound

### Requirement: Breadth at a container root counts every session beneath it
The SETUP skill SHALL count every session launched beneath a container root when it applies
the breadth test to that root's router, since the root's router loads in each of them.

#### Scenario: A gotcha one sub-project needs, in a container root's router
- **WHEN** a container root's router carries a gotcha that only one sub-project's sessions
  need
- **THEN** the plan counts every session launched under the container, and the block fails
  breadth
