# Tasks

## 1. The check, before any spec is edited

- [ ] 1.1 `check_specs.py` and an empty `ledger.md` in the change directory (D5), the base commit fixed in the script; verify that on the unchanged specs it finds every old clause, requirement name and scenario name, no requirement without a scenario, and reports strict validation at 1/5

## 2. The specs, one at a time

- [ ] 2.1 `docs-architecture-audit`: its three status notes removed (D1), each of its ten long requirements cut to one behavior per requirement with its scenarios moved beside the behavior they test (D2), non-behavior prose removed (D3), every removal and rewording in the ledger, the Purpose written (D6); verify `check_specs.py` reports nothing for this spec and `openspec validate docs-architecture-audit --type spec --strict` passes
- [ ] 2.2 `docs-architecture-maintain`: its status note removed (its halt rule is the ADDED delta), its six long requirements cut the same way, the ledger updated; verify `check_specs.py` reports nothing for this spec and its strict validation passes
- [ ] 2.3 `docs-architecture-setup`: its two status notes removed (the router-lean note's four rules are the ADDED delta), its eight long requirements cut the same way, the ledger updated, the Purpose written; verify `check_specs.py` reports nothing for this spec and its strict validation passes
- [ ] 2.4 `github-distribution`: its two long requirements cut the same way, the ledger updated; verify `check_specs.py` reports nothing for this spec and `openspec validate --specs --strict` passes 5/5

## 3. The convention and the reference docs

- [ ] 3.1 `DOMAIN.md`'s authoring conventions gain D7's line; the design doc's Always-on budget part ("are status notes in the specs") and Scope-from-the-routers part ("with status notes") say where the results live instead, and the latter's index line follows; then `split_doc.py --reindex` on the design doc, acting on its review list; verify `--check` is clean and a grep of the reference tier finds no claim that a main spec carries status notes

## 4. The reader reps

- [ ] 4.1 One Workflow at Sonnet/high, four reps labeled `[sonnet/high]`, one per spec, each given the spec's old text (at the base commit), its new text and, for setup and maintain, the ADDED delta, and asked for any behavior lost, added or changed by requirement name (D8); fix each finding, rerun that rep to no findings, and keep `check_specs.py` passing; verify the record `docs/<the day it is written> - main-specs-strict-clean.md` holds each rep's findings, the fixes and the token total

## 5. The record and the ship

- [ ] 5.1 `CHANGELOG.md` entry; the ROADMAP digest kept at five lines; the standing-truth answer (D7's line) for the ship commit; verify `openspec validate main-specs-strict-clean --strict` passes

## Workflow follow-up

- Archive with `openspec archive main-specs-strict-clean --yes`, judged by the output text; then `openspec validate --specs --strict` must pass 5/5 with the five ADDED requirements in place.
- Fast-forward `main` and push; `deploy.sh` is optional, since no skill changes.
