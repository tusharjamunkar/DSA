"""
0143. Reorder List
Difficulty: Medium
Topic: Linked List / Two Pointers
LeetCode Link: https://leetcode.com/problems/reorder-list/

Problem Statement:
You are given the head of a singly linked-list. The list can be represented as:
L0 -> L1 -> ... -> Ln - 1 -> Ln

Reorder the list to be on the following form:
L0 -> Ln -> L1 -> Ln - 1 -> L2 -> Ln - 2 -> ...

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
- The number of nodes in the list is in the range [1, 5 * 10^4].
- 1 <= Node.val <= 1000
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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Optimal Three-Step In-Place Reorder:

        Algorithmic Intuition:
        1. Find the Middle of the Linked List:
           Use slow and fast pointers (slow moves 1 step, fast moves 2 steps).
           When fast reaches the end, slow is at the end of the first half.
        2. Reverse the Second Half:
           Detach the second half (`second = slow.next`, `slow.next = None`)
           and reverse it using standard 3-pointer iterative reversal.
        3. Interleave (Merge) the Two Halves:
           Alternately weave nodes from the first half and the reversed second half.

        Complexity:
        - Time Complexity:  O(n) - One pass to find midpoint, one pass to reverse half, one pass to merge.
        - Space Complexity: O(1) - Mutates pointers strictly in-place.
        """
        if not head or not head.next:
            return

        # 1. Find midpoint (slow will be at the end of first half)
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head.next

        while fast and fast.next:
            slow = slow.next  # type: ignore
            fast = fast.next.next

        # 2. Reverse second half
        second = slow.next  # type: ignore
        slow.next = None  # type: ignore

        prev: Optional[ListNode] = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. Merge first half and reversed second half
        first: Optional[ListNode] = head
        second = prev

        while second:
            tmp1 = first.next  # type: ignore
            tmp2 = second.next

            first.next = second  # type: ignore
            second.next = tmp1

            first = tmp1
            second = tmp2


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_reorder_list():
    sol = Solution()

    # Test Case 1: Even number of nodes [1, 2, 3, 4] -> [1, 4, 2, 3]
    l1 = ListNode.from_list([1, 2, 3, 4])
    sol.reorderList(l1)
    assert l1 is not None and l1.to_list() == [1, 4, 2, 3]

    # Test Case 2: Odd number of nodes [1, 2, 3, 4, 5] -> [1, 5, 2, 4, 3]
    l2 = ListNode.from_list([1, 2, 3, 4, 5])
    sol.reorderList(l2)
    assert l2 is not None and l2.to_list() == [1, 5, 2, 4, 3]

    # Test Case 3: Single node [1] -> [1]
    l3 = ListNode.from_list([1])
    sol.reorderList(l3)
    assert l3 is not None and l3.to_list() == [1]

    # Test Case 4: Two nodes [1, 2] -> [1, 2]
    l4 = ListNode.from_list([1, 2])
    sol.reorderList(l4)
    assert l4 is not None and l4.to_list() == [1, 2]


if __name__ == "__main__":
    test_reorder_list()
    print("All Reorder List unit tests passed successfully!")
