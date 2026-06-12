#!/usr/bin/env bash
# Push all four prepared bundles to GitHub.
#
# Prerequisites:
#   1. Create the four repos at https://github.com/organizations/vfd-org/repositories/new
#      with these exact names (public, no README/license/.gitignore — bundles already have those):
#        - evidence-ledger
#        - translation-layer
#        - critical-line-pullback
#        - translation-engine-v2
#   2. Make sure you can authenticate to github.com (e.g., gh auth login, or git credentials).
#
# Then from anywhere:
#   bash release-bundles/push_all.sh
#
# OR from the release-bundles directory:
#   ./push_all.sh

set -e

HERE="$(cd "$(dirname "$0")" && pwd)"

bundles=(
  "evidence-ledger"
  "translation-layer"
  "critical-line-pullback"
  "translation-engine-v2"
)

for b in "${bundles[@]}"; do
  echo "===== Pushing $b ====="
  cd "$HERE/$b"
  git push -u origin main
  echo "  -> https://github.com/vfd-org/$b"
  echo ""
done

echo "All four bundles pushed."
echo ""
echo "Final URLs:"
for b in "${bundles[@]}"; do
  echo "  - https://github.com/vfd-org/$b"
done
