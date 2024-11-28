"""
You are given a 0-indexed 2D integer array grid of size m x n. Each cell has
one of two values:
- 0 represents an empty cell,
- 1 represents an obstacle that may be removed.

You can move up, down, left, or right from and to an empty cell.

Return the minimum number of obstacles to remove so you can move from the upper
left corner (0, 0) to the lower right corner (m - 1, n - 1).

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10^5
- 2 <= m * n <= 10^5
- grid[i][j] is either 0 or 1.
- grid[0][0] == grid[m - 1][n - 1] == 0
"""

import heapq


class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        """
        Priority queue based on bricks broken with memoization.
        Complexity:
            Time: O(n * m * log(n * m))
            Space: O(n * m)
        """
        height = len(grid)
        width = len(grid[0])
        # memoization of minimum number of moves needed to reach grid[i][j]
        breaks_needed = [[1_000_000] * width for _ in range(height)]

        deltas = ((-1, 0), (0, -1), (0, 1), (1, 0))
        # priority queue where queue[i] = [breaks needed to get to (row, col), row, col]
        prio_queue = [(grid[0][0], 0, 0)]
        # djistra search for fewest breaks to grid[-1][-1]
        while True:
            breaks, row, col = heapq.heappop(prio_queue)
            if breaks_needed[row][col] <= breaks:
                # cell already reached with equal or fewer breaks
                continue
            breaks_needed[row][col] = breaks
            # travers to neighbors
            for d_row, d_col in deltas:
                new_row = row + d_row
                new_col = col + d_col
                if not (0 <= new_row < height and 0 <= new_col < width):
                    # "neighbor" is not on grid
                    continue

                next_breaks = breaks + grid[new_row][new_col]
                if new_row == height - 1 and new_col == width - 1:
                    # reached bottom right
                    return next_breaks
                if next_breaks < breaks_needed[new_row][new_col]:
                    heapq.heappush(prio_queue, (next_breaks, new_row, new_col))
