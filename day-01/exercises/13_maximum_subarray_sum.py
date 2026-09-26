"""
Problem 13: Maximum Subarray Sum
-------------------------------------
Given an array of integers (possibly negative), find the largest sum
of any contiguous subarray.

Approach: Kadane's Algorithm. Track the best sum ending at the current
index, and the best sum seen overall.

Time Complexity:  O(n)
Space Complexity: O(1)
"""


def max_subarray_sum(nums: list[int]) -> int:
    if not nums:
        raise ValueError("Array must not be empty")

    best_ending_here = best_overall = nums[0]
    for n in nums[1:]:
        best_ending_here = max(n, best_ending_here + n)
        best_overall = max(best_overall, best_ending_here)
    return best_overall


if __name__ == "__main__":
    tests = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],  # -> 6 ([4, -1, 2, 1])
        [1, 2, 3, 4],                     # -> 10
        [-1, -2, -3],                     # -> -1
    ]
    for t in tests:
        print(f"max_subarray_sum({t}) -> {max_subarray_sum(t)}")
