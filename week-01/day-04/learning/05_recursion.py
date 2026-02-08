"""
Day 4 - Section 5: RECURSION
Every recursive function needs: BASE CASE + RECURSIVE CASE + PROGRESS toward base case.
Implement ALL functions below.
"""


def factorial(n):
    """n! = n * (n-1) * ... * 1. Base: 0! = 1"""
    pass

def fibonacci(n):
    """fib(0)=0, fib(1)=1, fib(n)=fib(n-1)+fib(n-2)"""
    pass

def sum_of_list(lst):
    """Sum recursively. Base: empty list → 0"""
    pass

def reverse_string(s):
    """Reverse recursively. Base: len <= 1"""
    pass

def power(base, exp):
    """base^exp. Base: exp==0 → 1. Optimize: even exp → square half."""
    pass

def binary_search_recursive(arr, target, left, right):
    """Binary search. Base: left > right → -1"""
    pass

def flatten_list(nested):
    """[1,[2,[3,4],5],6] → [1,2,3,4,5,6]"""
    pass


if __name__ == "__main__":
    print(factorial(5))       # 120
    print(fibonacci(10))      # 55
    print(sum_of_list([1,2,3,4,5]))  # 15
    print(reverse_string("hello"))    # olleh
    print(power(2, 10))       # 1024
    print(binary_search_recursive([1,3,5,7,9], 7, 0, 4))  # 3
    print(flatten_list([1,[2,[3,4],5],6]))  # [1,2,3,4,5,6]
