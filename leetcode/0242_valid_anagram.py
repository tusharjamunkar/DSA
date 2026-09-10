"""
0242. Valid Anagram
Difficulty: Easy
Topic: Arrays & Hashing / String
LeetCode Link: https://leetcode.com/problems/valid-anagram/

Problem Statement:
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- `s` and `t` consist of lowercase English letters.

Follow-up:
What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
- Using a Hash Map (e.g. `collections.defaultdict` or `collections.Counter`) naturally scales 
  to arbitrary Unicode code points with O(1) average lookup/insertion.
"""

from collections import Counter, defaultdict
from typing import Dict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Optimal Fixed Frequency Array Approach:
        - If lengths differ, they cannot be anagrams (instant O(1) exit).
        - Count frequency deltas across characters using a 26-element array.
        - Increment for s[i] and decrement for t[i].
        - If all counts return to zero, strings are valid anagrams.

        Time Complexity:  O(n) - Single pass through both strings where n = len(s).
        Space Complexity: O(1) - Fixed 26-element array regardless of input size.
        """
        if len(s) != len(t):
            return False

        count = [0] * 26
        base = ord("a")

        for char_s, char_t in zip(s, t):
            count[ord(char_s) - base] += 1
            count[ord(char_t) - base] -= 1

        return all(c == 0 for c in count)

    def isAnagramUnicode(self, s: str, t: str) -> bool:
        """
        Hash Map Approach (Generalizable to Unicode):
        - Handles arbitrary UTF-8 / Unicode characters by keying on characters directly.

        Time Complexity:  O(n) - Linear pass through strings.
        Space Complexity: O(k) - Where k is the number of distinct characters (at most n).
        """
        if len(s) != len(t):
            return False

        counts: Dict[str, int] = defaultdict(int)
        for char in s:
            counts[char] += 1

        for char in t:
            counts[char] -= 1
            if counts[char] < 0:
                return False

        return True

    def isAnagramCounter(self, s: str, t: str) -> bool:
        """
        Pythonic Counter Approach:
        - Uses Python's built-in Counter for idiomatic and concise comparison.

        Time Complexity:  O(n)
        Space Complexity: O(k)
        """
        return Counter(s) == Counter(t)

    def isAnagramSorting(self, s: str, t: str) -> bool:
        """
        Sorting Approach:
        - Sort both strings and assert equality.

        Time Complexity:  O(n log n)
        Space Complexity: O(1) or O(n) depending on Python's Timsort implementation.
        """
        return sorted(s) == sorted(t)


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_valid_anagram():
    sol = Solution()

    # Test Case 1: Standard anagram
    assert sol.isAnagram("anagram", "nagaram") is True
    assert sol.isAnagramUnicode("anagram", "nagaram") is True
    assert sol.isAnagramCounter("anagram", "nagaram") is True
    assert sol.isAnagramSorting("anagram", "nagaram") is True

    # Test Case 2: Different characters
    assert sol.isAnagram("rat", "car") is False
    assert sol.isAnagramUnicode("rat", "car") is False
    assert sol.isAnagramCounter("rat", "car") is False
    assert sol.isAnagramSorting("rat", "car") is False

    # Test Case 3: Different lengths
    assert sol.isAnagram("a", "ab") is False
    assert sol.isAnagramUnicode("a", "ab") is False
    assert sol.isAnagramCounter("a", "ab") is False
    assert sol.isAnagramSorting("a", "ab") is False

    # Test Case 4: Single identical character
    assert sol.isAnagram("z", "z") is True
    assert sol.isAnagramUnicode("z", "z") is True
    assert sol.isAnagramCounter("z", "z") is True
    assert sol.isAnagramSorting("z", "z") is True

    # Test Case 5: Duplicate frequencies mismatch
    assert sol.isAnagram("aacc", "ccac") is False
    assert sol.isAnagramUnicode("aacc", "ccac") is False
    assert sol.isAnagramCounter("aacc", "ccac") is False
    assert sol.isAnagramSorting("aacc", "ccac") is False

    # Test Case 6: Unicode support
    assert sol.isAnagramUnicode("café", "féca") is True
    assert sol.isAnagramCounter("café", "féca") is True
    assert sol.isAnagramUnicode("🚀🌟", "🌟🚀") is True

    print("All Valid Anagram tests passed successfully!")


if __name__ == "__main__":
    test_valid_anagram()
