"""
Day 5 - Quick Sort
Pick pivot, partition, recurse.
Time: O(n log n) avg, O(n^2) worst | Space: O(log n)
"""

def quick_sort(arr, low=0, high=None):
    # TODO: Implement from scratch
    pass

if __name__ == "__main__":
    test = [64, 34, 25, 12, 22, 11, 90]
    qs = test.copy()
    quick_sort(qs)
    print(qs)
