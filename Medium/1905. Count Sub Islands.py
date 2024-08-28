"""
You are given two m x n binary matrices grid1 and grid2 containing only 0's
(representing water) and 1's (representing land). An island is a group of 1's
connected 4-directionally (horizontal or vertical). Any cells outside of the
grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1
that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

Constraints:
- m == grid1.length == grid2.length
- n == grid1[i].length == grid2[i].length
- 1 <= m, n <= 500
- grid1[i][j] and grid2[i][j] are either 0 or 1.
"""


class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        """
        O(n * m) / O(n * m)     time / space complexity
        """
        islands: list[list[tuple[int, int]]] = [
            self._find_islands(grid2, i, j)
            for i, row in enumerate(grid2)
            for j, val in enumerate(row)
            if val == 1
        ]

        return sum(
            all(grid1[i][j] for i, j in island_group) for island_group in islands
        )

    deltas = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def _find_islands(
        self, grid: list[list[int]], i: int, j: int
    ) -> list[tuple[int, int]]:
        to_visit = [(i, j)]
        grid[i][j] = 2
        island_coords: list[tuple[int, int]] = []
        while to_visit:
            i, j = to_visit.pop()
            island_coords.append((i, j))
            for di, dj in self.deltas:
                new_i = i + di
                new_j = j + dj
                if (
                    0 <= new_i < len(grid)
                    and 0 <= new_j < len(grid[0])
                    and grid[new_i][new_j] == 1
                ):
                    to_visit.append((new_i, new_j))
                    grid[new_i][new_j] = 2

            grid[i][j] = 2
        return island_coords
