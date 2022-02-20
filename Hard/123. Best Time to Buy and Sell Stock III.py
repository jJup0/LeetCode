# just used my solution from k transactions, specific solution for just 2 is faster
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dpCopy = [[0] * (len(prices)) for _ in range(3)]
        for i in range(1, 3):
            maxDiff = float('-inf')

            for j in range(1, len(prices)):

                maxDiff = max(maxDiff, dpCopy[i-1][j-1] - prices[j-1])
                dpCopy[i][j] = max(prices[j] + maxDiff, dpCopy[i][j-1])

        return dpCopy[2][-1]

        # stolen
        # firstbuy, firstsell = float("-inf"), 0
        # secondbuy, secondsell = float("-inf"), 0
        # for price in prices:
        #     firstbuy = max(firstbuy, - price)
        #     firstsell = max(firstsell, firstbuy + price)
        #     secondbuy = max(secondbuy, firstsell - price)
        #     secondsell = max(secondsell, secondbuy + price)

        # return secondsell
