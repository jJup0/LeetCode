class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        def dfs(grid, row, col):
            if row < 0 or row >= len(grid):
                return
            if col < 0 or col >= len(grid[0]):
                return
            if grid[row][col] == "0":
                return

            grid[row][col] = "0"
            dfs(grid, row+1, col)
            dfs(grid, row, col+1)
            dfs(grid, row-1, col)
            dfs(grid, row, col-1)

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(grid, row, col)
                    count += 1

        return count


class SlowSolution:
    def numIslands(self, grid: [[str]]) -> int:
        if not grid:
            return 0
        islandsC = 0
        seen = []
        for _ in grid:
            seen.append([])

        def findNeighbours(x, y, zeroOrOne):
            nonlocal seen
            if grid[x][y] == zeroOrOne:
                seen[x].append(y)
                if x < len(grid)-1:
                    if not(y in seen[x+1]):
                        findNeighbours(x+1, y, zeroOrOne)
                if x > 0:
                    if not(y in seen[x-1]):
                        findNeighbours(x-1, y, zeroOrOne)
                if y < len(grid[x])-1:
                    if not(y+1 in seen[x]):
                        findNeighbours(x, y+1, zeroOrOne)
                if y > 0:
                    if not(y-1 in seen[x]):
                        findNeighbours(x, y-1, zeroOrOne)
        i, j = 0, 0
        while i < len(grid):
            while j < len(grid[0]):
                if not(j in seen[i]):
                    if grid[i][j] == '1':
                        findNeighbours(i, j, '1')
                        islandsC += 1
                    else:
                        findNeighbours(i, j, '0')
                j += 1
            j = 0
            i += 1

        return islandsC
