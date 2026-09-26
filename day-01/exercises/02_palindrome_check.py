"""
Problem 2: Palindrome Check
----------------------------
Check whether a given string is a palindrome, ignoring case and
non-alphanumeric characters (so "A man, a plan, a canal: Panama" works).

Time Complexity:  O(n)
Space Complexity: O(n)  (cleaned copy of the string)
"""


def is_palindrome(text: str) -> bool:
    cleaned = [ch.lower() for ch in text if ch.isalnum()]
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    tests = [
        "racecar",
        "hello",
        "A man, a plan, a canal: Panama",
        "",
        "Was it a car or a cat I saw?",
    ]
    for t in tests:
        print(f"is_palindrome({t!r}) -> {is_palindrome(t)}")
