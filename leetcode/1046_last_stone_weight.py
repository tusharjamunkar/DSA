"""
1046. Last Stone Weight
Difficulty: Easy
Topic: Heap (Priority Queue) / Array / Simulation
LeetCode Link: https://leetcode.com/problems/last-stone-weight/

Problem Statement:
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
- If x == y, both stones are destroyed.
- If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left.
Return the weight of the last remaining stone. If there are no stones left, return 0.

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Example 2:
Input: stones = [1]
Output: 1

Constraints:
- 1 <= stones.length <= 30
- 1 <= stones[i] <= 1000
"""

from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Optimal Max-Heap Simulation:

        Algorithmic Intuition:
        - Python's `heapq` module implements a min-heap by default.
        - To simulate a max-heap, we negate all stone weights: `-w`.
        - While more than 1 stone remains:
          1. Pop the heaviest stone: `first = -heapq.heappop(max_heap)`.
          2. Pop the second heaviest stone: `second = -heapq.heappop(max_heap)`.
          3. If `first != second`:
             The remaining piece `first - second` is pushed back onto the heap as `-(first - second)`.
          4. If `first == second`, both stones are destroyed and nothing is pushed back.
        - If 1 stone remains, return `-max_heap[0]`. Otherwise, return 0.

        Complexity:
        - Time Complexity:  O(n log n) - Converting to heap takes O(n). In each iteration, 2 stones are popped and at most 1 is inserted, taking O(log n) time per step. There are at most n steps.
        - Space Complexity: O(n) - To store the negated weights in the heap.
        """
        # Negate values to simulate max-heap
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            if first != second:
                heapq.heappush(max_heap, -(first - second))

        return -max_heap[0] if max_heap else 0


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_last_stone_weight():
    sol = Solution()

    # Test Case 1: Standard case from LeetCode
    assert sol.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1

    # Test Case 2: Single stone
    assert sol.lastStoneWeight([1]) == 1

    # Test Case 3: All stones cancel out to 0
    assert sol.lastStoneWeight([2, 2]) == 0

    # Test Case 4: Multiple identical stones
    assert sol.lastStoneWeight([3, 7, 2]) == 2

    # Test Case 5: Large values
    assert sol.lastStoneWeight([100, 50, 30, 20]) == 0


if __name__ == "__main__":
    test_last_stone_weight()
    print("All Last Stone Weight unit tests passed successfully!")
