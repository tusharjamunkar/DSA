"""
0199. Binary Tree Right Side View
Difficulty: Medium
Topic: Trees / Depth-First Search / Breadth-First Search / Binary Tree
LeetCode Link: https://leetcode.com/problems/binary-tree-right-side-view/

Problem Statement:
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

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


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Optimal Iterative BFS (Level-by-Level Last Node):

        Algorithmic Intuition:
        - Traverse the tree level by level using a queue.
        - For each level:
          - Iterate through all nodes in that level.
          - The last node processed in that level is the rightmost visible node.
          - Append this last node's value to the result list.

        Complexity:
        - Time Complexity:  O(n) - Every node is processed once.
        - Space Complexity: O(w) - Maximum width of the binary tree.
        """
        if not root:
            return []

        res: List[int] = []
        queue: deque[TreeNode] = deque([root])

        while queue:
            level_size = len(queue)
            rightmost_val = 0

            for _ in range(level_size):
                node = queue.popleft()
                rightmost_val = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(rightmost_val)

        return res

    def rightSideViewDFS(self, root: Optional[TreeNode]) -> List[int]:
        """
        Alternative Recursive DFS (Right-to-Left Preorder):
        Visits Root -> Right -> Left. The first node visited at each depth level is the rightmost node.

        Complexity:
        - Time Complexity:  O(n)
        - Space Complexity: O(h) - Call stack recursion depth.
        """
        res: List[int] = []

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return

            if depth == len(res):
                res.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_binary_tree_right_side_view():
    sol = Solution()

    # Test Case 1: [1,2,3,null,5,null,4] -> [1,3,4]
    t1 = TreeNode.from_level_order([1, 2, 3, None, 5, None, 4])
    assert sol.rightSideView(t1) == [1, 3, 4]
    assert sol.rightSideViewDFS(t1) == [1, 3, 4]

    # Test Case 2: [1,null,3] -> [1,3]
    t2 = TreeNode.from_level_order([1, None, 3])
    assert sol.rightSideView(t2) == [1, 3]
    assert sol.rightSideViewDFS(t2) == [1, 3]

    # Test Case 3: Empty tree [] -> []
    assert sol.rightSideView(None) == []
    assert sol.rightSideViewDFS(None) == []

    # Test Case 4: Left-heavy tree [1,2,null,3] -> [1,2,3]
    t4 = TreeNode.from_level_order([1, 2, None, 3])
    assert sol.rightSideView(t4) == [1, 2, 3]
    assert sol.rightSideViewDFS(t4) == [1, 2, 3]


if __name__ == "__main__":
    test_binary_tree_right_side_view()
    print("All Binary Tree Right Side View unit tests passed successfully!")
