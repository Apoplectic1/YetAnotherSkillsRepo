# docs-architecture-design: Per-doc charters — the placement test (part of ../docs-architecture-design.md)

> One topic of `../docs-architecture-design.md`, split out on 2026-10-12 when the file passed its
> budget; the heading keeps its text, so "docs-architecture-design § Per-doc charters — the placement test" resolves by grep over
> the file and `docs-architecture-design/`. The index is `../docs-architecture-design.md`.

## Per-doc charters — the placement test

A one-line charter per reference doc makes the Phase 2 audit objective (does this section
match its doc's charter? else move / cross-ref-and-delete). The table is **WBPP's instance**
(the grounding worked example — charters are per-project; the general roles live in the
table in § SETUP-skill spec):

| Doc | Charter |
|---|---|
| `CLAUDE.md` | always-on **router** + load-bearing gotchas only (no volatile content) |
| `ROADMAP.md` | feature-architecture · constant-rename table · validation matrix · *(port history → archive/)* |
| `ARCHITECTURE.md` | subsystem mechanics deep-dives (how it works) |
| `DOMAIN.md` | domain/strategy home — site · targets · workflow · tuning · contracts · repo conventions (WBPP's is historically `OBSERVING.md`) |
| `VERIFICATION.md` | run-verification runbook |
| `NOTEBOOK.md` | dated empirical findings (journal / lab notebook) |
| `docs/` | dated decision records, reviews & **cold-rationale** notes (journal + tier-3) |
| `nsg-v8-fork/NOTICE.md` | vendor fork playbook (patches, re-fork procedure) |
| `MEMORY.md` | stub delegating to repo docs (leave; cannot move) |

