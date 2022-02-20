class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        cmin = prices[0]
        retVal = 0
        for i in range(1, len(prices)):
            cmin = min(cmin, prices[i])
            retVal = max(retVal, prices[i]-cmin)
        return retVal
