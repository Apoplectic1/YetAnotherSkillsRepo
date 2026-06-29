#!/usr/bin/env bash
# Deploy skills from this repo (canonical source) to ~/.claude/skills/ (the live harness location).
# COPY, not symlink/move: the deployed copy is a disposable build artifact — edit skills HERE,
# then re-run this to refresh. Never edit ~/.claude/skills/ directly.
#
# Branch policy: only `main` deploys to the live harness. Develop and test on `dev` (use the
# RED/GREEN subagent harness — inject SKILL.md text into test agents — which needs no deploy);
# merge dev -> main; then deploy. To intentionally deploy the current branch for live Skill-tool
# dogfooding, pass --force (deploys dev/whatever-you're-on, with a warning).
set -euo pipefail

REPO="$(cd "$(dirname "$0")" && pwd)"
SRC="$REPO/skills"
DEST="${HOME}/.claude/skills"

FORCE="${1:-}"
BRANCH="$(git -C "$REPO" rev-parse --abbrev-ref HEAD)"

if [ "$BRANCH" != "main" ] && [ "$FORCE" != "--force" ]; then
  echo "deploy: refusing — on branch '$BRANCH', not 'main'." >&2
  echo "        Merge to main first, then deploy. To deploy this branch anyway for" >&2
  echo "        dogfooding, re-run: ./deploy.sh --force" >&2
  exit 1
fi

if [ "$BRANCH" != "main" ]; then
  echo "deploy: WARNING — force-deploying branch '$BRANCH' (NOT main) to the live harness." >&2
fi
if [ -n "$(git -C "$REPO" status --porcelain)" ]; then
  echo "deploy: WARNING — working tree has uncommitted changes; deploying tree state, not a commit." >&2
fi

mkdir -p "$DEST"
for d in "$SRC"/*/; do
  name="$(basename "$d")"
  rm -rf "${DEST:?}/$name"
  cp -r "$d" "$DEST/$name"
  echo "deployed: $name -> $DEST/$name"
done
