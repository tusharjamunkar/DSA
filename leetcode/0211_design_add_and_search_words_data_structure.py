"""
0211. Design Add and Search Words Data Structure
Difficulty: Medium
Topic: Tries / String / Depth-First Search / Design
LeetCode Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/

Problem Statement:
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:
- WordDictionary() Initializes the object.
- void addWord(word) Adds word to the data structure, it can be matched later.
- bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
  word may contain dots '.' where dots can be matched with any letter.

Example:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

Constraints:
- 1 <= word.length <= 25
- word in addWord consists of lowercase English letters.
- word in search consist of '.' or lowercase English letters.
- There will be at most 2 dots in word for search queries.
- At most 10^4 calls will be made to addWord and search.
"""

from typing import Dict, Optional


class TrieNode:
    """Trie node with child character mapping and terminal word marker."""
    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {}
        self.is_end_of_word: bool = False


class WordDictionary:
    """
    Optimal WordDictionary using Trie with Backtracking DFS Search:

    Algorithmic Intuition:
    - Standard words are added via trie insertion in O(m) time.
    - search(word) uses Depth-First Search:
      - If character is a letter (a-z):
        Check if char exists in current node's children. If yes, move to next index. If not, return False.
      - If character is the wildcard dot ('.'):
        Branch into ALL existing children nodes at this level. If any branch successfully matches the remainder, return True.
      - When index reaches the end of the word, return whether `curr.is_end_of_word` is True.

    Complexity:
    - Time Complexity:
      - addWord(word): O(m) where m is the length of word.
      - search(word):  O(m) if no wildcards; with wildcards, worst-case O(26^d * m) where d is number of dots (d <= 2 by constraint).
    - Space Complexity:
      - O(N * m) for stored trie nodes.
      - O(m) recursion stack depth during search.
    """

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, index: int) -> bool:
            if index == len(word):
                return node.is_end_of_word

            char = word[index]

            if char == ".":
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], index + 1)

        return dfs(self.root, 0)


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_word_dictionary():
    wd = WordDictionary()

    # Test Case 1: Example from problem statement
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")

    assert wd.search("pad") is False
    assert wd.search("bad") is True
    assert wd.search(".ad") is True
    assert wd.search("b..") is True

    # Test Case 2: Partial matches with length mismatch
    assert wd.search("b") is False
    assert wd.search("bade") is False
    assert wd.search("....") is False

    # Test Case 3: Wildcards matching whole word
    assert wd.search("...") is True

    # Test Case 4: Multiple branches with identical endings
    wd.addWord("apple")
    assert wd.search("a...e") is True
    assert wd.search("app..") is True
    assert wd.search("appl.") is True
    assert wd.search("orange") is False


if __name__ == "__main__":
    test_word_dictionary()
    print("All Design Add and Search Words Data Structure unit tests passed successfully!")
