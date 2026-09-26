"""
Problem 4: Remove Duplicates
------------------------------
Remove duplicate elements from a list while preserving the original
order of first occurrence.

Approach: Use a set/hash map to track what's been seen -- this is the
hash-map technique referenced in the DSA topics.

Time Complexity:  O(n)
Space Complexity: O(n)
"""


def remove_duplicates(items: list) -> list:
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


if __name__ == "__main__":
    tests = [
        [1, 2, 2, 3, 1, 4],
        ["a", "b", "a", "c", "b"],
        [],
        [5, 5, 5, 5],
    ]
    for t in tests:
        print(f"remove_duplicates({t}) -> {remove_duplicates(t)}")
