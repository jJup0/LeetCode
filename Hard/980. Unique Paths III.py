class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        def inBounds(i, j):
            return (0 <= i < len(grid)) & (0 <= j < len(grid[0]))

        # returns ways to reach goal
        def bfs(i, j, stepsCount):
            val = grid[i][j]
            # cant go through obstacle
            if val == -1:
                return 0
            # if reached the end, return if all squares were passed
            if val == 2:
                return stepsCount == emptySquares
            stepsCount += 1
            # mark square as visited, by turning into obstacle
            grid[i][j] = -1
            ret = 0
            # visit adjacents
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ni = i + di
                nj = j + dj
                if inBounds(ni, nj):
                    ret += bfs(ni, nj, stepsCount)
            # mark square as unvisited again
            grid[i][j] = 0
            return ret

        ssi, ssj = 0, 0
        emptySquares = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    ssi, ssj = i, j
                emptySquares += (not val)

        grid[ssi][ssj] = 0  # mark start as empty square
        return bfs(ssi, ssj, -1)    # count at -1, because [ssi][ssj] counts as empty square
