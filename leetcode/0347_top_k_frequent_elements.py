"""
0347. Top K Frequent Elements
Difficulty: Medium
Topic: Arrays & Hashing / Bucket Sort / Heap
LeetCode Link: https://leetcode.com/problems/top-k-frequent-elements/

Problem Statement:
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

import heapq
from collections import Counter
from typing import Dict, List, Tuple


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Optimal Bucket Sort Approach:
        - Step 1: Count element frequencies using a hash table (O(n)).
        - Step 2: Create a bucket array where index i stores a list of numbers 
          that appear with frequency i. The maximum frequency cannot exceed len(nums).
        - Step 3: Iterate backwards from the highest possible frequency (len(nums)) 
          down to 1, collecting elements into the result list until k elements are accumulated.
        
        Why this is optimal:
        - Frequencies are bounded by n (1 <= freq <= n).
        - Bucket indexing bypasses comparison-based sorting, achieving true linear time.

        Time Complexity:  O(n) - Counting takes O(n), populating buckets takes O(unique elements) <= O(n), 
                                 and traversing buckets backwards takes O(n).
        Space Complexity: O(n) - Hash map and bucket array together use O(n) space.
        """
        count = Counter(nums)
        n = len(nums)
        buckets: List[List[int]] = [[] for _ in range(n + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        result: List[int] = []
        for freq in range(n, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result

    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        """
        Min-Heap Approach:
        - Count element frequencies using a hash map.
        - Maintain a min-heap of size k storing (frequency, num).
        - If heap size exceeds k, pop the element with the smallest frequency.
        - Particularly useful in streaming contexts where the full array is not known ahead of time.

        Time Complexity:  O(n log k) - Pushing and popping from heap of size k takes O(log k) per unique element.
        Space Complexity: O(n + k)   - Hash map takes O(n), heap stores k elements.
        """
        count = Counter(nums)
        min_heap: List[Tuple[int, int]] = []

        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for _, num in min_heap]

    def topKFrequentSort(self, nums: List[int], k: int) -> List[int]:
        """
        Counter Most Common / Sorting Baseline:
        - Simple baseline using Python built-in frequency counting.

        Time Complexity:  O(n log n)
        Space Complexity: O(n)
        """
        count = Counter(nums)
        return [item[0] for item in count.most_common(k)]


# ==========================================
# Unit Tests & Verification
# ==========================================
def _match_k_elements(result: List[int], expected: List[int]) -> bool:
    return sorted(result) == sorted(expected)


def test_top_k_frequent():
    sol = Solution()

    # Test Case 1: Standard case with varying frequencies
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    expected1 = [1, 2]
    assert _match_k_elements(sol.topKFrequent(nums1, k1), expected1)
    assert _match_k_elements(sol.topKFrequentHeap(nums1, k1), expected1)
    assert _match_k_elements(sol.topKFrequentSort(nums1, k1), expected1)

    # Test Case 2: Single element array
    nums2 = [1]
    k2 = 1
    expected2 = [1]
    assert _match_k_elements(sol.topKFrequent(nums2, k2), expected2)
    assert _match_k_elements(sol.topKFrequentHeap(nums2, k2), expected2)
    assert _match_k_elements(sol.topKFrequentSort(nums2, k2), expected2)

    # Test Case 3: Negative numbers and zero
    nums3 = [4, 1, -1, 2, -1, 2, 3]
    k3 = 2
    expected3 = [-1, 2]
    assert _match_k_elements(sol.topKFrequent(nums3, k3), expected3)
    assert _match_k_elements(sol.topKFrequentHeap(nums3, k3), expected3)
    assert _match_k_elements(sol.topKFrequentSort(nums3, k3), expected3)

    # Test Case 4: All distinct elements
    nums4 = [10, 20, 30, 40]
    k4 = 1
    assert len(sol.topKFrequent(nums4, k4)) == 1
    assert len(sol.topKFrequentHeap(nums4, k4)) == 1
    assert len(sol.topKFrequentSort(nums4, k4)) == 1


if __name__ == "__main__":
    test_top_k_frequent()
    print("All Top K Frequent Elements tests passed successfully!")
