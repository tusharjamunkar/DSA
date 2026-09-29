"""
0226. Invert Binary Tree
Difficulty: Easy
Topic: Trees / Depth-First Search / Breadth-First Search / Binary Tree
LeetCode Link: https://leetcode.com/problems/invert-binary-tree/

Problem Statement:
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 100].
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Optimal Recursive DFS Inversion:

        Algorithmic Intuition:
        - Base case: If root is None, return None.
        - Recursively invert the left and right subtrees.
        - Swap the left and right child pointers:
          `root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)`
        - Return the root.

        Complexity:
        - Time Complexity:  O(n) - Visits each node exactly once.
        - Space Complexity: O(h) - Where h is the tree height (call stack frames: O(log n) balanced, O(n) worst).
        """
        if not root:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    def invertTreeBFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Alternative Iterative BFS Inversion:
        Uses a queue to level-order traverse and swap children at each node.

        Complexity:
        - Time Complexity:  O(n)
        - Space Complexity: O(n) - Maximum queue width.
        """
        if not root:
            return None

        queue: deque[TreeNode] = deque([root])
        while queue:
            curr = queue.popleft()
            curr.left, curr.right = curr.right, curr.left

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return root


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_invert_binary_tree():
    sol = Solution()

    # Test Case 1: [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]
    t1 = TreeNode.from_level_order([4, 2, 7, 1, 3, 6, 9])
    inv1 = sol.invertTree(t1)
    assert inv1 is not None and inv1.to_level_order() == [4, 7, 2, 9, 6, 3, 1]

    # Test Case 1 (BFS variant):
    t1_bfs = TreeNode.from_level_order([4, 2, 7, 1, 3, 6, 9])
    inv1_bfs = sol.invertTreeBFS(t1_bfs)
    assert inv1_bfs is not None and inv1_bfs.to_level_order() == [4, 7, 2, 9, 6, 3, 1]

    # Test Case 2: [2,1,3] -> [2,3,1]
    t2 = TreeNode.from_level_order([2, 1, 3])
    inv2 = sol.invertTree(t2)
    assert inv2 is not None and inv2.to_level_order() == [2, 3, 1]

    # Test Case 3: Empty tree [] -> []
    assert sol.invertTree(None) is None
    assert sol.invertTreeBFS(None) is None


if __name__ == "__main__":
    test_invert_binary_tree()
    print("All Invert Binary Tree unit tests passed successfully!")
