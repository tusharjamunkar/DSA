"""
0004. Median of Two Sorted Arrays
Difficulty: Hard
Topic: Binary Search / Array / Divide and Conquer
LeetCode Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

Problem Statement:
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Optimal Binary Search Partition:

        Algorithmic Intuition:
        - We want to partition both arrays such that the combined left partition has
          half = (m + n + 1) // 2 elements, and all elements in the left partition are
          <= all elements in the right partition.
        - To ensure logarithmic time with respect to the smaller array, we binary search
          on the cut point `i` of the smaller array `A` (where len(A) <= len(B)).
        - For a cut `i` in `A` (0 <= i <= len(A)), the corresponding cut in `B` is
          `j = half - i`.
        - The partition is valid if:
          A_left <= B_right and B_left <= A_right
        - Boundary handling:
          If i == 0, A_left = -infinity
          If i == len(A), A_right = +infinity
          Similarly for B_left and B_right.
        - If total length is odd, median = max(A_left, B_left).
        - If total length is even, median = (max(A_left, B_left) + min(A_right, B_right)) / 2.0.
        - If A_left > B_right, cut `i` is too far right: right = i - 1.
        - Else, cut `i` is too far left: left = i + 1.

        Complexity:
        - Time Complexity:  O(log(min(m, n))) - Binary search on smaller array.
        - Space Complexity: O(1) - Constant auxiliary space.
        """
        A, B = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        total = len(A) + len(B)
        half = (total + 1) // 2

        left, right = 0, len(A)

        while left <= right:
            i = left + (right - left) // 2
            j = half - i

            A_left = A[i - 1] if i > 0 else float("-inf")
            A_right = A[i] if i < len(A) else float("inf")
            B_left = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j] if j < len(B) else float("inf")

            if A_left <= B_right and B_left <= A_right:
                # Correct partition found
                if total % 2 != 0:
                    return float(max(A_left, B_left))
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
            elif A_left > B_right:
                right = i - 1
            else:
                left = i + 1

        raise ValueError("Input arrays are not sorted.")

    def findMedianSortedArraysMerge(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Linear Merge Simulation (Reference / Verification):
        Two-pointer merge tracking elements up to the median indices.

        Complexity:
        - Time Complexity:  O(m + n)
        - Space Complexity: O(1)
        """
        total = len(nums1) + len(nums2)
        mid1_idx = (total - 1) // 2
        mid2_idx = total // 2

        i = j = count = 0
        val1 = val2 = 0

        while count <= mid2_idx:
            if i < len(nums1) and (j >= len(nums2) or nums1[i] <= nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1

            if count == mid1_idx:
                val1 = curr
            if count == mid2_idx:
                val2 = curr
            count += 1

        return (val1 + val2) / 2.0


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_find_median_sorted_arrays():
    sol = Solution()

    # Test Case 1: Odd total length
    assert sol.findMedianSortedArrays([1, 3], [2]) == 2.0
    assert sol.findMedianSortedArraysMerge([1, 3], [2]) == 2.0

    # Test Case 2: Even total length
    assert sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert sol.findMedianSortedArraysMerge([1, 2], [3, 4]) == 2.5

    # Test Case 3: One array empty
    assert sol.findMedianSortedArrays([], [1]) == 1.0
    assert sol.findMedianSortedArrays([2], []) == 2.0
    assert sol.findMedianSortedArrays([], [2, 3]) == 2.5

    # Test Case 4: Disjoint non-overlapping ranges
    assert sol.findMedianSortedArrays([1, 2], [3, 4, 5, 6]) == 3.5
    assert sol.findMedianSortedArrays([5, 6, 7], [1, 2, 3, 4]) == 4.0

    # Test Case 5: Negative numbers
    assert sol.findMedianSortedArrays([-5, 3, 6], [-2, -1, 0, 7]) == 0.0
    assert sol.findMedianSortedArraysMerge([-5, 3, 6], [-2, -1, 0, 7]) == 0.0

    # Test Case 6: Duplicates across arrays
    assert sol.findMedianSortedArrays([1, 1, 1], [1, 1, 1]) == 1.0


if __name__ == "__main__":
    test_find_median_sorted_arrays()
    print("All Median of Two Sorted Arrays unit tests passed successfully!")
