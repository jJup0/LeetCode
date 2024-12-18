"""
You are given an integer array prices where prices[i] is the price of the ith
item in a shop.

There is a special discount for items in the shop. If you buy the ith item,
then you will receive a discount equivalent to prices[j] where j is the minimum
index such that j > i and prices[j] <= prices[i]. Otherwise, you will not
receive any discount at all.

Return an integer array answer where answer[i] is the final price you will pay
for the ith item of the shop, considering the special discount.

Constraints:
- 1 <= prices.length <= 500
- 1 <= prices[i] <= 1000
"""


class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        res: list[int] = [-1] * len(prices)
        # monotone increasing stack of past (price, index)
        stack: list[tuple[int, int]] = []
        for i, price in enumerate(prices):
            while stack and stack[-1][0] >= price:
                # apply discount to previous prices
                p, j = stack.pop()
                res[j] = p - price
            stack.append((price, i))

        # add all items with no discount to result
        for p, j in stack:
            res[j] = p
        return res
