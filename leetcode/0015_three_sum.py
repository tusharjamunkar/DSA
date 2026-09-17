"""
0015. 3Sum
Difficulty: Medium
Topic: Two Pointers / Sorting / Array
LeetCode Link: https://leetcode.com/problems/3sum/

Problem Statement:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
"""

from typing import List, Set, Tuple


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Optimal Sorting + Two-Pointer Approach:
        
        Mathematical / Algorithmic Intuition:
        - 3Sum reduces to finding pairs that sum to `-nums[i]`:
          `nums[i] + nums[j] + nums[k] == 0`  <=>  `nums[j] + nums[k] == -nums[i]`
        - Sorting the array in O(n log n) unlocks two critical advantages:
          1. Enables the Two-Pointer convergence pattern (Two Sum II) in O(n) per fixed element.
          2. Makes duplicate elimination trivial by comparing adjacent elements in O(1).
        
        Step-by-Step Execution:
        1. Sort `nums` in ascending order.
        2. Iterate index `i` from `0` to `len(nums) - 3`:
           - Early exit optimization: If `nums[i] > 0`, break immediately. Since the array is sorted,
             all subsequent elements are >= nums[i] > 0, so no three positive numbers can ever sum to 0.
           - Duplicate avoidance for the outer loop: If `i > 0` and `nums[i] == nums[i - 1]`, skip this `i`.
        3. Initialize two pointers for the remaining subarray:
           `left = i + 1`, `right = len(nums) - 1`.
        4. While `left < right`:
           - Compute `total = nums[i] + nums[left] + nums[right]`.
           - If `total < 0`: the sum is too small. Increment `left` to increase the sum.
           - If `total > 0`: the sum is too large. Decrement `right` to decrease the sum.
           - If `total == 0`:
             - We found a valid unique triplet `[nums[i], nums[left], nums[right]]`.
             - Add it to the result list.
             - Skip subsequent duplicate values for both `left` and `right`:
               `while left < right and nums[left] == nums[left + 1]: left += 1`
               `while left < right and nums[right] == nums[right - 1]: right -= 1`
             - Advance both pointers: `left += 1`, `right -= 1`.
        
        Time Complexity:  O(n^2) - Sorting takes O(n log n). Outer loop runs n times, and inner
                          two-pointer convergence takes O(n) per iteration. Total: O(n log n + n^2) = O(n^2).
        Space Complexity: O(1) or O(n) - O(1) auxiliary space beyond the output list (or O(n) auxiliary
                          space depending on the Python Timsort implementation).
        """
        nums.sort()
        n = len(nums)
        triplets: List[List[int]] = []

        for i in range(n - 2):
            # Early pruning: three positive numbers cannot sum to 0
            if nums[i] > 0:
                break

            # Avoid duplicate triplets from the same outer anchor
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate values for left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate values for right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return triplets

    def threeSumHashSet(self, nums: List[int]) -> List[List[int]]:
        """
        Alternative Hash Set Approach (No In-Place Sorting Needed):
        
        - If modifying or sorting the input array is strictly disallowed, we can fix `nums[i]`
          and use a Hash Set (Two Sum standard) to find complementary pairs in O(n).
        - To prevent duplicate triplets in the output, we normalize each found triplet
          into a sorted tuple and store in a `result_set`.
        
        Time Complexity:  O(n^2) - Two nested loops with O(1) hash set operations.
        Space Complexity: O(n) - Hash set for seen inner elements plus hash set for duplicate output tracking.
        """
        result_set: Set[Tuple[int, int, int]] = set()
        dups_outer: Set[int] = set()

        for i, val1 in enumerate(nums):
            if val1 in dups_outer:
                continue
            dups_outer.add(val1)

            seen_inner: Set[int] = set()
            for j in range(i + 1, len(nums)):
                val2 = nums[j]
                complement = -val1 - val2
                if complement in seen_inner:
                    triplet = tuple(sorted([val1, val2, complement]))
                    result_set.add(triplet)
                seen_inner.add(val2)

        return [list(t) for t in result_set]


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_three_sum():
    sol = Solution()

    def normalize(result: List[List[int]]) -> Set[Tuple[int, ...]]:
        """Helper to compare triplets independently of order."""
        return {tuple(sorted(trip)) for trip in result}

    # Test Case 1: Standard example with multiple positive/negative values
    nums1 = [-1, 0, 1, 2, -1, -4]
    expected1 = {(-1, -1, 2), (-1, 0, 1)}
    assert normalize(sol.threeSum(nums1.copy())) == expected1
    assert normalize(sol.threeSumHashSet(nums1)) == expected1

    # Test Case 2: No possible triplets
    nums2 = [0, 1, 1]
    assert sol.threeSum(nums2.copy()) == []
    assert sol.threeSumHashSet(nums2) == []

    # Test Case 3: All zeros
    nums3 = [0, 0, 0]
    expected3 = {(0, 0, 0)}
    assert normalize(sol.threeSum(nums3.copy())) == expected3
    assert normalize(sol.threeSumHashSet(nums3)) == expected3

    # Test Case 4: Multiple zeros with duplicate solutions
    nums4 = [0, 0, 0, 0]
    expected4 = {(0, 0, 0)}
    assert normalize(sol.threeSum(nums4.copy())) == expected4
    assert normalize(sol.threeSumHashSet(nums4)) == expected4

    # Test Case 5: Array with duplicate answers and symmetry
    nums5 = [-2, 0, 1, 1, 2]
    expected5 = {(-2, 0, 2), (-2, 1, 1)}
    assert normalize(sol.threeSum(nums5.copy())) == expected5
    assert normalize(sol.threeSumHashSet(nums5)) == expected5

    # Test Case 6: All negative numbers (should be empty)
    nums6 = [-5, -3, -1, -4, -2]
    assert sol.threeSum(nums6.copy()) == []
    assert sol.threeSumHashSet(nums6) == []

    # Test Case 7: All positive numbers (should be empty)
    nums7 = [1, 2, 3, 4, 5]
    assert sol.threeSum(nums7.copy()) == []
    assert sol.threeSumHashSet(nums7) == []


if __name__ == "__main__":
    test_three_sum()
    print("All 3Sum unit tests passed successfully!")
