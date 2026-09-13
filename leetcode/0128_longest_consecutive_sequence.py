"""
0128. Longest Consecutive Sequence
Difficulty: Medium
Topic: Arrays & Hashing / Hash Table / Union Find
LeetCode Link: https://leetcode.com/problems/longest-consecutive-sequence/

Problem Statement:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Explanation: The longest consecutive sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8]. Length is 9.

Constraints:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

from typing import List, Set


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Optimal Hash Set "Sequence Start" Approach:
        - Convert nums into a hash set for O(1) average lookup time.
        - Key Insight: A number `num` is the start of a consecutive sequence IF AND ONLY IF `num - 1` is NOT in the set.
        - If `num - 1` is in the set, skip it! Counting from `num` would be redundant because the sequence starting at
          the earlier number will cover it and be strictly longer.
        - When a sequence start `num` is found:
          - Increment `current_num = num + 1` while it exists in the set, keeping track of the current streak.
          - Update the global maximum streak.

        Why this is strictly O(n):
        - Although there is a nested while loop, each number is visited at most twice:
          once during the set traversal and once inside the while loop of its sequence start.
        - Elements that are not sequence starts are immediately skipped in O(1).

        Time Complexity:  O(n) - Set construction takes O(n); sequence exploration visits each element at most twice.
        Space Complexity: O(n) - Hash set stores up to n distinct elements.
        """
        num_set: Set[int] = set(nums)
        longest_streak = 0

        for num in num_set:
            # Only start counting if num is the beginning of a sequence
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

    def longestConsecutiveSort(self, nums: List[int]) -> int:
        """
        Sorting Approach (Baseline):
        - Sort the array and scan consecutively, ignoring duplicates.
        - Does not satisfy the strict O(n) follow-up constraint, but provides a simple benchmark.

        Time Complexity:  O(n log n)
        Space Complexity: O(1) or O(n) depending on Python's Timsort.
        """
        if not nums:
            return 0

        nums_sorted = sorted(nums)
        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums_sorted)):
            if nums_sorted[i] == nums_sorted[i - 1]:
                continue
            if nums_sorted[i] == nums_sorted[i - 1] + 1:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1

        return max(longest_streak, current_streak)


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_longest_consecutive():
    sol = Solution()

    # Test Case 1: Standard unsorted array
    nums1 = [100, 4, 200, 1, 3, 2]
    assert sol.longestConsecutive(nums1) == 4
    assert sol.longestConsecutiveSort(nums1) == 4

    # Test Case 2: Array with duplicates and zero
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    assert sol.longestConsecutive(nums2) == 9
    assert sol.longestConsecutiveSort(nums2) == 9

    # Test Case 3: Empty array
    nums3: List[int] = []
    assert sol.longestConsecutive(nums3) == 0
    assert sol.longestConsecutiveSort(nums3) == 0

    # Test Case 4: Single element
    nums4 = [10]
    assert sol.longestConsecutive(nums4) == 1
    assert sol.longestConsecutiveSort(nums4) == 1

    # Test Case 5: Negative numbers
    nums5 = [-5, -4, -3, 0, 2, -2]
    assert sol.longestConsecutive(nums5) == 4  # [-5, -4, -3, -2]
    assert sol.longestConsecutiveSort(nums5) == 4


if __name__ == "__main__":
    test_longest_consecutive()
    print("All Longest Consecutive Sequence tests passed successfully!")
