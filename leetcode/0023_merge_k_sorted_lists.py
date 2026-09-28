"""
0023. Merge k Sorted Lists
Difficulty: Hard
Topic: Linked List / Divide and Conquer / Heap (Priority Queue) / Merge Sort
LeetCode Link: https://leetcode.com/problems/merge-k-sorted-lists/

Problem Statement:
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 10^4.
"""

from typing import Optional, List
import heapq


class ListNode:
    """Definition for singly-linked list node."""
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, values: List[int]) -> Optional["ListNode"]:
        dummy = cls()
        curr = dummy
        for v in values:
            curr.next = cls(v)
            curr = curr.next
        return dummy.next

    def to_list(self) -> List[int]:
        res = []
        curr: Optional["ListNode"] = self
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Optimal Divide and Conquer (Pairwise Merge):

        Algorithmic Intuition:
        - Instead of sequentially merging lists one by one (O(k * N)), pair up the lists
          and merge each pair (like Bottom-up Merge Sort).
        - In each iteration, `k` lists become `ceil(k / 2)` lists.
        - Number of levels of reduction = O(log k).
        - Each level processes all N total nodes in O(N) time.
        - Total time: O(N log k).

        Complexity:
        - Time Complexity:  O(N log k) where N is total nodes across all k lists.
        - Space Complexity: O(1) auxiliary space (in-place pointer rearrangement).
        """
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_lists: List[Optional[ListNode]] = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_lists.append(self._merge_two_lists(l1, l2))

            lists = merged_lists

        return lists[0]

    def _merge_two_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Helper to merge two sorted lists in O(n + m) time, O(1) space."""
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        return dummy.next

    def mergeKListsHeap(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Alternative Min-Heap Approach:
        Push head nodes of all lists into a min-heap. Repeatedly pop minimum node and push its next.

        Complexity:
        - Time Complexity:  O(N log k)
        - Space Complexity: O(k) - Heap storage of at most k nodes.
        """
        min_heap = []
        dummy = ListNode(0)
        curr = dummy

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_merge_k_lists():
    sol = Solution()

    # Test Case 1: lists = [[1,4,5],[1,3,4],[2,6]] -> [1,1,2,3,4,4,5,6]
    l1 = ListNode.from_list([1, 4, 5])
    l2 = ListNode.from_list([1, 3, 4])
    l3 = ListNode.from_list([2, 6])
    res = sol.mergeKLists([l1, l2, l3])
    assert res is not None and res.to_list() == [1, 1, 2, 3, 4, 4, 5, 6]

    # Test Case 1 (Heap variant):
    l1_h = ListNode.from_list([1, 4, 5])
    l2_h = ListNode.from_list([1, 3, 4])
    l3_h = ListNode.from_list([2, 6])
    res_h = sol.mergeKListsHeap([l1_h, l2_h, l3_h])
    assert res_h is not None and res_h.to_list() == [1, 1, 2, 3, 4, 4, 5, 6]

    # Test Case 2: Empty list of lists []
    assert sol.mergeKLists([]) is None
    assert sol.mergeKListsHeap([]) is None

    # Test Case 3: List containing one empty list [[]]
    assert sol.mergeKLists([None]) is None
    assert sol.mergeKListsHeap([None]) is None


if __name__ == "__main__":
    test_merge_k_lists()
    print("All Merge k Sorted Lists unit tests passed successfully!")
