from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i, row in enumerate(grid):
            prev = 0
            for j, val in enumerate(row):
                if val:
                    perimeter += 4
                    if i:
                        perimeter -= grid[i-1][j] * 2
                    perimeter -= prev * 2
                prev = val
        return perimeter
