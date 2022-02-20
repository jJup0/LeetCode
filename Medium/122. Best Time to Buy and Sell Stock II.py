class Solution:
    def maxProfit(self, prices: [int]) -> int:
        prev = prices[0]
        profit = 0
        for price in prices:
            dailyDiff = price - prev
            if dailyDiff > 0:
                profit += dailyDiff
            prev = price
        return profit

        # profit = 0
        # curBuy = 0
        # day = 0
        # bought = False
        # while day < len(prices)-1:
        #     curPrice, nextPrice = prices[day], prices[day+1]
        #     if bought == False:
        #         if nextPrice > curPrice:
        #             curBuy = curPrice
        #             bought = True
        #     elif curBuy < curPrice and curPrice > nextPrice:
        #         profit += curPrice - curBuy
        #         bought = False
        #     day += 1
        # if bought == True:
        #     profit += prices[-1] - curBuy
        # return profit
