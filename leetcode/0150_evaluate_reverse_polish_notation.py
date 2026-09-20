"""
0150. Evaluate Reverse Polish Notation
Difficulty: Medium
Topic: Stack / Array / Math
LeetCode Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

Problem Statement:
You are given an array of strings tokens that represents an arithmetic expression
in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all intermediate calculations can be represented in a 32-bit integer.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Constraints:
- 1 <= tokens.length <= 10^4
- tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Optimal Stack Evaluation:

        Algorithmic Intuition:
        - In postfix notation, operands precede their operator.
        - Maintain a stack of intermediate integer results.
        - Iterate through each token:
          - If the token is an operator:
            - Pop the second operand `b = stack.pop()`.
            - Pop the first operand `a = stack.pop()`.
            - Compute `a (op) b`.
            - Note: In Python, `a // b` floors toward negative infinity (e.g. -7 // 3 = -3).
              The problem specifies truncation toward zero, so we use `int(a / b)`.
            - Push the result back onto the stack.
          - If the token is a number:
            - Convert to integer and push onto the stack.
        - Return the single remaining value on the stack.

        Complexity:
        - Time Complexity:  O(n) - Each token is visited and pushed/popped once.
        - Space Complexity: O(n) - Stack holds at most (n / 2) + 1 numbers.
        """
        stack = []
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),  # Truncate toward zero
        }

        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                stack.append(operators[token](a, b))
            else:
                stack.append(int(token))

        return stack[0]


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_evaluate_reverse_polish_notation():
    sol = Solution()

    # Test Case 1: Simple addition and multiplication
    assert sol.evalRPN(["2", "1", "+", "3", "*"]) == 9

    # Test Case 2: Truncation with division
    assert sol.evalRPN(["4", "13", "5", "/", "+"]) == 6

    # Test Case 3: Complex multi-operator expression
    tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    assert sol.evalRPN(tokens3) == 22

    # Test Case 4: Single token
    assert sol.evalRPN(["18"]) == 18

    # Test Case 5: Negative integer division truncation
    # -7 / 3 = -2.333... -> -2 (not -3)
    assert sol.evalRPN(["-7", "3", "/"]) == -2
    assert sol.evalRPN(["7", "-3", "/"]) == -2

    # Test Case 6: Subtraction order
    assert sol.evalRPN(["5", "3", "-"]) == 2


if __name__ == "__main__":
    test_evaluate_reverse_polish_notation()
    print("All Evaluate Reverse Polish Notation unit tests passed successfully!")
