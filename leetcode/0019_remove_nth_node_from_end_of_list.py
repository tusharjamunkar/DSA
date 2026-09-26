"""
0019. Remove Nth Node From End of List
Difficulty: Medium
Topic: Linked List / Two Pointers
LeetCode Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Problem Statement:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Optimal One-Pass Two-Pointer with Dummy Node:

        Algorithmic Intuition:
        - Use a dummy node pointing to `head` to gracefully handle deleting the head node.
        - Initialize `left = dummy` and `right = head`.
        - Advance `right` pointer by `n` steps ahead so the gap between `left` and `right` is `n`.
        - Move both `left` and `right` one step at a time until `right` reaches None.
        - `left` now points immediately prior to the node to delete.
        - Update `left.next = left.next.next` to remove the target node.
        - Return `dummy.next`.

        Complexity:
        - Time Complexity:  O(n) - Single pass traversal through list of length n.
        - Space Complexity: O(1) - Constant extra space.
        """
        dummy = ListNode(0, head)
        left: Optional[ListNode] = dummy
        right: Optional[ListNode] = head

        # Advance right pointer by n steps
        for _ in range(n):
            if right:
                right = right.next

        # Advance both until right reaches end
        while right:
            left = left.next  # type: ignore
            right = right.next

        # Remove the nth node from end
        if left and left.next:
            left.next = left.next.next

        return dummy.next


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_remove_nth_from_end():
    sol = Solution()

    # Test Case 1: Standard removal in middle [1, 2, 3, 4, 5], n = 2 -> [1, 2, 3, 5]
    l1 = ListNode.from_list([1, 2, 3, 4, 5])
    res1 = sol.removeNthFromEnd(l1, 2)
    assert res1 is not None and res1.to_list() == [1, 2, 3, 5]

    # Test Case 2: Remove sole head node [1], n = 1 -> []
    l2 = ListNode.from_list([1])
    res2 = sol.removeNthFromEnd(l2, 1)
    assert res2 is None

    # Test Case 3: Remove tail [1, 2], n = 1 -> [1]
    l3 = ListNode.from_list([1, 2])
    res3 = sol.removeNthFromEnd(l3, 1)
    assert res3 is not None and res3.to_list() == [1]

    # Test Case 4: Remove head of multi-node list [1, 2, 3], n = 3 -> [2, 3]
    l4 = ListNode.from_list([1, 2, 3])
    res4 = sol.removeNthFromEnd(l4, 3)
    assert res4 is not None and res4.to_list() == [2, 3]


if __name__ == "__main__":
    test_remove_nth_from_end()
    print("All Remove Nth Node From End of List unit tests passed successfully!")
