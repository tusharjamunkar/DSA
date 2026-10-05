"""
0124. Binary Tree Maximum Path Sum
Difficulty: Hard
Topic: Trees / Dynamic Programming / Depth-First Search / Binary Tree
LeetCode Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/

Problem Statement:
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Constraints:
- The number of nodes in the tree is in the range [1, 3 * 10^4].
- -1000 <= Node.val <= 1000
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Optimal Bottom-Up Post-Order DFS:

        Algorithmic Intuition:
        - At each node, any path that curves through the node (using both left and right subtrees)
          cannot be extended further up to the node's parent.
        - Therefore, for each node:
          1. Recursively compute the maximum branch gain from the left child:
             `left_gain = max(0, dfs(node.left))` (clamping negative gains to 0 since we can choose not to include them).
          2. Recursively compute the maximum branch gain from the right child:
             `right_gain = max(0, dfs(node.right))`.
          3. The maximum path sum passing *through* current node as the highest apex is:
             `current_path = node.val + left_gain + right_gain`.
          4. Update the global `max_sum = max(max_sum, current_path)`.
          5. Return to the parent the single branch that yields the highest contribution:
             `node.val + max(left_gain, right_gain)`.

        Complexity:
        - Time Complexity:  O(n) - Visits each node exactly once in post-order.
        - Space Complexity: O(h) - Call stack bounded by height of binary tree (O(log n) balanced, O(n) degenerate).
        """
        max_sum: float = -math.inf

        def max_gain(node: Optional[TreeNode]) -> int:
            nonlocal max_sum
            if not node:
                return 0

            # Max gain from left and right subtrees (clamp to 0 to ignore negative sums)
            left_gain = max(0, max_gain(node.left))
            right_gain = max(0, max_gain(node.right))

            # Price of the new path where current node is the apex/turning point
            price_newpath = node.val + left_gain + right_gain

            # Update global maximum path sum
            max_sum = max(max_sum, price_newpath)

            # Return max single-branch gain extending upward to parent
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return int(max_sum)


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_max_path_sum():
    sol = Solution()

    # Test Case 1: [1,2,3] -> 6
    t1 = TreeNode.from_level_order([1, 2, 3])
    assert sol.maxPathSum(t1) == 6

    # Test Case 2: [-10,9,20,null,null,15,7] -> 42 (15 + 20 + 7)
    t2 = TreeNode.from_level_order([-10, 9, 20, None, None, 15, 7])
    assert sol.maxPathSum(t2) == 42

    # Test Case 3: All negative values [-3] -> -3
    t3 = TreeNode(-3)
    assert sol.maxPathSum(t3) == -3

    # Test Case 4: Negative apex with positive children [-2, 1] -> 1
    t4 = TreeNode.from_level_order([-2, 1])
    assert sol.maxPathSum(t4) == 1

    # Test Case 5: Complex negative tree [2, -1] -> 2
    t5 = TreeNode.from_level_order([2, -1])
    assert sol.maxPathSum(t5) == 2


if __name__ == "__main__":
    test_max_path_sum()
    print("All Binary Tree Maximum Path Sum unit tests passed successfully!")
