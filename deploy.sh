#!/usr/bin/env bash
# Deploy skills from this repo (canonical source) to ~/.claude/skills/ (the live harness location).
# COPY, not symlink/move: the deployed copy is a disposable build artifact — edit skills HERE,
# then re-run this to refresh. Never edit ~/.claude/skills/ directly.
set -euo pipefail
SRC="$(cd "$(dirname "$0")/skills" && pwd)"
DEST="${HOME}/.claude/skills"
mkdir -p "$DEST"
for d in "$SRC"/*/; do
  name="$(basename "$d")"
  rm -rf "${DEST:?}/$name"
  cp -r "$d" "$DEST/$name"
  echo "deployed: $name -> $DEST/$name"
done
