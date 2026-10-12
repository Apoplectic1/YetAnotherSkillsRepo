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

## Variant `audit-scope` (2026-10-12, change `audit-scope-from-routers`)

Overlay `reefstack-fixture-variants/audit-scope/` on a fixture copy (its files replace or add
to the base), then baseline. AUDIT reps run from `ReefDash/` (AR cells) or `PulseMonitor/`
(SP, SS cells); the root `CLAUDE.md` is the ancestor router. Non-derived: the HDL tree's ATML
audit is the deriving evidence and is poisoned for these rules.

| ID | Where | Plant | Expected RED (current text) | Expected GREEN (candidate) |
|---|---|---|---|---|
| AR1 | `ReefDash/CLAUDE.md` gotcha "Alert palette rule (root `CLAUDE.md` § Conventions)" | Upward pointer to a rule the ancestor does not carry | Root not read, pointer unresolved, no flag | Dangling-reference flag naming the ancestor section |
| AR2 | Root § Conventions "UTC everywhere" vs `ReefDash/src/feed.py` `stamp()` (`datetime.now()`), and ARCHITECTURE § Feed rows "local receive time" | Repo code violating an ancestor convention; the repo doc agreeing with the code | Doc matches code, no flag (R6) | `flag-code-bug` citing the root line and `feed.py`; the doc not "fixed" toward the code |
| AR3 | `ReefDash/ARCHITECTURE.md` § Settings | Restates the root's "Settings are TOML" rule, unattributed | Kept, or `move-to DOMAIN` (R10) | `cross-ref+delete` (the rule loads as an ancestor) |
| AR4 | `ReefDash/CLAUDE.md` gotcha "Timestamps follow the portfolio's UTC rule" | A one-line pointer up to a rule the ancestor does carry (control) | No flag | No flag |
| SP1 | `PulseMonitor/docs/2026-07-01 - probe-wiring.md`, routed by the router as current truth | Dated name, reference role; ph/par channels swapped against `src/probes.py` | Excluded under R14 (`docs/`), no flag | Currency `fix-doc` (code wins) |
| SP2 | `PulseMonitor/docs/2026-06-15 - wiring-bringup.md` | Dated record not routed as reference, the old channel map (control) | No flag | No flag |
| SS1 | `PulseMonitor/openspec/specs/poll-loop/spec.md` "every 5 seconds", named by the router as a rule | A router-named spec with a false SHALL; `src/poll.py` and SCHEMA say 10 s | Excluded (tooling / workflow-only), or `fix-doc` in place | Currency flag, action `spec-change` (report-only), the spec untouched |
| SS2 | `PulseMonitor/openspec/specs/alert-webhook/spec.md` | A spec the router does not name, unbuilt feature (control) | No flag | No flag |

Neutral (neither credit nor fail): flags on the base fixture's planted root `Data contracts`
block (PC1) or on PulseMonitor's `config.db` against the TOML rule.

Added after the first RED pass (2026-10-12): the ReefDash router's own upward pointers (AR1,
AR4) led every rep into the root, so AR1 to AR4 cannot show whether an *uncited* ancestor
convention is audited, which is the field case (a rule for every repository beneath, cited by
none of them). AUDIT reps for these run from `DoseKeeper/`, whose router never points up.

| ID | Where | Plant | Expected RED | Expected GREEN |
|---|---|---|---|---|
| AR5 | Root "UTC everywhere" vs `DoseKeeper/src/doselog.py` `log_dose()` (`datetime.now()`), and ARCHITECTURE § Dose log "local wall-clock time" | Uncited ancestor convention violated by repo code; the repo doc agreeing | Root not read; doc matches code, no flag | `flag-code-bug` citing the root line and `doselog.py` |
| AR6 | Root "Settings are TOML" vs `DoseKeeper/settings.json` and ARCHITECTURE § Settings | Uncited ancestor convention violated by the repo's settings file; the doc agreeing | No flag | `flag-code-bug` (or the convention named in a flag) citing the root line |
