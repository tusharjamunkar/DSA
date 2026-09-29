"""
0104. Maximum Depth of Binary Tree
Difficulty: Easy
Topic: Trees / Depth-First Search / Breadth-First Search / Binary Tree
LeetCode Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Problem Statement:
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Optimal Recursive DFS Depth Computation:

        Algorithmic Intuition:
        - Base case: If root is None, depth is 0.
        - Recursively calculate the maximum depth of the left and right subtrees.
        - Return `1 + max(maxDepth(root.left), maxDepth(root.right))`.

        Complexity:
        - Time Complexity:  O(n) - Visits every node once.
        - Space Complexity: O(h) - Tree height call stack.
        """
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        """
        Iterative BFS Level-Order Traversal:
        Processes nodes level by level, incrementing depth at each level.

        Complexity:
        - Time Complexity:  O(n)
        - Space Complexity: O(n) - Queue size.
        """
        if not root:
            return 0

        level = 0
        queue: deque[TreeNode] = deque([root])

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1

        return level


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_max_depth():
    sol = Solution()

    # Test Case 1: [3, 9, 20, None, None, 15, 7] -> 3
    t1 = TreeNode.from_level_order([3, 9, 20, None, None, 15, 7])
    assert sol.maxDepth(t1) == 3
    assert sol.maxDepthBFS(t1) == 3

    # Test Case 2: [1, None, 2] -> 2
    t2 = TreeNode.from_level_order([1, None, 2])
    assert sol.maxDepth(t2) == 2
    assert sol.maxDepthBFS(t2) == 2

    # Test Case 3: Empty tree -> 0
    assert sol.maxDepth(None) == 0
    assert sol.maxDepthBFS(None) == 0

    # Test Case 4: Single node [42] -> 1
    t4 = TreeNode.from_level_order([42])
    assert sol.maxDepth(t4) == 1


if __name__ == "__main__":
    test_max_depth()
    print("All Maximum Depth of Binary Tree unit tests passed successfully!")
