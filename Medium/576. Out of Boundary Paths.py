"""
There is an m x n grid with a ball. The ball is initially at the position
[startRow, startColumn]. You are allowed to move the ball to one of the four
adjacent cells in the grid (possibly out of the grid crossing the grid
boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number
of paths to move the ball out of the grid boundary. Since the answer can be
very large, return it modulo10^9 + 7.

Constraints:
- 1 <= m, n <= 50
- 0 <= maxMove <= 50
- 0 <= startRow < m
- 0 <= startColumn < n
"""


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        """
        O(m * n * maxMaxove) / O(n*m)   time / space complexity
        """

        def total_boundary_balls() -> int:
            nonlocal m, moves_grid
            return (
                sum(moves_grid[0])
                + sum(moves_grid[-1])
                + sum(moves_grid[i][0] + moves_grid[i][-1] for i in range(1, m + 1))
            )

        moves_grid = [[0] * (n + 2) for _ in range(m + 2)]
        moves_grid[startRow + 1][startColumn + 1] = 1
        res = 0
        MOD = 10**9 + 7
        for _ in range(maxMove):
            new_moves_grid = [[0] * (n + 2) for _ in range(m + 2)]
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    ways = moves_grid[i][j]
                    new_moves_grid[i - 1][j] += ways
                    new_moves_grid[i + 1][j] += ways
                    new_moves_grid[i][j - 1] += ways
                    new_moves_grid[i][j + 1] += ways
            moves_grid = new_moves_grid
            res = (res + total_boundary_balls()) % MOD

        return res
