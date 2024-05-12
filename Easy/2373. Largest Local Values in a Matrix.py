"""
You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:
- maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid
  centered around row i + 1 and column j + 1.

In other words, we want to find the largest value in every contiguous 3 x 3
matrix in grid.

Return the generated matrix.

Constraints:
- n == grid.length == grid[i].length
- 3 <= n <= 100
- 1 <= grid[i][j] <= 100
"""


class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        """
        Naive implementation, but there did not seem to be any fast implementations other than loop unrolls.
        O(n^2) / O(n^2)     time / space complexity
        """
        res: list[list[int]] = []
        for i in range(1, len(grid) - 1):
            res.append([])
            for j in range(1, len(grid[0]) - 1):
                local_max = -1
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        local_max = max(local_max, grid[i + di][j + dj])
                res[-1].append(local_max)
        return res
