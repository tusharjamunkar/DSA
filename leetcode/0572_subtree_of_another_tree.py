"""
0572. Subtree of Another Tree
Difficulty: Easy
Topic: Trees / Depth-First Search / String Matching / Binary Tree / Hash Function
LeetCode Link: https://leetcode.com/problems/subtree-of-another-tree/

Problem Statement:
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Constraints:
- The number of nodes in the root tree is in the range [1, 2000].
- The number of nodes in the subRoot tree is in the range [1, 1000].
- -10^4 <= root.val <= 10^4
- -10^4 <= subRoot.val <= 10^4
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Optimal Recursive DFS (Subtree Pattern Matching):

        Algorithmic Intuition:
        - Base Cases:
          - If subRoot is None: An empty tree is always a valid subtree of any tree -> True.
          - If root is None (and subRoot is not None): An empty tree cannot contain a non-empty subtree -> False.
        - Check if current root and subRoot are identical using `isSameTree(root, subRoot)`.
        - If not, recursively check whether subRoot is a subtree of the left child OR right child:
          `self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)`.

        Complexity:
        - Time Complexity:  O(m * n) - Where m is nodes in root and n is nodes in subRoot. In worst case (skewed identical values), we check isSameTree at every node.
        - Space Complexity: O(h_root) - Recursion depth bounded by height of root tree.
        """
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Helper to determine if two binary trees are identical."""
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtreeSerialization(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Alternative Preorder Serialization Approach (Linear String Matching):
        Serializes both trees into unambiguous string representations (delimiting values with '#' and nulls with 'null').
        Then checks if subRoot string is a substring of root string.

        Complexity:
        - Time Complexity:  O(m + n) with KMP/Rabin-Karp (or standard Python 'in' operator).
        - Space Complexity: O(m + n) for serialization storage.
        """
        def serialize(node: Optional[TreeNode]) -> str:
            if not node:
                return ",#null"
            return f",#{node.val}" + serialize(node.left) + serialize(node.right)

        root_str = serialize(root)
        sub_str = serialize(subRoot)
        return sub_str in root_str


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_subtree_of_another_tree():
    sol = Solution()

    # Test Case 1: root = [3,4,5,1,2], subRoot = [4,1,2] -> True
    r1 = TreeNode.from_level_order([3, 4, 5, 1, 2])
    s1 = TreeNode.from_level_order([4, 1, 2])
    assert sol.isSubtree(r1, s1) is True
    assert sol.isSubtreeSerialization(r1, s1) is True

    # Test Case 2: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2] -> False
    r2 = TreeNode.from_level_order([3, 4, 5, 1, 2, None, None, None, None, 0])
    s2 = TreeNode.from_level_order([4, 1, 2])
    assert sol.isSubtree(r2, s2) is False
    assert sol.isSubtreeSerialization(r2, s2) is False

    # Test Case 3: Identical trees [1, 1] and [1, 1] -> True
    r3 = TreeNode.from_level_order([1, 1])
    s3 = TreeNode.from_level_order([1, 1])
    assert sol.isSubtree(r3, s3) is True
    assert sol.isSubtreeSerialization(r3, s3) is True

    # Test Case 4: subRoot is single node matching a leaf
    r4 = TreeNode.from_level_order([1, 2, 3])
    s4 = TreeNode(3)
    assert sol.isSubtree(r4, s4) is True
    assert sol.isSubtreeSerialization(r4, s4) is True


if __name__ == "__main__":
    test_subtree_of_another_tree()
    print("All Subtree of Another Tree unit tests passed successfully!")
