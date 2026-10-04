"""
1448. Count Good Nodes in Binary Tree
Difficulty: Medium
Topic: Trees / Depth-First Search / Breadth-First Search / Binary Tree
LeetCode Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

Problem Statement:
Given a binary tree root, a node X in the tree is named good if in the path from the root to X there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.

Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.

Constraints:
- The number of nodes in the binary tree is in the range [1, 10^5].
- Each node's value is between [-10^4, 10^4].
"""

from typing import Optional, List, Tuple
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
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        """
        Optimal Recursive Preorder DFS:

        Algorithmic Intuition:
        - As we traverse from root downward along any path, we maintain `max_so_far`,
          the maximum node value encountered along the ancestor path.
        - For each node:
          1. If `node.val >= max_so_far`:
             The node satisfies the condition; count it as 1 and update `max_so_far = node.val`.
          2. Else:
             Count is 0, and `max_so_far` remains unchanged.
          3. Recurse on left and right children and return `is_good + dfs(left) + dfs(right)`.

        Complexity:
        - Time Complexity:  O(n) - Visits each node exactly once.
        - Space Complexity: O(h) - Call stack recursion frames (O(log n) balanced, O(n) degenerate).
        """
        def dfs(node: Optional[TreeNode], max_so_far: int) -> int:
            if not node:
                return 0

            count = 1 if node.val >= max_so_far else 0
            new_max = max(max_so_far, node.val)

            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)
            return count

        if not root:
            return 0
        return dfs(root, root.val)

    def goodNodesBFS(self, root: Optional[TreeNode]) -> int:
        """
        Alternative Iterative BFS with Queue:
        Stores pairs of `(node, max_so_far)` in a queue.

        Complexity:
        - Time Complexity:  O(n)
        - Space Complexity: O(w) - Maximum tree width in queue.
        """
        if not root:
            return 0

        good_count = 0
        queue: deque[Tuple[TreeNode, int]] = deque([(root, root.val)])

        while queue:
            node, max_so_far = queue.popleft()

            if node.val >= max_so_far:
                good_count += 1

            new_max = max(max_so_far, node.val)

            if node.left:
                queue.append((node.left, new_max))
            if node.right:
                queue.append((node.right, new_max))

        return good_count


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_count_good_nodes():
    sol = Solution()

    # Test Case 1: [3,1,4,3,null,1,5] -> 4
    t1 = TreeNode.from_level_order([3, 1, 4, 3, None, 1, 5])
    assert sol.goodNodes(t1) == 4
    assert sol.goodNodesBFS(t1) == 4

    # Test Case 2: [3,3,null,4,2] -> 3
    t2 = TreeNode.from_level_order([3, 3, None, 4, 2])
    assert sol.goodNodes(t2) == 3
    assert sol.goodNodesBFS(t2) == 3

    # Test Case 3: Single node [1] -> 1
    t3 = TreeNode(1)
    assert sol.goodNodes(t3) == 1
    assert sol.goodNodesBFS(t3) == 1

    # Test Case 4: Negative values [-1,5,-2,4,4,2,-2] -> 3
    t4 = TreeNode.from_level_order([-1, 5, -2, 4, 4, 2, -2])
    assert sol.goodNodes(t4) == 3
    assert sol.goodNodesBFS(t4) == 3

    # Test Case 5: Empty tree -> 0
    assert sol.goodNodes(None) == 0
    assert sol.goodNodesBFS(None) == 0


if __name__ == "__main__":
    test_count_good_nodes()
    print("All Count Good Nodes in Binary Tree unit tests passed successfully!")
