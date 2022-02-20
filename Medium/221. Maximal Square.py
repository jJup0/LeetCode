class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m, n, retVal = len(matrix), len(matrix[0]), 0
        dp = [[0] * (n+1) for _ in range(m+1)]  # dp[i+1][j+1] is maximum square with [i][j] as bottom right corner
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j]) + 1
                    retVal = max(retVal, dp[i+1][j+1])
                else:
                    dp[i+1][j+1] = 0
        return retVal ** 2