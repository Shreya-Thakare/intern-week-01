"""
Problem 15: Searching Algorithms + Recursion
--------------------------------------------------
Covers two remaining DSA topics: searching, and recursion.

1) linear_search  -- O(n), checks every element, works on unsorted data.
2) binary_search  -- O(log n), requires a SORTED array; repeatedly
   halves the search space.
3) factorial (recursive)      -- classic recursion example.
4) fibonacci (recursive)      -- classic recursion example, with a
   note about exponential time complexity without memoization.
"""


def linear_search(nums: list[int], target: int) -> int:
    for i, n in enumerate(nums):
        if n == target:
            return i
    return -1


def binary_search(sorted_nums: list[int], target: int) -> int:
    low, high = 0, len(sorted_nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_nums[mid] == target:
            return mid
        elif sorted_nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    # Time complexity: O(2^n) without memoization -- fine for small n,
    # included here to illustrate plain recursion, not efficiency.
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    nums = [5, 3, 8, 1, 9, 2]
    sorted_nums = sorted(nums)

    print(f"linear_search({nums}, 8) -> {linear_search(nums, 8)}")
    print(f"sorted array -> {sorted_nums}")
    print(f"binary_search({sorted_nums}, 8) -> {binary_search(sorted_nums, 8)}")
    print(f"binary_search({sorted_nums}, 100) -> {binary_search(sorted_nums, 100)}")

    print(f"factorial(6) -> {factorial(6)}")
    print(f"fibonacci sequence (0..9) -> {[fibonacci(i) for i in range(10)]}")
