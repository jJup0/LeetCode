class Solution:
    """
    It is a sweltering summer day, and a boy wants to buy some ice cream bars.

    At the store, there are n ice cream bars. You are given an array costs of length n, where
    costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to
    spend, and he wants to buy as many ice cream bars as possible. 

    Return the maximum number of ice cream bars the boy can buy with coins coins.

    Note: The boy can buy the ice cream bars in any order.

    Constraints:
        costs.length == n
        1 <= n <= 10^5
        1 <= costs[i] <= 10^5
        1 <= coins <= 10^8
    """

    def maxIceCream(self, costs: list[int], coins: int) -> int:
        """
        sort costs, and buy cheapest ice cream until no more coins are left
        """

        costs.sort()
        res = 0
        for cost in costs:
            if cost <= coins:
                res += 1
                coins -= cost
            else:
                break
        return res
