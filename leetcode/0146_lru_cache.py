"""
0146. LRU Cache
Difficulty: Medium
Topic: Linked List / Hash Table / Design / Doubly-Linked List
LeetCode Link: https://leetcode.com/problems/lru-cache/

Problem Statement:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists.
  Otherwise, add the key-value pair to the cache. If the number of keys exceeds
  the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example 1:
Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output:
[null, null, null, 1, null, -1, null, -1, 3, 4]

Constraints:
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls will be made to get and put.
"""

from typing import Optional, Dict


class Node:
    """Doubly linked list node for O(1) removals and insertions."""
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None


class LRUCache:
    """
    Optimal Hash Map + Doubly Linked List:

    Algorithmic Intuition:
    - Hash Map (`cache`): Maps `key -> Node` for O(1) node access.
    - Doubly Linked List with Sentinel Nodes:
      - `left`: Dummy sentinel before the Least Recently Used (LRU) node.
      - `right`: Dummy sentinel after the Most Recently Used (MRU) node.
    - When a node is accessed or updated:
      - Detach it from its current position in O(1) via `_remove(node)`.
      - Re-insert it right before `right` (MRU position) via `_insert(node)`.
    - When capacity is exceeded during `put`:
      - Evict `left.next` (LRU node) and remove its key from `cache`.

    Complexity:
    - Time Complexity:  O(1) for both `get` and `put`.
    - Space Complexity: O(capacity) - Storage for at most `capacity` nodes.
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: Dict[int, Node] = {}

        # Sentinel dummy nodes
        self.left = Node(0, 0)   # LRU sentinel
        self.right = Node(0, 0)  # MRU sentinel
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node: Node) -> None:
        """Remove a node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        if prev_node and next_node:
            prev_node.next = next_node
            next_node.prev = prev_node

    def _insert(self, node: Node) -> None:
        """Insert a node right before right sentinel (MRU position)."""
        prev_node = self.right.prev
        if prev_node:
            prev_node.next = node
            node.prev = prev_node
            node.next = self.right
            self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert(new_node)

        if len(self.cache) > self.capacity:
            # Evict LRU node (left.next)
            lru = self.left.next
            if lru and lru != self.right:
                self._remove(lru)
                del self.cache[lru.key]


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_lru_cache():
    lru = LRUCache(2)

    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1       # returns 1, key 1 becomes MRU

    lru.put(3, 3)                # evicts key 2 (LRU)
    assert lru.get(2) == -1      # returns -1 (not found)

    lru.put(4, 4)                # evicts key 1 (LRU)
    assert lru.get(1) == -1      # returns -1 (not found)
    assert lru.get(3) == 3       # returns 3
    assert lru.get(4) == 4       # returns 4


if __name__ == "__main__":
    test_lru_cache()
    print("All LRU Cache unit tests passed successfully!")
