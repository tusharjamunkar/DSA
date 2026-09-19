"""
0003. Longest Substring Without Repeating Characters
Difficulty: Medium
Topic: Sliding Window / Hash Table / String
LeetCode Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Problem Statement:
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Optimal Sliding Window with Last-Seen Index Map:

        Algorithmic Intuition:
        - Maintain a sliding window [left, right] of characters without duplicates.
        - Use a hash map `last_seen` to store the most recent index where each character appeared.
        - As `right` iterates from 0 to len(s) - 1:
          - If `s[right]` was seen at index `prev_idx >= left`, we have encountered a duplicate
            inside our active window.
          - We immediately advance `left = prev_idx + 1` (jumping over the duplicate).
          - Update `last_seen[s[right]] = right`.
          - Window length is `right - left + 1`.
          - Update `max_len = max(max_len, right - left + 1)`.

        Complexity:
        - Time Complexity:  O(n) - Each character is visited at most once by `right`.
        - Space Complexity: O(min(m, n)) - Where m is the charset size (at most 128 for ASCII).
        """
        last_seen = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1
            last_seen[char] = right
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len

        return max_len

    def lengthOfLongestSubstringSet(self, s: str) -> int:
        """
        Sliding Window with Hash Set:

        Algorithmic Intuition:
        - Maintain a set `seen` of characters in the window [left, right].
        - If `s[right]` is already in `seen`, contract the window from the left (`seen.remove(s[left]); left += 1`)
          until `s[right]` is removed.
        - Add `s[right]` to `seen` and update `max_len`.

        Complexity:
        - Time Complexity:  O(n) - Each character is inserted and deleted at most once.
        - Space Complexity: O(min(m, n)).
        """
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_longest_substring_without_repeating_characters():
    sol = Solution()

    # Test Case 1: Standard repeating pattern
    s1 = "abcabcbb"
    assert sol.lengthOfLongestSubstring(s1) == 3
    assert sol.lengthOfLongestSubstringSet(s1) == 3

    # Test Case 2: All identical characters
    s2 = "bbbbb"
    assert sol.lengthOfLongestSubstring(s2) == 1
    assert sol.lengthOfLongestSubstringSet(s2) == 1

    # Test Case 3: Repeating characters in middle
    s3 = "pwwkew"
    assert sol.lengthOfLongestSubstring(s3) == 3
    assert sol.lengthOfLongestSubstringSet(s3) == 3

    # Test Case 4: Empty string
    s4 = ""
    assert sol.lengthOfLongestSubstring(s4) == 0
    assert sol.lengthOfLongestSubstringSet(s4) == 0

    # Test Case 5: Single character
    s5 = " "
    assert sol.lengthOfLongestSubstring(s5) == 1
    assert sol.lengthOfLongestSubstringSet(s5) == 1

    # Test Case 6: All unique characters
    s6 = "abcdef"
    assert sol.lengthOfLongestSubstring(s6) == 6
    assert sol.lengthOfLongestSubstringSet(s6) == 6

    # Test Case 7: Mixed symbols, spaces, digits
    s7 = "tmmzuxt"
    assert sol.lengthOfLongestSubstring(s7) == 5  # "mzuxt"
    assert sol.lengthOfLongestSubstringSet(s7) == 5

    # Test Case 8: Repeating with spaces and symbols
    s8 = "a b!a b!"
    assert sol.lengthOfLongestSubstring(s8) == 4  # "a b!"
    assert sol.lengthOfLongestSubstringSet(s8) == 4


if __name__ == "__main__":
    test_longest_substring_without_repeating_characters()
    print("All Longest Substring Without Repeating Characters unit tests passed successfully!")
