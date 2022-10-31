from collections import deque
from typing import Deque, List, Tuple


class Solution:
    """
    You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle).
    You can move up, down, left, or right from and to an empty cell in one step.

    Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right
    corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible
    to find such walk return -1.

    Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 40
        1 <= k <= m * n
        grid[i][j] is either 0 or 1.
        grid[0][0] == grid[m - 1][n - 1] == 0
    """

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        m_dec = m - 1
        n_dec = n - 1

        # bfs queue for traversing grid, deque[x] = (steps, k_remaining, i, j)
        queue: Deque[Tuple[int, int, int, int]] = deque([(0, k, 0, 0)])

        # seen matrix storing highest remaining wall breaks availible when a cell grid[i][j] has
        # been reached. Since the algorithm is bfs, a cell will be reached first with the smallest
        # amount of steps
        seen = [[-1] * n for _ in range(m)]

        while queue:
            # get state from queue
            steps, k_rem, i, j = queue.popleft()

            # if the current cell is a wall, use up a wall break
            k_rem -= grid[i][j]

            # if this cell has been reached previously with fewer wall breaks, no need to continue.
            # also takes care of when k_rem < 0
            if k_rem <= seen[i][j]:
                continue
            # current k_rem is highest so far
            seen[i][j] = k_rem

            # if target cell has been reached, return steps. Guaranteed to be minimum steps since
            # bfs is used
            if i == m_dec and j == n_dec:
                return steps

            # increment steps needed for visiting next cell
            steps += 1

            # visit all neighbors that are within the grid
            if i > 0:
                queue.append((steps, k_rem, i - 1, j))
            if i < m_dec:
                queue.append((steps, k_rem, i + 1, j))
            if j > 0:
                queue.append((steps, k_rem, i, j - 1))
            if j < n_dec:
                queue.append((steps, k_rem, i, j + 1))

        return -1
