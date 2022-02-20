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
                    # dp [i+1][j+1] is basically matrix[i][j] but with first row and column filled with zeroes so that when accessing previous cells there is no index out of range error. Here the minimum value (=smallest possible square),  is taken and increased by one. If above, left and above-left are all 1's, then the current cell will be of size 2. If a single cell (l, a, l-a) is 0, then the current cell can only be of size 1.
                    retVal += dp[i+1][j+1]
        return retVal
