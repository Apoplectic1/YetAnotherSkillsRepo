---
paths: ["openspec/**"]
---

# openspec CLI gotchas (loads when an openspec file is touched)

Moved out of `CLAUDE.md` on 2026-10-12 (SETUP S8: an activity's gotchas go behind a trigger
line); the router's trigger names this file.

- **openspec CLI:** always `openspec archive <name> --yes` (it prompts interactively and dies
  in non-interactive shells) and judge success by **output text, never exit code** (archive
  can exit 0 on a validation abort — don't chain with `&&`). The spec validator wants
  SHALL/MUST on a requirement's **lead line**, and only validates files a change touches.
  A MODIFIED block may not drop a scenario name the main spec still has, and a rename
  counts as a drop: rename the `#### Scenario:` heading directly in the main spec and
  carry the new name in the delta. A change with no delta (a Purpose edit, prose only)
  needs `skip_specs: true` in its `.openspec.yaml` or validate refuses it with "no
  deltas". (Field origins: NOTEBOOK 2026-07-07/10, 2026-09-26.)
- `openspec new change <name>` scaffolds into the openspec root nearest the shell's working
  directory, and the Bash tool's directory persists across calls: `cd` to the repo root in
  the same command (NOTEBOOK 2026-10-12).
