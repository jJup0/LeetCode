"""
You are given a rows x cols matrix grid representing a field of cherries where
grid[i][j] represents the number of cherries that you can collect from the (i,
j) cell.

You have two robots that can collect cherries for you:
- Robot #1 is located at the top-left corner(0, 0), and
- Robot #2 is located at the top-right corner(0, cols - 1).

Return the maximum number of cherries collection using both robots by following
the rules below:
- From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i
+ 1, j + 1).
- When any robot passes through a cell, It picks up all cherries, and the cell
becomes an empty cell.
- When both robots stay in the same cell, only one takes the cherries.
- Both robots cannot move outside of the grid at any moment.
- Both robots should reach the bottom row in grid.

Constraints:
- rows == grid.length
- cols == grid[i].length
- 2 <= rows, cols <= 70
- 0 <= grid[i][j] <= 100
"""

import copy
import heapq
from collections import defaultdict
from typing import NamedTuple


class QueueNode(NamedTuple):
    cherries: int
    col1: int
    col2: int


class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        return self.cherryPickup_v2(grid)

    def cherryPickup_v2(self, grid: list[list[int]]) -> int:
        """
        n := len(grid[0]), m := len(grid)
        O(m * n^2) / O(n^2)     time / space complexity
        """
        height = len(grid)
        width = len(grid[0])

        # bot1 and bot2 positions
        positions: set[tuple[int, int]] = set([(0, width - 1)])
        # best_for_row[i][j] = best cherry score for bot1 on column i and bot2 on column j for current row
        best_for_row = [[-1] * width for _ in range(width)]
        best_for_row[0][-1] = grid[0][0] + grid[0][-1]

        # same structures but for next row
        new_positions = positions.copy()
        new_best_for_row = copy.deepcopy(best_for_row)

        # iterate through rows of the grid
        for curr_row_idx in range(1, height):
            curr_grid_row = grid[curr_row_idx]
            # create positions and best cherry score array for current iteration
            # iterate through all bot position combos
            for col1, col2 in positions:
                cherries = best_for_row[col1][col2]
                # iterate through all new bot positions
                for new_col1 in range(max(0, col1 - 1), min(width, col1 + 2)):
                    new_cherries1 = curr_grid_row[new_col1]
                    # make sure bot2 is always to the right of bot1 to
                    # minimize search space, without loss of generality
                    for new_col2 in range(max(0, col2 - 1, col1), min(width, col2 + 2)):
                        new_cherries2 = curr_grid_row[new_col2] * (new_col1 != new_col2)
                        new_total_cherries = cherries + new_cherries1 + new_cherries2
                        if new_total_cherries > new_best_for_row[new_col1][new_col2]:
                            # if total cherries for the bot position combo are best so far, update
                            new_best_for_row[new_col1][new_col2] = new_total_cherries
                            new_positions.add((new_col1, new_col2))

            # switch arrays for next iteration
            best_for_row, new_best_for_row = new_best_for_row, best_for_row
            positions, new_positions = new_positions, positions

        # return the best score
        return max(max(col1s) for col1s in best_for_row)

    def cherryPickup_v1(self, grid: list[list[int]]) -> int:
        """
        Used a priority queue for no good reason.
        Works, but times out in leetcode submission.
        """

        class QueueNode1(NamedTuple):
            neg_cherries: int
            row: int
            col1: int
            col2: int

        height = len(grid)
        width = len(grid[0])

        # dp = [[0] * width for _ in range(height)]
        dp: list[defaultdict[tuple[int, int], int]] = [
            defaultdict(int) for _ in range(height)
        ]

        initial_cherries = grid[0][0] + grid[0][-1]
        queue = [QueueNode1(-initial_cherries, 0, 0, width - 1)]

        res = 0
        while queue:
            neg_cherries, row, col1, col2 = heapq.heappop(queue)
            cherries = -neg_cherries
            if cherries < dp[row][col1, col2]:
                continue
            dp[row][col1, col2] = cherries
            if row == height - 1:
                if cherries > res:
                    res = cherries
                    print(f"{cherries=} {col1=} {col2=}")
                continue

            new_row = row + 1
            for new_col1 in range(max(0, col1 - 1), min(width, col1 + 2)):
                additional_cherries1 = grid[new_row][new_col1]
                for new_col2 in range(max(0, col2 - 1), min(width, col2 + 2)):
                    additional_cherries2 = grid[new_row][new_col2] * (
                        new_col1 != new_col2
                    )
                    heapq.heappush(
                        queue,
                        QueueNode1(
                            neg_cherries - additional_cherries1 - additional_cherries2,
                            new_row,
                            new_col1,
                            new_col2,
                        ),
                    )
        return res
