class Solution:
    def maxProfit(self, prices: [int]) -> int:
        profit = 0
        curBuy = 0
        day = 0
        bought = False
        while day < len(prices)-1:
            curPrice, nextPrice = prices[day], prices[day+1]
            if bought == False:
                if nextPrice > curPrice:
                    curBuy = curPrice
                    bought = True
            elif curBuy < curPrice and curPrice > nextPrice:
                profit += curPrice - curBuy
                bought = False
            day += 1
        if bought == True:
            profit += prices[-1] - curBuy
        return profit


def maxProfitShortAndDumb(prices):
    ans = 0
    for i in range(1, len(prices)):
        ans += max(prices[i] - prices[i-1], 0)
    return ans

