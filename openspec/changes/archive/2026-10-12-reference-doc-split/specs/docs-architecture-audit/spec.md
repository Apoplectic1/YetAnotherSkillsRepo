# docs-architecture-audit: delta for reference-doc-split

## ADDED Requirements

### Requirement: A split reference doc's parts are in scope and its section citations resolve
The audit's in-scope set SHALL include the parts a split reference doc's index names
(`<DOC>/<topic>.md`), each audited as the same tier and charter as its index, and the
cross-reference pass SHALL resolve a section citation ("ARCHITECTURE § Build chain") in the
doc or in its split directory, as a dated citation resolves in a journal's overflow
directory.

#### Scenario: A part is currency-audited
- **WHEN** an audit runs on a project whose ARCHITECTURE has been split and a part states a
  value the code has moved past
- **THEN** a currency flag is emitted for the part as for any reference doc

#### Scenario: A section citation into a part resolves
- **WHEN** a doc cites "ARCHITECTURE § Build chain" and that section now lives in
  `ARCHITECTURE/build-chain.md`
- **THEN** the cross-reference pass does not report the citation as dangling
