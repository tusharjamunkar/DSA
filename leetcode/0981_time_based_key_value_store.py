"""
0981. Time Based Key-Value Store
Difficulty: Medium
Topic: Binary Search / Hash Table / Design
LeetCode Link: https://leetcode.com/problems/time-based-key-value-store/

Problem Statement:
Design a time-based key-value data structure that can store multiple values for the same
key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:
- TimeMap() Initializes the object of the data structure.
- void set(String key, String value, int timestamp) Stores the key key with the value value
  at the given time timestamp.
- String get(String key, int timestamp) Returns a value such that set was called previously,
  with timestamp_prev <= timestamp. If there are multiple such values, it returns the value
  associated with the largest timestamp_prev. If there are no values, it returns "".

Example 1:
Input:
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output:
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation:
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"

Constraints:
- 1 <= key.length, value.length <= 100
- key and value consist of lowercase English letters and digits.
- 1 <= timestamp <= 10^7
- All the timestamps timestamp of set are strictly increasing.
- At most 2 * 10^5 calls will be made to set and get.
"""

from collections import defaultdict


class TimeMap:
    """
    Optimal Hash Map with Ordered Timestamp Arrays & Binary Search:

    Algorithmic Intuition:
    - We map each key to a dynamic list of (timestamp, value) pairs: `store[key]`.
    - Invariant: Problem guarantees `set` timestamps arrive in strictly increasing order.
      Therefore, `store[key]` is already sorted by timestamp without manual sorting!
    - For `get(key, timestamp)`:
      - If key does not exist or target timestamp is smaller than the very first timestamp,
        return "".
      - Otherwise, perform binary search on `store[key]` to find the largest timestamp <= query timestamp:
        - If `pairs[mid][0] <= timestamp`: candidate found! Record `res = pairs[mid][1]`
          and look for an even closer/larger timestamp to the right: `left = mid + 1`.
        - Else: `right = mid - 1`.

    Complexity:
    - Time Complexity:
      - `set()`: O(1) - Amortized list append.
      - `get()`: O(log m) where m is the number of values stored for that key.
    - Space Complexity: O(total number of set calls).
    """

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.store.get(key, [])
        if not pairs or timestamp < pairs[0][0]:
            return ""

        left, right = 0, len(pairs) - 1
        res = ""

        while left <= right:
            mid = left + (right - left) // 2
            if pairs[mid][0] <= timestamp:
                res = pairs[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return res


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_time_based_key_value_store():
    tm = TimeMap()

    # Test Case 1: Example 1
    tm.set("foo", "bar", 1)
    assert tm.get("foo", 1) == "bar"
    assert tm.get("foo", 3) == "bar"

    tm.set("foo", "bar2", 4)
    assert tm.get("foo", 4) == "bar2"
    assert tm.get("foo", 5) == "bar2"

    # Test Case 2: Query timestamp before first entry
    assert tm.get("foo", 0) == ""

    # Test Case 3: Non-existent key
    assert tm.get("non_existent", 10) == ""

    # Test Case 4: Multiple keys
    tm.set("love", "high", 10)
    tm.set("love", "low", 20)
    assert tm.get("love", 5) == ""
    assert tm.get("love", 10) == "high"
    assert tm.get("love", 15) == "high"
    assert tm.get("love", 20) == "low"
    assert tm.get("love", 25) == "low"


if __name__ == "__main__":
    test_time_based_key_value_store()
    print("All Time Based Key-Value Store unit tests passed successfully!")
