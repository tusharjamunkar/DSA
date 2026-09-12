"""
Automated Test Suite for all LeetCode solutions in the DSA repository.
"""

import importlib
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def test_suite_two_sum():
    mod = importlib.import_module("leetcode.0001_two_sum")
    sol = mod.Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]
    assert sol.twoSum([3, 3], 6) == [0, 1]


def test_suite_contains_duplicate():
    mod = importlib.import_module("leetcode.0217_contains_duplicate")
    sol = mod.Solution()
    assert sol.containsDuplicate([1, 2, 3, 1]) is True
    assert sol.containsDuplicate([1, 2, 3, 4]) is False
    assert sol.containsDuplicateSetLength([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True


def test_suite_valid_anagram():
    mod = importlib.import_module("leetcode.0242_valid_anagram")
    sol = mod.Solution()
    assert sol.isAnagram("anagram", "nagaram") is True
    assert sol.isAnagram("rat", "car") is False
    assert sol.isAnagramUnicode("café", "féca") is True
    assert sol.isAnagramCounter("hello", "olleh") is True


def test_suite_group_anagrams():
    mod = importlib.import_module("leetcode.0049_group_anagrams")
    sol = mod.Solution()
    res = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    canonical = sorted([sorted(g) for g in res])
    expected = sorted([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    assert canonical == expected


def test_suite_top_k_frequent():
    mod = importlib.import_module("leetcode.0347_top_k_frequent_elements")
    sol = mod.Solution()
    assert sorted(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert sorted(sol.topKFrequentHeap([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert sorted(sol.topKFrequentSort([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert sol.topKFrequent([1], 1) == [1]


def test_suite_product_except_self():
    mod = importlib.import_module("leetcode.0238_product_of_array_except_self")
    sol = mod.Solution()
    assert sol.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert sol.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert sol.productExceptSelfWithArrays([1, 2, 3, 4]) == [24, 12, 8, 6]

