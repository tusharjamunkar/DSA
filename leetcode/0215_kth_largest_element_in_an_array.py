"""
0215. Kth Largest Element in an Array
Difficulty: Medium
Topic: Array / Divide and Conquer / Sorting / Heap (Priority Queue) / Quickselect
LeetCode Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

Problem Statement:
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

from typing import List
import heapq
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Optimal Min-Heap of Size k:

        Algorithmic Intuition:
        - Maintain a min-heap containing at most k elements.
        - For each number in `nums`:
          - Push `num` into the heap.
          - If heap size exceeds `k`, pop the smallest element (`heapq.heappop`).
        - After scanning all n elements, the heap contains the k largest elements from `nums`.
        - The root `min_heap[0]` is the minimum among these k largest, which is precisely the kth largest!

        Complexity:
        - Time Complexity:  O(n log k) - We perform n heap operations on a heap of size at most k.
        - Space Complexity: O(k) - Auxiliary storage bounded strictly by k.
        """
        min_heap: List[int] = []

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            elif num > min_heap[0]:
                heapq.heappushpop(min_heap, num)

        return min_heap[0]

    def findKthLargestQuickselect(self, nums: List[int], k: int) -> int:
        """
        Alternative Quickselect (Hoare's Selection Algorithm):
        Finds the (n - k)th smallest element in O(n) average time.

        Complexity:
        - Time Complexity:  O(n) average, O(n^2) worst case (mitigated by randomized pivot).
        - Space Complexity: O(1) iterative partition or O(log n) recursion stack.
        """
        target_idx = len(nums) - k

        def quickselect(l: int, r: int) -> int:
            pivot_idx = random.randint(l, r)
            pivot = nums[pivot_idx]
            # Move pivot to end
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]

            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]

            if p == target_idx:
                return nums[p]
            elif p < target_idx:
                return quickselect(p + 1, r)
            else:
                return quickselect(l, p - 1)

        # Work on a copy to avoid mutating caller's input
        arr = nums[:]
        return quickselect(0, len(arr) - 1)

    def findKthLargestCountingSort(self, nums: List[int], k: int) -> int:
        """
        Alternative Counting Sort Bucket Approach (exploiting constraint -10^4 <= nums[i] <= 10^4):

        Complexity:
        - Time Complexity:  O(n + M) where M is the range of values (20,001).
        - Space Complexity: O(M) for frequency bucket array.
        """
        offset = 10000
        count = [0] * 20001

        for num in nums:
            count[num + offset] += 1

        for val in range(20000, -1, -1):
            k -= count[val]
            if k <= 0:
                return val - offset

        return -1


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_find_kth_largest():
    sol = Solution()

    # Test Case 1: Example 1
    nums1 = [3, 2, 1, 5, 6, 4]
    assert sol.findKthLargest(nums1, 2) == 5
    assert sol.findKthLargestQuickselect(nums1, 2) == 5
    assert sol.findKthLargestCountingSort(nums1, 2) == 5

    # Test Case 2: Example 2 (with duplicates)
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    assert sol.findKthLargest(nums2, 4) == 4
    assert sol.findKthLargestQuickselect(nums2, 4) == 4
    assert sol.findKthLargestCountingSort(nums2, 4) == 4

    # Test Case 3: k = 1 (Maximum element)
    nums3 = [7, 10, 4, 3, 20, 15]
    assert sol.findKthLargest(nums3, 1) == 20
    assert sol.findKthLargestQuickselect(nums3, 1) == 20
    assert sol.findKthLargestCountingSort(nums3, 1) == 20

    # Test Case 4: k = len(nums) (Minimum element)
    nums4 = [7, 10, 4, 3, 20, 15]
    assert sol.findKthLargest(nums4, len(nums4)) == 3
    assert sol.findKthLargestQuickselect(nums4, len(nums4)) == 3
    assert sol.findKthLargestCountingSort(nums4, len(nums4)) == 3

    # Test Case 5: Single element
    assert sol.findKthLargest([42], 1) == 42
    assert sol.findKthLargestQuickselect([42], 1) == 42
    assert sol.findKthLargestCountingSort([42], 1) == 42


if __name__ == "__main__":
    test_find_kth_largest()
    print("All Kth Largest Element in an Array unit tests passed successfully!")
