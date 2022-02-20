class Solution:
    def change(self, amount: int, coins: [int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1       # there is one way to get a total of zero coins
        for coinVal in coins:
            for curAmount in range(coinVal, amount+1):
                # to get n coins, we can use a previous base of n-coin, because with the current coin value: n - coin + coin is a nother way to get n coins
                dp[curAmount] += dp[curAmount-coinVal]
        return dp[amount]
