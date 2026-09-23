"""
0074. Search a 2D Matrix
Difficulty: Medium
Topic: Binary Search / Matrix / Array
LeetCode Link: https://leetcode.com/problems/search-a-2d-matrix/

Problem Statement:
You are given an m x n integer matrix matrix with the following two properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -10^4 <= matrix[i][j], target <= 10^4
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Optimal Virtual Flattened 1D Binary Search:

        Algorithmic Intuition:
        - Because each row is sorted and the first element of each row exceeds the last element
          of the previous row, the entire m x n matrix can be viewed as a single contiguous sorted
          1D array of length `m * n`.
        - Map any virtual 1D index `idx` in `[0, m * n - 1]` to 2D coordinates:
          `row = idx // n`
          `col = idx % n`
        - Standard binary search on virtual range `[0, m * n - 1]`.

        Complexity:
        - Time Complexity:  O(log(m * n)) = O(log m + log n).
        - Space Complexity: O(1) - No array flattening or copy, index math only.
        """
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_val = matrix[mid // n][mid % n]

            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def searchMatrixTwoPass(self, matrix: List[List[int]], target: int) -> bool:
        """
        Alternative Two-Pass Binary Search (Row Selection + Column Search):
        """
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1
        target_row = -1

        while top <= bottom:
            mid_row = top + (bottom - top) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                target_row = mid_row
                break
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            else:
                top = mid_row + 1

        if target_row == -1:
            return False

        row = matrix[target_row]
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_search_2d_matrix():
    sol = Solution()

    # Test Case 1: Target exists in middle row
    m1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert sol.searchMatrix(m1, 3) is True
    assert sol.searchMatrixTwoPass(m1, 3) is True

    # Test Case 2: Target absent
    assert sol.searchMatrix(m1, 13) is False
    assert sol.searchMatrixTwoPass(m1, 13) is False

    # Test Case 3: 1x1 matrix - found & absent
    assert sol.searchMatrix([[1]], 1) is True
    assert sol.searchMatrix([[1]], 2) is False

    # Test Case 4: Target at boundaries
    assert sol.searchMatrix(m1, 1) is True
    assert sol.searchMatrix(m1, 60) is True

    # Test Case 5: 1xN matrix
    m2 = [[1, 3, 5, 7]]
    assert sol.searchMatrix(m2, 5) is True
    assert sol.searchMatrix(m2, 4) is False

    # Test Case 6: Mx1 matrix
    m3 = [[1], [3], [5], [7]]
    assert sol.searchMatrix(m3, 3) is True
    assert sol.searchMatrix(m3, 6) is False


if __name__ == "__main__":
    test_search_2d_matrix()
    print("All Search a 2D Matrix unit tests passed successfully!")
