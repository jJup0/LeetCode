"""
You are given row x col grid representing a map where grid[i][j] = 1 represents
land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is
completely surrounded by water, and there is exactly one island (i.e., one or
more connected land cells).

The island doesn't have"lakes", meaning the water inside isn't connected to the
water around the island. One cell is a square with side length 1. The grid is
rectangular, width and height don't exceed 100. Determine the perimeter of the
island.

Constraints:
- row == grid.length
- col == grid[i].length
- 1 <= row, col <= 100
- grid[i][j] is 0 or 1.
- There is exactly one island in grid.
"""


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        """
        O(n * m) / O(1)     time / space complexity
        """
        perimeter = 0
        for i, row in enumerate(grid):
            left_neighbor_val = 0
            for j, val in enumerate(row):
                if not val:
                    # if tile is sea, no increase to perimeter
                    left_neighbor_val = 0
                    continue

                # by each tile of land will increase the perimeter by 4
                perimeter += 4
                if i > 0 and grid[i - 1][j]:
                    # if there is a land above, decrease the perimeter by 2
                    perimeter -= 2
                # if the previous plot was land, decrease the perimeter by 2
                perimeter -= left_neighbor_val * 2
                left_neighbor_val = 1
        return perimeter
