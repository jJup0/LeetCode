from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacle_grid: List[List[int]]) -> int:

        # if grid is empty or start/end cell is blocked, there are no unique paths to goal
        if not obstacle_grid or obstacle_grid[0][0] or obstacle_grid[-1][-1]:
            return 0

        m, n = len(obstacle_grid), len(obstacle_grid[0])

        # fill grid with unique nr of ways to get to each position, since robot can only move right
        # or down, to calculate unique paths to a square only unique paths to left and upper neighbor
        # need to be known

        # set number of ways to reach starting cell to 1
        obstacle_grid[0][0] = 1

        # initialize first col, if upper neighbor can not be reached, or obstacle on cell, cell can not be reached
        for i in range(1, m):
            obstacle_grid[i][0] = obstacle_grid[i-1][0] * (1 - obstacle_grid[i][0])
        # initialize first row, if left neighbor can not be reached, or obstacle on cell, cell can not be reached
        for j in range(1, n):
            obstacle_grid[0][j] = obstacle_grid[0][j-1] * (1 - obstacle_grid[0][j])

        # fill in gaps from initalized rows, any cell accessed will still have 0 or 1 depending on if
        # obstacle or space, all cells below and to the left are already initialized
        # value to a cell is equal to sum of upper and left neighbor paths if cell does not contain an obstacle, else 0
        for i in range(1, m):
            for j in range(1, n):
                obstacle_grid[i][j] = (obstacle_grid[i-1][j] + obstacle_grid[i][j-1]) * (1 - obstacle_grid[i][j])

        # return nr of paths to end cell
        return obstacle_grid[-1][-1]
