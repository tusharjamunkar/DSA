"""
0239. Sliding Window Maximum
Difficulty: Hard
Topic: Sliding Window / Monotonic Queue / Heap / Deque
LeetCode Link: https://leetcode.com/problems/sliding-window-maximum/

Problem Statement:
You are given an array of integers nums, there is a sliding window of size k which is moving
from the very left of the array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length
"""

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Optimal Monotonic Deque Approach:

        Algorithmic Intuition:
        - Maintain a monotonically decreasing deque `q` that stores indices of `nums`.
        - Elements inside `q` are kept strictly in decreasing order of values (`nums[q[0]] > nums[q[1]] > ...`).
        - For each index `i` from 0 to len(nums) - 1:
          1. Evict elements outside current window: while `q[0] < i - k + 1`, pop from left.
          2. Maintain monotonic property: while `q` is not empty and `nums[q[-1]] < nums[i]`,
             pop from right. (Any smaller element preceding `nums[i]` can never be the max in any
             future window that includes `nums[i]`).
          3. Append current index `i` to `q`.
          4. Record max: once `i >= k - 1` (valid full window), append `nums[q[0]]` to result.

        Complexity:
        - Time Complexity:  O(n) - Every index is pushed and popped at most once.
        - Space Complexity: O(k) - Deque holds at most k indices at any moment.
        """
        q = deque()  # stores indices
        result = []

        for i in range(len(nums)):
            # 1. Remove indices outside the sliding window
            if q and q[0] < i - k + 1:
                q.popleft()

            # 2. Pop smaller elements from the tail of deque
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            # 3. Add current element index
            q.append(i)

            # 4. Record the maximum for the window
            if i >= k - 1:
                result.append(nums[q[0]])

        return result


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_sliding_window_maximum():
    sol = Solution()

    # Test Case 1: Standard mixed array
    assert sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]

    # Test Case 2: Single element window
    assert sol.maxSlidingWindow([1], 1) == [1]

    # Test Case 3: Monotonically increasing
    assert sol.maxSlidingWindow([1, 2, 3, 4, 5], 3) == [3, 4, 5]

    # Test Case 4: Monotonically decreasing
    assert sol.maxSlidingWindow([5, 4, 3, 2, 1], 2) == [5, 4, 3, 2]

    # Test Case 5: All identical elements
    assert sol.maxSlidingWindow([4, 4, 4, 4], 2) == [4, 4, 4]

    # Test Case 6: Negative numbers
    assert sol.maxSlidingWindow([-7, -8, -7, 5, 7, 1, 6, 0], 4) == [5, 7, 7, 7, 7]

    # Test Case 7: Window size equals array size
    assert sol.maxSlidingWindow([9, 11], 2) == [11]


if __name__ == "__main__":
    test_sliding_window_maximum()
    print("All Sliding Window Maximum unit tests passed successfully!")
