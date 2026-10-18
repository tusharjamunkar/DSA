"""
0621. Task Scheduler
Difficulty: Medium
Topic: Array / Hash Table / Greedy / Sorting / Heap (Priority Queue) / Counting
LeetCode Link: https://leetcode.com/problems/task-scheduler/

Problem Statement:
You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n.
Each cycle or interval allows the completion of one task. Tasks can be completed in any order,
but there's a constraint: identical tasks must be separated by at least n intervals of cooling time or idle.

Return the minimum number of intervals required to complete all tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
There are 8 intervals needed.

Example 2:
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A -> B -> C -> D -> A -> B.
There are 6 intervals needed.

Example 3:
Input: tasks = ["A","A","A", "B","B","B"], n = 3
Output: 10
Explanation: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
There are 10 intervals needed.

Constraints:
- 1 <= tasks.length <= 10^4
- tasks[i] is an uppercase English letter.
- 0 <= n <= 100
"""

from typing import List, Tuple
from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Optimal Greedy Math Formula:

        Algorithmic Intuition:
        - Let `max_freq` be the maximum frequency of any task.
        - The task(s) with `max_freq` dictate the minimum frame size:
          - We have `(max_freq - 1)` chunks of size `(n + 1)`.
          - The final chunk only contains the tasks that share `max_freq` (`max_count`).
        - Formula: `min_intervals = (max_freq - 1) * (n + 1) + max_count`.
        - However, if there are so many distinct tasks that no idle slots are required,
          the total intervals is simply `len(tasks)`.
        - Therefore, the answer is `max(len(tasks), (max_freq - 1) * (n + 1) + max_count)`.

        Complexity:
        - Time Complexity:  O(T) where T = len(tasks) to count frequencies (at most 26 unique characters).
        - Space Complexity: O(1) - The character set is fixed (26 uppercase letters).
        """
        counts = list(Counter(tasks).values())
        max_freq = max(counts)
        max_count = counts.count(max_freq)

        return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)

    def leastIntervalHeap(self, tasks: List[str], n: int) -> int:
        """
        Alternative Max-Heap + Cooldown Queue Simulation:

        Algorithmic Intuition:
        - Always pick the task with the highest remaining frequency to run next (Greedy choice).
        - A Max-Heap stores task counts (negated for Python's min-heap).
        - A FIFO queue stores `(remaining_count, available_at_time)`.
        - In each clock cycle:
          1. Increment `time += 1`.
          2. If `max_heap` has tasks, pop the most frequent, decrement its count.
             If count remains > 0, enqueue it with release time `time + n`.
          3. If the queue has a task whose cooldown has expired (`q[0][1] == time`),
             pop it from queue and re-insert into `max_heap`.

        Complexity:
        - Time Complexity:  O(total_time * log(26)) = O(total_time).
        - Space Complexity: O(26) = O(1) auxiliary space for heap and cooldown queue.
        """
        task_counts = Counter(tasks)
        max_heap = [-cnt for cnt in task_counts.values()]
        heapq.heapify(max_heap)

        cooldown_queue: deque[Tuple[int, int]] = deque()  # stores (remaining_count, available_time)
        time = 0

        while max_heap or cooldown_queue:
            time += 1

            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)  # Since count was negated, adding 1 decreases magnitude
                if cnt < 0:
                    cooldown_queue.append((cnt, time + n))

            if cooldown_queue and cooldown_queue[0][1] == time:
                ready_cnt, _ = cooldown_queue.popleft()
                heapq.heappush(max_heap, ready_cnt)

        return time


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_task_scheduler():
    sol = Solution()

    # Test Case 1: Example 1
    t1 = ["A", "A", "A", "B", "B", "B"]
    assert sol.leastInterval(t1, 2) == 8
    assert sol.leastIntervalHeap(t1, 2) == 8

    # Test Case 2: Example 2
    t2 = ["A", "C", "A", "B", "D", "B"]
    assert sol.leastInterval(t2, 1) == 6
    assert sol.leastIntervalHeap(t2, 1) == 6

    # Test Case 3: Example 3
    t3 = ["A", "A", "A", "B", "B", "B"]
    assert sol.leastInterval(t3, 3) == 10
    assert sol.leastIntervalHeap(t3, 3) == 10

    # Test Case 4: Zero cooldown (n = 0)
    t4 = ["A", "A", "B", "C"]
    assert sol.leastInterval(t4, 0) == 4
    assert sol.leastIntervalHeap(t4, 0) == 4

    # Test Case 5: Many different tasks exceeding idle slots
    t5 = ["A", "A", "B", "C", "D", "E", "F", "G"]
    assert sol.leastInterval(t5, 2) == 8
    assert sol.leastIntervalHeap(t5, 2) == 8


if __name__ == "__main__":
    test_task_scheduler()
    print("All Task Scheduler unit tests passed successfully!")
