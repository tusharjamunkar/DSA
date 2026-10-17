"""
0973. K Closest Points to Origin
Difficulty: Medium
Topic: Heap (Priority Queue) / Array / Math / Divide and Conquer / Geometry / Sorting / Quickselect
LeetCode Link: https://leetcode.com/problems/k-closest-points-to-origin/

Problem Statement:
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)^2 + (y1 - y2)^2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Constraints:
- 1 <= k <= points.length <= 10^4
- -10^4 <= xi, yi <= 10^4
"""

from typing import List, Tuple
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Optimal Max-Heap of Size k:

        Algorithmic Intuition:
        - The Euclidean squared distance from (x, y) to (0, 0) is `x^2 + y^2`.
          We can avoid computing square roots because `d1^2 < d2^2` implies `d1 < d2`.
        - To maintain the k closest points, we use a max-heap of size k storing `(-dist, x, y)`.
        - For each point:
          1. Calculate `dist = x * x + y * y`.
          2. If the heap contains fewer than k points, push `(-dist, x, y)`.
          3. If the heap already has k points and `dist < -max_heap[0][0]` (i.e., point is closer than the current furthest in our top-k):
             Evict the furthest point and insert the new closer point.
          4. Otherwise, discard the point.
        - Unpack and return the k points stored in the heap.

        Complexity:
        - Time Complexity:  O(n log k) - For n points, each heap push/pop takes O(log k). When k << n, this is significantly faster than O(n log n) full sorting.
        - Space Complexity: O(k) - Auxiliary space bounded strictly by the max-heap capacity k.
        """
        max_heap: List[Tuple[int, int, int]] = []

        for x, y in points:
            dist = x * x + y * y
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-dist, x, y))
            elif dist < -max_heap[0][0]:
                heapq.heappushpop(max_heap, (-dist, x, y))

        return [[x, y] for _, x, y in max_heap]

    def kClosestMinHeap(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Alternative Min-Heap Approach:
        Construct a min-heap with all points in O(n) time, then pop k closest points in O(k log n).

        Complexity:
        - Time Complexity:  O(n + k log n)
        - Space Complexity: O(n) to store all points in the min-heap.
        """
        min_heap = [(x * x + y * y, x, y) for x, y in points]
        heapq.heapify(min_heap)

        result: List[List[int]] = []
        for _ in range(k):
            _, x, y = heapq.heappop(min_heap)
            result.append([x, y])

        return result


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_k_closest_points():
    sol = Solution()

    # Test Case 1: Example 1
    p1 = [[1, 3], [-2, 2]]
    res1 = sol.kClosest(p1, 1)
    assert res1 == [[-2, 2]]
    assert sol.kClosestMinHeap(p1, 1) == [[-2, 2]]

    # Test Case 2: Example 2
    p2 = [[3, 3], [5, -1], [-2, 4]]
    res2 = sorted(sol.kClosest(p2, 2))
    expected2 = sorted([[3, 3], [-2, 4]])
    assert res2 == expected2
    assert sorted(sol.kClosestMinHeap(p2, 2)) == expected2

    # Test Case 3: k equals length of array
    p3 = [[0, 1], [1, 0]]
    assert sorted(sol.kClosest(p3, 2)) == sorted([[0, 1], [1, 0]])

    # Test Case 4: Points with negative coordinates and varying distances
    p4 = [[-5, 4], [-6, -5], [4, 6]]
    res4 = sol.kClosest(p4, 1)
    assert res4 == [[-5, 4]]  # dist = 25 + 16 = 41 vs 61 vs 52


if __name__ == "__main__":
    test_k_closest_points()
    print("All K Closest Points to Origin unit tests passed successfully!")
