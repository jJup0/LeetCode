"""
You are given an n x n binary matrix grid. You are allowed to change at most
one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1 s.

Constraints:
- n == grid.length
- n == grid[i].length
- 1 <= n <= 500
- grid[i][j] is either 0 or 1.
"""


class Solution:

    def largestIsland(self, grid: list[list[int]]) -> int:
        self.height = len(grid)
        self.width = len(grid[0])
        if all(val for row in grid for val in row):
            return self.width * self.height

        self.grid = grid
        self.island_id_to_size: dict[int, int] = {}
        self.cell_to_island_id = [[-1] * self.width for _ in range(self.height)]
        # populates `self.island_id_to_size` and `self.cell_to_island_id`
        self._find_all_islands()

        # get max score for flipping a single water cell to land
        return max(
            self._get_connecting_score(i, j)
            for i, row in enumerate(grid)
            for j, val in enumerate(row)
            if not val
        )

    def _find_all_islands(self) -> None:
        for i, row in enumerate(self.grid):
            for j, val in enumerate(row):
                if not val:
                    # water cell, continue
                    continue
                if self.cell_to_island_id[i][j] != -1:
                    # part of already discovered island
                    continue

                island_id = i * self.width + j
                self.island_id_to_size[island_id] = self._dfs_get_island_size(
                    i, j, island_id
                )

    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def _get_land_neighbors(self, i: int, j: int) -> list[tuple[int, int]]:
        res: list[tuple[int, int]] = []
        for di, dj in self.deltas:
            newi = i + di
            newj = j + dj
            if not (0 <= newi < self.height and 0 <= newj < self.width):
                continue
            if self.grid[newi][newj] == 0:
                continue
            res.append((newi, newj))
        return res

    def _dfs_get_island_size(self, i: int, j: int, island_id: int) -> int:
        """Gets size of connected land cells and sets `self.cell_to_island_id[i][j]` to island_id."""
        self.cell_to_island_id[i][j] = island_id
        res = 1
        for newi, newj in self._get_land_neighbors(i, j):
            if self.cell_to_island_id[newi][newj] == island_id:
                continue
            res += self._dfs_get_island_size(newi, newj, island_id)
        return res

    def _get_connecting_score(self, i: int, j: int):
        """Get size of joined island after flipping grid[i][j] from 0 to 1."""
        neighbors = self._get_land_neighbors(i, j)
        seen_island_ids: list[int] = []
        res = 1
        for neighbor_i, neighbor_j in neighbors:
            island_id = self.cell_to_island_id[neighbor_i][neighbor_j]
            if island_id in seen_island_ids or island_id == -1:
                continue
            seen_island_ids.append(island_id)
            res += self.island_id_to_size[island_id]
        return res
