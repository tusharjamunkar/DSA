"""
0102. Binary Tree Level Order Traversal
Difficulty: Medium
Topic: Trees / Breadth-First Search / Binary Tree
LeetCode Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

Problem Statement:
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Optimal Iterative BFS Level-Order Traversal:

        Algorithmic Intuition:
        - Maintain a FIFO queue initialized with `root` (if not None).
        - While the queue is non-empty:
          1. Record `level_size = len(queue)`.
          2. Loop `level_size` times to process exactly all nodes belonging to the current level:
             - Pop front node from queue.
             - Append its value to `current_level` array.
             - Push its non-null left and right children to the queue for the next level.
          3. Append `current_level` to result list `res`.

        Complexity:
        - Time Complexity:  O(n) - Every node is enqueued and dequeued exactly once.
        - Space Complexity: O(w) - Bounded by maximum tree width (up to n/2 in full binary tree).
        """
        if not root:
            return []

        res: List[List[int]] = []
        queue: deque[TreeNode] = deque([root])

        while queue:
            level_size = len(queue)
            current_level: List[int] = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(current_level)

        return res

    def levelOrderDFS(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Alternative Recursive DFS Preorder Traversal with Level Depth Index:

        Complexity:
        - Time Complexity:  O(n)
        - Space Complexity: O(h) - Call stack recursion depth.
        """
        res: List[List[int]] = []

        def dfs(node: Optional[TreeNode], level: int) -> None:
            if not node:
                return

            if len(res) == level:
                res.append([])

            res[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return res


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_binary_tree_level_order_traversal():
    sol = Solution()

    # Test Case 1: [3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]
    t1 = TreeNode.from_level_order([3, 9, 20, None, None, 15, 7])
    assert sol.levelOrder(t1) == [[3], [9, 20], [15, 7]]
    assert sol.levelOrderDFS(t1) == [[3], [9, 20], [15, 7]]

    # Test Case 2: [1] -> [[1]]
    t2 = TreeNode(1)
    assert sol.levelOrder(t2) == [[1]]
    assert sol.levelOrderDFS(t2) == [[1]]

    # Test Case 3: Empty tree [] -> []
    assert sol.levelOrder(None) == []
    assert sol.levelOrderDFS(None) == []

    # Test Case 4: Full binary tree [1,2,3,4,5,6,7] -> [[1],[2,3],[4,5,6,7]]
    t4 = TreeNode.from_level_order([1, 2, 3, 4, 5, 6, 7])
    assert sol.levelOrder(t4) == [[1], [2, 3], [4, 5, 6, 7]]
    assert sol.levelOrderDFS(t4) == [[1], [2, 3], [4, 5, 6, 7]]


if __name__ == "__main__":
    test_binary_tree_level_order_traversal()
    print("All Binary Tree Level Order Traversal unit tests passed successfully!")
