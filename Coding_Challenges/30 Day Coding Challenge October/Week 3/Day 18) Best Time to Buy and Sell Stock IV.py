class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        if k >= n//2:  # can buy any time
            res = 0
            for i in range(1, n):
                res += max(0, prices[i]-prices[i-1])
            return res

        dp = [[0]*n for _ in range(k+1)]

        for i in range(1, k+1):
            buy_price = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(prices[j]+buy_price, dp[i][j-1])
                buy_price = max(buy_price, dp[i-1][j-1]-prices[j])
        return dp[-1][-1]
