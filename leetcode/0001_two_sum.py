"""
0001. Two Sum
Difficulty: Easy
Topic: Arrays & Hashing / Two Pointers
LeetCode Link: https://leetcode.com/problems/two-sum/

Problem Statement:
Given an array of integers `nums` and an integer `target`, return indices of the two numbers 
such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same 
element twice. You can return the answer in any order.

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.
"""

from typing import List, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Optimal One-Pass Hash Map Approach:
        - Iterate through the array while maintaining a map of {num: index}.
        - For each number, compute its complement: complement = target - num.
        - If complement exists in map, we found the pair in O(1) lookup time.
        - Otherwise, store current number and its index in map.

        Time Complexity:  O(n) - Single pass traversal through array with O(1) hash map operations.
        Space Complexity: O(n) - Stores at most n elements in the hash map.
        """
        seen: Dict[int, int] = {}

        for idx, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], idx]
            seen[num] = idx

        return []


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_two_sum():
    sol = Solution()

    # Test Case 1: Standard case
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]

    # Test Case 2: Indices not at start
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]

    # Test Case 3: Duplicate numbers summing to target
    assert sol.twoSum([3, 3], 6) == [0, 1]

    # Test Case 4: Negative numbers
    assert sol.twoSum([-3, 4, 3, 90], 0) == [0, 2]

    # Test Case 5: Zeroes
    assert sol.twoSum([0, 4, 3, 0], 0) == [0, 3]

    print("All Two Sum tests passed successfully!")


if __name__ == "__main__":
    test_two_sum()
