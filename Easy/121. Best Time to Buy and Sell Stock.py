from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cmin = prices[0]
        res = 0
        for p in prices:
            if p < cmin:
                cmin = p
            elif p - cmin > res:
                res = p - cmin
        return res