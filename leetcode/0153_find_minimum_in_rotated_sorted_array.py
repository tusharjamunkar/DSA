"""
0153. Find Minimum in Rotated Sorted Array
Difficulty: Medium
Topic: Binary Search / Array
LeetCode Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Problem Statement:
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:
- [4,5,6,7,0,1,2] if it was rotated 4 times.
- [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the
array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

Constraints:
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of nums are unique.
- nums is sorted and rotated between 1 and n times.
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Optimal Binary Search via Right Boundary Comparison:

        Algorithmic Intuition:
        - The array consists of two sorted subarrays separated by an inflection point (minimum).
        - Compare `nums[mid]` with `nums[right]`:
          - If `nums[mid] > nums[right]`:
            The minimum must lie strictly to the right of `mid`, because `mid` belongs to the
            left (higher) sorted portion. Set `left = mid + 1`.
          - If `nums[mid] <= nums[right]`:
            `mid` belongs to the right (lower) sorted portion. The minimum could be `mid` itself
            or to the left of `mid`. Set `right = mid`.
        - When `left == right`, the search space has converged to the inflection point `nums[left]`.

        Complexity:
        - Time Complexity:  O(log n) - Search interval is halved in each step.
        - Space Complexity: O(1) - Constant auxiliary space.
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_find_min_rotated():
    sol = Solution()

    # Test Case 1: Standard rotation
    assert sol.findMin([3, 4, 5, 1, 2]) == 1

    # Test Case 2: Rotation with 0 at inflection
    assert sol.findMin([4, 5, 6, 7, 0, 1, 2]) == 0

    # Test Case 3: Fully sorted array (rotated n times)
    assert sol.findMin([11, 13, 15, 17]) == 11

    # Test Case 4: Single element array
    assert sol.findMin([1]) == 1

    # Test Case 5: Two elements (rotated and unrotated)
    assert sol.findMin([2, 1]) == 1
    assert sol.findMin([1, 2]) == 1

    # Test Case 6: Three elements (all rotations)
    assert sol.findMin([1, 2, 3]) == 1
    assert sol.findMin([3, 1, 2]) == 1
    assert sol.findMin([2, 3, 1]) == 1


if __name__ == "__main__":
    test_find_min_rotated()
    print("All Find Minimum in Rotated Sorted Array unit tests passed successfully!")
