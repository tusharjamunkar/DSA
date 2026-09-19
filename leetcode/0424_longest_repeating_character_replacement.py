"""
0424. Longest Repeating Character Replacement
Difficulty: Medium
Topic: Sliding Window / Hash Table / String
LeetCode Link: https://leetcode.com/problems/longest-repeating-character-replacement/

Problem Statement:
You are given a string s and an integer k. You can choose any character of the string
and change it to any other uppercase English character. You can perform this operation
at most k times.

Return the length of the longest substring containing the same letter you can get after
performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only uppercase English letters.
- 0 <= k <= s.length
"""

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Optimal Sliding Window Approach:

        Algorithmic Intuition:
        - A substring of length `L = right - left + 1` can be made into all identical characters
          if `L - max_frequency <= k`, meaning the number of characters we must change to match
          the most frequent character in the window does not exceed `k`.
        - Maintain a frequency map `count` of characters within window [left, right].
        - Track `max_freq`: the maximum frequency of any single character ever seen in any valid window.
          Key Insight: We never need to decrement `max_freq` when shrinking the window because a window
          can only beat our global `max_len` if it contains a character with frequency > `max_freq`.
        - If `(right - left + 1) - max_freq > k`, the current window is invalid:
          - Decrement `count[s[left]]` and advance `left += 1`.
        - The maximum window length reached is `len(s) - left` or accumulated `max_len`.

        Complexity:
        - Time Complexity:  O(n) - Both pointers only move forward.
        - Space Complexity: O(26) = O(1) - Only uppercase English letters stored in frequency map.
        """
        count = defaultdict(int)
        max_freq = 0
        left = 0
        max_len = 0

        for right in range(len(s)):
            count[s[right]] += 1
            if count[s[right]] > max_freq:
                max_freq = count[s[right]]

            # If current window requires more than k replacements, shift left boundary
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_longest_repeating_character_replacement():
    sol = Solution()

    # Test Case 1: Example 1
    assert sol.characterReplacement("ABAB", 2) == 4

    # Test Case 2: Example 2
    assert sol.characterReplacement("AABABBA", 1) == 4

    # Test Case 3: k = 0 (no replacement allowed, longest contiguous identical run)
    assert sol.characterReplacement("ABBB", 0) == 3

    # Test Case 4: Single character string
    assert sol.characterReplacement("A", 0) == 1

    # Test Case 5: Entire string can be replaced (k >= len(s))
    assert sol.characterReplacement("ABCDE", 5) == 5

    # Test Case 6: Alternating characters with k = 1
    assert sol.characterReplacement("ABAA", 0) == 2
    assert sol.characterReplacement("ABAA", 1) == 4

    # Test Case 7: All same characters
    assert sol.characterReplacement("AAAA", 2) == 4


if __name__ == "__main__":
    test_longest_repeating_character_replacement()
    print("All Longest Repeating Character Replacement unit tests passed successfully!")
