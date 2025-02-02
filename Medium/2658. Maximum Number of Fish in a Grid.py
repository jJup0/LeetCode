"""
You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:
- A land cell if grid[r][c] = 0, or
- A water cell containing grid[r][c] fish, if grid[r][c] > 0.

A fisher can start at any water cell (r, c) and can do the following operations
any number of times:
- Catch all the fish at cell (r, c), or
- Move to any adjacent water cell.

Return the maximum number of fish the fisher can catch if he chooses his
starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1),
(r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- 0 <= grid[i][j] <= 10
"""


class Solution:
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def findMaxFish(self, grid: list[list[int]]) -> int:
        """
        Simply DFS fish all neighboring cells starting from each cell.
        Complexity:
            Time: O(n * m)
            Space: O(n * m)
        """
        self.grid = grid
        return max(
            self._collect_adjacent_fish(row, col)
            for row in range(len(grid))
            for col in range(len(grid[0]))
        )

    def _collect_adjacent_fish(self, starting_row: int, starting_col: int) -> int:
        if self.grid[starting_row][starting_col] == 0:
            # nothing to fish
            return 0

        queue = [(starting_row, starting_col)]
        total_fish = 0
        while queue:
            row, col = queue.pop()
            # remove fish from grid and add to total
            total_fish += self.grid[row][col]
            self.grid[row][col] = 0
            queue.extend(self._get_neighboring_fish_coords(row, col))
        return total_fish

    def _get_neighboring_fish_coords(self, row: int, col: int):
        for delta_row, delta_col in self.deltas:
            newi = row + delta_row
            newj = col + delta_col
            if not (0 <= newi < len(self.grid) and 0 <= newj < len(self.grid[0])):
                continue
            if self.grid[newi][newj] == 0:
                continue
            yield newi, newj
