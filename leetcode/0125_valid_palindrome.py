"""
0125. Valid Palindrome
Difficulty: Easy
Topic: Two Pointers / String
LeetCode Link: https://leetcode.com/problems/valid-palindrome/

Problem Statement:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Optimal Two-Pointer In-Place Approach:
        - Place two pointers: `left` at the start (0) and `right` at the end (len(s) - 1).
        - Advance `left` forward while the character at `s[left]` is not alphanumeric.
        - Move `right` backward while the character at `s[right]` is not alphanumeric.
        - Once both point to alphanumeric characters:
          - Compare `s[left].lower()` with `s[right].lower()`.
          - If they do not match, return False immediately.
          - If they match, increment `left` and decrement `right`.
        - If the pointers cross (`left >= right`), the entire string is verified as a palindrome.

        Why this is optimal:
        - Avoids creating an intermediate sanitized string or array of characters.
        - Evaluates in-place with zero heap allocations for character arrays.

        Time Complexity:  O(n) - Single pass over string length n; each pointer moves at most n times.
        Space Complexity: O(1) - Constant auxiliary space (only two integer pointers).
        """
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

    def isPalindromeFiltered(self, s: str) -> bool:
        """
        Filtered String Comparison Approach (Alternative):
        - Filter out all non-alphanumeric characters and convert to lowercase.
        - Compare the sanitized string against its reversed slice `[::-1]`.

        Time Complexity:  O(n) - Filtering takes O(n), reversing takes O(n), comparison takes O(n).
        Space Complexity: O(n) - Requires storing the filtered string and reversed string in memory.
        """
        filtered = [c.lower() for c in s if c.isalnum()]
        return filtered == filtered[::-1]


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_valid_palindrome():
    sol = Solution()

    # Test Case 1: Standard palindrome with spaces and punctuation
    s1 = "A man, a plan, a canal: Panama"
    assert sol.isPalindrome(s1) is True
    assert sol.isPalindromeFiltered(s1) is True

    # Test Case 2: Non-palindrome
    s2 = "race a car"
    assert sol.isPalindrome(s2) is False
    assert sol.isPalindromeFiltered(s2) is False

    # Test Case 3: Empty / Whitespace-only string
    s3 = " "
    assert sol.isPalindrome(s3) is True
    assert sol.isPalindromeFiltered(s3) is True

    # Test Case 4: Alphanumeric mismatch with digits
    s4 = "0P"
    assert sol.isPalindrome(s4) is False
    assert sol.isPalindromeFiltered(s4) is False

    # Test Case 5: Single character
    s5 = "a"
    assert sol.isPalindrome(s5) is True
    assert sol.isPalindromeFiltered(s5) is True

    # Test Case 6: Punctuation and underscore handling
    s6 = "ab_a"
    assert sol.isPalindrome(s6) is True
    assert sol.isPalindromeFiltered(s6) is True

    # Test Case 7: Numbers palindrome
    s7 = "12321"
    assert sol.isPalindrome(s7) is True
    assert sol.isPalindromeFiltered(s7) is True

    # Test Case 8: Numbers non-palindrome
    s8 = "123421"
    assert sol.isPalindrome(s8) is False
    assert sol.isPalindromeFiltered(s8) is False


if __name__ == "__main__":
    test_valid_palindrome()
    print("All Valid Palindrome tests passed successfully!")
