from typing import List


class Solution:

    """
    You are given an integer array prices where prices[i] is the price of a given stock on the ith
    day, and an integer k.
    Find the maximum profit you can achieve. You may complete at most k transactions.
    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock
    before you buy again).
    Constraints:
        1 <= k <= 100
        1 <= prices.length <= 1000
        0 <= prices[i] <= 1000
    """

    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        O(n * k) / O(n * k)     time / space complexity
        """

        n = len(prices)
        # dp[i][j] contains the maximum profit for i trades until the jth day
        dp = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            max_diff = -10_000
            for j in range(1, len(prices)):
                # update max_diff if buying on previous day has the most potential for profit
                max_diff = max(max_diff, dp[i-1][j-1] - prices[j-1])

                # dp[i][j] is updated to the more profitable strategy out of:
                #   same strategy as for 1 less trade availible, and
                #   buying on day with max diff and selling on day j
                dp[i][j] = max(prices[j] + max_diff, dp[i][j-1])

        # return max profit for k trades on the last day
        return dp[k][n-1]
