"""
0049. Group Anagrams
Difficulty: Medium
Topic: Arrays & Hashing / Hash Table / String
LeetCode Link: https://leetcode.com/problems/group-anagrams/

Problem Statement:
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- `strs[i]` consists of lowercase English letters.
"""

from collections import defaultdict
from typing import Dict, List, Tuple


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Optimal Character Count Hash Map Approach:
        - For each word, compute a 26-element character count array representing 
          the frequency of each lowercase English letter ('a' through 'z').
        - Convert this count array into a hashable tuple: tuple(count).
        - Use this tuple as the key in a hash map where values are lists of anagram words.
        - Avoids sorting strings, achieving true linear-in-string-length runtime.

        Time Complexity:  O(N * K) - Where N is len(strs) and K is the maximum length of a string in strs.
        Space Complexity: O(N * K) - Total information stored across hash map keys and grouped lists.
        """
        anagram_map: Dict[Tuple[int, ...], List[str]] = defaultdict(list)
        base = ord("a")

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - base] += 1
            anagram_map[tuple(count)].append(s)

        return list(anagram_map.values())

    def groupAnagramsSortedKey(self, strs: List[str]) -> List[List[str]]:
        """
        Sorted String Canonical Key Approach:
        - Sort each string alphabetically and use the sorted string as the hash map key.
        - Simple and intuitive baseline.

        Time Complexity:  O(N * K log K)
        Space Complexity: O(N * K)
        """
        anagram_map: Dict[str, List[str]] = defaultdict(list)
        for s in strs:
            sorted_key = "".join(sorted(s))
            anagram_map[sorted_key].append(s)
        return list(anagram_map.values())


# ==========================================
# Unit Tests & Verification
# ==========================================
def _canonical_groups(groups: List[List[str]]) -> List[List[str]]:
    """Helper to sort groups and items within groups for order-agnostic test assertions."""
    return sorted([sorted(group) for group in groups])


def test_group_anagrams():
    sol = Solution()

    # Test Case 1: Standard multi-group list
    input1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected1 = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert _canonical_groups(sol.groupAnagrams(input1)) == _canonical_groups(expected1)
    assert _canonical_groups(sol.groupAnagramsSortedKey(input1)) == _canonical_groups(expected1)

    # Test Case 2: Single empty string
    input2 = [""]
    expected2 = [[""]]
    assert _canonical_groups(sol.groupAnagrams(input2)) == _canonical_groups(expected2)
    assert _canonical_groups(sol.groupAnagramsSortedKey(input2)) == _canonical_groups(expected2)

    # Test Case 3: Single character
    input3 = ["a"]
    expected3 = [["a"]]
    assert _canonical_groups(sol.groupAnagrams(input3)) == _canonical_groups(expected3)
    assert _canonical_groups(sol.groupAnagramsSortedKey(input3)) == _canonical_groups(expected3)

    # Test Case 4: Words with duplicate letters
    input4 = ["bdddddddddd", "bbbbbbbbbbc"]
    expected4 = [["bbbbbbbbbbc"], ["bdddddddddd"]]
    assert _canonical_groups(sol.groupAnagrams(input4)) == _canonical_groups(expected4)
    assert _canonical_groups(sol.groupAnagramsSortedKey(input4)) == _canonical_groups(expected4)

    # Test Case 5: Repeated identical words
    input5 = ["abc", "bca", "abc", "cab"]
    expected5 = [["abc", "abc", "bca", "cab"]]
    assert _canonical_groups(sol.groupAnagrams(input5)) == _canonical_groups(expected5)
    assert _canonical_groups(sol.groupAnagramsSortedKey(input5)) == _canonical_groups(expected5)

    # Test Case 6: No anagrams (all distinct letter sets)
    input6 = ["cat", "dog", "bird"]
    expected6 = [["bird"], ["cat"], ["dog"]]
    assert _canonical_groups(sol.groupAnagrams(input6)) == _canonical_groups(expected6)
    assert _canonical_groups(sol.groupAnagramsSortedKey(input6)) == _canonical_groups(expected6)

    print("All Group Anagrams tests passed successfully!")


if __name__ == "__main__":
    test_group_anagrams()
