"""
0110. Balanced Binary Tree
Difficulty: Easy
Topic: Trees / Depth-First Search / Binary Tree
LeetCode Link: https://leetcode.com/problems/balanced-binary-tree/

Problem Statement:
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

Constraints:
- The number of nodes in the tree is in the range [0, 5000].
- -10^4 <= Node.val <= 10^4
"""

from typing import Optional, List, Tuple
from collections import deque


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

    def to_level_order(self) -> List[Optional[int]]:
        res: List[Optional[int]] = []
        queue: deque[Optional[TreeNode]] = deque([self])

        while queue:
            node = queue.popleft()
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append(None)

        while res and res[-1] is None:
            res.pop()
        return res


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Optimal Bottom-Up DFS (Post-order):

        Algorithmic Intuition:
        - Instead of computing heights from top to bottom (which incurs repeated subproblem computations taking O(n^2)),
          we compute height bottom-up in post-order DFS.
        - For each subtree:
          1. Recursively check if the left subtree is balanced and get its height. If unbalanced, immediately propagate -1.
          2. Recursively check if the right subtree is balanced and get its height. If unbalanced, immediately propagate -1.
          3. If abs(left_height - right_height) > 1, the current node violates balance; return -1.
          4. Otherwise, return the true height: 1 + max(left_height, right_height).
        - The tree is balanced if dfs(root) != -1.

        Complexity:
        - Time Complexity:  O(n) - Every node is visited at most once.
        - Space Complexity: O(h) - Where h is tree height (O(log n) balanced, O(n) degenerate call stack).
        """
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_height = dfs(node.left)
            if left_height == -1:
                return -1

            right_height = dfs(node.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return 1 + max(left_height, right_height)

        return dfs(root) != -1

    def isBalancedTuple(self, root: Optional[TreeNode]) -> bool:
        """
        Alternative Tuple-based Bottom-Up DFS:
        Returns (is_balanced, height) for each subtree.
        """
        def dfs(node: Optional[TreeNode]) -> Tuple[bool, int]:
            if not node:
                return True, 0

            left_balanced, left_h = dfs(node.left)
            if not left_balanced:
                return False, 0

            right_balanced, right_h = dfs(node.right)
            if not right_balanced:
                return False, 0

            balanced = abs(left_h - right_h) <= 1
            return balanced, 1 + max(left_h, right_h)

        return dfs(root)[0]


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_balanced_binary_tree():
    sol = Solution()

    # Test Case 1: [3,9,20,null,null,15,7] -> True
    t1 = TreeNode.from_level_order([3, 9, 20, None, None, 15, 7])
    assert sol.isBalanced(t1) is True
    assert sol.isBalancedTuple(t1) is True

    # Test Case 2: [1,2,2,3,3,null,null,4,4] -> False
    t2 = TreeNode.from_level_order([1, 2, 2, 3, 3, None, None, 4, 4])
    assert sol.isBalanced(t2) is False
    assert sol.isBalancedTuple(t2) is False

    # Test Case 3: Empty tree [] -> True
    assert sol.isBalanced(None) is True
    assert sol.isBalancedTuple(None) is True

    # Test Case 4: Single node [1] -> True
    t4 = TreeNode(1)
    assert sol.isBalanced(t4) is True
    assert sol.isBalancedTuple(t4) is True

    # Test Case 5: Skewed line [1,2,null,3,null,4] -> False
    t5 = TreeNode.from_level_order([1, 2, None, 3, None, 4])
    assert sol.isBalanced(t5) is False
    assert sol.isBalancedTuple(t5) is False


if __name__ == "__main__":
    test_balanced_binary_tree()
    print("All Balanced Binary Tree unit tests passed successfully!")
