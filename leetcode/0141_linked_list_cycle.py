"""
0141. Linked List Cycle
Difficulty: Easy
Topic: Linked List / Two Pointers
LeetCode Link: https://leetcode.com/problems/linked-list-cycle/

Problem Statement:
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached
again by continuously following the next pointer. Internally, pos is used to denote the
index of the node that tail's next pointer is connected to. Note that pos is not passed
as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true

Example 3:
Input: head = [1], pos = -1
Output: false

Constraints:
- The number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list.
"""

from typing import Optional, List


class ListNode:
    """Definition for singly-linked list node."""
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    @classmethod
    def from_list_with_cycle(cls, values: List[int], pos: int) -> Optional["ListNode"]:
        """Helper to create linked list with cycle at index `pos` (-1 for no cycle)."""
        if not values:
            return None
        nodes = [cls(v) for v in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        if 0 <= pos < len(nodes):
            nodes[-1].next = nodes[pos]
        return nodes[0]


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Optimal Floyd's Tortoise and Hare Cycle Detection:

        Algorithmic Intuition:
        - Use two pointers moving at different speeds:
          `slow` advances 1 node per iteration.
          `fast` advances 2 nodes per iteration.
        - If there is no cycle, `fast` (or `fast.next`) will reach `None`.
        - If there is a cycle, the relative distance between `fast` and `slow` decreases
          by 1 node per step within the loop, guaranteeing that `fast` and `slow`
          will meet (`slow == fast`).

        Complexity:
        - Time Complexity:  O(n) - Linear traversal; within loop, at most O(k) steps where k <= n.
        - Space Complexity: O(1) - Constant memory.
        """
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head

        while fast and fast.next:
            slow = slow.next  # type: ignore
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_linked_list_cycle():
    sol = Solution()

    # Test Case 1: Cycle at index 1 [3, 2, 0, -4] -> True
    l1 = ListNode.from_list_with_cycle([3, 2, 0, -4], 1)
    assert sol.hasCycle(l1) is True

    # Test Case 2: Cycle at index 0 [1, 2] -> True
    l2 = ListNode.from_list_with_cycle([1, 2], 0)
    assert sol.hasCycle(l2) is True

    # Test Case 3: Single node without cycle [1], pos = -1 -> False
    l3 = ListNode.from_list_with_cycle([1], -1)
    assert sol.hasCycle(l3) is False

    # Test Case 4: Empty list -> False
    assert sol.hasCycle(None) is False


if __name__ == "__main__":
    test_linked_list_cycle()
    print("All Linked List Cycle unit tests passed successfully!")
