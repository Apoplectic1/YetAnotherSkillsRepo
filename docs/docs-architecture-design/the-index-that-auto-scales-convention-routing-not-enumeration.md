# docs-architecture-design: The index that auto-scales — convention-routing, not enumeration (part of ../docs-architecture-design.md)

> One topic of `../docs-architecture-design.md`, split out on 2026-10-12 when the file passed its
> budget; the heading keeps its text, so "docs-architecture-design § The index that auto-scales — convention-routing, not enumeration" resolves by grep over
> the file and `docs-architecture-design/`. The index is `../docs-architecture-design.md`.

## The index that auto-scales — convention-routing, not enumeration

CLAUDE.md routes the two tiers **differently**, and that asymmetry is the whole trick:

- **Reference docs → enumerate by name.** ~5 docs, stable, rarely added. A few router lines.
  Manual enumeration is fine *because the set doesn't grow* (graduation consolidates, it
  doesn't multiply).
- **Journal → route by convention, never list.** One drift-proof line, e.g.: *"`docs/` holds
  dated decision records & reviews — `glob docs/*.md` for the current list (filenames are
  self-describing), grep for content; standing truths graduate into the reference docs
  above."* Add 50 files and that line is still accurate. (Enumerating a *growing* set is the
  anti-pattern that orphaned NOTEBOOK.)

No `DOCS.md`. Router lines are **purpose/use-centric** ("what it's for / when to read / what
to grep") — the high-signal form for both a human skimming and the agent routing.

Two cheap conventions make the free tools sing (the docs/ entries already do both):
1. **Self-describing filenames:** `2026-06-28-nsg-drizzle-ordering.md`, not `notes3.md`.
2. **First line `# <date> — <purpose>` + a one-sentence "what this is / when to read"** — so
   the agent can `Read` line 1 only of each grep hit to triage.

