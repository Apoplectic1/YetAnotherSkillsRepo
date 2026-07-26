# Design: openspec-archive-awareness

## Context

The docs-architecture family treats `openspec/` as tooling: setup B1 excludes it from
scaffolding and writes that exclusion into the router; audit R13 default-excludes it; maintain's
source list (journal `docs/` + `NOTEBOOK.md`) never mentions it. That posture was deliberate
(2026-07-17 decision: openspec is quiescent at skill runtime — changes are archived before doc
skills run, specs stay synced by construction) and remains correct for `openspec/specs/` and
in-flight `openspec/changes/*`.

The gap is the **archive**: `openspec/changes/archive/<id>/design.md` is where opsx parks the
rationale for shipped decisions. Once a change archives, no skill ever reads it again — audit's
flag schema requires a `claim:` and absence makes no claim; maintain doesn't source it;
whats-next only sweeps in-flight work. Hardened rationale (why a constraint exists, why a
fallback was removed) silently exits the doc system. Today the user closes this manually at
archive time; on less-attended projects it just leaks.

## Goals / Non-Goals

**Goals:**
- Give archived `design.md` rationale a recurring promotion path into the reference tier
  (maintain), so nothing depends on remembering at archive time.
- Make audit safe around the cross-refs maintain will create (no misfires, no edits to the
  immutable archive).
- Keep the router's exclusion wording from contradicting maintain's new source class (setup).

**Non-Goals:**
- No audit completeness axis ("a fact that should be documented isn't" is unbounded; the flag
  schema rightly requires a claim).
- No scaffolding into `openspec/` (B1 stands), no reading of in-flight changes beyond
  whats-next's existing sweep, no changes to whats-next.
- No T1 change in setup — T1 is *authoring* guidance and archived `design.md` is never an
  authoring target; maintain's source rule is the sole home for "what maintain reads."
- No `openspec update`-managed file edits (`.claude/skills/openspec-*`,
  `.claude/commands/opsx/*`) — tool-owned, overwritten on update.

## Decisions

### D1 — maintain carries the change; the disposition is pinned to `cross-ref`

Archived `openspec/changes/archive/*/design.md` becomes a maintain **source class**, classified
per M1–M4 like any journal item. The linchpin (M5–M7) requires a source-disposition on every
graduate, and **all three existing dispositions edit or relocate the source** — applied to an
openspec archive they would corrupt the immutable change record. So the rule pins the
disposition: **`cross-ref`-only, and the pointer prose lives in the *reference doc*** (the
graduated truth cites the archived design.md as its evidence), never as an edit to the archive.
`stub` and `archive` are forbidden for this source class.

The rule also carries an **override clause**: a router's generic `openspec/` exclusion note
does not exempt this source. Without it, every *existing* project's router (written under the
old blanket wording) could nudge a worker into skipping the archive — and "manually edit N
routers" is exactly the remembered obligation the skill-rule approach exists to eliminate. One
sentence in the skill text makes the net deployment-free across old and new projects alike.

*Alternatives rejected:* convention-at-archive-time (requires remembering once, at exactly the
right moment, forever, per project — a skill rule requires remembering nothing and catches the
miss on any later sweep); editing the opsx archive skill (tool-generated, `openspec update`
overwrites it, per-project not portable).

### D2 — audit gets two scope clarifications, not a new axis

1. **R14 disambiguation:** the never-currency-audited journal set explicitly includes
   `openspec/changes/archive/`. Generic "`archive/`" is worker-ambiguous; undecided ambiguity in
   a fan-out yields inconsistent flags.
2. **R15 carve-out:** when a reference doc cites an archived `design.md` (exactly the
   cross-refs D1 creates), the check is **decision-consistency only** — does the reasoning
   still support the decision? Tier-violation flags for code-coupled facts are **suppressed**:
   an openspec design doc is dense with code-coupled facts *by design* and is immutable
   history, so R15's normal "code-coupled fact in a cold doc = misplacement" logic would emit a
   pile of unactionable flags on a file audit must never edit (R3/R17-style read-only).

*Alternative rejected:* completeness axis (see Non-Goals).

### D3 — setup gets one clause, not a B1 restructure

B1's router-exclusion wording gains a carve-out clause: `openspec/` remains excluded from
scaffolding, and the router's exclusion note reads approximately "…tooling (`.claude/`,
`openspec/` — archived `changes/archive/*/design.md` are historical records the maintain sweep
reads)." Rationale: maintain's scope is defined by its own skill rules, not the router — and D1's
override clause already makes the sweep robust against old wording. The setup clause is
therefore *hygiene*, not protection: routers setup writes or aligns going forward carry
wording consistent with the convention, and existing routers heal lazily (next setup run or
any doc pass that touches them) rather than requiring a per-project edit. Splitting B1 or
touching T1 is over-engineering (see Non-Goals).

### D4 — land as one change; sequencing is a coherence preference, not a dependency

The R15 misfire needs both maintain's cross-refs to exist *and* audit to run before its
carve-out lands. Landing together closes that window; it is not a hard ordering constraint.

### D5 — RED/GREEN on the two behavior-bearing edits; wording-only edits skip the harness

- **maintain graduate path (RED):** fixture with an archived design.md holding graduable
  rationale; does an unguided/current-skill run either miss the source entirely or apply
  `stub`/`archive` to the archive? GREEN: candidate text sources it and pins `cross-ref`.
- **audit R15 path (RED):** fixture where ARCHITECTURE.md cites an archived design.md dense
  with code-coupled facts; does the current skill emit tier-violation flags on it? GREEN:
  candidate text yields decision-consistency check only.
- Setup's B1 clause and audit's R14 wording are scope-vocabulary edits with no behavioral
  fork worth a fixture run — per the house no-failure gate, encode without a harness pass and
  let a future failing run justify more.

Per house convention the fixture is created on demand (`VERIFICATION.md`), and its reset
contract (`git clean -fd`) applies after every mutating run.

## Risks / Trade-offs

- [Skill bloat — maintain is the leanest skill] → one rule (source class + pinned
  disposition), no procedural additions; audit adds clauses to two existing rules rather than
  new rules.
- [Rule fires on projects without openspec] → source class is conditional by construction
  (glob finds nothing → no-op), same graceful degradation as whats-next's change-tool row.
- [Workers still edit the archive despite the pin] → that is precisely the RED assertion for
  maintain; if RED passes without explicit text, the no-failure gate says don't add it.
- [Suppressed tier-violations hide genuinely misplaced *current* truth parked in an archived
  design.md] → accepted: the graduate path (D1) is the correct surfacing mechanism for that
  content, not a misplacement flag on an immutable file.
- [Deployed-footer contract] → `docs/docs-architecture-design.md` is edited in place; no
  rename/move (every shipped footer links it by URL).

## Migration Plan

None — per house rule, no back-compat: skills deploy atomically via `deploy.sh` from `main`;
consumers re-run the skill fresh. Rollback = revert commit + redeploy.

## Open Questions

- None blocking. (Whether `proposal.md`/`specs/` in the archive ever deserve the same source
  treatment is deferred — design.md is where rationale concentrates; extend later if a real
  miss shows up.)
