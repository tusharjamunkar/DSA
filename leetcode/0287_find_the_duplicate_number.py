"""
0287. Find the Duplicate Number
Difficulty: Medium
Topic: Array / Two Pointers / Binary Search / Bit Manipulation
LeetCode Link: https://leetcode.com/problems/find-the-duplicate-number/

Problem Statement:
Given an array of integers nums containing n + 1 integers where each integer is in
the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [3,3,3,3,3]
Output: 3

Constraints:
- 1 <= n <= 10^5
- nums.length == n + 1
- 1 <= nums[i] <= n
- All the integers in nums appear only once except for precisely one integer which appears two or more times.
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Optimal Floyd's Cycle Detection (Tortoise & Hare on Array Indices):

        Algorithmic Intuition:
        - Treat the array as a functional linked list where index `i` points to `nums[i]`.
        - Because values are in `[1, n]` and the array length is `n + 1`, index `0` is
          guaranteed never to be pointed to (it is an entry point).
        - A duplicate value means two or more indices point to the same destination,
          which creates a cycle.
        - Step 1 (Find intersection inside the cycle):
          `slow = nums[slow]`
          `fast = nums[nums[fast]]`
          Repeat until `slow == fast`.
        - Step 2 (Locate entry point of cycle = duplicate number):
          Reset `slow2 = 0`.
          Advance `slow` and `slow2` at equal speed (1 step at a time):
          `slow = nums[slow]`, `slow2 = nums[slow2]`.
          When they meet (`slow == slow2`), that index is the start of the cycle,
          which corresponds to the duplicate number.

        Complexity:
        - Time Complexity:  O(n) - Linear traversal.
        - Space Complexity: O(1) - Constant auxiliary storage without mutating `nums`.
        """
        # Step 1: Detect cycle intersection point
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Step 2: Find the entrance to the cycle
        slow2 = 0
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]

        return slow


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_find_duplicate():
    sol = Solution()

    # Test Case 1: [1, 3, 4, 2, 2] -> 2
    assert sol.findDuplicate([1, 3, 4, 2, 2]) == 2

    # Test Case 2: [3, 1, 3, 4, 2] -> 3
    assert sol.findDuplicate([3, 1, 3, 4, 2]) == 3

    # Test Case 3: Multiple identical duplicates [3, 3, 3, 3, 3] -> 3
    assert sol.findDuplicate([3, 3, 3, 3, 3]) == 3

    # Test Case 4: Cycle at head [2, 5, 9, 6, 9, 3, 8, 9, 7, 1] -> 9
    assert sol.findDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]) == 9


if __name__ == "__main__":
    test_find_duplicate()
    print("All Find the Duplicate Number unit tests passed successfully!")
