#!/bin/bash
# Usage: ./scripts/daily-commit.sh "LinkedList + 6 problems"
MSG="${1:-daily progress}"
git add -A
if git diff --cached --quiet; then
    echo "No changes to commit."
    exit 0
fi
git commit -m "$MSG"
git push origin main
echo "✅ Committed and pushed: $MSG"
