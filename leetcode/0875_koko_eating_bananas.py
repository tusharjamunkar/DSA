"""
0875. Koko Eating Bananas
Difficulty: Medium
Topic: Binary Search / Array
LeetCode Link: https://leetcode.com/problems/koko-eating-bananas/

Problem Statement:
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile
of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats
all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23

Constraints:
- 1 <= piles.length <= 10^4
- piles.length <= h <= 10^9
- 1 <= piles[i] <= 10^9
"""

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Optimal Binary Search on Answer Space:

        Algorithmic Intuition:
        - The minimum conceivable eating speed is `1` banana/hr.
        - The maximum necessary eating speed is `max(piles)` bananas/hr (at which she finishes
          each pile in at most 1 hour, completing in `len(piles) <= h` hours).
        - Monotonic Property:
          If eating speed `k` allows Koko to finish within `h` hours, any speed `k' > k` will
          also suffice. Conversely, if `k` is too slow, any `k'' < k` will also fail.
        - For a candidate speed `mid`:
          Calculate total hours required: `total_hours = sum(math.ceil(p / mid) for p in piles)`.
          - If `total_hours <= h`: `mid` is feasible; record `res = mid` and search slower speeds:
            `right = mid - 1`.
          - If `total_hours > h`: `mid` is too slow; must increase speed: `left = mid + 1`.

        Complexity:
        - Time Complexity:  O(n * log(max(piles))) where n = len(piles).
          Since max(piles) <= 10^9, log2(10^9) ~ 30 iterations.
        - Space Complexity: O(1) - Constant auxiliary space.
        """
        left, right = 1, max(piles)
        res = right

        while left <= right:
            mid = left + (right - left) // 2

            # Compute hours taken at speed `mid`
            # ceil(p / mid) is equivalent to (p + mid - 1) // mid
            total_hours = 0
            for p in piles:
                total_hours += (p + mid - 1) // mid

            if total_hours <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_koko_eating_bananas():
    sol = Solution()

    # Test Case 1: Example 1
    assert sol.minEatingSpeed([3, 6, 7, 11], 8) == 4

    # Test Case 2: Example 2 (h equals number of piles, speed must be max pile)
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30

    # Test Case 3: Example 3
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23

    # Test Case 4: Single pile
    assert sol.minEatingSpeed([100], 1) == 100
    assert sol.minEatingSpeed([100], 2) == 50
    assert sol.minEatingSpeed([100], 3) == 34

    # Test Case 5: Large h
    assert sol.minEatingSpeed([312884470], 968709470) == 1


if __name__ == "__main__":
    test_koko_eating_bananas()
    print("All Koko Eating Bananas unit tests passed successfully!")
