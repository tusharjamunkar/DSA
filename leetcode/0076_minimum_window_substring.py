"""
0076. Minimum Window Substring
Difficulty: Hard
Topic: Sliding Window / Hash Table / String
LeetCode Link: https://leetcode.com/problems/minimum-window-substring/

Problem Statement:
Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
- m == s.length
- n == t.length
- 1 <= m, n <= 10^5
- s and t consist of uppercase and lowercase English letters.
"""

from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Optimal Sliding Window with Frequency Counts:

        Algorithmic Intuition:
        - Use two frequency tables: `target_count` (required frequencies for t) and
          `window_count` (character frequencies in active window [left, right]).
        - Maintain `have` and `need`:
          - `need = len(target_count)`: number of distinct characters in t that must be fully satisfied.
          - `have`: number of distinct characters currently meeting the target count in the window.
        - Advance `right`:
          - Increment `window_count[s[right]]`.
          - If `window_count[s[right]] == target_count[s[right]]`, increment `have += 1`.
        - While `have == need` (the window is valid):
          - Compare current window length `right - left + 1` with `min_len` and record boundaries.
          - Shrink window from the left: decrement `window_count[s[left]]`.
          - If `window_count[s[left]] < target_count[s[left]]`, decrement `have -= 1`.
          - Advance `left += 1`.

        Complexity:
        - Time Complexity:  O(m + n) - Each character in s is visited at most twice (once by right, once by left).
        - Space Complexity: O(m + n) - At most 52 distinct uppercase and lowercase English letters in hash tables.
        """
        if not t or not s or len(s) < len(t):
            return ""

        target_count = Counter(t)
        window_count = defaultdict(int)

        have, need = 0, len(target_count)
        res, res_len = [-1, -1], float("inf")
        left = 0

        for right, char in enumerate(s):
            window_count[char] += 1

            if char in target_count and window_count[char] == target_count[char]:
                have += 1

            while have == need:
                window_len = right - left + 1
                if window_len < res_len:
                    res = [left, right]
                    res_len = window_len

                # Pop left character
                l_char = s[left]
                window_count[l_char] -= 1
                if l_char in target_count and window_count[l_char] < target_count[l_char]:
                    have -= 1
                left += 1

        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_minimum_window_substring():
    sol = Solution()

    # Test Case 1: Standard multi-candidate window
    assert sol.minWindow("ADOBECODEBANC", "ABC") == "BANC"

    # Test Case 2: Exact single character match
    assert sol.minWindow("a", "a") == "a"

    # Test Case 3: Impossible duplicate requirement
    assert sol.minWindow("a", "aa") == ""

    # Test Case 4: Entire string is minimal window
    assert sol.minWindow("ab", "ab") == "ab"

    # Test Case 5: Duplicate characters in t satisfied
    assert sol.minWindow("aaflslflabb", "aab") == "aflslflab"
    assert sol.minWindow("bdab", "ab") == "ab"

    # Test Case 6: Target character at boundary
    assert sol.minWindow("bba", "ab") == "ba"

    # Test Case 7: Case sensitivity
    assert sol.minWindow("aAbBC", "ABC") == "AbBC"
    assert sol.minWindow("aAbBc", "ABC") == ""


if __name__ == "__main__":
    test_minimum_window_substring()
    print("All Minimum Window Substring unit tests passed successfully!")
