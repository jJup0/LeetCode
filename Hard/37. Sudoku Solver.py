"""
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:
1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3
   sub-boxes of the grid.
The'.' character indicates empty cells.
Constraints:
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit or'.'.
- It is guaranteed that the input board has only one solution.
"""

BOX_LENGTH = 3
SIDE_LENGTH = BOX_LENGTH * BOX_LENGTH


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        n := side length of sudoku grid = 9
        """
        self.board = board
        self.remaining_count = sum(row.count(".") for row in board)
        self._solve(self._construct_allowed_nums(board))

    def _construct_allowed_nums(self, board: list[list[str]]) -> list[int]:
        """
        Complexity:
            Time: O(n^3)
            Space: O(n^2)
        """
        allowed_nums = [((1 << SIDE_LENGTH) - 1) << 1] * SIDE_LENGTH * SIDE_LENGTH
        for row_nr, row in enumerate(board):
            for colr_nr, val in enumerate(row):
                if val != ".":
                    self._set_num(row_nr, colr_nr, int(val), allowed_nums)
        return allowed_nums

    def _solve(self, allowed_nums: list[int]) -> bool:
        """
        Complexity:
            Time: O(n^O(n^2))
            Space: (n^2)
        """
        if self.remaining_count == 0:
            return True
        min_poss = SIDE_LENGTH
        min_row = min_col = -1
        for row_col, bm in enumerate(allowed_nums):
            bc = bm.bit_count()
            if bc > 0 and bc < min_poss:
                min_poss = bc
                min_row, min_col = divmod(row_col, SIDE_LENGTH)

        self.remaining_count -= 1
        for val in range(1, SIDE_LENGTH + 1):
            if allowed_nums[min_row * SIDE_LENGTH + min_col] & (1 << val):
                allowed_nums_copy = allowed_nums[:]
                self._set_num(min_row, min_col, val, allowed_nums_copy)
                if self._is_possible_to_solve(allowed_nums_copy) and self._solve(
                    allowed_nums_copy
                ):
                    return True
                self.board[min_row][min_col] = "."
        self.remaining_count += 1
        return False

    def _set_num(self, row: int, col: int, num: int, allowed_nums: list[int]):
        """
        Complexity:
            Time: O(n)
            Space: O(1)
        """
        # unset bit for value in allowed_nums for row, column and square
        bit_mask = ((1 << (SIDE_LENGTH + 1)) - 1) ^ (1 << num)
        for _col in range(SIDE_LENGTH):
            allowed_nums[row * SIDE_LENGTH + _col] &= bit_mask
        for _row in range(SIDE_LENGTH):
            allowed_nums[_row * SIDE_LENGTH + col] &= bit_mask
        for _row, _col in self._get_cells_in_square(row, col):
            allowed_nums[_row * SIDE_LENGTH + _col] &= bit_mask
        allowed_nums[row * SIDE_LENGTH + col] = 0

        self.board[row][col] = str(num)

    def _get_cells_in_square(self, row: int, col: int):
        top = (row // BOX_LENGTH) * BOX_LENGTH
        left = (col // BOX_LENGTH) * BOX_LENGTH
        return [
            (r, c)
            for r in range(top, top + BOX_LENGTH)
            for c in range(left, left + BOX_LENGTH)
        ]

    def _is_possible_to_solve(self, allowed_nums: list[int]) -> bool:
        """
        Complexity:
            Time: O(n^2)
            Space: O(1)
        """
        for row_nr, row in enumerate(self.board):
            for col_nr, val in enumerate(row):
                if val == "." and allowed_nums[row_nr * SIDE_LENGTH + col_nr] == 0:
                    return False
        return True
