#!/bin/bash
# Usage: ./scripts/new-solution.sh 206 "Reverse Linked List" Easy "Linked List" week-02/day-08/leetcode
NUM=$1; NAME=$2; DIFF=$3; PATTERN=$4; FOLDER=$5
PADDED=$(printf "%04d" $NUM)
SLUG=$(echo "$NAME" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
FILE="${FOLDER}/${PADDED}_${SLUG}.py"
mkdir -p "$FOLDER"
cat > "$FILE" << PYEOF
# ${NUM}. ${NAME}
# Difficulty: ${DIFF}
# Pattern: ${PATTERN}
# Time: O(?) | Space: O(?)
# Date: $(date +"%b %d, %Y")

class Solution:
    def solve(self):
        # TODO: Implement
        pass

if __name__ == "__main__":
    sol = Solution()
    # TODO: Test cases
    print("${NUM}. ${NAME} - Tests passed!")
PYEOF
echo "Created: $FILE"
