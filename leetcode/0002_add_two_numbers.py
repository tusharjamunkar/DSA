"""
0002. Add Two Numbers
Difficulty: Medium
Topic: Linked List / Math / Recursion
LeetCode Link: https://leetcode.com/problems/add-two-numbers/

Problem Statement:
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Optimal Iterative Simulation with Carry:

        Algorithmic Intuition:
        - Digits are already stored in reverse order (least significant digit at head).
        - Traverse both lists simultaneously using a dummy head node.
        - Maintain a `carry` variable (initially 0).
        - At each step:
          `total = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)`
          `carry = total // 10`
          `curr.next = ListNode(total % 10)`
          Advance `curr` and any active list pointers.
        - Continue as long as `l1`, `l2`, or `carry > 0`.
        - Return `dummy.next`.

        Complexity:
        - Time Complexity:  O(max(m, n)) - Traverses through the longer list.
        - Space Complexity: O(max(m, n)) - For the newly constructed result list.
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_add_two_numbers():
    sol = Solution()

    # Test Case 1: [2, 4, 3] + [5, 6, 4] = [7, 0, 8] (342 + 465 = 807)
    l1 = ListNode.from_list([2, 4, 3])
    l2 = ListNode.from_list([5, 6, 4])
    res = sol.addTwoNumbers(l1, l2)
    assert res is not None and res.to_list() == [7, 0, 8]

    # Test Case 2: [0] + [0] = [0]
    l1_2 = ListNode.from_list([0])
    l2_2 = ListNode.from_list([0])
    res2 = sol.addTwoNumbers(l1_2, l2_2)
    assert res2 is not None and res2.to_list() == [0]

    # Test Case 3: Unequal lengths with multiple carries
    # [9,9,9,9,9,9,9] + [9,9,9,9] = [8,9,9,9,0,0,0,1]
    l1_3 = ListNode.from_list([9, 9, 9, 9, 9, 9, 9])
    l2_3 = ListNode.from_list([9, 9, 9, 9])
    res3 = sol.addTwoNumbers(l1_3, l2_3)
    assert res3 is not None and res3.to_list() == [8, 9, 9, 9, 0, 0, 0, 1]


if __name__ == "__main__":
    test_add_two_numbers()
    print("All Add Two Numbers unit tests passed successfully!")
