"""
0704. Binary Search
Difficulty: Easy
Topic: Binary Search / Array
LeetCode Link: https://leetcode.com/problems/binary-search/

Problem Statement:
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index.
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in nums are unique.
- nums is sorted in ascending order.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Optimal Iterative Binary Search:

        Algorithmic Intuition:
        - Maintain two pointers, `left` and `right`, defining the active search interval [left, right].
        - At each step, examine the midpoint `mid = left + (right - left) // 2`.
        - If `nums[mid] == target`, target is found at index `mid`.
        - If `nums[mid] < target`, target must lie strictly to the right: `left = mid + 1`.
        - If `nums[mid] > target`, target must lie strictly to the left: `right = mid - 1`.
        - If `left > right`, the target does not exist in the array, return -1.

        Complexity:
        - Time Complexity:  O(log n) - Search space is halved on each iteration.
        - Space Complexity: O(1) - Constant auxiliary space.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_binary_search():
    sol = Solution()

    # Test Case 1: Target present in array
    assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4

    # Test Case 2: Target absent from array
    assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1

    # Test Case 3: Single element array - found
    assert sol.search([5], 5) == 0

    # Test Case 4: Single element array - not found
    assert sol.search([5], -5) == -1

    # Test Case 5: Target at first element
    assert sol.search([1, 2, 3, 4, 5], 1) == 0

    # Test Case 6: Target at last element
    assert sol.search([1, 2, 3, 4, 5], 5) == 4

    # Test Case 7: Even length array
    assert sol.search([2, 5], 5) == 1
    assert sol.search([2, 5], 2) == 0
    assert sol.search([2, 5], 3) == -1


if __name__ == "__main__":
    test_binary_search()
    print("All Binary Search unit tests passed successfully!")
