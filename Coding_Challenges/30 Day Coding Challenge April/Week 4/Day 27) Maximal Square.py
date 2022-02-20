class Solution:
    def countSquares(self, matrix: [[int]]) -> int:
        if not matrix:
            return 0
        retVal = 0
        dp = [[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j]) + 1
                    retVal += max(retVal, dp[i+1][j+1])
        return retVal
