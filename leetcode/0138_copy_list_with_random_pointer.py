"""
0138. Copy List with Random Pointer
Difficulty: Medium
Topic: Linked List / Hash Table
LeetCode Link: https://leetcode.com/problems/copy-list-with-random-pointer/

Problem Statement:
A linked list of length n is given such that each node contains an additional random pointer,
which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes,
where each new node has its value set to the value of its corresponding original node.
Both the next and random pointer of the new nodes should point to new nodes in the copied list
such that the pointers in the original list and copied list represent the same list state.
None of the pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Constraints:
- 0 <= n <= 1000
- -10^4 <= Node.val <= 10^4
- Node.random is null or is pointing to some node in the linked list.
"""

from typing import Optional, List, Tuple, Dict


class Node:
    """Definition for a Node with next and random pointers."""
    def __init__(self, x: int, next: Optional["Node"] = None, random: Optional["Node"] = None):
        self.val = int(x)
        self.next = next
        self.random = random

    @classmethod
    def from_nested_list(cls, data: List[List[Optional[int]]]) -> Optional["Node"]:
        """Helper to create random pointer linked list from [[val, random_idx], ...]."""
        if not data:
            return None

        nodes = [cls(item[0]) for item in data]  # type: ignore
        for i, item in enumerate(data):
            if i + 1 < len(nodes):
                nodes[i].next = nodes[i + 1]
            rand_idx = item[1]
            if rand_idx is not None:
                nodes[i].random = nodes[rand_idx]

        return nodes[0]

    def to_nested_list(self) -> List[List[Optional[int]]]:
        """Helper to convert random pointer list to [[val, random_idx], ...]."""
        nodes = []
        curr: Optional["Node"] = self
        while curr:
            nodes.append(curr)
            curr = curr.next

        node_to_idx = {node: i for i, node in enumerate(nodes)}
        res = []
        for node in nodes:
            rand_idx = node_to_idx[node.random] if node.random in node_to_idx else None
            res.append([node.val, rand_idx])
        return res


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        Optimal Interweaving Algorithm (O(1) Auxiliary Space):

        Algorithmic Intuition:
        - Pass 1: Duplicate each node in-place and insert it immediately after the original node:
          A -> A' -> B -> B' -> C -> C'
        - Pass 2: Assign random pointers for cloned nodes:
          `curr.next.random = curr.random.next` (if `curr.random` exists).
        - Pass 3: Decouple original and cloned lists to restore original structure and isolate the clone:
          `curr.next = curr.next.next`, `clone.next = clone.next.next`.

        Complexity:
        - Time Complexity:  O(n) - Three linear passes over the list.
        - Space Complexity: O(1) - Constant auxiliary space (excluding memory for the deep copy).
        """
        if not head:
            return None

        # Pass 1: Interweave original and copied nodes
        curr: Optional[Node] = head
        while curr:
            nxt = curr.next
            clone = Node(curr.val, next=nxt)
            curr.next = clone
            curr = nxt

        # Pass 2: Set random pointers for copied nodes
        curr = head
        while curr:
            if curr.random and curr.next:
                curr.next.random = curr.random.next
            curr = curr.next.next if curr.next else None

        # Pass 3: Unweave the lists
        dummy = Node(0)
        copy_curr: Optional[Node] = dummy
        curr = head

        while curr:
            clone = curr.next
            curr.next = clone.next if clone else None
            if copy_curr:
                copy_curr.next = clone
                copy_curr = copy_curr.next
            curr = curr.next

        return dummy.next

    def copyRandomListHashMap(self, head: Optional[Node]) -> Optional[Node]:
        """
        Alternative Hash Map Approach:
        Two passes using a hash map mapping original node -> cloned node.

        Complexity:
        - Time Complexity:  O(n)
        - Space Complexity: O(n) - Hash map storage.
        """
        if not head:
            return None

        old_to_new: Dict[Optional[Node], Optional[Node]] = {None: None}

        curr: Optional[Node] = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            cloned = old_to_new[curr]
            if cloned:
                cloned.next = old_to_new[curr.next]
                cloned.random = old_to_new[curr.random]
            curr = curr.next

        return old_to_new[head]


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_copy_random_list():
    sol = Solution()

    # Test Case 1: Standard list with random links
    data1 = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    head1 = Node.from_nested_list(data1)
    copied1 = sol.copyRandomList(head1)
    assert copied1 is not None and copied1.to_nested_list() == data1
    # Check that copy is deep (different references)
    assert copied1 is not head1

    # Test Case 1 with Hash Map variant:
    head1_hm = Node.from_nested_list(data1)
    copied1_hm = sol.copyRandomListHashMap(head1_hm)
    assert copied1_hm is not None and copied1_hm.to_nested_list() == data1

    # Test Case 2: Self-pointing random and circular links
    data2 = [[1, 1], [2, 1]]
    head2 = Node.from_nested_list(data2)
    copied2 = sol.copyRandomList(head2)
    assert copied2 is not None and copied2.to_nested_list() == data2

    # Test Case 3: Empty list
    assert sol.copyRandomList(None) is None
    assert sol.copyRandomListHashMap(None) is None


if __name__ == "__main__":
    test_copy_random_list()
    print("All Copy List with Random Pointer unit tests passed successfully!")
