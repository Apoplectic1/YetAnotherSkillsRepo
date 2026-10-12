# Tasks

## 1. RED
- [x] 1.1 `harness/journal-index-fixture/NOTEBOOK/2026-10-01.md`: a rolled file in the bare-date form (bold-lead entries, a plain bullet, an indented bullet, a titled dated sub-heading with a bold-lead bullet under it, a bold run past `TITLE_MAX`); today's script gives three date-only lines

## 2. The script
- [x] 2.1 `journal_index.py`: the bold-lead entry under a bare date heading (D1 to D5); docstring
- [x] 2.2 `rollover.py` unchanged: a dry run on the fixture in live form reports the heading form, three dated entries, byte check passing (D6)

## 3. GREEN and the regression
- [x] 3.1 The new script's output byte-matches `harness/journal-index-fixture/INDEX.expected.md`
- [x] 3.2 Old and new script on copies of the six HDL rolled directories: no entry line removed or changed; Arty's `CHANGELOG/` gains its 33 bold-lead units

## 4. The text
- [x] 4.1 MAINTAIN M17, SETUP T1, the design doc's rollover paragraph; the maintain spec's requirement and a scenario
- [x] 4.2 `harness/README.md` names the fixture; `VERIFICATION.md` names the script-level check; ROADMAP item to Recently shipped; NOTEBOOK entry

## 5. Ship
- [x] 5.1 `openspec validate rolled-index-titled-entries --strict`; archive with `--yes`, judged by output text; `main` fast-forwarded; `deploy.sh`
- [x] 5.2 EP7314600: regenerate `NOTEBOOK/INDEX.md` with the deployed script (done from here on the F: working copy, commit f720250 there: 43 titled lines, nothing else changed)
