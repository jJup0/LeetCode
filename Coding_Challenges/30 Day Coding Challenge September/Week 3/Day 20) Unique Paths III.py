class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def traverseGrid(ci, cj, squaresLeft):
            for newi, newj in ((ci+1, cj), (ci-1, cj), (ci, cj+1), (ci, cj-1)):
                if 0 <= newi < len(grid) and 0 <= newj < len(grid[newi]):
                    if grid[newi][newj] == 0:
                        grid[newi][newj] = -1
                        traverseGrid(newi, newj, squaresLeft-1)
                        grid[newi][newj] = 0
                    elif grid[newi][newj] == 2:
                        self.retVal += not squaresLeft

        self.retVal = 0
        starti = None
        totalSquares = 0
        for i, row in enumerate(grid):
            totalSquares += row.count(0)
            if starti == None and 1 in row:
                starti, startj = i, row.index(1)

        traverseGrid(starti, startj, totalSquares)
        return self.retVal
