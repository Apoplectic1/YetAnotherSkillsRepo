# docs-architecture-maintain — delta: maintain-right-sizing

## ADDED Requirements

### Requirement: Sweep report carries a required prune/growth accounting slot
The dated maintain report SHALL end with a required accounting slot: the prune/archive
candidates found this sweep — or the explicit line "prune candidates: none found" — and a
one-line net reference-tier delta (what the run added to reference docs vs removed or
struck). Silence is not a legal value for either element. No numeric graduation cap is
imposed, and MAINTAIN gains no reference-tier deletion authority (that remains AUDIT's
job). Gating record: the net-delta line was absent in the synthetic RED rep (and in every
prior field/fixture report); ad-hoc prune listings existed but were uncontracted.

#### Scenario: Nothing to prune is stated, not silent
- **WHEN** a sweep finds no prune/archive candidates
- **THEN** the report's accounting slot states "prune candidates: none found" explicitly

#### Scenario: Ratchet visible per run
- **WHEN** any sweep completes
- **THEN** the report states in one line what the run added to the reference tier vs what
  it removed or struck, so add:remove is visible without diffing

#### Scenario: Candidates found are listed in the slot
- **WHEN** the sweep prunes or archives items
- **THEN** they are listed in the accounting slot (not only scattered through prose)

## Gating notes (no-failure outcomes, per the iron law)

Two proposed halves passed RED and ship **no text** (status-noted here per the 2026-07-07
precedent):
- **Trigger-based description rewording** — invocation probes 0/2: agents under the
  *current* description already declined a low-yield sweep (2 h after the last, one change
  since), reasoning "too soon to count as periodic." The TSM double-run remains field-only
  evidence; DOMAIN § When-to-reach carries the trigger guidance doc-side.
- **Mandatory dedicated prune pass** — the RED rep found and correctly handled both planted
  prune cells (PR1 struck with a candid scope note, PR2 archived) without a forced pass;
  findability did not fail at fixture scale. The accounting slot's "none found" contract
  supplies the search pressure without an unproven mandate.
