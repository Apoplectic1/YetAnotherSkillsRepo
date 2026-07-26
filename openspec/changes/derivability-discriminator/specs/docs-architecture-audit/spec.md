# docs-architecture-audit — delta: derivability-discriminator

## ADDED Requirements

### Requirement: Fix-or-delete discriminator on derivable claims
The AUDIT skill SHALL apply a derivability discriminator to currency `fix-doc` flags: when
the stale claim is both cheaply derivable from code (one grep/read re-derives it — a count,
a version, an enumerated list) AND carries no rationale, contract force, or gotcha weight,
the flag's proposed fix SHALL lead with removing the claim or rewording it without the
perishable value (keeping the durable statement), offering the value-update as the stated
alternative for adjudication. Claims with rationale attached, contract guarantees (R7
territory), or gotcha weight are outside the discriminator — they get a normal fix. The
discriminator changes only the proposed fix-shape; flagging, evidence, and
adjudicate-before-apply are unchanged. Gated on RED→GREEN per the iron law (no-failure →
status-note only).

#### Scenario: Stale rationale-free count
- **WHEN** a reference doc says "ships with 12 curated stations", code shows 18, and no
  rationale or guarantee attaches to the number
- **THEN** the flag proposes removing/de-valuing the count (e.g. "a curated station
  registry") with "update to 18" as the alternative, and the user adjudicates

#### Scenario: Rationale-bearing number is not deletion-proposed
- **WHEN** a stale value is load-bearing for a stated why (a threshold with its rationale, a
  benchmark figure justifying a recommendation) or asserts a guarantee
- **THEN** no deletion proposal is made — the flag takes the normal fix path (or R7 if a
  contract is violated)

#### Scenario: Live-section control preserved
- **WHEN** the discriminator applies to a claim in a live (non-history) section
- **THEN** the claim is still flagged with evidence as before — the discriminator alters
  the proposed fix, never suppresses the flag
