from typing import List


class Solution:
    """
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
    return the number of islands.
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or
    vertically. You may assume all four edges of the grid are all surrounded by water.
    Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 300
        grid[i][j] is '0' or '1'.
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        O(n * m) / O(1)     time / space complexity
        """
        def checkNeighbours(row, col):
            # dfs search in grid for "1" fills with "0" after visiting cell
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0":
                return
            grid[row][col] = "0"
            checkNeighbours(row+1, col)
            checkNeighbours(row, col+1)
            checkNeighbours(row-1, col)
            checkNeighbours(row, col-1)

        # result variable
        island_count = 0

        # go through each cell checking if there is an unexplored piece of island
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # if there is, explore it, and increase island count
                if grid[row][col] == "1":
                    checkNeighbours(row, col)
                    island_count += 1

        return island_count
