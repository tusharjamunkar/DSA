"""
0208. Implement Trie (Prefix Tree)
Difficulty: Medium
Topic: Tries / Design / Hash Table / String
LeetCode Link: https://leetcode.com/problems/implement-trie-prefix-tree/

Problem Statement:
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

Constraints:
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters.
- At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.
"""

from typing import Dict, Optional


class TrieNode:
    """Definition of a Trie node supporting child navigation and word boundary flags."""
    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {}
        self.is_end_of_word: bool = False


class Trie:
    """
    Optimal Trie (Prefix Tree) Implementation:

    Algorithmic Intuition:
    - A Trie organizes characters in a tree structure where all descendants of a node share a common prefix.
    - Each node contains a dictionary mapping character -> child TrieNode, plus a boolean flag `is_end_of_word`.
    - insert(word):
      Traverse down character by character. If a character is absent in `curr.children`, instantiate a new TrieNode.
      At the terminal character, mark `is_end_of_word = True`.
    - search(word):
      Traverse down matching characters. If any character is missing, return False.
      At the end of traversal, return `curr.is_end_of_word`.
    - startsWith(prefix):
      Traverse down matching characters. If all prefix characters exist, return True (regardless of `is_end_of_word`).

    Complexity:
    - Time Complexity:
      - insert(word):      O(m) where m is len(word).
      - search(word):      O(m) where m is len(word).
      - startsWith(prefix): O(p) where p is len(prefix).
    - Space Complexity:
      - O(N * m) worst case, where N is total number of words inserted and m is average word length.
      - Each operation uses O(1) auxiliary space (iterative traversal).
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_implement_trie():
    trie = Trie()

    # Test Case 1: Example 1 from LeetCode
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True

    trie.insert("app")
    assert trie.search("app") is True

    # Test Case 2: Non-existent prefix and words
    assert trie.search("appl") is False
    assert trie.search("banana") is False
    assert trie.startsWith("ban") is False

    # Test Case 3: Single character operations
    trie.insert("a")
    assert trie.search("a") is True
    assert trie.startsWith("a") is True
    assert trie.search("b") is False

    # Test Case 4: Long common prefixes
    trie.insert("application")
    assert trie.search("application") is True
    assert trie.startsWith("applic") is True
    assert trie.startsWith("apple") is True


if __name__ == "__main__":
    test_implement_trie()
    print("All Trie (Prefix Tree) unit tests passed successfully!")
