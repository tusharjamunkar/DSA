"""
0020. Valid Parentheses
Difficulty: Easy
Topic: Stack / String
LeetCode Link: https://leetcode.com/problems/valid-parentheses/

Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Optimal Stack Approach:

        Algorithmic Intuition:
        - A closing bracket must match the most recently opened bracket of the same type (LIFO).
        - Maintain a stack of opening brackets.
        - Map each closing bracket to its expected opening counterpart:
          {')': '(', '}': '{', ']': '['}.
        - For each character `c` in `s`:
          - If `c` is a closing bracket:
            - If stack is empty or `stack.pop() != mapping[c]`, then brackets are mismatched.
          - Else:
            - Push `c` onto the stack.
        - After scanning all characters, the string is valid if and only if the stack is empty.

        Complexity:
        - Time Complexity:  O(n) - Single pass through string `s`.
        - Space Complexity: O(n) - Stack stores at most n brackets in the worst case (e.g. "(((").
        """
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_valid_parentheses():
    sol = Solution()

    # Test Case 1: Simple valid pairs
    assert sol.isValid("()") is True
    assert sol.isValid("()[]{}") is True

    # Test Case 2: Mismatched pair
    assert sol.isValid("(]") is False

    # Test Case 3: Nested valid brackets
    assert sol.isValid("([])") is True
    assert sol.isValid("{[()]}") is True

    # Test Case 4: Interleaved mismatched brackets
    assert sol.isValid("([)]") is False

    # Test Case 5: Single bracket
    assert sol.isValid("(") is False
    assert sol.isValid("]") is False

    # Test Case 6: Unclosed open brackets
    assert sol.isValid("(()") is False
    assert sol.isValid("((({})))") is True


if __name__ == "__main__":
    test_valid_parentheses()
    print("All Valid Parentheses unit tests passed successfully!")
