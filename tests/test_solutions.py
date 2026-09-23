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

def test_suite_trapping_rain_water():
    mod = importlib.import_module("leetcode.0042_trapping_rain_water")
    sol = mod.Solution()
    assert sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

    assert sol.trapDP([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert sol.trapMonotonicStack([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert sol.trap([4, 2, 0, 3, 2, 5]) == 9
    assert sol.trap([3, 3, 3]) == 0


def test_suite_best_time_to_buy_and_sell_stock():
    mod = importlib.import_module("leetcode.0121_best_time_to_buy_and_sell_stock")
    sol = mod.Solution()
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfitRunningMin([7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
    assert sol.maxProfit([1, 2, 3, 4, 5]) == 4


def test_suite_longest_substring_without_repeating_characters():
    mod = importlib.import_module("leetcode.0003_longest_substring_without_repeating_characters")
    sol = mod.Solution()
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstringSet("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    assert sol.lengthOfLongestSubstring("") == 0
    assert sol.lengthOfLongestSubstring("tmmzuxt") == 5


def test_suite_longest_repeating_character_replacement():
    mod = importlib.import_module("leetcode.0424_longest_repeating_character_replacement")
    sol = mod.Solution()
    assert sol.characterReplacement("ABAB", 2) == 4
    assert sol.characterReplacement("AABABBA", 1) == 4
    assert sol.characterReplacement("ABBB", 0) == 3
    assert sol.characterReplacement("A", 0) == 1
    assert sol.characterReplacement("ABCDE", 5) == 5


def test_suite_permutation_in_string():
    mod = importlib.import_module("leetcode.0567_permutation_in_string")
    sol = mod.Solution()
    assert sol.checkInclusion("ab", "eidbaooo") is True
    assert sol.checkInclusionDirect("ab", "eidbaooo") is True
    assert sol.checkInclusion("ab", "eidboaoo") is False
    assert sol.checkInclusionDirect("ab", "eidboaoo") is False
    assert sol.checkInclusion("aab", "baab") is True


def test_suite_minimum_window_substring():
    mod = importlib.import_module("leetcode.0076_minimum_window_substring")
    sol = mod.Solution()
    assert sol.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert sol.minWindow("a", "a") == "a"
    assert sol.minWindow("a", "aa") == ""
    assert sol.minWindow("aAbBC", "ABC") == "AbBC"


def test_suite_sliding_window_maximum():
    mod = importlib.import_module("leetcode.0239_sliding_window_maximum")
    sol = mod.Solution()
    assert sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert sol.maxSlidingWindow([1], 1) == [1]
    assert sol.maxSlidingWindow([5, 4, 3, 2, 1], 2) == [5, 4, 3, 2]


def test_suite_valid_parentheses():
    mod = importlib.import_module("leetcode.0020_valid_parentheses")
    sol = mod.Solution()
    assert sol.isValid("()") is True
    assert sol.isValid("()[]{}") is True
    assert sol.isValid("(]") is False
    assert sol.isValid("([])") is True
    assert sol.isValid("([)]") is False


def test_suite_min_stack():
    mod = importlib.import_module("leetcode.0155_min_stack")
    ms = mod.MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    assert ms.getMin() == -3
    ms.pop()
    assert ms.top() == 0
    assert ms.getMin() == -2


def test_suite_evaluate_reverse_polish_notation():
    mod = importlib.import_module("leetcode.0150_evaluate_reverse_polish_notation")
    sol = mod.Solution()
    assert sol.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert sol.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert sol.evalRPN(["-7", "3", "/"]) == -2


def test_suite_generate_parentheses():
    mod = importlib.import_module("leetcode.0022_generate_parentheses")
    sol = mod.Solution()
    assert sol.generateParenthesis(1) == ["()"]
    assert sorted(sol.generateParenthesis(2)) == sorted(["(())", "()()"])
    assert len(sol.generateParenthesis(3)) == 5


def test_suite_daily_temperatures():
    mod = importlib.import_module("leetcode.0739_daily_temperatures")
    sol = mod.Solution()
    assert sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert sol.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert sol.dailyTemperatures([30, 60, 90]) == [1, 1, 0]


def test_suite_car_fleet():
    mod = importlib.import_module("leetcode.0853_car_fleet")
    sol = mod.Solution()
    assert sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    assert sol.carFleet(10, [3], [3]) == 1
    assert sol.carFleet(100, [0, 2, 4], [4, 2, 1]) == 1


def test_suite_largest_rectangle_in_histogram():
    mod = importlib.import_module("leetcode.0084_largest_rectangle_in_histogram")
    sol = mod.Solution()
    assert sol.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert sol.largestRectangleArea([2, 4]) == 4
    assert sol.largestRectangleArea([1, 2, 3, 4, 5]) == 9


def test_suite_binary_search():
    mod = importlib.import_module("leetcode.0704_binary_search")
    sol = mod.Solution()
    assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert sol.search([5], 5) == 0


def test_suite_search_2d_matrix():
    mod = importlib.import_module("leetcode.0074_search_a_2d_matrix")
    sol = mod.Solution()
    m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert sol.searchMatrix(m, 3) is True
    assert sol.searchMatrix(m, 13) is False
    assert sol.searchMatrixTwoPass(m, 3) is True


def test_suite_koko_eating_bananas():
    mod = importlib.import_module("leetcode.0875_koko_eating_bananas")
    sol = mod.Solution()
    assert sol.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23





