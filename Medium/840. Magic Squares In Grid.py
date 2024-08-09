"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9
such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 contiguous magic square
subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may
contain numbers up to 15.

Constraints:
- row == grid.length
- col == grid[i].length
- 1 <= row, col <= 10
- 0 <= grid[i][j] <= 15
"""


class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        """
        Naive approach, check each 3x3 zone without storing any information.
        O(n^2) / O(1)   time / space complexity
        """
        self._grid = grid
        res = 0
        for start_row in range(len(grid) - 2):
            for start_col in range(len(grid[0]) - 2):
                res += self._is_magic(start_row, start_col)
        return res

    def _is_magic(self, starting_row: int, starting_col: int) -> bool:
        """
        Checks if 3x3 starting at (starting_row, starting_col) is magic.
        O(1) / O(1)     time / space complexity
        """
        grid = self._grid

        # check 1-9 contained in 3x3
        counts = [0] * 9
        for i in range(starting_row, starting_row + 3):
            for j in range(starting_col, starting_col + 3):
                val = grid[i][j]
                if val == 0 or val > 9:
                    return False
                counts[val - 1] += 1
        if not all(counts):
            return False

        # check rows, cols and diagonals have equal sums
        sum_needed = sum(grid[starting_row][starting_col : starting_col + 3])
        for row in range(starting_row + 1, starting_row + 3):
            row_sum = sum(grid[row][starting_col : starting_col + 3])
            if row_sum != sum_needed:
                return False

        for col in range(starting_col, starting_col + 3):
            col_sum = sum(
                grid[row][col] for row in range(starting_row, starting_row + 3)
            )
            if col_sum != sum_needed:
                return False

        diag_1 = sum(grid[starting_row + x][starting_col + x] for x in range(3))
        if diag_1 != sum_needed:
            return False
        diag_2 = sum(grid[starting_row + x][starting_col + 2 - x] for x in range(3))
        if diag_2 != sum_needed:
            return False

        return True
