"""
Problem 3: Largest and Second-Largest Number
----------------------------------------------
Find the largest and second-largest distinct values in a list of
numbers in a single pass, without using max()/sorted().

Time Complexity:  O(n)
Space Complexity: O(1)
"""


def largest_and_second_largest(nums: list[int]):
    if len(nums) < 2:
        raise ValueError("Need at least two numbers")

    largest = second = float("-inf")
    for n in nums:
        if n > largest:
            second = largest
            largest = n
        elif largest > n > second:
            second = n

    if second == float("-inf"):
        return largest, None  # all values were equal
    return largest, second


if __name__ == "__main__":
    tests = [
        [3, 1, 4, 1, 5, 9, 2, 6],
        [10, 10, 10],
        [-5, -2, -9, -1],
        [7, 7, 8],
    ]
    for t in tests:
        print(f"largest_and_second_largest({t}) -> {largest_and_second_largest(t)}")
