class Solution:
    """
    Given a m x n grid filled with non-negative numbers, find a path from top left
    to bottom right, which minimizes the sum of all numbers along its path.

    Note: You can only move either down or right at any point in time.

        Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 200
        0 <= grid[i][j] <= 100
    """

    def minPathSum(self, grid: list[list[int]]) -> int:
        """
        Simple dynamic programming with linear sapce, at each step move
        *from* left or from above, depending on which is cheaper.
        O(n * m) / O(n)     time / space complexity
        """

        # stores shortest paths to cells in previous row
        shortests_to_prev_row = [float("inf")] * len(grid[0])

        # shortest path to previous cell while traversing row
        shortest_to_left_cell = 0

        for _, row in enumerate(grid):
            for x, cell_val in enumerate(row):
                # shortest path to current cell is smaller of upper
                # (in prev row at same collumn) and prev cell in same row
                shortest_to_cell = cell_val + min(
                    shortest_to_left_cell, shortests_to_prev_row[x]
                )

                # update left cell to current
                shortest_to_left_cell = shortest_to_cell

                # update "previous" row to current
                shortests_to_prev_row[x] = shortest_to_cell

        return shortests_to_prev_row[-1]
