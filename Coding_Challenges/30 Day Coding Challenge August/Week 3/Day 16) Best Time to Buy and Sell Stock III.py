class Solution:
    def maxProfit(self, prices: [int]) -> int:
        if not prices:
            return 0
        k = 2
        dp = [[0 for x in prices] + [0] for x in range(k+1)]
        for t in range(1, k+1):
            maxSoFar = float('-inf')
            for i in range(1, len(prices)):
                maxSoFar = max(maxSoFar, dp[t-1][i-1] - prices[i-1])
                dp[t][i] = max(dp[t][i-1], maxSoFar + prices[i])
        return dp[k][-2]
