# Proposal: publish-to-github

## Why

The four-skill docs-architecture family is stable, deployed, and field-hardened (first self-audit 2026-07-10; worker-death hardening shipped the same day), and the user has created its public distribution channel: https://github.com/Apoplectic1/docs-architecture (empty, open in browser). The repo currently has no public face — the old README was deliberately dissolved on 2026-07-10 with the explicit note that a public README would be "rewritten fresh at publish time." That time is now. There is also no LICENSE (publishing without one leaves the repo all-rights-reserved) and no git remote.

## What Changes

- **New root `README.md`** — purely GitHub/public-facing, modeled on the OpenSpec README's style (user-named exemplar). Backbone replicates the three sections the user called out, adapted: **Why docs-architecture**, **Updating**, **Usage Notes** — plus the minimum a public README needs around them (what it is, the four skills, install). It documents the *product* (the skills); the journal/openspec trail is oriented as visible provenance, not product docs.
- **New `LICENSE`** — MIT (user-selected 2026-07-10).
- **Git remote wiring** — `origin` → `github.com/Apoplectic1/docs-architecture`; push `main` only (`main` = distribution-ready ref per RELEASING.md; `dev` stays local authoring per the local-disk-is-truth convention).
- **Router/doc integration** — one-line placement decision so future audits treat README correctly: CLAUDE.md router names `README.md` as the public/GitHub-facing artifact, *excluded* from the AI reference-doc set (it is not a charter'd reference doc; the audit's router-anchored scope must not currency-audit it as one). ROADMAP gains the shipped digest line.

## Capabilities

### New Capabilities
- `github-distribution`: the public distribution channel — what the public README must contain (the three adapted OpenSpec-style sections + essentials), the MIT license requirement, remote/push mechanics (main-only), and the consumer update flow (`git pull` + `deploy.sh`).

### Modified Capabilities

(none — no skill requirement changes; `docs-architecture-audit`, `docs-architecture-setup`, `whats-next` specs untouched)

## Impact

- **New files:** `README.md`, `LICENSE` (repo root).
- **Edited docs:** `CLAUDE.md` (router line naming README as public-facing, out of the reference set), `ROADMAP.md` (digest line). No skill text changes; no deploy needed (README/LICENSE are not deployed artifacts).
- **Git state:** new `origin` remote; `main` pushed publicly. **Publishing exposes the entire history and working tree publicly** — journal (NOTEBOOK.md, dated docs/), openspec archive, `.claude/` tooling, and absolute local paths (`E:\Projects\...`) inside docs. Accepted: the RED/GREEN provenance trail is part of the repo's public value, and the paths are inert documentation — but this is the one irreversible step (history is public once pushed) and is called out in tasks as the final, explicitly-confirmed action.
