"""
Problem 5: Find the Missing Number
-------------------------------------
Given a list containing n distinct numbers taken from 0..n (inclusive),
find the one number missing from the list.

Approach: Use the Gauss sum formula. The expected sum of 0..n is
n*(n+1)/2; subtracting the actual sum gives the missing number.

Time Complexity:  O(n)
Space Complexity: O(1)
"""


def find_missing_number(nums: list[int]) -> int:
    n = len(nums)  # one number from 0..n is missing, so array has n elements
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


if __name__ == "__main__":
    tests = [
        [3, 0, 1],       # missing 2
        [0, 1],          # missing 2
        [9, 6, 4, 2, 3, 5, 7, 0, 1],  # missing 8
    ]
    for t in tests:
        print(f"find_missing_number({t}) -> {find_missing_number(t)}")
