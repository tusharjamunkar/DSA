"""
0297. Serialize and Deserialize Binary Tree
Difficulty: Hard
Topic: Trees / String / Depth-First Search / Breadth-First Search / Design / Binary Tree
LeetCode Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Problem Statement:
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -1000 <= Node.val <= 1000
"""

from typing import Optional, List, Iterator
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


class Codec:
    """
    Optimal Preorder DFS Codec:

    Algorithmic Intuition:
    - Serialization:
      Perform preorder DFS traversal (Root -> Left -> Right).
      If node is None, write sentinel "#,".
      Otherwise, write "str(node.val)," followed by serializing left and right subtrees.
    - Deserialization:
      Split string by comma into an iterator/deque of tokens.
      Consume next token:
      If "#", return None.
      Else create `node = TreeNode(int(val))`, recursively build `node.left` then `node.right`.

    Complexity:
    - Time Complexity:  O(n) for both serialize and deserialize.
    - Space Complexity: O(n) for encoded string and recursion call stack.
    """
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        vals: List[str] = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                vals.append("#")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        if not data:
            return None

        tokens = iter(data.split(","))

        def dfs() -> Optional[TreeNode]:
            val = next(tokens)
            if val == "#":
                return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


class CodecBFS:
    """
    Alternative Level-Order BFS Codec:
    Encodes and decodes level-by-level using a FIFO queue.
    """
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        res: List[str] = []
        queue: deque[Optional[TreeNode]] = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("#")

        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        tokens = deque(data.split(","))
        first_token = tokens.popleft()
        if first_token == "#":
            return None

        root = TreeNode(int(first_token))
        queue: deque[TreeNode] = deque([root])

        while queue and tokens:
            parent = queue.popleft()

            left_token = tokens.popleft()
            if left_token != "#":
                parent.left = TreeNode(int(left_token))
                queue.append(parent.left)

            if tokens:
                right_token = tokens.popleft()
                if right_token != "#":
                    parent.right = TreeNode(int(right_token))
                    queue.append(parent.right)

        return root


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_serialize_deserialize_binary_tree():
    codec = Codec()
    codec_bfs = CodecBFS()

    # Test Case 1: [1,2,3,null,null,4,5]
    t1 = TreeNode.from_level_order([1, 2, 3, None, None, 4, 5])
    s1 = codec.serialize(t1)
    d1 = codec.deserialize(s1)
    assert d1 is not None and d1.to_level_order() == [1, 2, 3, None, None, 4, 5]

    s1_bfs = codec_bfs.serialize(t1)
    d1_bfs = codec_bfs.deserialize(s1_bfs)
    assert d1_bfs is not None and d1_bfs.to_level_order() == [1, 2, 3, None, None, 4, 5]

    # Test Case 2: Empty tree []
    assert codec.deserialize(codec.serialize(None)) is None
    assert codec_bfs.deserialize(codec_bfs.serialize(None)) is None

    # Test Case 3: Single node [-42]
    t3 = TreeNode(-42)
    assert codec.deserialize(codec.serialize(t3)).to_level_order() == [-42]
    assert codec_bfs.deserialize(codec_bfs.serialize(t3)).to_level_order() == [-42]

    # Test Case 4: Skewed tree [1, 2, null, 3, null, 4]
    t4 = TreeNode.from_level_order([1, 2, None, 3, None, 4])
    assert codec.deserialize(codec.serialize(t4)).to_level_order() == [1, 2, None, 3, None, 4]
    assert codec_bfs.deserialize(codec_bfs.serialize(t4)).to_level_order() == [1, 2, None, 3, None, 4]


if __name__ == "__main__":
    test_serialize_deserialize_binary_tree()
    print("All Serialize and Deserialize Binary Tree unit tests passed successfully!")
