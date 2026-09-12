"""
0238. Product of Array Except Self
Difficulty: Medium
Topic: Arrays & Hashing / Prefix & Suffix Products
LeetCode Link: https://leetcode.com/problems/product-of-array-except-self/

Problem Statement:
Given an integer array nums, return an array answer such that answer[i] is equal 
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? 
(The output array does not count as extra space for space complexity analysis.)
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Optimal Two-Pass O(1) Extra Space Approach:
        - For each index i, answer[i] is equal to (product of elements to the left) * (product of elements to the right).
        - Pass 1 (Left to Right): Populate answer[i] with the product of all elements to the left of i.
          Initialize answer[0] = 1. For i > 0, answer[i] = answer[i - 1] * nums[i - 1].
        - Pass 2 (Right to Left): Maintain a running right_product variable initialized to 1.
          Multiply answer[i] by right_product, then update right_product *= nums[i].

        Time Complexity:  O(n) - Two linear passes over array of size n.
        Space Complexity: O(1) extra space - Output array answer uses O(n) storage as required by return type.
        """
        n = len(nums)
        answer = [1] * n

        # Left prefix pass
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        # Right suffix pass with running accumulator
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer

    def productExceptSelfWithArrays(self, nums: List[int]) -> List[int]:
        """
        Explicit Prefix & Suffix Arrays Approach:
        - Build prefix array where prefix[i] = product of nums[0..i-1].
        - Build suffix array where suffix[i] = product of nums[i+1..n-1].
        - Output answer[i] = prefix[i] * suffix[i].

        Time Complexity:  O(n)
        Space Complexity: O(n) extra space for explicit prefix and suffix arrays.
        """
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        return [prefix[i] * suffix[i] for i in range(n)]


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_product_except_self():
    sol = Solution()

    # Test Case 1: Standard positive numbers
    nums1 = [1, 2, 3, 4]
    expected1 = [24, 12, 8, 6]
    assert sol.productExceptSelf(nums1) == expected1
    assert sol.productExceptSelfWithArrays(nums1) == expected1

    # Test Case 2: Array containing zero and negative values
    nums2 = [-1, 1, 0, -3, 3]
    expected2 = [0, 0, 9, 0, 0]
    assert sol.productExceptSelf(nums2) == expected2
    assert sol.productExceptSelfWithArrays(nums2) == expected2

    # Test Case 3: Array containing multiple zeros
    nums3 = [0, 4, 0]
    expected3 = [0, 0, 0]
    assert sol.productExceptSelf(nums3) == expected3
    assert sol.productExceptSelfWithArrays(nums3) == expected3

    # Test Case 4: Minimal length (2 elements)
    nums4 = [5, 10]
    expected4 = [10, 5]
    assert sol.productExceptSelf(nums4) == expected4
    assert sol.productExceptSelfWithArrays(nums4) == expected4


if __name__ == "__main__":
    test_product_except_self()
    print("All Product of Array Except Self tests passed successfully!")
