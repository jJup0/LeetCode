"""
You are given a 0-indexed m x n matrix grid consisting of positive integers.

You can start at any cell in the first column of the matrix, and traverse the
grid in the following way:
- From a cell (row, col), you can move to any of the cells: (row - 1, col + 1),
  (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move
  to, should be strictly bigger than the value of the current cell.

Return the maximum number of moves that you can perform.

Constraints:
- m == grid.length
- n == grid[i].length
- 2 <= m, n <= 1000
- 4 <= m * n <= 10^5
- 1 <= grid[i][j] <= 10^6
"""


class Solution:
    def maxMoves(self, grid: list[list[int]]) -> int:
        """
        Complexity:
            Time: O(n * m)
            Space: O(n)
        """
        row_count = len(grid)
        col_count = len(grid[0])
        # row indices reachable for current column
        available_rows = set(range(row_count))
        for col in range(col_count - 1):
            if not available_rows:
                # cannot make any more steps
                return col - 1

            next_available_rows: set[int] = set()
            next_col = col + 1
            for row in available_rows:
                val = grid[row][col]
                # check reaching row - 1, row and row + 1
                if row > 0 and grid[row - 1][next_col] > val:
                    next_available_rows.add(row - 1)
                if grid[row][next_col] > val:
                    next_available_rows.add(row)
                if row < row_count - 1 and grid[row + 1][next_col] > val:
                    next_available_rows.add(row + 1)
            available_rows = next_available_rows

        # reached last column, add 1 to result if rows still reachable
        return col_count + bool(available_rows) - 2