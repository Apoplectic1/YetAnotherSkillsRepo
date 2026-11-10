# docs-architecture-setup: delta for main-specs-strict-clean

## ADDED Requirements

### Requirement: A router block at release cadence goes to ROADMAP
The SETUP skill SHALL move a router block whose content changes at release cadence, such as
a status block naming the current release and the work in progress, to ROADMAP, since it
fails the stability test.

#### Scenario: A State block in the router
- **WHEN** the router carries a "State" block naming the release and what is in progress
- **THEN** the plan moves the block to ROADMAP for failing stability

### Requirement: Breadth at a container root counts every session beneath it
The SETUP skill SHALL count every session launched beneath a container root when it applies
the breadth test to that root's router, since the root's router loads in each of them.

#### Scenario: A gotcha one sub-project needs, in a container root's router
- **WHEN** a container root's router carries a gotcha that only one sub-project's sessions
  need
- **THEN** the plan counts every session launched under the container, and the block fails
  breadth
