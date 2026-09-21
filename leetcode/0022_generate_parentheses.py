"""
0022. Generate Parentheses
Difficulty: Medium
Topic: Stack / Backtracking / String
LeetCode Link: https://leetcode.com/problems/generate-parentheses/

Problem Statement:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
- 1 <= n <= 8
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Optimal Backtracking with Stack / State Variables:

        Algorithmic Intuition:
        - We build well-formed parentheses combinations incrementally.
        - Two strict invariants govern valid transitions:
          1. Can add an opening bracket '(' only if open_count < n.
          2. Can add a closing bracket ')' only if close_count < open_count.
        - When open_count == close_count == n, the current path is a valid combination.

        Complexity:
        - Time Complexity:  O(4^n / sqrt(n)) - Bound by the n-th Catalan number C_n = (1 / (n+1)) * (2n choose n).
        - Space Complexity: O(n) - Maximum recursion depth is 2n for the stack path.
        """
        result = []
        stack = []

        def backtrack(open_count: int, close_count: int) -> None:
            if open_count == close_count == n:
                result.append("".join(stack))
                return

            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, close_count)
                stack.pop()

            if close_count < open_count:
                stack.append(")")
                backtrack(open_count, close_count + 1)
                stack.pop()

        backtrack(0, 0)
        return result


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_generate_parentheses():
    sol = Solution()

    # Test Case 1: n = 1
    assert sol.generateParenthesis(1) == ["()"]

    # Test Case 2: n = 2
    assert sorted(sol.generateParenthesis(2)) == sorted(["(())", "()()"])

    # Test Case 3: n = 3
    expected_3 = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert sorted(sol.generateParenthesis(3)) == sorted(expected_3)

    # Test Case 4: Catalan number count validation for n = 4 (C_4 = 14)
    res_4 = sol.generateParenthesis(4)
    assert len(res_4) == 14
    for p in res_4:
        # Check every generated string is balanced
        bal = 0
        for ch in p:
            bal += 1 if ch == "(" else -1
            assert bal >= 0
        assert bal == 0


if __name__ == "__main__":
    test_generate_parentheses()
    print("All Generate Parentheses unit tests passed successfully!")
