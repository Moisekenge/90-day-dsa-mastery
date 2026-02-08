"""
Day 5 - Binary Search (Iterative + Recursive + Variants)
Time: O(log n) | Space: O(1) iterative, O(log n) recursive
"""

def binary_search_iterative(arr, target):
    # TODO: Implement
    pass

def binary_search_recursive(arr, target, left, right):
    # TODO: Implement
    pass

def first_occurrence(arr, target):
    # TODO: Find FIRST occurrence in sorted array with duplicates
    pass

def last_occurrence(arr, target):
    # TODO: Find LAST occurrence
    pass

if __name__ == "__main__":
    arr = [1, 3, 5, 5, 5, 7, 9]
    print(binary_search_iterative(arr, 5))  # 2, 3, or 4
    print(first_occurrence(arr, 5))          # 2
    print(last_occurrence(arr, 5))           # 4
