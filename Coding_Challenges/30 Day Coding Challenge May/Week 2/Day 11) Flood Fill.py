class Solution:
    def floodFill(self, image: [[int]], sr: int, sc: int, newColor: int) -> [[int]]:
        def dfs(curR, curC):
            if curR < 0 or curR == len(self.image) or curC < 0 or curC == len(self.image[0]) or self.image[curR][curC] == self.newColor:
                return
            if(self.image[curR][curC] == self.oldColor):
                self.image[curR][curC] = self.newColor
                dfs(curR + 1, curC)
                dfs(curR - 1, curC)
                dfs(curR, curC + 1)
                dfs(curR, curC - 1)

        self.image = image
        self.newColor = newColor
        self.oldColor = image[sr][sc]
        dfs(sr, sc)
        return self.image
