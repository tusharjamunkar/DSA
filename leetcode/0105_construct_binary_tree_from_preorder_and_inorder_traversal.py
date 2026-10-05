"""
0105. Construct Binary Tree from Preorder and Inorder Traversal
Difficulty: Medium
Topic: Trees / Array / Hash Table / Divide and Conquer / Binary Tree
LeetCode Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Problem Statement:
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree
and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- preorder and inorder consist of unique values.
- Each value of inorder also appears in preorder.
- preorder is guaranteed to be the preorder traversal of the tree.
- inorder is guaranteed to be the inorder traversal of the tree.
"""

from typing import Optional, List, Dict
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Optimal Hash Map + Index Bounding Divide and Conquer:

        Algorithmic Intuition:
        - In `preorder` traversal [Root, Left Subtree, Right Subtree], the first element is always the root.
        - In `inorder` traversal [Left Subtree, Root, Right Subtree], the root splits all elements into the left and right subtrees.
        - Precompute an `inorder_map` (value -> index) for O(1) root lookups.
        - For a sub-array range in preorder [pre_start, pre_end] and inorder [in_start, in_end]:
          1. Create `root = TreeNode(preorder[pre_start])`.
          2. Find `in_root_idx = inorder_map[root.val]`.
          3. `left_size = in_root_idx - in_start`.
          4. Recurse left:
             - preorder: [pre_start + 1, pre_start + left_size]
             - inorder:  [in_start, in_root_idx - 1]
          5. Recurse right:
             - preorder: [pre_start + left_size + 1, pre_end]
             - inorder:  [in_root_idx + 1, in_end]

        Complexity:
        - Time Complexity:  O(n) - Builds each node in O(1) time using hash map index lookups.
        - Space Complexity: O(n) - O(n) for hash map + O(h) recursion stack.
        """
        inorder_map: Dict[int, int] = {val: idx for idx, val in enumerate(inorder)}

        def helper(pre_start: int, pre_end: int, in_start: int, in_end: int) -> Optional[TreeNode]:
            if pre_start > pre_end or in_start > in_end:
                return None

            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            in_root_idx = inorder_map[root_val]
            left_size = in_root_idx - in_start

            root.left = helper(pre_start + 1, pre_start + left_size, in_start, in_root_idx - 1)
            root.right = helper(pre_start + left_size + 1, pre_end, in_root_idx + 1, in_end)

            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_build_tree():
    sol = Solution()

    # Test Case 1: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7] -> [3,9,20,null,null,15,7]
    pre1 = [3, 9, 20, 15, 7]
    in1 = [9, 3, 15, 20, 7]
    tree1 = sol.buildTree(pre1, in1)
    assert tree1 is not None and tree1.to_level_order() == [3, 9, 20, None, None, 15, 7]

    # Test Case 2: preorder = [-1], inorder = [-1] -> [-1]
    pre2 = [-1]
    in2 = [-1]
    tree2 = sol.buildTree(pre2, in2)
    assert tree2 is not None and tree2.to_level_order() == [-1]

    # Test Case 3: Left-skewed tree: preorder = [1, 2, 3], inorder = [3, 2, 1] -> [1, 2, null, 3]
    pre3 = [1, 2, 3]
    in3 = [3, 2, 1]
    tree3 = sol.buildTree(pre3, in3)
    assert tree3 is not None and tree3.to_level_order() == [1, 2, None, 3]

    # Test Case 4: Right-skewed tree: preorder = [1, 2, 3], inorder = [1, 2, 3] -> [1, null, 2, null, 3]
    pre4 = [1, 2, 3]
    in4 = [1, 2, 3]
    tree4 = sol.buildTree(pre4, in4)
    assert tree4 is not None and tree4.to_level_order() == [1, None, 2, None, 3]


if __name__ == "__main__":
    test_build_tree()
    print("All Construct Binary Tree from Preorder and Inorder Traversal unit tests passed successfully!")
