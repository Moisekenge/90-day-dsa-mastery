#!/bin/bash
# Usage: ./scripts/new-day.sh 8 02
DAY=$1; WEEK=$2
WPAD=$(printf "%02d" $WEEK); DPAD=$(printf "%02d" $DAY)
DIR="week-${WPAD}/day-${DPAD}"
mkdir -p "${DIR}/learning" "${DIR}/leetcode"
cat > "${DIR}/log.md" << EOF
# Day ${DAY} - $(date +"%b %d, %Y")
## 🎯 Goal

## ✅ Problems Solved
| # | Problem | Difficulty | Time | Pattern | Status |
|---|---------|-----------|------|---------|--------|

## 📚 Learned
-
## ⚠️ Struggled
-
## 📊 Stats
- Total Problems:
EOF
echo "Created: ${DIR}/"
