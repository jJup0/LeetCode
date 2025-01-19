"""
Given an m x n grid. Each cell of the grid has a sign pointing to the next cell
you should visit if you are currently in this cell. The sign of grid[i][j] can be:
- 1 which means go to the cell to the right. (i.e go from grid[i][j] to
  grid[i][j + 1] )
- 2 which means go to the cell to the left. (i.e go from grid[i][j] to
  grid[i][j - 1] )
- 3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j] )
- 4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j] )

Notice that there could be some signs on the cells of the grid that point
outside the grid.

You will initially start at the upper left cell (0, 0). A valid path in the
grid is a path that starts from the upper left cell (0, 0) and ends at the
bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid
path does not have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a
cell one time only.

Return the minimum cost to make the grid have at least one valid path.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- 1 <= grid[i][j] <= 4
"""

import heapq


class Solution:

    # deltas[_] = (delta code, delta column, delta row)
    deltas = (
        (1, 1, 0),
        (2, -1, 0),
        (3, 0, 1),
        (4, 0, -1),
    )

    def minCost(self, grid: list[list[int]]) -> int:
        """
        Simple dynamic programming approach.
        Complexity:
            Time: O(n * m)
            Space: O(n * m)
        """
        # best[row][col] = fewest changes needed to reach
        # bottom right corner from top left corner
        fewest_changes = [[1_000_000] * len(grid[0]) for _ in range(len(grid))]

        goal_col = len(grid[0]) - 1
        goal_row = len(grid) - 1

        # exploration states priority queue for finding shortest path to
        # bottom right corner from top left corner
        queue: list[tuple[int, int, int]] = [(0, 0, 0)]
        while True:
            # get state with fewest changes from priority queue
            changes, col, row = heapq.heappop(queue)
            if col == goal_col and row == goal_row:
                # shortest path to bottom right corner found
                return changes

            curr_code = grid[row][col]
            # visit neighbors
            for code, d_col, d_row in self.deltas:
                new_col = col + d_col
                new_row = row + d_row
                if not (0 <= new_col <= goal_col and 0 <= new_row <= goal_row):
                    # out of bounds
                    continue

                next_changes = changes + (code != curr_code)
                if fewest_changes[new_row][new_col] <= next_changes:
                    # do not traverse to neighbor if path with fewer changes has been found
                    continue
                fewest_changes[new_row][new_col] = next_changes

                heapq.heappush(queue, (next_changes, new_col, new_row))
