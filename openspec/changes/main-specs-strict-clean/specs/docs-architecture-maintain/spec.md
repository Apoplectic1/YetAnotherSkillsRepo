# docs-architecture-maintain: delta for main-specs-strict-clean

## ADDED Requirements

### Requirement: A held promotion under a ROADMAP halt follows the halt's terms
The MAINTAIN skill SHALL sequence a held promotion's landing by the terms of a halt the
project's ROADMAP states, not hold every promotion until the halt lifts: a halt that admits
documentation admits the landing after the split.

#### Scenario: A halt that admits documentation
- **WHEN** a promotion is held against an ARCHITECTURE past its budget, and ROADMAP states a
  halt under which only documentation and bench records change
- **THEN** the report holds the promotion (M14) and sequences its landing after the split,
  as documentation the halt permits
