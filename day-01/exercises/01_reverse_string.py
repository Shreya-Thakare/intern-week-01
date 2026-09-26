"""
Problem 1: Reverse a String
----------------------------
Given a string, return the string reversed.

Approach: Two-pointer swap in place (using a list, since Python strings
are immutable) instead of relying on slicing, so the underlying
algorithm is visible.

Time Complexity:  O(n)
Space Complexity: O(n)  (new list/string is created)
"""


def reverse_string(text: str) -> str:
    chars = list(text)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return "".join(chars)


if __name__ == "__main__":
    tests = ["hello", "Python", "a", "", "racecar"]
    for t in tests:
        print(f"reverse_string({t!r}) -> {reverse_string(t)!r}")
