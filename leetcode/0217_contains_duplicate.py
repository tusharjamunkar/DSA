"""
0217. Contains Duplicate
Difficulty: Easy
Topic: Arrays & Hashing
LeetCode Link: https://leetcode.com/problems/contains-duplicate/

Problem Statement:
Given an integer array `nums`, return `true` if any value appears at least twice in the array, 
and return `false` if every element is distinct.

Example 1:
Input: nums = [1, 2, 3, 1]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false

Example 3:
Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: true

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

from typing import List, Set


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Optimal Hash Set Early-Exit Approach:
        - Iterate through nums while tracking elements in a hash set.
        - As soon as an element is encountered that already exists in the set, return True immediately.
        - If the iteration finishes without finding any duplicate, return False.

        Time Complexity:  O(n) - Single pass with average O(1) hash set lookups and insertions.
        Space Complexity: O(n) - Stores at most n distinct elements in the hash set.
        """
        seen: Set[int] = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    def containsDuplicateSetLength(self, nums: List[int]) -> bool:
        """
        One-liner Hash Set Length Approach:
        - Compares the length of the list with the length of its set conversion.
        - If lengths differ, duplicates exist.

        Time Complexity:  O(n)
        Space Complexity: O(n)
        """
        return len(nums) != len(set(nums))


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_contains_duplicate():
    sol = Solution()

    # Test Case 1: Duplicate at ends
    assert sol.containsDuplicate([1, 2, 3, 1]) is True
    assert sol.containsDuplicateSetLength([1, 2, 3, 1]) is True

    # Test Case 2: All unique elements
    assert sol.containsDuplicate([1, 2, 3, 4]) is False
    assert sol.containsDuplicateSetLength([1, 2, 3, 4]) is False

    # Test Case 3: Multiple duplicates
    assert sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert sol.containsDuplicateSetLength([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True

    # Test Case 4: Single element (no duplicates possible)
    assert sol.containsDuplicate([42]) is False
    assert sol.containsDuplicateSetLength([42]) is False

    # Test Case 5: Negative numbers with duplicate
    assert sol.containsDuplicate([-1, -2, -3, -1]) is True
    assert sol.containsDuplicateSetLength([-1, -2, -3, -1]) is True

    # Test Case 6: Negative numbers all distinct
    assert sol.containsDuplicate([-5, -10, 0, 5, 10]) is False
    assert sol.containsDuplicateSetLength([-5, -10, 0, 5, 10]) is False

    # Test Case 7: Large values
    assert sol.containsDuplicate([1000000000, -1000000000, 1000000000]) is True
    assert sol.containsDuplicateSetLength([1000000000, -1000000000, 1000000000]) is True

    print("All Contains Duplicate tests passed successfully!")


if __name__ == "__main__":
    test_contains_duplicate()
