"""
Problem 9: Merge Two Sorted Arrays
--------------------------------------
Merge two already-sorted lists into a single sorted list without
using the built-in sorted()/sort().

Approach: Classic two-pointer merge, same idea used in merge sort.

Time Complexity:  O(n + m)
Space Complexity: O(n + m)
"""


def merge_sorted_arrays(a: list[int], b: list[int]) -> list[int]:
    i, j = 0, 0
    merged = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged


if __name__ == "__main__":
    tests = [
        ([1, 3, 5], [2, 4, 6]),
        ([], [1, 2, 3]),
        ([1, 1, 1], [1, 1]),
    ]
    for a, b in tests:
        print(f"merge_sorted_arrays({a}, {b}) -> {merge_sorted_arrays(a, b)}")
