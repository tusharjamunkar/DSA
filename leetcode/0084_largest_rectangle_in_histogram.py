"""
0084. Largest Rectangle in Histogram
Difficulty: Hard
Topic: Stack / Monotonic Stack / Array
LeetCode Link: https://leetcode.com/problems/largest-rectangle-in-histogram/

Problem Statement:
Given an array of integers heights representing the histogram's bar height where the width
of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units (height 5, width 2).

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
- 1 <= heights.length <= 10^5
- 0 <= heights[i] <= 10^4
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Optimal Monotonic Increasing Stack Approach:

        Algorithmic Intuition:
        - To maximize rectangular area `height * width`, for each bar of height `h`, we want
          to determine how far it can extend to the left and to the right without encountering
          a shorter bar.
        - Maintain a stack of pairs `(start_idx, height)` with strictly increasing heights.
        - As we iterate through each bar `(i, h)`:
          - If `h < stack[-1][1]`, the rectangle of height `stack[-1][1]` can no longer extend rightward.
            - We pop `(prev_idx, prev_h)` and compute its bounded area: `prev_h * (i - prev_idx)`.
            - Update `max_area = max(max_area, area)`.
            - Since the current bar `h` is shorter than `prev_h`, bar `h` could have extended
              leftwards back to `prev_idx`!
            - Set `start_idx = prev_idx`.
          - Push `(start_idx, h)` onto the stack.
        - After scanning all bars, any remaining bars on the stack could extend all the way to
          the right end of the histogram (`n = len(heights)`):
          - For each `(idx, h)` in stack: `max_area = max(max_area, h * (n - idx))`.

        Complexity:
        - Time Complexity:  O(n) - Each bar index is pushed and popped at most once.
        - Space Complexity: O(n) - Stack stores at most n elements.
        """
        max_area = 0
        stack = []  # stores pairs: (start_index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                prev_idx, prev_h = stack.pop()
                max_area = max(max_area, prev_h * (i - prev_idx))
                start = prev_idx
            stack.append((start, h))

        n = len(heights)
        for idx, h in stack:
            max_area = max(max_area, h * (n - idx))

        return max_area


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_largest_rectangle_in_histogram():
    sol = Solution()

    # Test Case 1: Standard peak
    assert sol.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10

    # Test Case 2: Two bars
    assert sol.largestRectangleArea([2, 4]) == 4

    # Test Case 3: Monotonically increasing
    assert sol.largestRectangleArea([1, 2, 3, 4, 5]) == 9  # height 3 * width 3 = 9

    # Test Case 4: Monotonically decreasing
    assert sol.largestRectangleArea([5, 4, 3, 2, 1]) == 9

    # Test Case 5: All identical heights
    assert sol.largestRectangleArea([3, 3, 3, 3]) == 12

    # Test Case 6: Single bar
    assert sol.largestRectangleArea([7]) == 7

    # Test Case 7: Bar of height 0 in the middle
    assert sol.largestRectangleArea([2, 1, 2]) == 3
    assert sol.largestRectangleArea([3, 0, 3]) == 3


if __name__ == "__main__":
    test_largest_rectangle_in_histogram()
    print("All Largest Rectangle in Histogram unit tests passed successfully!")
