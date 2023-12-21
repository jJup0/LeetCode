"""
You are given an integer array prices representing the prices of various
chocolates in a store. You are also given a single integer money, which
represents your initial amount of money.

ou must buy exactly two chocolates in such a way that you still have
some non-negative leftover money. You would like to minimize the sum
of the prices of the two chocolates you buy.

Return the amount of money you will have leftover after buying the two
chocolates. If there is no way for you to buy two chocolates without ending
up in debt, return money. Note that the leftover must be non-negative.

Constraints:
- 2 <= prices.length <= 50
- 1 <= prices[i] <= 100
- 1 <= money <= 100
"""


class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        """
        O(n) / O(1)     time / space complexity
        """
        cheapest = second_cheapest = 1_000
        for p in prices:
            if p < cheapest:
                second_cheapest = cheapest
                cheapest = p
            elif p < second_cheapest:
                second_cheapest = p

        total_cost = cheapest + second_cheapest
        if total_cost > money:
            return money
        return money - total_cost
