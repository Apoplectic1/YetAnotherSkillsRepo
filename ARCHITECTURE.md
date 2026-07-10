# ARCHITECTURE.md — how this project works

**Charter:** subsystem mechanics — repo layout, the skill family's structure, and the
dev→deploy pipeline. Read before changing structure or adding a skill. The full design
rationale (tier model, anti-staleness principles, RED/GREEN provenance) is the canonical
design doc: `docs/docs-architecture-design.md`.

## Layout
- `skills/<name>/SKILL.md` — one directory per skill; the SKILL.md *is* the product.
- `docs/` — journal (dated records) + the canonical design doc + benchmark data
  (`docs/audit-benchmark/` — scripts, sweeps, raw workflow outputs behind the 2026-06-29 note).
- `deploy.sh` — copies `skills/*/` → `~/.claude/skills/`, marker-stamps each copy, prunes
  family-stale deployed dirs (see `RELEASING.md`).
- `openspec/`, `.claude/` — tooling, excluded from the doc set.

## The skill family (all 4 built + deployed)
A 3-tier doc model (journal · reference · cold-rationale) + 4 skills, built in order:
1. **SETUP** — bootstraps the doc skeleton (enforced filename set, charter-guarded) + the
   CLAUDE.md router + conventions in any project. (Generalizes WBPP Phase 1.) RED/GREEN-validated.
2. **AUDIT** — placement (vs charter) + currency (vs live code) via a structured-schema
   fan-out + cross-ref pass + loop-until-dry; evidence-carrying flags → adjudicate → fix.
   (Generalizes WBPP Phase 2.) RED/GREEN-validated.
3. **MAINTAIN** — graduate journal → reference + prune-the-source (preserve the why/when);
   reuses AUDIT's fan-out. (Generalizes WBPP graduate/prune.) RED/GREEN-validated.
4. **TRIAGE** (`whats-next`) — sweep every backlog source → categorized/prioritized backlog +
   coverage manifest + accepted-constraints list; live-vs-accepted crux; reuses AUDIT's
   fan-out. (Planning layer; consumes the trio's outputs.) RED/GREEN-validated.

**Dependency:** AUDIT, MAINTAIN, and TRIAGE assume the docs-architecture conventions are
already in place (a CLAUDE.md router + charter'd reference set) — **SETUP must have run
first**. On a raw project run SETUP before the other three. `whats-next` composes after
AUDIT when doc currency is in doubt — a stale reference tier yields a stale backlog.

## Pipeline
Author here (version-controlled) → validate via the RED/GREEN subagent harness (see
`VERIFICATION.md`) → merge `dev` → `main` → `deploy.sh` copies to `~/.claude/skills/`, the
live harness location (deploy mechanics + the never-edit-the-deployed-copy rule:
`RELEASING.md`). Genesis: the WBPP docs-reorg, 2026-06-28 — full record in
`docs/docs-architecture-design.md`.
