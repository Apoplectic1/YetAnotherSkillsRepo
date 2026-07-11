# Tasks: publish-to-github

## 1. Public artifacts (on `dev`)

- [x] 1.1 Write root `README.md` per design decision 1 (8-section structure; the three adapted OpenSpec-style sections as backbone; link to skill files/evidence docs instead of restating numbers)
- [x] 1.2 Add `LICENSE` (MIT, copyright holder Dan / repo owner, year 2026)
- [x] 1.3 Add the `README.md` exclusion line to CLAUDE.md's "Excluded from the doc set" list (public GitHub-facing distribution artifact)
- [x] 1.4 Add ROADMAP.md Recently-shipped digest line for the publication

## 2. Review + merge

- [x] 2.1 User reviews README.md text (public voice, section content) — amendments applied ("looks good", no amendments)
- [x] 2.2 Commit on `dev` (single commit: README, LICENSE, CLAUDE.md, ROADMAP.md + change artifacts), merge `dev` → `main` (ff) — `4b8c17b`

## 3. Publish (irreversible — explicit confirm)

- [x] 3.1 Wire remote: `origin` → `https://github.com/Apoplectic1/docs-architecture` (verified via `gh repo view`: exists, PUBLIC, empty)
- [x] 3.2 Confirm with user, then `git push -u origin main` — main only; `dev` stays local (user: "push"; `4b8c17b` → origin/main, upstream set; ls-remote shows main as sole head)
- [x] 3.3 Verify on github.com: README renders correctly (sections, table), LICENSE detected as MIT by GitHub (WebFetch verification: all 8 sections render, relative links resolve, sidebar shows "MIT license")

## 4. Close out

- [x] 4.1 Verify against specs scenarios (stranger-can-install read-through ✓; three sections + subheadings present ✓; update-flow text with marker/prune note ✓; main-only remote ✓; MIT consistent ✓; router exclusion committed ✓)
- [x] 4.2 Archive the change (`openspec archive` — check output text, not exit code, per NOTEBOOK gotcha)
