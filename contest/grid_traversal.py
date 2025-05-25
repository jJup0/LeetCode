class Solution:
    deltas = ((-1, 0), (0, -1), (0, 1), (1, 0))

    def _is_on_board(self, grid: list[list[int]], row: int, col: int):
        return 0 <= row <= len(grid) and 0 <= col <= len(grid[0])

    def _get_land_neighbors(
        self, grid: list[list[int]], row: int, col: int
    ) -> list[tuple[int, int]]:
        res: list[tuple[int, int]] = []
        for di, dj in self.deltas:
            new_row = row + di
            new_col = col + dj
            if not self._is_on_board(grid, new_row, new_col):
                continue
            # skip if visited
            res.append((new_row, new_col))
        return res
