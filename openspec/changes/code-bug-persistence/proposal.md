# code-bug-persistence — proposal

## Why

Code-bug findings from the doc skills currently die with the chat. AUDIT's `flag-code-bug`
(R4/R7) is report-only and "handed off (to the dev/diagnose flow and `whats-next`)" — but
nothing mandates the flags land on disk, so unless the user manually saves the run report,
the bugs are lost. MAINTAIN is worse: its schema (`graduate | keep | archive | prune-only`)
has no code-bug channel at all, so bug observations are out-of-schema improvisation. Field
RED: a MAINTAIN run on TSM (2026-07-26, separate session) surfaced real code bugs with no
sanctioned place to put them (NOTEBOOK 2026-07-26 entry).

User decision (2026-07-26): the doc system itself becomes the bug tracker — persistence into
the *target project's* own tiers, no fix-round orchestration inside the skills (honesty
posture: skills never edit code, never substitute for dev work).

## What Changes

- **AUDIT**: new rule — surviving (adjudicated) `flag-code-bug` / `revisit-plan` flags MUST
  be persisted to the target project's tiers in the apply step: one line each in
  ROADMAP § Open + full evidence in a dated `docs/YYYY-MM-DD-<skill>-report.md`. "Handed
  off" becomes "written down"; `whats-next` already sweeps both locations — zero new
  machinery.
- **MAINTAIN**: new rule(s) — an in-schema code-bug channel mirroring AUDIT R4/R7 (report-only
  `flag-code-bug`; a journal claim contradicted by code where the claim is a contract →
  the code is the suspect, never classify the journal entry as stale), plus the same
  persistence mandate for surviving flags.
- **No change to whats-next or SETUP** — whats-next already treats `flag-code-bug` outputs,
  ROADMAP open items, and dated journal docs as backlog sources; persistence feeds it for free.
- **Gate (iron law)**: field evidence alone does not ship text. Synthetic RED→GREEN on the
  TidePool fixture, extended with a new plant class (journal claim vs buggy code, plus a
  bugs-found-then-report-discarded persistence cell). New plants are not derived from TSM
  specifics, so no fixture poisoning.

## Capabilities

### New Capabilities

*(none)*

### Modified Capabilities

- `docs-architecture-audit`: apply step gains a persistence requirement — adjudicated
  report-only flags (code bugs, plan revisits) must land in the target project's ROADMAP
  § Open (one line each) and a dated `docs/` report before the run ends.
- `docs-architecture-maintain`: gains a report-only code-bug channel (mirror of AUDIT
  R4/R7 semantics inside MAINTAIN's flag schema) and the same persistence requirement for
  surviving flags.

## Impact

- `skills/docs-architecture-audit/SKILL.md` — one new appended rule ID (next free: R27) +
  procedure step 5 wording; word-count delta must stay within family precedent.
- `skills/docs-architecture-maintain/SKILL.md` — new appended rule IDs (next free: M12+) +
  flag-schema row + procedure step 4 wording.
- `harness/tidepool-fixture/` + `harness/catalog-tidepool.md` — new plant class + catalog
  entries; RED/GREEN reps per VERIFICATION.md.
- Rule IDs append-only per DOMAIN.md § Authoring conventions.
- Deploys with the next `dev` → `main` merge + `deploy.sh`.
