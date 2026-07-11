# Tasks: publish-to-github

## 1. Public artifacts (on `dev`)

- [x] 1.1 Write root `README.md` per design decision 1 (8-section structure; the three adapted OpenSpec-style sections as backbone; link to skill files/evidence docs instead of restating numbers)
- [x] 1.2 Add `LICENSE` (MIT, copyright holder Dan / repo owner, year 2026)
- [x] 1.3 Add the `README.md` exclusion line to CLAUDE.md's "Excluded from the doc set" list (public GitHub-facing distribution artifact)
- [x] 1.4 Add ROADMAP.md Recently-shipped digest line for the publication

## 2. Review + merge

- [ ] 2.1 User reviews README.md text (public voice, section content) — amendments applied
- [ ] 2.2 Commit on `dev` (single commit: README, LICENSE, CLAUDE.md, ROADMAP.md), merge `dev` → `main` (ff)

## 3. Publish (irreversible — explicit confirm)

- [ ] 3.1 Wire remote: `origin` → `https://github.com/Apoplectic1/docs-architecture` (verify with `gh repo view` if authed)
- [ ] 3.2 Confirm with user, then `git push -u origin main` — main only; `dev` stays local
- [ ] 3.3 Verify on github.com: README renders correctly (sections, table), LICENSE detected as MIT by GitHub

## 4. Close out

- [ ] 4.1 Verify against specs scenarios (stranger-can-install read-through; three sections present; update-flow text; router exclusion in place)
- [ ] 4.2 Archive the change (`openspec archive` — check output text, not exit code, per NOTEBOOK gotcha)
