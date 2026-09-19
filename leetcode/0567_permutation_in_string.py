"""
0567. Permutation in String
Difficulty: Medium
Topic: Sliding Window / Hash Table / Two Pointers
LeetCode Link: https://leetcode.com/problems/permutation-in-string/

Problem Statement:
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
- 1 <= s1.length, s2.length <= 10^4
- s1 and s2 consist of lowercase English letters.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Optimal Fixed-Length Sliding Window with Match Counter:

        Algorithmic Intuition:
        - A permutation of s1 inside s2 must have the exact same length: `k = len(s1)`.
        - Maintain two 26-element frequency arrays: `s1_count` and `s2_count`.
        - Instead of comparing all 26 elements at every shift (O(26 * n)), maintain a scalar
          `matches` tracking how many letters currently have identical counts in both s1 and the
          active s2 window.
        - As the window slides by adding `s2[right]` and removing `s2[left]`:
          - Update counts and adjust `matches` in O(1) time.
          - If `matches == 26`, an exact permutation is found!

        Complexity:
        - Time Complexity:  O(n) where n = len(s2). Initializing takes O(len(s1)), each slide is O(1).
        - Space Complexity: O(1) - Fixed 26-element integer arrays.
        """
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            r_idx = ord(s2[right]) - ord("a")
            s2_count[r_idx] += 1
            if s2_count[r_idx] == s1_count[r_idx]:
                matches += 1
            elif s2_count[r_idx] == s1_count[r_idx] + 1:
                matches -= 1

            l_idx = ord(s2[left]) - ord("a")
            s2_count[l_idx] -= 1
            if s2_count[l_idx] == s1_count[l_idx]:
                matches += 1
            elif s2_count[l_idx] == s1_count[l_idx] - 1:
                matches -= 1

            left += 1

        return matches == 26

    def checkInclusionDirect(self, s1: str, s2: str) -> bool:
        """
        Direct Array Comparison Sliding Window:

        Algorithmic Intuition:
        - Slide a window of length len(s1) and compare the 26-element array directly at each step.
        - Time Complexity: O(26 * n) = O(n).
        - Space Complexity: O(1).
        """
        if len(s1) > len(s2):
            return False

        target = [0] * 26
        for c in s1:
            target[ord(c) - ord("a")] += 1

        window = [0] * 26
        k = len(s1)
        for i in range(k):
            window[ord(s2[i]) - ord("a")] += 1

        if window == target:
            return True

        for i in range(k, len(s2)):
            window[ord(s2[i]) - ord("a")] += 1
            window[ord(s2[i - k]) - ord("a")] -= 1
            if window == target:
                return True

        return False


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_permutation_in_string():
    sol = Solution()

    # Test Case 1: Standard positive permutation
    assert sol.checkInclusion("ab", "eidbaooo") is True
    assert sol.checkInclusionDirect("ab", "eidbaooo") is True

    # Test Case 2: Standard negative permutation
    assert sol.checkInclusion("ab", "eidboaoo") is False
    assert sol.checkInclusionDirect("ab", "eidboaoo") is False

    # Test Case 3: s1 longer than s2
    assert sol.checkInclusion("hello", "he") is False
    assert sol.checkInclusionDirect("hello", "he") is False

    # Test Case 4: Exact match
    assert sol.checkInclusion("abc", "cba") is True
    assert sol.checkInclusionDirect("abc", "cba") is True

    # Test Case 5: Single character matches
    assert sol.checkInclusion("a", "a") is True
    assert sol.checkInclusion("a", "b") is False

    # Test Case 6: Permutation at the very end
    assert sol.checkInclusion("adc", "dcda") is True
    assert sol.checkInclusionDirect("adc", "dcda") is True

    # Test Case 7: Duplicate characters
    assert sol.checkInclusion("aab", "baab") is True
    assert sol.checkInclusion("aab", "baba") is True
    assert sol.checkInclusion("aab", "aba") is True
    assert sol.checkInclusion("aab", "abb") is False


if __name__ == "__main__":
    test_permutation_in_string()
    print("All Permutation in String unit tests passed successfully!")
