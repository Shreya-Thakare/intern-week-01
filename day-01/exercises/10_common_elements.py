"""
Problem 10: Common Elements Between Two Arrays
---------------------------------------------------
Find the elements that appear in both lists (set intersection),
without duplicates in the result.

Time Complexity:  O(n + m)
Space Complexity: O(n + m)
"""


def common_elements(a: list, b: list) -> list:
    set_a = set(a)
    set_b = set(b)
    return list(set_a & set_b)


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4], [3, 4, 5, 6]),
        (["a", "b", "c"], ["x", "y", "z"]),
        ([1, 1, 2], [1, 2, 2]),
    ]
    for a, b in tests:
        print(f"common_elements({a}, {b}) -> {sorted(common_elements(a, b), key=str)}")
