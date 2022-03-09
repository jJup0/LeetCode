from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        if not prices:
            return 0

        dpCopy = [[0] * (len(prices)) for _ in range(k + 1)]
        for i in range(1, k + 1):
            maxDiff = -10000    # constraint 0 <= prices[i] <= 1000, avoid float('-inf') for type checker

            for j in range(1, len(prices)):

                maxDiff = max(maxDiff, dpCopy[i-1][j-1] - prices[j-1])
                dpCopy[i][j] = max(prices[j] + maxDiff, dpCopy[i][j-1])

        return dpCopy[k][-1]
