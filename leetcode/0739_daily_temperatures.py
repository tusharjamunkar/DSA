"""
0739. Daily Temperatures
Difficulty: Medium
Topic: Stack / Monotonic Stack / Array
LeetCode Link: https://leetcode.com/problems/daily-temperatures/

Problem Statement:
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait
after the ith day to get a warmer temperature. If there is no future day for which
this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Optimal Monotonic Decreasing Stack Approach:

        Algorithmic Intuition:
        - We need the distance to the next strictly greater element to the right.
        - Maintain a stack of indices whose next warmer day has not yet been found.
        - Elements on the stack have strictly decreasing temperatures from bottom to top.
        - When examining day `curr_idx` with temperature `curr_temp`:
          - While stack is not empty and `curr_temp > temperatures[stack[-1]]`:
            - We found the first warmer day for `prev_idx = stack.pop()`.
            - `answer[prev_idx] = curr_idx - prev_idx`.
          - Push `curr_idx` onto the stack.
        - Any days remaining in the stack have no warmer future day, so their answer stays 0.

        Complexity:
        - Time Complexity:  O(n) - Every index is pushed and popped from the stack at most once.
        - Space Complexity: O(n) - Stack can hold up to n elements in monotonically decreasing cases.
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []  # stores indices

        for curr_idx, curr_temp in enumerate(temperatures):
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                answer[prev_idx] = curr_idx - prev_idx
            stack.append(curr_idx)

        return answer


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_daily_temperatures():
    sol = Solution()

    # Test Case 1: Standard mixed fluctuation
    t1 = [73, 74, 75, 71, 69, 72, 76, 73]
    assert sol.dailyTemperatures(t1) == [1, 1, 4, 2, 1, 1, 0, 0]

    # Test Case 2: Strictly increasing
    t2 = [30, 40, 50, 60]
    assert sol.dailyTemperatures(t2) == [1, 1, 1, 0]

    # Test Case 3: Strictly decreasing (no warmer days)
    t3 = [90, 80, 70, 60]
    assert sol.dailyTemperatures(t3) == [0, 0, 0, 0]

    # Test Case 4: Single temperature day
    assert sol.dailyTemperatures([50]) == [0]

    # Test Case 5: Equal temperatures (must be strictly warmer)
    assert sol.dailyTemperatures([70, 70, 70]) == [0, 0, 0]

    # Test Case 6: Late warmer jump
    assert sol.dailyTemperatures([70, 60, 50, 80]) == [3, 2, 1, 0]


if __name__ == "__main__":
    test_daily_temperatures()
    print("All Daily Temperatures unit tests passed successfully!")
