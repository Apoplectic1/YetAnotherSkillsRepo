# Proposal: openspec-archive-awareness

## Why

On opsx-driven projects (now all of this user's projects), the *why* behind a shipped change
lands in `openspec/changes/archive/<id>/design.md` — and no skill in the docs-architecture
family can ever surface it again: maintain doesn't list it as a source, audit excludes
`openspec/` and would misfire on it if cited, setup's router wording brands the whole tree
"tooling — excluded." Hardened rationale silently dies in the archive, and the failure mode is
exactly the one the reference tier exists to prevent: a later agent re-adds a deliberately
removed thing because nothing it reads says "removed on purpose, here's why."

## What Changes

- **maintain** (center of gravity): archived `openspec/changes/archive/*/design.md` becomes a
  journal-tier **source class** for the graduate sweep, with the source-disposition **pinned to
  `cross-ref`-only** — the archive is an immutable change record; `stub` (edit source) and
  `archive` (relocate source) must never touch it.
- **audit** (two scope clarifications, no new axis):
  - `openspec/changes/archive/` is unambiguously archive-tier — never currency-audited
    (resolves the R14 ambiguity where generic `archive/` may or may not match it).
  - When a reference doc cites an archived `design.md` (the cross-refs maintain creates), the
    R15 cold-rationale check applies as **decision-consistency only**: tier-violation flags for
    code-coupled facts are **suppressed** (an openspec design doc is dense with code-coupled
    facts by design and is immutable history), and the file is never edited.
- **setup** (one clause): B1's router-exclusion wording gains the carve-out — `openspec/`
  stays excluded from scaffolding, but the router notes archived `design.md` files as
  historical records the maintain sweep reads.
- **whats-next**: untouched — it already sweeps in-flight `openspec/` changes; surfacing
  un-graduated archived rationale is maintain's job.
- RED/GREEN harness coverage on the two behavior-bearing edits: maintain's graduate path
  (disposition pinning) and audit's R15 behavior on archived design docs.

## Capabilities

### New Capabilities
- `docs-architecture-maintain`: no spec exists for the MAINTAIN skill yet; this change creates
  it covering only the new requirement — archived openspec design docs as a graduate source
  with `cross-ref`-only disposition (per house convention: not a retroactive full spec).

### Modified Capabilities
- `docs-architecture-audit`: the cold-rationale decision-consistency requirement gains an
  archived-openspec-design-doc carve-out (consistency check yes, tier-violation flags
  suppressed, never edited); the journal-tier set gains `openspec/changes/archive/`.
- `docs-architecture-setup`: the scope-exclusion requirement's router wording gains the
  archived-`design.md` carve-out clause.

## Impact

- `skills/docs-architecture-maintain/SKILL.md` — new source-class rule + pinned disposition.
- `skills/docs-architecture-audit/SKILL.md` — R14 wording, R15 carve-out.
- `skills/docs-architecture-setup/SKILL.md` — B1 clause.
- `docs/docs-architecture-design.md` — canonical design records the rationale (footer-linked
  from every deployed skill; edit in place, no rename/move).
- RED/GREEN fixture runs (`harness/`, `VERIFICATION.md` contract) for maintain + audit edits.
- Deploy via `deploy.sh` from `main` after merge; authored on `dev`.
