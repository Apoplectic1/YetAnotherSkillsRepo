# whats-next: delta for journal-rollover

## ADDED Requirements

### Requirement: Open items are read from the live journal
The journal sweep row SHALL read the live `NOTEBOOK.md` (its "Open threads (carried at a
rollover)" section first) and `docs/`; a journal's rolled files (`NOTEBOOK/`) SHALL be treated
as frozen history whose open threads were carried at rollover, and SHALL NOT be swept for open
items, the coverage manifest noting them as not reached by design.

#### Scenario: A carried thread is listed, a rolled closed one is not
- **WHEN** the live file carries one open thread from a rolled entry and a rolled file holds
  an item a later live entry closed
- **THEN** the backlog lists the carried thread and not the closed item, and the manifest
  names the rolled files as not reached (carried at rollover)

**Status note (2026-09-26):** satisfied by baseline behavior, not by skill text. The RED probe
read the 18 KB live file only, listed the carried thread as a future-feature item, treated the
closed item as closed, and marked the rolled files "not reached, carry-forward invariant" in
the manifest; it noted the depth was its own call. Per the no-failure gate the skill text was
not changed; if a future run sweeps rolled files or lists a closed item, encode then.
