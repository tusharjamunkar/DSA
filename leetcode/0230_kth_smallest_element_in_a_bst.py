"""
0230. Kth Smallest Element in a BST
Difficulty: Medium
Topic: Trees / Depth-First Search / Binary Search Tree / Binary Tree
LeetCode Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Problem Statement:
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:
- The number of nodes in the tree is n.
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4

Follow-up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Optimal Iterative In-Order Traversal with Early Termination:

        Algorithmic Intuition:
        - In-order traversal (Left -> Node -> Right) visits nodes of a BST in strictly sorted ascending order.
        - Rather than traversing all `n` nodes and collecting a full array, we use an explicit stack to simulate in-order traversal:
          1. Traverse down the leftmost path, pushing nodes onto the stack.
          2. Pop top node from stack (the current smallest unvisited node).
          3. Decrement `k -= 1`. If `k == 0`, we have reached the kth smallest element; return `curr.val` immediately!
          4. Otherwise, move to `curr.right` and repeat.

        Complexity:
        - Time Complexity:  O(h + k) - We traverse down to smallest leaf in O(h) time, then visit k elements.
        - Space Complexity: O(h) - Stack stores at most h nodes (tree height).
        """
        stack: List[TreeNode] = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val

            curr = curr.right

        return -1

    def kthSmallestRecursive(self, root: Optional[TreeNode], k: int) -> int:
        """
        Alternative Recursive In-Order DFS with Counter:

        Complexity:
        - Time Complexity:  O(h + k)
        - Space Complexity: O(h) - Call stack frames.
        """
        count = 0
        ans = -1

        def inorder(node: Optional[TreeNode]) -> None:
            nonlocal count, ans
            if not node or ans != -1:
                return

            inorder(node.left)

            count += 1
            if count == k:
                ans = node.val
                return

            inorder(node.right)

        inorder(root)
        return ans


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_kth_smallest_element_bst():
    sol = Solution()

    # Test Case 1: [3,1,4,null,2], k = 1 -> 1
    t1 = TreeNode.from_level_order([3, 1, 4, None, 2])
    assert sol.kthSmallest(t1, 1) == 1
    assert sol.kthSmallestRecursive(t1, 1) == 1

    # Test Case 2: [5,3,6,2,4,null,null,1], k = 3 -> 3
    t2 = TreeNode.from_level_order([5, 3, 6, 2, 4, None, None, 1])
    assert sol.kthSmallest(t2, 3) == 3
    assert sol.kthSmallestRecursive(t2, 3) == 3

    # Test Case 3: k = 5 in same tree -> 5
    assert sol.kthSmallest(t2, 5) == 5
    assert sol.kthSmallestRecursive(t2, 5) == 5

    # Test Case 4: Single node [1], k = 1 -> 1
    t4 = TreeNode(1)
    assert sol.kthSmallest(t4, 1) == 1
    assert sol.kthSmallestRecursive(t4, 1) == 1


if __name__ == "__main__":
    test_kth_smallest_element_bst()
    print("All Kth Smallest Element in a BST unit tests passed successfully!")
