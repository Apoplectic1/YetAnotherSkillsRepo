# ReefStack ground-truth catalog — portfolio container fixture

For the `b4-portfolio-domain` RED/GREEN rounds. Kept OUTSIDE the fixture (poisoned-fixture
rule). Fixture: `harness/reefstack-fixture/` — a fictional reef-tank automation portfolio:
container root (router + thin status ROADMAP + scripts/) over three routered sub-projects
(PulseMonitor — owns `readings.db` via `SCHEMA.md`; ReefDash; DoseKeeper). Sub-projects
carry routers but no nested `.git` (B3 qualifies on router alone; nested gits would break
copy resets). Per-run: copy fixture → `git init` → baseline marker commit; reset contract
as usual. Non-derived: built fresh for this change; the Astronomy container and TSM are
the deriving evidence and are poisoned for validating this rule.

## Planted cells

| ID | Where | Plant | Expected — RED (current text) | Expected — GREEN (B4′ + M15 candidate) |
|---|---|---|---|---|
| PC1 | Root `CLAUDE.md` § Data contracts | Genuine cross-repo reference prose: readings.db ownership/contract detail, the two-stores-named-`config.db` disambiguation, the Quiet-window shared convention | S7↔B4 collision, divergent improvisation (probe signature): prose → root ROADMAP, or kept-as-"gotcha", or scattered per-project; capture each rep's resolution verbatim | Thin portfolio `DOMAIN.md` created at the container root, chartered *cross-repo truth only*; config.db disambiguation + quiet-window convention move there; router keeps at most one-line gotchas + pointer |
| PC2 | readings.db detail inside PC1's block vs `PulseMonitor/SCHEMA.md` (owner) | Owned contract duplicated in the root router | — | Owner rule honored: portfolio DOMAIN (and router) point **down** to `PulseMonitor/SCHEMA.md` by name; the WAL/table detail is NOT duplicated up. Duplicating it = fail |
| PC3 | Container root file set | — | Record what reps scaffold | No portfolio ARCHITECTURE / NOTEBOOK / VERIFICATION / docs/ / CHANGELOG; the existing thin status ROADMAP stays (legalized). Scaffolding the set = fail |
| PC4 | SETUP run from `ReefDash/` alone (single-project control) | — | — | No portfolio DOMAIN is created anywhere; the amendment changes container behavior only. Creating one = over-fire, fail |
| PL1 | `ReefDash/NOTEBOOK.md` 2026-07-18 — decided portfolio-wide "salinity event" definition ("spans all three apps... no obvious home in this repo's docs") | Portfolio-level graduate, **no portfolio DOMAIN present** | MAINTAIN improvises: graduates into ReefDash DOMAIN (feeding the L1 loop), writes a cross-repo pointer into a sibling, or hedges — capture verbatim | **Flag-and-ask**: presented for user placement with its portfolio-level classification; no sibling-repo writes; entry keeps its why/when |
| PL2 | Same graduate, portfolio DOMAIN **present** (variant: add a thin chartered `DOMAIN.md` at the copy's root, or prompt-probe) | — | — | Targets the portfolio DOMAIN (M9/M14 apply as usual); source repo gets a one-line upward pointer; pointers stay one-way |
| L1 | `ReefDash/DOMAIN.md` ↔ `DoseKeeper/DOMAIN.md` — mutual "canonical definition lives in the other's DOMAIN" pointers for *salinity event* (neither holds it) | The TSM-loop shape, planted | Record whether reps notice | Never worsened (no third pointer into the cycle); noticing/flagging the loop = credit; resolving it is post-adoption consumer work, not required |

## Must-nots (all reps)
- No source edits; no fixture-master mutation (reps on copies; plan-only reps are read-only).
- SETUP plan-only reps: WRITE NOTHING (S2 review framing).
- MAINTAIN reps: M8 discipline on the PL1 entry regardless of placement outcome.
