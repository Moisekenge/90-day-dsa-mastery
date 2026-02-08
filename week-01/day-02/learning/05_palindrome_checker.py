"""
Day 2 - Project: Palindrome Checker
Handle case, spaces, punctuation.
"A man, a plan, a canal: Panama" → True
"""


def is_palindrome(s):
    # TODO: Implement
    # 1. Clean string (lowercase, remove non-alphanumeric)
    # 2. Compare with reverse
    pass


if __name__ == "__main__":
    print(is_palindrome("racecar"))       # True
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("hello"))          # False
