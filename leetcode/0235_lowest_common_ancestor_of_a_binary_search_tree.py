"""
0235. Lowest Common Ancestor of a Binary Search Tree
Difficulty: Medium
Topic: Trees / Binary Search Tree / Depth-First Search / Binary Tree
LeetCode Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Problem Statement:
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2

Constraints:
- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p != q
- p and q will exist in the BST.
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

    def find_node(self, target: int) -> Optional["TreeNode"]:
        """Helper to find a node with a specific value in the subtree."""
        if self.val == target:
            return self
        if target < self.val and self.left:
            return self.left.find_node(target)
        if target > self.val and self.right:
            return self.right.find_node(target)
        return None


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        """
        Optimal Iterative BST Search:

        Algorithmic Intuition:
        - In a Binary Search Tree (BST), the left child is strictly smaller and the right child is strictly larger.
        - Starting from `root`:
          1. If both `p.val > curr.val` and `q.val > curr.val`:
             Both nodes reside entirely in the right subtree -> move `curr = curr.right`.
          2. If both `p.val < curr.val` and `q.val < curr.val`:
             Both nodes reside entirely in the left subtree -> move `curr = curr.left`.
          3. Otherwise (a split occurs, or `curr` equals `p` or `q`):
             `curr` is the lowest common ancestor where the search paths diverge!

        Complexity:
        - Time Complexity:  O(h) - Where h is tree height (O(log n) balanced BST, O(n) degenerate BST).
        - Space Complexity: O(1) - Constant auxiliary space for pointer traversal.
        """
        curr: Optional[TreeNode] = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr

        return root

    def lowestCommonAncestorRecursive(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        """
        Alternative Recursive BST LCA:

        Complexity:
        - Time Complexity:  O(h)
        - Space Complexity: O(h) - Call stack recursion frames.
        """
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestorRecursive(root.right, p, q)  # type: ignore
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestorRecursive(root.left, p, q)  # type: ignore
        return root


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_lowest_common_ancestor_bst():
    sol = Solution()

    # Tree: [6,2,8,0,4,7,9,null,null,3,5]
    tree = TreeNode.from_level_order([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    assert tree is not None

    p1 = tree.find_node(2)
    q1 = tree.find_node(8)
    assert p1 and q1
    lca1 = sol.lowestCommonAncestor(tree, p1, q1)
    lca1_rec = sol.lowestCommonAncestorRecursive(tree, p1, q1)
    assert lca1.val == 6 and lca1_rec.val == 6

    # Test Case 2: p = 2, q = 4 -> LCA is 2
    p2 = tree.find_node(2)
    q2 = tree.find_node(4)
    assert p2 and q2
    lca2 = sol.lowestCommonAncestor(tree, p2, q2)
    lca2_rec = sol.lowestCommonAncestorRecursive(tree, p2, q2)
    assert lca2.val == 2 and lca2_rec.val == 2

    # Test Case 3: p = 3, q = 5 -> LCA is 4
    p3 = tree.find_node(3)
    q3 = tree.find_node(5)
    assert p3 and q3
    lca3 = sol.lowestCommonAncestor(tree, p3, q3)
    lca3_rec = sol.lowestCommonAncestorRecursive(tree, p3, q3)
    assert lca3.val == 4 and lca3_rec.val == 4

    # Test Case 4: Tree [2, 1], p = 2, q = 1 -> LCA is 2
    tree2 = TreeNode.from_level_order([2, 1])
    assert tree2 is not None
    p4 = tree2.find_node(2)
    q4 = tree2.find_node(1)
    assert p4 and q4
    lca4 = sol.lowestCommonAncestor(tree2, p4, q4)
    assert lca4.val == 2


if __name__ == "__main__":
    test_lowest_common_ancestor_bst()
    print("All Lowest Common Ancestor BST unit tests passed successfully!")
