"""
Problem 7: Character Frequency Count
---------------------------------------
Count how many times each character appears in a string.

Time Complexity:  O(n)
Space Complexity: O(k), k = number of distinct characters
"""


def character_frequency(text: str) -> dict:
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


if __name__ == "__main__":
    tests = ["hello world", "aabbcc", ""]
    for t in tests:
        print(f"character_frequency({t!r}) -> {character_frequency(t)}")
