"""
0167. Two Sum II - Input Array Is Sorted
Difficulty: Medium
Topic: Two Pointers / Binary Search / Array
LeetCode Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Problem Statement:
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number. Let these two numbers
be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array
[index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

Constraints:
- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order.
- -1000 <= target <= 1000
- The tests are generated such that there is exactly one solution.
"""

from bisect import bisect_left
from typing import Dict, List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Optimal Two-Pointer Converging Approach:
        - Capitalize on the sorted invariant: `numbers[i] <= numbers[i + 1]`.
        - Initialize `left = 0` (smallest element) and `right = len(numbers) - 1` (largest element).
        - At each step, compute `current_sum = numbers[left] + numbers[right]`:
          - If `current_sum == target`: we found the unique solution! Return 1-based indices `[left + 1, right + 1]`.
          - If `current_sum < target`: the sum is too small. Because `numbers` is sorted, moving `right` leftward
            would only produce even smaller sums. The only way to increase the sum is to increment `left`.
          - If `current_sum > target`: the sum is too large. Incrementing `left` would only produce even larger sums.
            The only way to decrease the sum is to decrement `right`.
        - Guaranteed to terminate in at most n steps with O(1) auxiliary space.

        Time Complexity:  O(n) - In the worst case, each step advances either left or right pointer by 1.
        Space Complexity: O(1) - Strictly constant space; no additional data structures used.
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return []

    def twoSumBinarySearch(self, numbers: List[int], target: int) -> List[int]:
        """
        Binary Search Approach (Alternative):
        - For each index `i`, binary search for its complement `target - numbers[i]`
          in the subarray `numbers[i + 1:]`.
        - Uses bisect_left to locate the complement in O(log n) time per element.

        Time Complexity:  O(n log n) - n iterations with binary search of length up to n.
        Space Complexity: O(1) - Constant auxiliary space.
        """
        n = len(numbers)
        for i in range(n - 1):
            complement = target - numbers[i]
            # Search in range [i + 1, n - 1]
            low, high = i + 1, n - 1
            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] == complement:
                    return [i + 1, mid + 1]
                elif numbers[mid] < complement:
                    low = mid + 1
                else:
                    high = mid - 1

        return []

    def twoSumHashMap(self, numbers: List[int], target: int) -> List[int]:
        """
        Hash Map Approach (Baseline):
        - Standard two-sum hash map lookup.
        - Does NOT take advantage of the sorted property and requires O(n) auxiliary space.

        Time Complexity:  O(n)
        Space Complexity: O(n)
        """
        seen: Dict[int, int] = {}
        for idx, num in enumerate(numbers):
            diff = target - num
            if diff in seen:
                return [seen[diff] + 1, idx + 1]
            seen[num] = idx
        return []


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_two_sum_ii():
    sol = Solution()

    # Test Case 1: Standard positive numbers
    nums1, target1 = [2, 7, 11, 15], 9
    assert sol.twoSum(nums1, target1) == [1, 2]
    assert sol.twoSumBinarySearch(nums1, target1) == [1, 2]
    assert sol.twoSumHashMap(nums1, target1) == [1, 2]

    # Test Case 2: Consecutive elements
    nums2, target2 = [2, 3, 4], 6
    assert sol.twoSum(nums2, target2) == [1, 3]
    assert sol.twoSumBinarySearch(nums2, target2) == [1, 3]
    assert sol.twoSumHashMap(nums2, target2) == [1, 3]

    # Test Case 3: Negative numbers and zero
    nums3, target3 = [-1, 0], -1
    assert sol.twoSum(nums3, target3) == [1, 2]
    assert sol.twoSumBinarySearch(nums3, target3) == [1, 2]
    assert sol.twoSumHashMap(nums3, target3) == [1, 2]

    # Test Case 4: Duplicate elements forming target
    nums4, target4 = [0, 0, 3, 4], 0
    assert sol.twoSum(nums4, target4) == [1, 2]
    assert sol.twoSumBinarySearch(nums4, target4) == [1, 2]
    assert sol.twoSumHashMap(nums4, target4) == [1, 2]

    # Test Case 5: Wider array with negative and positive values
    nums5, target5 = [-5, -3, 0, 2, 4, 6, 8], 5
    assert sol.twoSum(nums5, target5) == [2, 7]  # -3 + 8 = 5
    assert sol.twoSumBinarySearch(nums5, target5) == [2, 7]
    assert sol.twoSumHashMap(nums5, target5) == [2, 7]


if __name__ == "__main__":
    test_two_sum_ii()
    print("All Two Sum II tests passed successfully!")
