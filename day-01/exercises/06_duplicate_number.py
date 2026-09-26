"""
Problem 6: Find the Duplicate Number
---------------------------------------
Given a list of n+1 integers where each integer is between 1 and n,
find the one duplicated number (there's guaranteed to be exactly one).

Approach: Track counts with a hash map (dictionary) and return the
first value whose count exceeds 1.

Time Complexity:  O(n)
Space Complexity: O(n)
"""


def find_duplicate(nums: list[int]) -> int:
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1
        if counts[n] > 1:
            return n
    raise ValueError("No duplicate found")


if __name__ == "__main__":
    tests = [
        [1, 3, 4, 2, 2],
        [3, 1, 3, 4, 2],
        [1, 1],
    ]
    for t in tests:
        print(f"find_duplicate({t}) -> {find_duplicate(t)}")
