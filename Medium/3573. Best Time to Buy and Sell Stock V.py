"""
You are given an integer array prices where prices[i] is the price of a stock
in dollars on the ith day, and an integer k.

You are allowed to make at most k transactions, where each transaction can be
either of the following:
- Normal transaction: Buy on day i, then sell on a later day j where i < j. You
  profit prices[j] - prices[i].
- Short selling transaction: Sell on day i, then buy back on a later day j
  where i < j. You profit prices[i] - prices[j].

Note that you must complete each transaction before starting another.
Additionally, you can't buy or sell on the same day you are selling or buying
back as part of a previous transaction.

Return the maximum total profit you can earn by making at most k transactions.

Constraints:
- 2 <= prices.length <= 10^3
- 1 <= prices[i] <= 10^9
- 1 <= k <= prices.length / 2
"""

import random
import sys
from functools import cache

sys.setrecursionlimit(100000)
import cProfile

MOD = 10**9 + 7


class Solution1:
    def maximumProfit(self, prices: list[int], k: int) -> int:
        self.prices = prices
        self._calc_max_single_profit(prices)
        self._mp_inc2()
        return self.mp2(0, k)

    def _calc_max_single_profit(self, prices: list[int]):
        self.max_single_profit: list[list[int]] = []
        for i in range(len(prices)):
            profits2 = [0] * (i + 1)
            smallest = biggest = prices[i]
            for j in range(i + 1, len(prices)):
                num = prices[j]
                profit = max(biggest - num, num - smallest, profits2[j - 1])
                profits2.append(profit)
                if num > biggest:
                    biggest = num
                if num < smallest:
                    smallest = num
            self.max_single_profit.append(profits2)

    def _mp_inc2(self):
        self.max_profits_inc2: list[list[tuple[int, int]]] = []
        for i, profits in enumerate(self.max_single_profit):
            inc_profits = [(0, i)]
            for j in range(i + 1, len(self.prices)):
                p = profits[j]
                if p > inc_profits[-1][0]:
                    inc_profits.append((p, j))
            self.max_profits_inc2.append(inc_profits)

    @cache
    def mp2(self, start: int, k: int) -> int:
        if start >= len(self.prices):
            return 0
        if k == 1:
            return self.max_single_profit[start][-1]
        return max(
            profit + self.mp2(j + 1, k - 1)
            for profit, j in self.max_profits_inc2[start]
        )


class Solution2:
    def maximumProfit(self, prices: list[int], k: int) -> int:
        @cache
        def solve(idx: int, k: int, state: int) -> int:
            if idx >= len(prices):
                return 0 if state == NO_BAGS else -INT_INF
            if k == 0:
                return 0

            best_if_sell = best_if_buy = -INT_INF
            if state == SHORTED:
                # buy back after short
                best_if_buy = -prices[idx] + solve(idx + 1, k - 1, NO_BAGS)
            elif state == BOUGHT:
                # sell after buy
                best_if_sell = prices[idx] + solve(idx + 1, k - 1, NO_BAGS)
            else:
                # try buying or selling
                best_if_buy = -prices[idx] + solve(idx + 1, k, BOUGHT)
                best_if_sell = prices[idx] + solve(idx + 1, k, SHORTED)

            best_if_skip = solve(idx + 1, k, state)
            return max(best_if_buy, best_if_sell, best_if_skip)

        INT_INF = 10**9 * len(prices)
        SHORTED, BOUGHT, NO_BAGS = 0, 1, 2
        res = solve(0, k, NO_BAGS)
        # when running tests gargabe collector is not fast enough
        solve.cache_clear()
        return res


class Solution(Solution2):
    pass


def test():
    s = Solution()
    res = s.maximumProfit([14, 6, 10, 19], 1)
    real = 13
    assert res == real, res

    res = s.maximumProfit([8, 4, 15, 7, 4, 7, 2, 14, 15], 3)
    real = 28
    assert res == real, res


def big_test():
    random.seed(1)
    arr = [random.randint(1, 10000000) for _ in range(1300)]
    s = Solution()
    s.maximumProfit(arr, 400)
    # print(s.mp2.cache_info())


test()
cProfile.run("big_test()", sort="cumtime")
