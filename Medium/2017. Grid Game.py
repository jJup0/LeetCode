"""
You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c]
represents the number of points at position (r, c) on the matrix. Two robots
are playing a game on this matrix.

Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot
may only move to the right ( (r, c) to (r, c + 1) ) or down ( (r, c) to
(r + 1, c) ).

At the start of the game, the first robot moves from (0, 0) to (1, n-1),
collecting all the points from the cells on its path. For all cells (r, c)
traversed on the path, grid[r][c] is set to 0. Then, the second robot moves
from (0, 0) to (1, n-1), collecting the points on its path. Note that their
paths may intersect with one another.

The first robot wants to minimize the number of points collected by the second
robot. In contrast, the second robot wants to maximize the number of points it
collects. If both robots play optimally, return the number of points collected
by the second robot.

Constraints:
- grid.length == 2
- n == grid[r].length
- 1 <= n <= 5 * 10^4
- 1 <= grid[r][c] <= 10^5
"""


class Solution:
    """
    The optimal way for player 2 to play is to move down either at the first
    or last square, depending which has more points. The optimal way for
    player 1 to play it to minimize the maximum of these two paths.
    """

    def gridGame(self, grid: list[list[int]]) -> int:
        """
        Can be optimized, but asymptotic time and space complexity are optimal.
        Complexity:
            Time: O(n)
            Space: O(1)
        """
        top, bottom = grid
        res = points_top = sum(top)
        points_bottom = 0
        for t, b in zip(top, bottom):
            points_top -= t
            res = min(res, max(points_top, points_bottom))
            points_bottom += b
        return res
