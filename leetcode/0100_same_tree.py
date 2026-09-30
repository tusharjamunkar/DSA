"""
0100. Same Tree
Difficulty: Easy
Topic: Trees / Depth-First Search / Breadth-First Search / Binary Tree
LeetCode Link: https://leetcode.com/problems/same-tree/

Problem Statement:
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
- The number of nodes in both trees is in the range [0, 100].
- -10^4 <= Node.val <= 10^4
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Optimal Recursive DFS:

        Algorithmic Intuition:
        - Base Cases:
          1. If both p and q are None: structurally identical empty subtrees -> True.
          2. If only one is None or values differ (p.val != q.val) -> False.
        - Recursive Step:
          - Check if left subtrees are identical: self.isSameTree(p.left, q.left)
          - Check if right subtrees are identical: self.isSameTree(p.right, q.right)
          - Return conjunction of both.

        Complexity:
        - Time Complexity:  O(min(n, m)) - In worst case visits all nodes up to smaller tree.
        - Space Complexity: O(min(h_p, h_q)) - Call stack bounded by height of trees.
        """
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTreeBFS(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Alternative Iterative BFS with Queue:
        Pushes pairs of nodes into a double queue to verify level-by-level structural equivalence.

        Complexity:
        - Time Complexity:  O(min(n, m))
        - Space Complexity: O(min(w_p, w_q)) - Maximum queue width.
        """
        queue: deque[Tuple[Optional[TreeNode], Optional[TreeNode]]] = deque([(p, q)])

        while queue:
            node_p, node_q = queue.popleft()

            if not node_p and not node_q:
                continue
            if not node_p or not node_q or node_p.val != node_q.val:
                return False

            queue.append((node_p.left, node_q.left))
            queue.append((node_p.right, node_q.right))

        return True


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_same_tree():
    sol = Solution()

    # Test Case 1: p = [1,2,3], q = [1,2,3] -> True
    p1 = TreeNode.from_level_order([1, 2, 3])
    q1 = TreeNode.from_level_order([1, 2, 3])
    assert sol.isSameTree(p1, q1) is True
    assert sol.isSameTreeBFS(p1, q1) is True

    # Test Case 2: p = [1,2], q = [1,null,2] -> False
    p2 = TreeNode.from_level_order([1, 2])
    q2 = TreeNode.from_level_order([1, None, 2])
    assert sol.isSameTree(p2, q2) is False
    assert sol.isSameTreeBFS(p2, q2) is False

    # Test Case 3: p = [1,2,1], q = [1,1,2] -> False
    p3 = TreeNode.from_level_order([1, 2, 1])
    q3 = TreeNode.from_level_order([1, 1, 2])
    assert sol.isSameTree(p3, q3) is False
    assert sol.isSameTreeBFS(p3, q3) is False

    # Test Case 4: Both None -> True
    assert sol.isSameTree(None, None) is True
    assert sol.isSameTreeBFS(None, None) is True


if __name__ == "__main__":
    test_same_tree()
    print("All Same Tree unit tests passed successfully!")
