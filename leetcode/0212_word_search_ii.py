"""
0212. Word Search II
Difficulty: Hard
Topic: Tries / Array / String / Backtracking / Matrix
LeetCode Link: https://leetcode.com/problems/word-search-ii/

Problem Statement:
Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 12
- board[i][j] is a lowercase English letter.
- 1 <= words.length <= 3 * 10^4
- 1 <= words[i].length <= 10
- words[i] consists of lowercase English letters.
- All the strings of words are unique.
"""

from typing import List, Dict, Optional


class TrieNode:
    """TrieNode storing child pointers, a word reference at terminal nodes, and a usage count."""
    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {}
        self.word: Optional[str] = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Optimal Trie + 2D Backtracking with Trie Pruning:

        Algorithmic Intuition:
        - Naive DFS for each word takes O(W * M * N * 4^L). With 30,000 words, this TLEs.
        - Reverse the search: Build a Trie from `words` and perform DFS over the `board` once,
          matching all words simultaneously along Trie branches.
        - By storing `node.word = word` directly on the terminal TrieNode:
          - We can retrieve the complete word in O(1) time without rebuilding strings.
          - We avoid duplicate answers by setting `node.word = None` once collected.
        - Trie Pruning:
          - If a leaf TrieNode has no children after exploration, it can be pruned from its parent's
            `children` dictionary, preventing future redundant traversals.

        Complexity:
        - Time Complexity:  O(W * L + M * N * 4 * 3^(L-1))
          - Building Trie: O(W * L) where W = len(words) and L = average word length.
          - Board Traversal: Up to M * N starting points, exploring up to depth L with 3 directions per step (4 at start).
        - Space Complexity: O(W * L) for storing the Trie, and O(L) for DFS call stack depth.
        """
        # Step 1: Construct the Trie
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word

        rows, cols = len(board), len(board[0])
        result: List[str] = []

        # Step 2: Backtracking DFS helper
        def dfs(r: int, c: int, parent_node: TrieNode) -> None:
            char = board[r][c]
            curr_node = parent_node.children[char]

            # If this node represents a matched word
            if curr_node.word:
                result.append(curr_node.word)
                curr_node.word = None  # Prevent duplicate collection

            # Mark cell visited in-place
            board[r][c] = "#"

            # Explore 4-directionally
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    next_char = board[nr][nc]
                    if next_char in curr_node.children:
                        dfs(nr, nc, curr_node)

            # Backtrack: Restore original board character
            board[r][c] = char

            # Optimization: Prune leaf node if it has no children
            if not curr_node.children:
                del parent_node.children[char]

        # Step 3: Launch DFS from every grid cell matching a Trie root child
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return sorted(result)


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_word_search_ii():
    sol = Solution()

    # Test Case 1: Example 1
    board1 = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]
    ]
    words1 = ["oath", "pea", "eat", "rain"]
    assert sol.findWords([row[:] for row in board1], words1) == ["eat", "oath"]

    # Test Case 2: Example 2 (Cannot reuse same cell in word)
    board2 = [
        ["a", "b"],
        ["c", "d"]
    ]
    words2 = ["abcb"]
    assert sol.findWords([row[:] for row in board2], words2) == []

    # Test Case 3: Multiple overlapping words
    board3 = [
        ["a", "b", "c"],
        ["a", "e", "d"],
        ["a", "f", "g"]
    ]
    words3 = ["abcdefg", "befa", "ea", "aea"]
    res3 = sol.findWords([row[:] for row in board3], words3)
    assert sorted(res3) == ["abcdefg", "befa", "ea"]

    # Test Case 4: Single cell matching
    board4 = [["a"]]
    words4 = ["a", "b"]
    assert sol.findWords([row[:] for row in board4], words4) == ["a"]


if __name__ == "__main__":
    test_word_search_ii()
    print("All Word Search II unit tests passed successfully!")
