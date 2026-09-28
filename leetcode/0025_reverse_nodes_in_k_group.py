"""
0025. Reverse Nodes in k-Group
Difficulty: Hard
Topic: Linked List / Recursion
LeetCode Link: https://leetcode.com/problems/reverse-nodes-in-k-group/

Problem Statement:
Given the head of a linked list, reverse the nodes of the list k at a time,
and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end,
should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:
- The number of nodes in the list is n.
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000
"""

from typing import Optional, List


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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Optimal Iterative k-Group Reversal:

        Algorithmic Intuition:
        - Use a `dummy` sentinel node before `head`.
        - Maintain `group_prev` pointing to the node immediately prior to current k-group.
        - In each iteration:
          1. Find the `kth` node of the current group using helper `_get_kth(group_prev, k)`.
          2. If `kth` is `None` (fewer than k nodes remain), terminate.
          3. Save `group_next = kth.next`.
          4. Reverse the k nodes between `group_prev.next` and `kth` (standard 3-pointer reversal).
          5. Reconnect pointers:
             - `tmp = group_prev.next` (old group head, now group tail).
             - `group_prev.next = kth` (new group head).
             - `group_prev = tmp` (advance group_prev to tail of reversed group).

        Complexity:
        - Time Complexity:  O(n) - Each node inspected and reversed once.
        - Space Complexity: O(1) - Constant auxiliary space (mutates pointers in-place).
        """
        dummy = ListNode(0, head)
        group_prev: Optional[ListNode] = dummy

        while True:
            kth = self._get_kth(group_prev, k)
            if not kth:
                break

            group_next = kth.next

            # Reverse group
            prev = kth.next
            curr = group_prev.next  # type: ignore

            while curr != group_next:
                nxt = curr.next  # type: ignore
                curr.next = prev  # type: ignore
                prev = curr
                curr = nxt

            # Reconnect group_prev to reversed group
            tmp = group_prev.next  # type: ignore
            group_prev.next = kth  # type: ignore
            group_prev = tmp

        return dummy.next

    def _get_kth(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Helper to find the kth node from curr."""
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_reverse_k_group():
    sol = Solution()

    # Test Case 1: [1, 2, 3, 4, 5], k = 2 -> [2, 1, 4, 3, 5]
    l1 = ListNode.from_list([1, 2, 3, 4, 5])
    res1 = sol.reverseKGroup(l1, 2)
    assert res1 is not None and res1.to_list() == [2, 1, 4, 3, 5]

    # Test Case 2: [1, 2, 3, 4, 5], k = 3 -> [3, 2, 1, 4, 5]
    l2 = ListNode.from_list([1, 2, 3, 4, 5])
    res2 = sol.reverseKGroup(l2, 3)
    assert res2 is not None and res2.to_list() == [3, 2, 1, 4, 5]

    # Test Case 3: k = 1 (identity)
    l3 = ListNode.from_list([1, 2, 3])
    res3 = sol.reverseKGroup(l3, 1)
    assert res3 is not None and res3.to_list() == [1, 2, 3]

    # Test Case 4: Length equals k [1, 2, 3, 4], k = 4 -> [4, 3, 2, 1]
    l4 = ListNode.from_list([1, 2, 3, 4])
    res4 = sol.reverseKGroup(l4, 4)
    assert res4 is not None and res4.to_list() == [4, 3, 2, 1]


if __name__ == "__main__":
    test_reverse_k_group()
    print("All Reverse Nodes in k-Group unit tests passed successfully!")
