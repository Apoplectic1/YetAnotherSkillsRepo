# DOMAIN.md — DoseKeeper

**Charter:** dosing + safety conventions.

## Vocabulary
- **Salinity event** — canonical definition lives in ReefDash's `DOMAIN.md`
  (`../ReefDash/DOMAIN.md`); dosing locks out for the event's duration plus 30 min.
- **Lockout** — any condition that blocks the dose queue (event, quiet window, manual).

## Safety conventions
- Never dose during a lockout; the queue holds, never drops.
