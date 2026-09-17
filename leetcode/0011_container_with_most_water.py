"""
0011. Container With Most Water
Difficulty: Medium
Topic: Two Pointers / Greedy / Array
LeetCode Link: https://leetcode.com/problems/container-with-most-water/

Problem Statement:
You are given an integer array height of length n. There are n vertical lines drawn
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container
contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water the container can contain is between indices 1 and 8:
min(8, 7) * (8 - 1) = 7 * 7 = 49.

Example 2:
Input: height = [1,1]
Output: 1
Explanation: min(1, 1) * (1 - 0) = 1 * 1 = 1.

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Optimal Two-Pointer Greedy Approach:
        
        Mathematical / Algorithmic Proof:
        - The area formed between two indices `left` and `right` is:
          `Area = min(height[left], height[right]) * (right - left)`
        - We initialize `left = 0` and `right = len(height) - 1`, which maximizes the width `(right - left)`.
        - To explore potentially larger areas, we must move at least one pointer inward.
          Moving inward strictly decreases the width `(right - left)` by 1 at each step.
        - Suppose `height[left] < height[right]`:
          - The current height bottleneck is `height[left]`.
          - If we were to move `right` inward to any `right'`, the new width would be strictly smaller,
            and the new height could NEVER exceed `height[left]`.
            Therefore: `min(height[left], height[right']) * (right' - left) < min(height[left], height[right]) * (right - left)`.
          - Thus, NO pair involving `left` and any inner index `right'` can possibly beat the current area!
          - By moving `left` inward (`left += 1`), we safely discard `left` from consideration without missing the optimal pair.
        - Symmetrically, if `height[right] < height[left]`, we discard `right` by moving `right -= 1`.
        - If `height[left] == height[right]`, moving either (or both) pointer(s) inward is safe because any pair between
          an inner index and either end is strictly bounded by that height with smaller width.
        
        Time Complexity:  O(n) - Single pass; left and right pointers meet after exactly n - 1 steps.
        Space Complexity: O(1) - Constant auxiliary space (stores only pointers and max area integer).
        """
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            h_left, h_right = height[left], height[right]

            if h_left < h_right:
                area = h_left * width
                if area > max_water:
                    max_water = area
                left += 1
            else:
                area = h_right * width
                if area > max_water:
                    max_water = area
                right -= 1

        return max_water

    def maxAreaOptimized(self, height: List[int]) -> int:
        """
        Optimized Two-Pointer with Fast-Forward Skipping:
        
        - When advancing `left` or `right`, any subsequent line that is shorter than or equal to
          the discarded boundary can NEVER yield a larger area (width is smaller, height is not larger).
        - We can fast-forward past all such inferior heights using an inner while loop,
          substantially reducing the number of multiplication and comparison operations on benchmark inputs.
        
        Time Complexity:  O(n) - Still at most n pointer movements total, with lower constant factor.
        Space Complexity: O(1) - Constant auxiliary space.
        """
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            h_left, h_right = height[left], height[right]

            if h_left < h_right:
                area = h_left * width
                if area > max_water:
                    max_water = area
                # Fast forward past all lines <= current bottleneck
                while left < right and height[left] <= h_left:
                    left += 1
            else:
                area = h_right * width
                if area > max_water:
                    max_water = area
                # Fast forward past all lines <= current bottleneck
                while left < right and height[right] <= h_right:
                    right -= 1

        return max_water

    def maxAreaBruteForce(self, height: List[int]) -> int:
        """
        Brute Force Baseline Approach (Reference):
        
        - Check every possible pair (i, j) and compute the water area.
        
        Time Complexity:  O(n^2) - Pairwise combinations n * (n - 1) / 2.
        Space Complexity: O(1) - Constant space.
        """
        max_water = 0
        n = len(height)
        for i in range(n):
            for j in range(i + 1, n):
                area = min(height[i], height[j]) * (j - i)
                if area > max_water:
                    max_water = area
        return max_water


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_container_with_most_water():
    sol = Solution()

    # Test Case 1: Standard LeetCode example
    h1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert sol.maxArea(h1) == 49
    assert sol.maxAreaOptimized(h1) == 49
    assert sol.maxAreaBruteForce(h1) == 49

    # Test Case 2: Minimal 2-element array
    h2 = [1, 1]
    assert sol.maxArea(h2) == 1
    assert sol.maxAreaOptimized(h2) == 1
    assert sol.maxAreaBruteForce(h2) == 1

    # Test Case 3: Decreasing staircase
    h3 = [4, 3, 2, 1, 4]
    assert sol.maxArea(h3) == 16  # min(4, 4) * (4 - 0) = 16
    assert sol.maxAreaOptimized(h3) == 16
    assert sol.maxAreaBruteForce(h3) == 16

    # Test Case 4: Tall peaks in the middle vs wider ends
    h4 = [1, 2, 1]
    assert sol.maxArea(h4) == 2  # min(1, 1) * 2 = 2 or min(2, 1) * 1 = 1 -> max is 2
    assert sol.maxAreaOptimized(h4) == 2
    assert sol.maxAreaBruteForce(h4) == 2

    # Test Case 5: Zero height elements
    h5 = [0, 2, 0, 3, 1, 0]
    assert sol.maxArea(h5) == 4  # min(2, 1) * (4 - 1) = 3 or min(2, 3) * (3 - 1) = 4
    assert sol.maxAreaOptimized(h5) == 4
    assert sol.maxAreaBruteForce(h5) == 4

    # Test Case 6: Ascending array
    h6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Optimal: index 4 (val 5) and index 9 (val 10): 5 * 5 = 25
    assert sol.maxArea(h6) == 25
    assert sol.maxAreaOptimized(h6) == 25
    assert sol.maxAreaBruteForce(h6) == 25


if __name__ == "__main__":
    test_container_with_most_water()
    print("All Container With Most Water unit tests passed successfully!")
