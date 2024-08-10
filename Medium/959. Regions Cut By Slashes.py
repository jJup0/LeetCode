r"""
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of
a'/','\', or blank space''. These characters divide the square into contiguous
regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a'\' is represented as'\\'.

Constraints:
- n == grid.length == grid[i].length
- 1 <= n <= 30
- grid[i][j] is either'/','\', or''.
"""


class Solution:
    deltas = ((-1, 0), (0, -1), (0, 1), (1, 0))

    def regionsBySlashes(self, grid: list[str]) -> int:
        """
        Convert to binary grid array approach.
        O(n^2) / O(n^2)     time / space complexity
        """
        binary_grid = self._convert_grid_to_binary(grid)
        res = 0
        for i in range(1, len(binary_grid) - 1):
            for j in range(1, len(binary_grid) - 1):
                res += self._find_islands(binary_grid, i, j)
        return res

    def _convert_grid_to_binary(self, grid: list[str]) -> list[list[int]]:
        """
        Converts the slash grid into a binary grid.
        O(n^2) / O(n^2)     time / space complexity
        """
        # 0 reprents empty space, 1 represents border or line
        binary_grid: list[list[int]] = [[1] * (len(grid) * 3 + 2)]
        for row in grid:
            # left border
            block_row1 = [1]
            block_row2 = [1]
            block_row3 = [1]
            for char in row:
                if char == " ":
                    block_row1.extend((0, 0, 0))
                    block_row2.extend((0, 0, 0))
                    block_row3.extend((0, 0, 0))
                elif char == "/":
                    block_row1.extend((0, 0, 1))
                    block_row2.extend((0, 1, 0))
                    block_row3.extend((1, 0, 0))
                else:  # "\"
                    block_row1.extend((1, 0, 0))
                    block_row2.extend((0, 1, 0))
                    block_row3.extend((0, 0, 1))

            # right border
            block_row1.append(1)
            block_row2.append(1)
            block_row3.append(1)
            binary_grid.append(block_row1)
            binary_grid.append(block_row2)
            binary_grid.append(block_row3)

        binary_grid.append([1] * (len(grid) * 3 + 2))
        return binary_grid

    def _find_islands(self, binary_grid: list[list[int]], i: int, j: int) -> int:
        """
        Returns 0 if binary_grid[i][j] != 0, otherwise flood fills binary_grid with the value 2 and returns 1.
        Could fill binary grid with 1 as well, but 2 makes debugging easier.
        O(n) / O(1)     time / space complexity
        O(1) / O(1)     average time / space complexity
        """
        if binary_grid[i][j] != 0:
            return 0

        dfs_queue: list[tuple[int, int]] = [(i, j)]
        while dfs_queue:
            i, j = dfs_queue.pop()

            for di, dj in self.deltas:
                newi = i + di
                newj = j + dj
                if binary_grid[newi][newj] == 0:
                    # 2 represents visited empty space
                    binary_grid[newi][newj] = 2
                    dfs_queue.append((newi, newj))
        return 1
