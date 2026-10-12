# Docs-architecture skill family — design & spec (canonical)

**Canonical design** for the global docs-architecture skills (SETUP · AUDIT · MAINTAIN ·
TRIAGE), maintained here in `E:\Projects\AI\Skills\doc-architecture`. The goal these skills serve: make an AI
agent's work in any project trustworthy — every fact current, single-sourced, and accessible
**token-efficiently, without being pointed at files**.

**Genesis / worked example:** derived by reorganizing the WBPP project's docs (2026-06-28 —
"Phase 1" structure + "Phase 2" audit). The WBPP-specific *execution* record stays in WBPP;
the WBPP examples kept below are the grounding worked-example.

> **Note (2026-06-28):** graduated out of WBPP `docs/2026-06-28-docs-reorg-plan.md` — that copy
> was removed same-day (WBPP `1bd0e68`; git is the backstop); **this** file is canonical. The WBPP-first "Phase 1/2 executed"
> framing below is retained as the grounding worked-example (all four skills are now authored —
> nothing pending behind that framing).

> **Status:** Phases 1 & 2 **executed 2026-06-28**. Phase 1 (structure, `docs-reorg-phase1`) —
> CLAUDE.md router + always-on lean (20→14 KB), ROADMAP port-history → `archive/`, per-doc
> charters. Phase 2 (content/currency audit, `docs-reorg-phase2-audit`) — 41 flags adjudicated
> & applied across the live reference tier (currency fixes, single-source relocations, GPU +
> correspondence → archive/design-doc). **Phase 3 (skillify) completed 2026-06-28** (family-complete + fix-batch records below). This note
> follows the conventions it proposes (dated journal entry, purpose-first header, cross-refs)
> — dog-fooding the model.

---

Split (since 2026-10-12): past 40 KB this doc's `##` topics live in `docs-architecture-design/`, one
file per topic named by its heading, and this file is the index. A section citation
("docs-architecture-design § <heading>") resolves by `grep -n "<heading>" docs-architecture-design.md docs-architecture-design/*.md`.

## Parts

- **Why — the meta-goal** (`docs-architecture-design/why-the-meta-goal.md`, 0.5 KB): The overriding objective is **not** "tidy the docs." It is to **make current work
- **How Claude actually accesses docs — the model that drives everything** (`docs-architecture-design/how-claude-actually-accesses-docs-the-model-that-drives-everything.md`, 2.5 KB): **A chain of files auto-loads into context each session** (three when this was first
- **The doc tiers: journal · reference · cold rationale** (`docs-architecture-design/the-doc-tiers-journal-reference-cold-rationale.md`, 3.1 KB): Resolves the two-patterns tension.
- **The index that auto-scales — convention-routing, not enumeration** (`docs-architecture-design/the-index-that-auto-scales-convention-routing-not-enumeration.md`, 1.3 KB): CLAUDE.md routes the two tiers **differently**, and that asymmetry is the whole trick:
- **Per-doc charters — the placement test** (`docs-architecture-design/per-doc-charters-the-placement-test.md`, 1.1 KB): A one-line charter per reference doc makes the Phase 2 audit objective (does this section
- **Anti-staleness design principles** (`docs-architecture-design/anti-staleness-design-principles.md`, 6.6 KB): Staleness danger scales as **(how always-on) × (how duplicated) × (how volatile / code-coupled)**.
- **Decisions locked** (`docs-architecture-design/decisions-locked.md`, 0.9 KB): CLAUDE.md = router; three-tier (journal → reference · cold rationale, refined from two
- **The phased arc** (`docs-architecture-design/the-phased-arc.md`, 34.1 KB): Sequencing rationale: Phase 1 enables Phase 2 (charters make the audit objective) *and*
- **SETUP-skill spec (Phase 3 design — grounded in target projects)** (`docs-architecture-design/setup-skill-spec.md`, 7.9 KB): Grounded 2026-06-28 in a survey of the projects the skills will first run on (sibling C#/.NET
- **Journal rollover: 2026-09-26** (`docs-architecture-design/journal-rollover-2026-09-26.md`, 0.8 KB): The journal tier's growth got a mechanism: rollover by date into a directory named for the
- **Scope from the routers: 2026-10-12** (`docs-architecture-design/scope-from-the-routers-2026-10-12.md`, 1.0 KB): AUDIT's scope follows the routers rather than directories or names: a router-named spec is
- **Always-on budget: 2026-10-12** (`docs-architecture-design/always-on-budget-2026-10-12.md`, 4.4 KB): The 40 KB gate was the harness's per-file warning applied to one file: the right budget at
- **Open / still to decide** (`docs-architecture-design/open-still-to-decide.md`, 0.7 KB): *(All three original opens resolved by execution — closed 2026-07-07, resolutions inline.)*
