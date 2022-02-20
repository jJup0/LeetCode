class Solution:
    def orangesRotting(self, grid: [[int]]) -> int:
        contaminators = []
        minutes = -1
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    contaminators.append((i, j))
        while contaminators:
            newcs = []
            for i, j in contaminators:
                for newi, newj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if 0 <= newi and newi < m and 0 <= newj and newj < n and grid[newi][newj] == 1:
                        grid[newi][newj] = 2
                        newcs.append((newi, newj))
            contaminators = newcs
            minutes += 1
        return -1 if 1 in [j for sub in grid for j in sub] else max(0, minutes)
