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

- **Why — the meta-goal** (`docs-architecture-design/why-the-meta-goal.md`, 0.5 KB): The objective the skills serve: every fact the agent acts on current, single-sourced and legibly so, with AI access first; structure is in service of that.
- **How Claude actually accesses docs — the model that drives everything** (`docs-architecture-design/how-claude-actually-accesses-docs-the-model-that-drives-everything.md`, 2.5 KB): The chain of files that auto-loads each session versus everything pulled on demand through the router; the agent's four access primitives and their costs (auto-load, `Glob`, `Grep`, a sliced `Read`); why no manifest file; retrieval versus synthesis and the structure each wants.
- **The doc tiers: journal · reference · cold rationale** (`docs-architecture-design/the-doc-tiers-journal-reference-cold-rationale.md`, 3.1 KB): The three tiers (journal: dated records, `NOTEBOOK.md`, `CHANGELOG.md` and their overflow directories; reference: the four topic docs edited in place; cold rationale), graduation with prune between them, and the extract discriminator for what may move to a cold doc.
- **The index that auto-scales — convention-routing, not enumeration** (`docs-architecture-design/the-index-that-auto-scales-convention-routing-not-enumeration.md`, 1.3 KB): How the router names the stable reference docs one by one but routes the growing journal by convention (one `glob docs/*.md` line, never a list), why there is no `DOCS.md`, and the filename and first-line conventions that make grep triage cheap.
- **Per-doc charters — the placement test** (`docs-architecture-design/per-doc-charters-the-placement-test.md`, 1.1 KB): Why a one-line charter per doc makes placement auditable, with WBPP's charter table as the worked instance (router, ROADMAP, ARCHITECTURE, DOMAIN, VERIFICATION, NOTEBOOK, `docs/`, a vendor fork's playbook, the memory stub).
- **Anti-staleness design principles** (`docs-architecture-design/anti-staleness-design-principles.md`, 7.6 KB): Staleness danger as always-on times duplicated times volatile, and the five antidotes in order; the `archive/` convention; `CHANGELOG.md` for shipped history; the journal rollover and the reference-doc split in brief, with why a split index's line is written and checked; OpenSpec as workflow only.
- **Decisions locked** (`docs-architecture-design/decisions-locked.md`, 0.9 KB): The decisions settled at the start: the router, the three tiers with graduation and prune, journal routing by convention with no `DOCS.md`, the always-on lean, OpenSpec as workflow only (qualified for router-named specs), the global file and memory stub left in place.
- **The phased arc** (`docs-architecture-design/the-phased-arc.md`, 34.1 KB): The three phases (structure, audit, skillify), then the dated build and validation record of every skill since: each RED/GREEN result, the AUDIT worker-model benchmark and its tier advice, the fix batches, the hybrid-rulebook rewrite, and the 2026-07 changes (archive awareness, code-bug persistence, B4, right-sizing).
- **SETUP-skill spec (Phase 3 design — grounded in target projects)** (`docs-architecture-design/setup-skill-spec.md`, 7.9 KB): The 2026-06-28 survey the setup skill was grounded in, the enforced filename set and which members are conditional, the scope-exclusion list and router-anchored scope, sub-projects versus vendored trees, coexist-never-clobber, charter-guarded thin files, and the design-heavy project's DESIGN slot.
- **Journal rollover: 2026-09-26** (`docs-architecture-design/journal-rollover-2026-09-26.md`, 0.8 KB): The rollover's provenance: derived on the HDL tree, validated RED and GREEN on TidePool's `big-journal` variant, with pointers to its record and its archived change.
- **Scope from the routers: 2026-10-12** (`docs-architecture-design/scope-from-the-routers-2026-10-12.md`, 1.0 KB): AUDIT's scope taken from the routers: a router-named spec is reference for currency and never edited, its stale claim the report-only `spec-change`; the two no-failed halves held as status notes; provenance and pointers.
- **Always-on budget: 2026-10-12** (`docs-architecture-design/always-on-budget-2026-10-12.md`, 4.4 KB): What a session pays at launch (the chain, measured), the three-term cost model, the breadth and stability test for an always-on item and the on-demand homes with their load triggers, `chain_budget.py`, and the HDL pilot's field fixes (the per-file line budget).
- **Open / still to decide** (`docs-architecture-design/open-still-to-decide.md`, 0.7 KB): The original open questions, all resolved by execution on 2026-07-07; nothing is open.
- **Tools over prose: 2026-10-12** (`docs-architecture-design/tools-over-prose-2026-10-12.md`, 3.6 KB): The shift to detection in scripts and judgment in prose: why the skill text was trimmed, what `survey.py`, `scope.py` and `sweep.py` each print, the sizes before and after, and the regression gate a trim ships under.
