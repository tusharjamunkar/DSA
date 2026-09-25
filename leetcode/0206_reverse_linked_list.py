"""
0206. Reverse Linked List
Difficulty: Easy
Topic: Linked List
LeetCode Link: https://leetcode.com/problems/reverse-linked-list/

Problem Statement:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000
"""

from typing import Optional, List


class ListNode:
    """Definition for singly-linked list node."""
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, values: List[int]) -> Optional["ListNode"]:
        """Factory helper: converts Python list of values to a linked list."""
        dummy = cls()
        curr = dummy
        for v in values:
            curr.next = cls(v)
            curr = curr.next
        return dummy.next

    def to_list(self) -> List[int]:
        """Serialization helper: converts linked list to Python list."""
        res = []
        curr: Optional["ListNode"] = self
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Optimal Iterative Three-Pointer Approach:

        Algorithmic Intuition:
        - Maintain `prev` (initially None) and `curr` (initially head).
        - At each step:
          1. Store `nxt = curr.next`.
          2. Reverse the link: `curr.next = prev`.
          3. Advance pointers: `prev = curr`, `curr = nxt`.
        - When `curr` is None, `prev` points to the new head of the reversed list.

        Complexity:
        - Time Complexity:  O(n) - Single pass through all n nodes.
        - Space Complexity: O(1) - Constant auxiliary memory.
        """
        prev: Optional[ListNode] = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Companion Recursive Approach:

        Algorithmic Intuition:
        - Base case: empty list or single node is already reversed.
        - Recursively reverse the rest of the list: `new_head = reverseListRecursive(head.next)`.
        - Make next node point back to current: `head.next.next = head`.
        - Clear current node's next pointer: `head.next = None`.
        - Return `new_head`.

        Complexity:
        - Time Complexity:  O(n)
        - Space Complexity: O(n) - Call stack frames.
        """
        if not head or not head.next:
            return head

        new_head = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return new_head


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_reverse_linked_list():
    sol = Solution()

    # Test Case 1: Standard list [1, 2, 3, 4, 5]
    l1 = ListNode.from_list([1, 2, 3, 4, 5])
    rev1 = sol.reverseList(l1)
    assert rev1 is not None and rev1.to_list() == [5, 4, 3, 2, 1]

    # Test Case 1 (Recursive variant):
    l1_rec = ListNode.from_list([1, 2, 3, 4, 5])
    rev1_rec = sol.reverseListRecursive(l1_rec)
    assert rev1_rec is not None and rev1_rec.to_list() == [5, 4, 3, 2, 1]

    # Test Case 2: Two elements [1, 2]
    l2 = ListNode.from_list([1, 2])
    rev2 = sol.reverseList(l2)
    assert rev2 is not None and rev2.to_list() == [2, 1]

    # Test Case 3: Empty list []
    assert sol.reverseList(None) is None
    assert sol.reverseListRecursive(None) is None

    # Test Case 4: Single element [42]
    l4 = ListNode.from_list([42])
    rev4 = sol.reverseList(l4)
    assert rev4 is not None and rev4.to_list() == [42]


if __name__ == "__main__":
    test_reverse_linked_list()
    print("All Reverse Linked List unit tests passed successfully!")
