"""
0098. Validate Binary Search Tree
Difficulty: Medium
Topic: Trees / Depth-First Search / Binary Search Tree / Binary Tree
LeetCode Link: https://leetcode.com/problems/validate-binary-search-tree/

Problem Statement:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys strictly less than the node's key.
- The right subtree of a node contains only nodes with keys strictly greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1
"""

from typing import Optional, List
from collections import deque
import math


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_level_order(cls, values: List[Optional[int]]) -> Optional["TreeNode"]:
        if not values or values[0] is None:
            return None

        root = cls(values[0])
        queue: deque[TreeNode] = deque([root])
        i = 1

        while queue and i < len(values):
            curr = queue.popleft()

            if i < len(values) and values[i] is not None:
                curr.left = cls(values[i])  # type: ignore
                queue.append(curr.left)
            i += 1

            if i < len(values) and values[i] is not None:
                curr.right = cls(values[i])  # type: ignore
                queue.append(curr.right)
            i += 1

        return root


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Optimal Recursive DFS with Valid Range Bounds:

        Algorithmic Intuition:
        - A node is valid in a BST if its value strictly lies within an open interval `(low, high)`.
        - Initially for `root`, the valid range is `(-infinity, +infinity)`.
        - When branching into the left child:
          - All left descendant values must be `< node.val`, so the upper bound becomes `node.val` -> `(low, node.val)`.
        - When branching into the right child:
          - All right descendant values must be `> node.val`, so the lower bound becomes `node.val` -> `(node.val, high)`.
        - If any node violates `low < node.val < high`, immediately return False.

        Complexity:
        - Time Complexity:  O(n) - Every node is verified once.
        - Space Complexity: O(h) - Call stack recursion depth (O(log n) balanced, O(n) degenerate).
        """
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True

            if not (low < node.val < high):
                return False

            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root, -math.inf, math.inf)

    def isValidBSTInorder(self, root: Optional[TreeNode]) -> bool:
        """
        Alternative Iterative In-Order Traversal with Stack:
        In-order traversal of a valid BST must produce a strictly monotonically increasing sequence.

        Complexity:
        - Time Complexity:  O(n)
        - Space Complexity: O(h) - Explicit stack frames.
        """
        stack: List[TreeNode] = []
        curr = root
        prev_val = -math.inf

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            if curr.val <= prev_val:
                return False
            prev_val = curr.val

            curr = curr.right

        return True


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_validate_binary_search_tree():
    sol = Solution()

    # Test Case 1: [2,1,3] -> True
    t1 = TreeNode.from_level_order([2, 1, 3])
    assert sol.isValidBST(t1) is True
    assert sol.isValidBSTInorder(t1) is True

    # Test Case 2: [5,1,4,null,null,3,6] -> False
    t2 = TreeNode.from_level_order([5, 1, 4, None, None, 3, 6])
    assert sol.isValidBST(t2) is False
    assert sol.isValidBSTInorder(t2) is False

    # Test Case 3: Tricky violation in deep right-left subtree [5,4,6,null,null,3,7] -> False (3 < 5)
    t3 = TreeNode.from_level_order([5, 4, 6, None, None, 3, 7])
    assert sol.isValidBST(t3) is False
    assert sol.isValidBSTInorder(t3) is False

    # Test Case 4: Single node [1] -> True
    t4 = TreeNode(1)
    assert sol.isValidBST(t4) is True
    assert sol.isValidBSTInorder(t4) is True

    # Test Case 5: Duplicate values [2,2,2] -> False (strictly less/greater required)
    t5 = TreeNode.from_level_order([2, 2, 2])
    assert sol.isValidBST(t5) is False
    assert sol.isValidBSTInorder(t5) is False


if __name__ == "__main__":
    test_validate_binary_search_tree()
    print("All Validate Binary Search Tree unit tests passed successfully!")
