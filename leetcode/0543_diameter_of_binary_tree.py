"""
0543. Diameter of Binary Tree
Difficulty: Easy
Topic: Trees / Depth-First Search / Binary Tree
LeetCode Link: https://leetcode.com/problems/diameter-of-binary-tree/

Problem Statement:
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -100 <= Node.val <= 100
"""

from typing import Optional, List
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


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Optimal Bottom-Up Post-Order DFS:

        Algorithmic Intuition:
        - The diameter through any given node `N` is `height(N.left) + height(N.right)`.
        - A single post-order traversal computes the height of each subtree while
          simultaneously tracking the global maximum diameter.
        - Helper `dfs(node)` returns the height of the subtree rooted at `node`:
          `height = 1 + max(left_height, right_height)`.
        - At each step, update `max_diameter = max(max_diameter, left_height + right_height)`.

        Complexity:
        - Time Complexity:  O(n) - Single pass through all n nodes.
        - Space Complexity: O(h) - Height of recursion call stack.
        """
        max_diameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal max_diameter
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # Update maximum path length (number of edges = sum of heights)
            max_diameter = max(max_diameter, left_height + right_height)

            return 1 + max(left_height, right_height)

        dfs(root)
        return max_diameter


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_diameter_of_binary_tree():
    sol = Solution()

    # Test Case 1: [1, 2, 3, 4, 5] -> 3 (Path: 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3)
    t1 = TreeNode.from_level_order([1, 2, 3, 4, 5])
    assert sol.diameterOfBinaryTree(t1) == 3

    # Test Case 2: [1, 2] -> 1
    t2 = TreeNode.from_level_order([1, 2])
    assert sol.diameterOfBinaryTree(t2) == 1

    # Test Case 3: Empty tree -> 0
    assert sol.diameterOfBinaryTree(None) == 0

    # Test Case 4: Deep path entirely in left subtree
    # Tree where longest path doesn't pass through root
    t4 = TreeNode.from_level_order([1, 2, None, 3, 4, 5, None, None, 6])
    assert sol.diameterOfBinaryTree(t4) == 4


if __name__ == "__main__":
    test_diameter_of_binary_tree()
    print("All Diameter of Binary Tree unit tests passed successfully!")
