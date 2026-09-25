"""
0021. Merge Two Sorted Lists
Difficulty: Easy
Topic: Linked List
LeetCode Link: https://leetcode.com/problems/merge-two-sorted-lists/

Problem Statement:
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing
together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Optimal Iterative Dummy-Node Approach:

        Algorithmic Intuition:
        - Use a pre-allocated dummy head node to simplify head pointer logic.
        - Maintain `tail` pointing to the end of the merged list.
        - While both `list1` and `list2` are non-null:
          - Compare `list1.val` and `list2.val`.
          - Splice the smaller node to `tail.next` and advance that list's pointer.
          - Advance `tail`.
        - Splice remaining nodes from whichever list is not exhausted (`tail.next = list1 or list2`).
        - Return `dummy.next`.

        Complexity:
        - Time Complexity:  O(n + m) - Each node inspected once.
        - Space Complexity: O(1) - In-place splicing; constant extra memory.
        """
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2
        return dummy.next

    def mergeTwoListsRecursive(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Companion Recursive Approach:

        Algorithmic Intuition:
        - Base cases: if either list is empty, return the other list.
        - If list1.val <= list2.val, list1 becomes head, its next is merged result of
          list1.next and list2.
        - Else, list2 becomes head, its next is merged result of list1 and list2.next.

        Complexity:
        - Time Complexity:  O(n + m)
        - Space Complexity: O(n + m) - Call stack frames.
        """
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoListsRecursive(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoListsRecursive(list1, list2.next)
            return list2


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_merge_two_sorted_lists():
    sol = Solution()

    # Test Case 1: Standard lists [1, 2, 4] and [1, 3, 4]
    l1 = ListNode.from_list([1, 2, 4])
    l2 = ListNode.from_list([1, 3, 4])
    merged = sol.mergeTwoLists(l1, l2)
    assert merged is not None and merged.to_list() == [1, 1, 2, 3, 4, 4]

    # Test Case 1 (Recursive variant):
    l1_r = ListNode.from_list([1, 2, 4])
    l2_r = ListNode.from_list([1, 3, 4])
    merged_r = sol.mergeTwoListsRecursive(l1_r, l2_r)
    assert merged_r is not None and merged_r.to_list() == [1, 1, 2, 3, 4, 4]

    # Test Case 2: Both empty []
    assert sol.mergeTwoLists(None, None) is None
    assert sol.mergeTwoListsRecursive(None, None) is None

    # Test Case 3: One empty list
    l3 = ListNode.from_list([0])
    res3 = sol.mergeTwoLists(None, l3)
    assert res3 is not None and res3.to_list() == [0]

    # Test Case 4: Unequal lengths with negatives
    l4a = ListNode.from_list([-10, -5, 0, 7])
    l4b = ListNode.from_list([-7, -2, 5])
    res4 = sol.mergeTwoLists(l4a, l4b)
    assert res4 is not None and res4.to_list() == [-10, -7, -5, -2, 0, 5, 7]


if __name__ == "__main__":
    test_merge_two_sorted_lists()
    print("All Merge Two Sorted Lists unit tests passed successfully!")
