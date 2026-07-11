# Tasks: readme-portability

## 1. README edits (on `dev`)

- [x] 1.1 Reword "What you get" intro line (standard Agent Skills; authored/tested on Claude Code; anchor link to Beyond Claude Code)
- [x] 1.2 Reword Quick Start requirements line (Agent Skills-compatible agent alternative + anchor link)
- [x] 1.3 Add "Beyond Claude Code" subsection to Usage Notes (open format + 5 marquee adopters + live showcase link; manual-copy install; two degradation caveats + router adaptation)

## 2. Verify + commit (NO PUSH)

- [x] 2.1 Verify: both anchor links target `#beyond-claude-code`; named adopters ⊆ agentskills.io showcase (fetched 2026-07-10); no answer-engine claims; Perplexity absent (grep-verified)
- [x] 2.2 Commit on `dev`. Do NOT merge to `main`, do NOT push — user gate ("No push yet", 2026-07-10). Rider in same commit: journal defined at first table use; "behind the notebook" synonym removed (user-reported, 2026-07-10)

## 3. Later, on user go-ahead (outside this change if deferred)

- [x] 3.1 Merge `dev` → `main` (ff), `git push origin main`, verify rendered subsection + anchors on github.com (WebFetch: 4/4 checks pass — sections, adopters+caveats, journal gloss, anchors)
- [x] 3.2 Archive the change (`openspec archive readme-portability --yes` — judge by output text)
