"""
Day 3 - Project: Word Frequency Counter
Implement with Counter AND without (manual dict).
"""
from collections import Counter


def word_freq_manual(text, n=5):
    # TODO: Implement without Counter
    pass


def word_freq_counter(text, n=5):
    # TODO: Implement with Counter
    pass


if __name__ == "__main__":
    text = "the quick brown fox jumps over the lazy dog the fox the the"
    print(word_freq_manual(text, 3))
    print(word_freq_counter(text, 3))
