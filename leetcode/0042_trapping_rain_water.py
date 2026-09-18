"""
0042. Trapping Rain Water
Difficulty: Hard
Topic: Two Pointers / Dynamic Programming / Monotonic Stack
LeetCode Link: https://leetcode.com/problems/trapping-rain-water/

Problem Statement:
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Optimal Two-Pointer Converging Approach:
        
        Mathematical / Algorithmic Intuition:
        - For any column at index i, the water volume trapped directly above it is:
            water[i] = max(0, min(max_left[i], max_right[i]) - height[i])
        - Instead of precomputing prefix and suffix max arrays in O(n) space, we can converge
          two pointers from the left and right boundaries with strictly O(1) auxiliary space.
        
        Invariant & Proof:
        - Maintain `left = 0`, `right = len(height) - 1`, and running maximums `left_max` and `right_max`.
        - At each step:
          - If `left_max <= right_max`:
            - The water level at `left` is strictly bounded by `left_max`. Why? Because `right_max >= left_max`,
              and `right_max` is just the maximum seen from the right boundary so far; the true absolute maximum
              to the right of `left` is at least `right_max >= left_max`. Therefore, the bottleneck for `left`
              is definitively `left_max`, regardless of any hidden taller peaks in between!
            - We can safely accumulate `left_max - height[left]` water at index `left`.
            - Advance `left += 1` and update `left_max`.
          - Symmetrically, if `right_max < left_max`:
            - The bottleneck for `right` is definitively `right_max`.
            - Accumulate `right_max - height[right]` water at index `right`.
            - Advance `right -= 1` and update `right_max`.
        
        Time Complexity:  O(n) - Exactly n steps; each pointer advances until left and right meet.
        Space Complexity: O(1) - Constant auxiliary space (only four integer state variables).
        """
        if not height or len(height) < 3:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total_water = 0

        while left < right:
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                total_water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]

        return total_water

    def trapDP(self, height: List[int]) -> int:
        """
        Dynamic Programming (Prefix & Suffix Maximum Arrays):
        
        - Precompute `left_max[i]` = max(height[0..i]).
        - Precompute `right_max[i]` = max(height[i..n-1]).
        - For each column i, water = min(left_max[i], right_max[i]) - height[i].
        
        Time Complexity:  O(n) - Three linear passes.
        Space Complexity: O(n) - Two arrays of size n for left_max and right_max.
        """
        n = len(height)
        if n < 3:
            return 0

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        total_water = 0
        for i in range(n):
            water_level = min(left_max[i], right_max[i])
            if water_level > height[i]:
                total_water += water_level - height[i]

        return total_water

    def trapMonotonicStack(self, height: List[int]) -> int:
        """
        Monotonic Decreasing Stack Approach:
        
        - Maintain a stack of indices with strictly decreasing bar heights.
        - When encountering a bar taller than the stack top, it forms a right boundary of a basin.
        - Pop the bottom of the basin (the valley).
        - If the stack is not empty, the new stack top is the left boundary.
        - Calculate bounded height = min(height[left], height[right]) - height[bottom].
        - Calculate width = right - left - 1.
        - Add bounded height * width to total water.
        
        Time Complexity:  O(n) - Each element is pushed and popped at most once.
        Space Complexity: O(n) - Stack can hold up to n elements in monotonically decreasing cases.
        """
        stack: List[int] = []
        total_water = 0

        for current_idx, current_height in enumerate(height):
            while stack and current_height > height[stack[-1]]:
                bottom_idx = stack.pop()

                if not stack:
                    break

                left_idx = stack[-1]
                distance = current_idx - left_idx - 1
                bounded_height = min(current_height, height[left_idx]) - height[bottom_idx]
                total_water += distance * bounded_height

            stack.append(current_idx)

        return total_water


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_trapping_rain_water():
    sol = Solution()

    # Test Case 1: Standard jagged elevation map
    h1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert sol.trap(h1) == 6
    assert sol.trapDP(h1) == 6
    assert sol.trapMonotonicStack(h1) == 6

    # Test Case 2: Deep basin
    h2 = [4, 2, 0, 3, 2, 5]
    assert sol.trap(h2) == 9
    assert sol.trapDP(h2) == 9
    assert sol.trapMonotonicStack(h2) == 9

    # Test Case 3: Flat elevation (no water)
    h3 = [3, 3, 3, 3]
    assert sol.trap(h3) == 0
    assert sol.trapDP(h3) == 0
    assert sol.trapMonotonicStack(h3) == 0

    # Test Case 4: Strictly increasing (no basin)
    h4 = [1, 2, 3, 4, 5]
    assert sol.trap(h4) == 0
    assert sol.trapDP(h4) == 0
    assert sol.trapMonotonicStack(h4) == 0

    # Test Case 5: Strictly decreasing (no basin)
    h5 = [5, 4, 3, 2, 1]
    assert sol.trap(h5) == 0
    assert sol.trapDP(h5) == 0
    assert sol.trapMonotonicStack(h5) == 0

    # Test Case 6: V-shaped basin
    h6 = [5, 0, 5]
    assert sol.trap(h6) == 5
    assert sol.trapDP(h6) == 5
    assert sol.trapMonotonicStack(h6) == 5

    # Test Case 7: Less than 3 bars (cannot trap water)
    assert sol.trap([]) == 0
    assert sol.trap([1]) == 0
    assert sol.trap([1, 2]) == 0


if __name__ == "__main__":
    test_trapping_rain_water()
    print("All Trapping Rain Water unit tests passed successfully!")
