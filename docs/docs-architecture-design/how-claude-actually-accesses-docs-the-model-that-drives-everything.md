# docs-architecture-design: How Claude actually accesses docs — the model that drives everything (part of ../docs-architecture-design.md)

> One topic of `../docs-architecture-design.md`, split out on 2026-10-12 when the file passed its
> budget; the heading keeps its text, so "docs-architecture-design § How Claude actually accesses docs — the model that drives everything" resolves by grep over
> the file and `docs-architecture-design/`. The index is `../docs-architecture-design.md`.

## How Claude actually accesses docs — the model that drives everything

**Only three files auto-load into context each session** (verified from this session's
start-up context block):

- `~/.claude/CLAUDE.md` — global cross-project rules (genuinely global; does **not** move into
  the repo).
- `<project>/CLAUDE.md` — project orientation + gotchas. **The router.**
- `<memory>/MEMORY.md` — auto-memory; harness-fixed path, cannot be relocated into the tree.
  (In the WBPP survey session this was a ~1.3 KB delegating stub with no content worth
  moving; per-project contents vary — this repo's is a standing-findings index.)

Consequence: **everything else (ROADMAP, ARCHITECTURE, DOMAIN, VERIFICATION, NOTEBOOK,
docs/*, NOTICE.md) is pull-on-demand.** The agent finds those *only because CLAUDE.md
describes and routes to them.* CLAUDE.md is a router; the organization is "accessible" exactly
to the degree CLAUDE.md indexes every leaf. (This is why `NOTEBOOK.md`, absent from the
router, was effectively invisible — the bug that motivated this review.)

The agent's four access primitives and their costs:

| Primitive | Cost | Gives |
|---|---|---|
| Auto-load (CLAUDE.md, MEMORY.md) | paid **every session** | always-on context — must stay small + high-value |
| `Glob docs/*.md` | ~free | the **filename list** — a live table of contents *if names self-describe* |
| `Grep` across docs | ~free | content search — file+line for a keyword without reading |
| `Read` w/ offset | cheap if sliced | one section, *if* the agent knows which |

**Key inference:** a hand-maintained manifest file (a `DOCS.md`) is just a drift-prone cache
of what `Glob` + `Grep` already compute live. The most automatic, always-current manifest is
**no manifest** — a self-describing file tree the agent's free tools read directly.

Two access patterns, wanting opposite structures:

- **Retrieval** ("I know the topic, where's the fact?") → served by many small, well-named,
  greppable files. Fragmentation *helps*.
- **Synthesis** ("what do I need to know about subsystem X?") → served by one consolidated
  narrative. Fragmentation *hurts*, and worse: a pile of dated files leaves the agent unable
  to tell **stale from current** cheaply. This is "detail/nuance lost in a plethora of
  files," stated mechanically.

