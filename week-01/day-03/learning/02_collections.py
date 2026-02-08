"""
Day 3 - Section 2: Collections Module
defaultdict, Counter, OrderedDict — you NEED these for DSA.
"""
from collections import defaultdict, Counter, OrderedDict, namedtuple

# --- defaultdict ---
# defaultdict(list) → missing key creates empty list
# defaultdict(int) → missing key creates 0
# TODO: Practice — eliminates KeyError checking


# --- Counter ---
# Counter("hello") → {'l': 2, 'h': 1, 'e': 1, 'o': 1}
# .most_common(n), arithmetic on Counters
# TODO: Practice


# --- namedtuple ---
# Point = namedtuple('Point', ['x', 'y'])
# TODO: Practice


if __name__ == "__main__":
    pass
