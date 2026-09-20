"""
0155. Min Stack
Difficulty: Medium
Topic: Stack / Design
LeetCode Link: https://leetcode.com/problems/min-stack/

Problem Statement:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Example 1:
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output:
[null,null,null,null,-3,null,0,-2]

Explanation:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:
- -2^31 <= val <= 2^31 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks.
- At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
"""


class MinStack:
    """
    Optimal Two-Stack Design:

    Algorithmic Intuition:
    - Standard stacks cannot query the minimum in O(1) without extra state.
    - We maintain two parallel stacks:
      1. `stack`: Stores all actual values pushed.
      2. `min_stack`: Stores the current running minimum at each stack height.
    - On `push(val)`:
      - Always push `val` to `stack`.
      - Push `min(val, min_stack[-1])` to `min_stack` (or `val` if `min_stack` is empty).
    - On `pop()`:
      - Pop from both `stack` and `min_stack`.
    - On `top()`:
      - Return `stack[-1]`.
    - On `getMin()`:
      - Return `min_stack[-1]`.

    Complexity:
    - Time Complexity:  O(1) for push, pop, top, and getMin.
    - Space Complexity: O(n) total auxiliary space.
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


class MinStackPair:
    """
    Alternative Single-Stack Design using (value, current_min) tuples:
    """

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        cur_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, cur_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_min_stack():
    for StackClass in [MinStack, MinStackPair]:
        ms = StackClass()
        ms.push(-2)
        ms.push(0)
        ms.push(-3)
        assert ms.getMin() == -3
        ms.pop()
        assert ms.top() == 0
        assert ms.getMin() == -2

        # Test Case 2: Duplicate minimums
        ms2 = StackClass()
        ms2.push(2)
        ms2.push(0)
        ms2.push(3)
        ms2.push(0)
        assert ms2.getMin() == 0
        ms2.pop()
        assert ms2.getMin() == 0
        ms2.pop()
        assert ms2.getMin() == 0
        ms2.pop()
        assert ms2.getMin() == 2

        # Test Case 3: Monotonically decreasing values
        ms3 = StackClass()
        ms3.push(5)
        ms3.push(4)
        ms3.push(3)
        ms3.push(2)
        ms3.push(1)
        assert ms3.getMin() == 1
        ms3.pop()
        assert ms3.getMin() == 2


if __name__ == "__main__":
    test_min_stack()
    print("All Min Stack unit tests passed successfully!")
