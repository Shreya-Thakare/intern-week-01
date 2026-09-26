"""
Problem 8: First Non-Repeating Character
--------------------------------------------
Find the first character in a string that does not repeat anywhere
else in the string. Return None if every character repeats.

Approach: Build a frequency map in one pass, then scan the string
again in order and return the first char with a count of 1.

Time Complexity:  O(n)
Space Complexity: O(k)
"""


def first_non_repeating_char(text: str):
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in text:
        if freq[ch] == 1:
            return ch
    return None


if __name__ == "__main__":
    tests = ["swiss", "aabbcc", "teeter", ""]
    for t in tests:
        print(f"first_non_repeating_char({t!r}) -> {first_non_repeating_char(t)!r}")
