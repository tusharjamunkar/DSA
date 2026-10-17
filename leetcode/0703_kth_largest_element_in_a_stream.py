"""
0703. Kth Largest Element in a Stream
Difficulty: Easy
Topic: Heap (Priority Queue) / Data Stream / Design / Binary Search Tree
LeetCode Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/

Problem Statement:
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:
- KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
- int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Example 1:
Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output:
[null, 4, 5, 5, 8, 8]

Explanation:
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

Constraints:
- 1 <= k <= 10^4
- 0 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- -10^4 <= val <= 10^4
- At most 10^4 calls will be made to add.
- It is guaranteed that there will be at least k elements in the array when you search for the kth element.
"""

from typing import List
import heapq


class KthLargest:
    """
    Optimal Min-Heap of Size k:

    Algorithmic Intuition:
    - If we maintain a min-heap containing only the k largest elements seen so far:
      - The smallest element in this min-heap (at root `min_heap[0]`) is precisely the kth largest element of the entire stream.
      - Any element smaller than `min_heap[0]` can never be in the top k elements, so it can be discarded.
    - In `__init__`:
      - We convert `nums` to a min-heap and pop elements until only `k` elements remain.
    - In `add(val)`:
      - Push `val` into the min-heap.
      - If size exceeds `k`, pop the smallest element (`heapq.heappop`).
      - Return `self.min_heap[0]`.

    Complexity:
    - Time Complexity:
      - __init__: O(n log k) or O(n + (n - k) log n) using heapify.
      - add:      O(log k) per addition, since the heap size is strictly bounded by k.
    - Space Complexity:
      - O(k) auxiliary space to store at most k elements in the min-heap.
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)

        # Evict smaller elements until exactly k elements remain in the heap
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_kth_largest():
    # Test Case 1: Example 1 from LeetCode
    kl1 = KthLargest(3, [4, 5, 8, 2])
    assert kl1.add(3) == 4
    assert kl1.add(5) == 5
    assert kl1.add(10) == 5
    assert kl1.add(9) == 8
    assert kl1.add(4) == 8

    # Test Case 2: Initial nums length is smaller than k
    kl2 = KthLargest(1, [])
    assert kl2.add(-3) == -3
    assert kl2.add(-2) == -2
    assert kl2.add(-4) == -2
    assert kl2.add(0) == 0
    assert kl2.add(4) == 4

    # Test Case 3: Duplicate values
    kl3 = KthLargest(2, [5, 5, 5])
    assert kl3.add(5) == 5
    assert kl3.add(6) == 5
    assert kl3.add(7) == 6


if __name__ == "__main__":
    test_kth_largest()
    print("All Kth Largest Element in a Stream unit tests passed successfully!")
