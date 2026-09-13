"""
0036. Valid Sudoku
Difficulty: Medium
Topic: Arrays & Hashing / Matrix / Hash Table
LeetCode Link: https://leetcode.com/problems/valid-sudoku/

Problem Statement:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

Constraints:
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit '1'-'9' or '.'.
"""

from collections import defaultdict
from typing import Dict, List, Set, Tuple


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Optimal Hash Set Tracking Approach:
        - Maintain hash sets for each row, each column, and each 3x3 sub-box.
        - The 3x3 box coordinate is identified by integer division: (row // 3, col // 3).
        - Single pass over the 9x9 board:
          - If the cell contains '.', skip it.
          - If the digit already exists in the current row set, col set, or box set, return False.
          - Otherwise, add the digit to all three sets.
        - If the entire board passes without collisions, return True.

        Time Complexity:  O(1) - The board size is fixed at 9 x 9 = 81 cells. Constant time O(81) = O(1).
        Space Complexity: O(1) - Storing at most 81 entries across row, column, and box hash sets.
        """
        rows: Dict[int, Set[str]] = defaultdict(set)
        cols: Dict[int, Set[str]] = defaultdict(set)
        boxes: Dict[Tuple[int, int], Set[str]] = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                box_key = (r // 3, c // 3)

                if val in rows[r] or val in cols[c] or val in boxes[box_key]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_key].add(val)

        return True

    def isValidSudokuBitmask(self, board: List[List[str]]) -> bool:
        """
        Bitmask Space-Optimized Approach:
        - Instead of hash sets, use 9-bit integers as bitmasks for rows, cols, and boxes.
        - The k-th bit (1 << (digit - 1)) indicates whether digit k has been seen.
        - Check collision with bitwise AND (&). Mark presence with bitwise OR (|).

        Time Complexity:  O(1)
        Space Complexity: O(1) - Only 3 arrays of 9 integers each.
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                digit = int(val)
                mask = 1 << (digit - 1)
                box_idx = (r // 3) * 3 + (c // 3)

                if (rows[r] & mask) or (cols[c] & mask) or (boxes[box_idx] & mask):
                    return False

                rows[r] |= mask
                cols[c] |= mask
                boxes[box_idx] |= mask

        return True


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_valid_sudoku():
    sol = Solution()

    # Test Case 1: Valid board
    board1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert sol.isValidSudoku(board1) is True
    assert sol.isValidSudokuBitmask(board1) is True

    # Test Case 2: Invalid board (duplicate 8 in top-left 3x3 box)
    board2 = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert sol.isValidSudoku(board2) is False
    assert sol.isValidSudokuBitmask(board2) is False

    # Test Case 3: Empty board
    board3 = [["." for _ in range(9)] for _ in range(9)]
    assert sol.isValidSudoku(board3) is True
    assert sol.isValidSudokuBitmask(board3) is True

    # Test Case 4: Duplicate in same column
    board4 = [["." for _ in range(9)] for _ in range(9)]
    board4[0][0] = "2"
    board4[8][0] = "2"
    assert sol.isValidSudoku(board4) is False
    assert sol.isValidSudokuBitmask(board4) is False


if __name__ == "__main__":
    test_valid_sudoku()
    print("All Valid Sudoku tests passed successfully!")
