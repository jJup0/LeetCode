class Solution:
    """
    You are given an array prices where prices[i] is the price of a given stock on
    the ith day, and an integer fee representing a transaction fee.

    Find the maximum profit you can achieve. You may complete as many transactions
    as you like, but you need to pay the transaction fee for each transaction.

    Note: You may not engage in multiple transactions simultaneously (i.e., you
    must sell the stock before you buy again).

    Constraints:
    - 1 <= prices.length <= 5 * 10^4
    - 1 <= prices[i] < 5 * 10^4
    - 0 <= fee < 5 * 10^4
    """

    def maxProfit(self, prices: list[int], fee: int) -> int:
        """
        Quasi-dynamic-programming approach:
        O(n) / O(1)     time / space complexity
        """
        # 0 profit if nothing to sell
        highest_total_profit_after_sell = 0

        # if stock is bought on first day, total profit minus fee and price
        highest_profit_after_buy = -fee - prices[0]

        for p in prices:
            # best possible profit after buying on the current day =
            #   best profit when not holding any stock minus fee and price
            buy_now = highest_total_profit_after_sell - fee - p
            if buy_now > highest_profit_after_buy:
                highest_profit_after_buy = buy_now

            # best possible profit after selling on current day =
            #   most profit previously possible after buying + price of stock on current day
            sell_now = highest_profit_after_buy + p
            if sell_now > highest_total_profit_after_sell:
                highest_total_profit_after_sell = sell_now

        # maximum possible profit after holding no stock on the last day
        return highest_total_profit_after_sell
