"""
You are given a map of a server center, represented as a m * n integer matrix
grid, where 1 means that on that cell there is a server and 0 means that it is
no server. Two servers are said to communicate if they are on the same row or
on the same column. Return the number of servers that communicate with any
other server.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m <= 250
- 1 <= n <= 250
- grid[i][j] == 0 or 1
"""


class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        """
        Complexity:
            Time: O(n * m)
            Space: O(n + m)
        """
        col_server_count = [0] * len(grid[0])
        row_server_count = [0] * len(grid)

        for col_nr, grid_row in enumerate(grid):
            for row_nr, val in enumerate(grid_row):
                if val:
                    col_server_count[row_nr] += 1
                    row_server_count[col_nr] += 1

        res = 0
        for col_nr, grid_row in enumerate(grid):
            for row_nr, val in enumerate(grid_row):
                if val:
                    # server is reachable if either column or row has more than one server
                    res += (col_server_count[row_nr] > 1) or (
                        row_server_count[col_nr] > 1
                    )
        return res
