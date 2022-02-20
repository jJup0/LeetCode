class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.deltas = ((0, 1), (0, -1), (1, 0), (-1, 0))
        rotten = []
        freshCount = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 2:
                    rotten.append((i, j))
                else:
                    freshCount += val
        minutesPassed = 0
        while freshCount > 0 and rotten:
            newRotten = []
            for i, j in rotten:
                newRotten.extend(self.bfs(i, j))
            minutesPassed += 1
            freshCount -= len(newRotten)
            rotten = newRotten

        return -1 if freshCount else minutesPassed

    def bfs(self, i, j):
        ret = []
        for di, dj in self.deltas:
            newi, newj = i + di, j + dj
            # print(newi, newj)
            if self.ingrid(newi, newj) and self.grid[newi][newj] == 1:
                ret.append((newi, newj))
                self.grid[newi][newj] = 2
        return ret

    def ingrid(self, i, j):
        return i >= 0 and i < len(self.grid) and j >= 0 and j < len(self.grid[0])
