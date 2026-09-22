"""
0853. Car Fleet
Difficulty: Medium
Topic: Stack / Monotonic Stack / Sorting / Array
LeetCode Link: https://leetcode.com/problems/car-fleet/

Problem Statement:
There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

You are given two integer arrays position and speed, both of length n, where position[i] is
the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car cannot pass another car ahead of it, but it can catch up to it and drive bumper-to-bumper
at the same speed. The faster car will slow down to match the slower car's speed. The distance
between them is ignored.

A car fleet is some non-empty set of cars driving at the same position and speed. Note that a single
car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered
as one car fleet.

Return the number of car fleets that will arrive at the destination.

Example 1:
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
- The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
- The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
- The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6.
  The fleet moves at speed 1 until it reaches target 12.

Example 2:
Input: target = 10, position = [3], speed = [3]
Output: 1
Explanation: There is only one car, hence there is only one fleet.

Example 3:
Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
Explanation:
- The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4.
  The fleet moves at speed 2.
- Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting at 6.
  The fleet moves at speed 1 until target 100.

Constraints:
- n == position.length == speed.length
- 1 <= n <= 10^5
- 0 < target <= 10^6
- 0 <= position[i] < target
- All values of position are unique.
- 0 < speed[i] <= 10^6
"""

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Optimal Monotonic Stack / Position-Descending Sweep:

        Algorithmic Intuition:
        - A car cannot overtake any car ahead of it. Therefore, the car closest to the target
          dictates the arrival time of any car behind it that catches up.
        - Pair each car's (position, speed) and sort in descending order of position.
        - Compute the time needed to reach the target for each car: `time = (target - pos) / spd`.
        - Maintain a stack of fleet arrival times:
          - If the current car takes <= time of the fleet ahead (`stack[-1]`), it will collide
            with and join that fleet before or at the target. Thus it does NOT create a new fleet.
          - If the current car takes > time of the fleet ahead, it can never catch up, and
            instead forms a separate, slower fleet behind it. Push its time onto the stack.
        - The number of surviving fleets is `len(stack)`.

        Complexity:
        - Time Complexity:  O(n log n) - Dominated by sorting n cars by starting position.
        - Space Complexity: O(n) - Storing car pairs and stack of arrival times.
        """
        # Pair position with speed, sort by position descending (closest to target first)
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        stack = []  # stores arrival times of leading fleet cars

        for pos, spd in cars:
            time_to_target = (target - pos) / spd
            if not stack or time_to_target > stack[-1]:
                stack.append(time_to_target)

        return len(stack)


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_car_fleet():
    sol = Solution()

    # Test Case 1: Example 1
    assert sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3

    # Test Case 2: Single car
    assert sol.carFleet(10, [3], [3]) == 1

    # Test Case 3: All cars merge into a single fleet
    assert sol.carFleet(100, [0, 2, 4], [4, 2, 1]) == 1

    # Test Case 4: No cars catch up (monotonically faster as position decreases)
    assert sol.carFleet(10, [6, 8], [3, 2]) == 2

    # Test Case 5: Cars catch up right at destination
    # Car 1 at pos 0 speed 2 -> time 5
    # Car 2 at pos 5 speed 1 -> time 5
    assert sol.carFleet(10, [0, 5], [2, 1]) == 1


if __name__ == "__main__":
    test_car_fleet()
    print("All Car Fleet unit tests passed successfully!")
