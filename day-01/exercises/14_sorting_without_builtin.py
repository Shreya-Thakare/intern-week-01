"""
Problem 14: Sorting Without Built-in Sort Functions
---------------------------------------------------------
Implement two classic sorting algorithms from scratch, without using
Python's sorted()/list.sort().

1) Bubble Sort  -- simple, O(n^2), good for teaching the concept.
2) Merge Sort   -- divide and conquer, O(n log n), better for larger inputs.
"""


def bubble_sort(nums: list[int]) -> list[int]:
    arr = nums[:]  # copy so we don't mutate the caller's list
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # already sorted, no need to keep looping
    return arr


def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


if __name__ == "__main__":
    tests = [
        [5, 2, 9, 1, 5, 6],
        [],
        [3, 3, 3],
        [-5, 10, -1, 0],
    ]
    for t in tests:
        print(f"bubble_sort({t}) -> {bubble_sort(t)}")
        print(f"merge_sort({t}) -> {merge_sort(t)}")
