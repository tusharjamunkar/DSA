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


def test_suite_valid_sudoku():
    mod = importlib.import_module("leetcode.0036_valid_sudoku")
    sol = mod.Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert sol.isValidSudoku(board) is True
    assert sol.isValidSudokuBitmask(board) is True


def test_suite_longest_consecutive():
    mod = importlib.import_module("leetcode.0128_longest_consecutive_sequence")
    sol = mod.Solution()
    assert sol.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert sol.longestConsecutive([]) == 0
    assert sol.longestConsecutiveSort([100, 4, 200, 1, 3, 2]) == 4


def test_suite_valid_palindrome():
    mod = importlib.import_module("leetcode.0125_valid_palindrome")
    sol = mod.Solution()
    assert sol.isPalindrome("A man, a plan, a canal: Panama") is True
    assert sol.isPalindrome("race a car") is False
    assert sol.isPalindrome(" ") is True
    assert sol.isPalindrome("0P") is False
    assert sol.isPalindromeFiltered("A man, a plan, a canal: Panama") is True
    assert sol.isPalindromeFiltered("race a car") is False


def test_suite_two_sum_ii():
    mod = importlib.import_module("leetcode.0167_two_sum_ii_input_array_is_sorted")
    sol = mod.Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert sol.twoSum([2, 3, 4], 6) == [1, 3]
    assert sol.twoSum([-1, 0], -1) == [1, 2]
    assert sol.twoSumBinarySearch([2, 7, 11, 15], 9) == [1, 2]
    assert sol.twoSumBinarySearch([2, 3, 4], 6) == [1, 3]
    assert sol.twoSumHashMap([2, 7, 11, 15], 9) == [1, 2]




def test_suite_three_sum():
    mod = importlib.import_module("leetcode.0015_three_sum")
    sol = mod.Solution()
    
    def normalize(result):
        return {tuple(sorted(trip)) for trip in result}

    nums1 = [-1, 0, 1, 2, -1, -4]
    expected1 = {(-1, -1, 2), (-1, 0, 1)}
    assert normalize(sol.threeSum(nums1.copy())) == expected1
    assert normalize(sol.threeSumHashSet(nums1)) == expected1

    assert sol.threeSum([0, 1, 1]) == []
    assert normalize(sol.threeSum([0, 0, 0])) == {(0, 0, 0)}


def test_suite_container_with_most_water():
    mod = importlib.import_module("leetcode.0011_container_with_most_water")
    sol = mod.Solution()

    h1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert sol.maxArea(h1) == 49
    assert sol.maxAreaOptimized(h1) == 49
    assert sol.maxAreaBruteForce(h1) == 49

    h2 = [1, 1]
    assert sol.maxArea(h2) == 1
    assert sol.maxAreaOptimized(h2) == 1

    h3 = [4, 3, 2, 1, 4]
    assert sol.maxArea(h3) == 16
    assert sol.maxAreaOptimized(h3) == 16
