# Journal rollover: the pilot's scripts (2026-09-26)

The scripts that rolled the HDL tree's journals on 2026-09-26 (ROADMAP, "Journal rollover and
the overflow directory"). The skill change decides where they live when it ships and what
wraps them; until then they are the record of what ran.

- `rollover.py <repo>/<JOURNAL>.md [--apply]`: rolls a journal past 40 KB into
  `<JOURNAL>/<first-date>.md` by whole days, each file under 40 KB, about 20 KB kept live;
  checks the move byte for byte; refuses an existing rolled file, a journal under budget, an
  overflow directory without the live note. Detects a newest-first CHANGELOG from its dates.
  Carrying an open thread out of a rolled entry is the operator's step before `--apply`.
- `journal_index.py <repo>/<JOURNAL>/`: writes `INDEX.md`, one section per rolled file (its
  date span and size) and one line per dated entry (date and title; a dated `###` sub-entry
  indented). `rollover.py --apply` runs it.

Verified by replaying `rollover.py` on the pre-rollover versions of HlsLibrary's NOTEBOOK and
the Arty's CHANGELOG (newest first): the rolled bodies and the live file came out identical to
the pilot's commits.
