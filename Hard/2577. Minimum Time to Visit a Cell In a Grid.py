"""
You are given a m x n matrix grid consisting of non-negative integers where
grid[row][col] represents the minimum time required to be able to visit the
cell (row, col), which means you can visit the cell (row, col) only when the
time you visit it is greater than or equal to grid[row][col].

You are standing in the top-left cell of the matrix in the 0th second, and you
must move to any adjacent cell in the four directions: up, down, left, and
right. Each move you make takes 1 second.

Return the minimum time required in which you can visit the bottom-right cell
of the matrix. If you cannot visit the bottom-right cell, then return -1.

Constraints:
- m == grid.length
- n == grid[i].length
- 2 <= m, n <= 1000
- 4 <= m * n <= 10^5
- 0 <= grid[i][j] <= 10^5
- grid[0][0] == 0
"""

import heapq


class Solution:
    def minimumTime(self, grid: list[list[int]]) -> int:
        """
        Complexity:
            Time: O(n * m * log(n * m))
            Space: O(n * m)
        """
        if grid[0][1] > 1 and grid[1][0] > 1:
            # only way to not reach the end is if cells neigboring start are greater than 1
            return -1

        height = len(grid)
        width = len(grid[0])
        # dp[row][col] = memoization for minimum moves to get to grid[row][col]
        dp = [[1_000_000_000] * width for _ in range(height)]

        # deltas for visiting neighbors
        deltas = ((0, 1), (1, 0), (0, -1), (-1, 0))

        # priority queue for visiting cells in grid
        prio_queue = [(0, 0, 0)]
        while True:
            moves, row, col = heapq.heappop(prio_queue)
            if row == height - 1 and col == width - 1:
                # reached goal
                return moves
            if moves >= dp[row][col]:
                # previously reached cell with fewer moves, no advantage
                continue
            dp[row][col] = moves
            next_move = moves + 1
            # visit neighbors
            for d_row, d_col in deltas:
                new_row = row + d_row
                new_col = col + d_col
                if not (0 <= new_row < height and 0 <= new_col < width):
                    # "neighbor" is not on grid
                    continue

                min_moves = grid[new_row][new_col]
                if min_moves <= next_move:
                    # can move to next grid without wasting time
                    actual_move = next_move
                elif next_move % 2 == min_moves % 2:
                    # need to waste time going to previous square and current square
                    actual_move = min_moves
                else:
                    # need to waste time going to previous square and
                    # current square, but move parity means we have to
                    # waste one extra turn going to a previous square
                    actual_move = min_moves + 1
                heapq.heappush(prio_queue, (actual_move, new_row, new_col))
