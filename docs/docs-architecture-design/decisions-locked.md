# docs-architecture-design: Decisions locked (part of ../docs-architecture-design.md)

> One topic of `../docs-architecture-design.md`, split out on 2026-10-12 when the file passed its
> budget; the heading keeps its text, so "docs-architecture-design § Decisions locked" resolves by grep over
> the file and `docs-architecture-design/`. The index is `../docs-architecture-design.md`.

## Decisions locked

- CLAUDE.md = router; three-tier (journal → reference · cold rationale, refined from two
  2026-06-28: see § The doc tiers: journal · reference · cold rationale) + graduation/prune workflow adopted.
- Convention-routing for the journal; enumerate-by-name only the stable reference set; **no
  DOCS.md**. Purpose/use-centric router lines.
- Always-on lean: agent will propose cuts to CLAUDE.md (volatile detail down, routing +
  load-bearing gotchas stay).
- OpenSpec = workflow-only. graphify dropped. `archive/` adopted. *(Qualified 2026-10-12,
  change `audit-scope-from-routers`: a spec the router names as the project's rules is
  reference-tier for AUDIT's currency pass, never an edit target; its stale claim is the
  report-only `spec-change`.)*
- Global `~/.claude/CLAUDE.md` and the memory stub stay put (not project-specific / harness-fixed).

