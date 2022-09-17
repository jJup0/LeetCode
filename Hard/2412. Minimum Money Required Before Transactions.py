from typing import List


class Solution:
    """
    You are given a 0-indexed 2D integer array transactions, where
    transactions[i] = [costi, cashbacki].
    The array describes transactions, where each transaction must be completed exactly once in some
    order. At any given moment, you have a certain amount of money. In order to complete
    transaction i, money >= costi must hold true. After performing a transaction, money becomes
    money - costi + cashbacki.
    Return the minimum amount of money required before any transaction so that all of the
    transactions can be completed regardless of the order of the transactions.
    Constraints:
        1 <= transactions.length <= 10^5
        transactions[i].length == 2
        0 <= costi, cashbacki <= 10^9
    """

    def minimumMoney(self, transactions: List[List[int]]) -> int:
        """
        Calculate money need for worst case scenario which goes like this: first all the
        transactions with cost>cashback in order of cashback, then largest cost transaction
        with cost<=cashback, then all other cost<=cashback transactions
        """
        # current money availible, and starting money needed in worst case scenario
        money = starting = 0

        # greedily iterate through all transactions with cost > cashback, in order of cashback size
        # this will ensure that the largest amount of starting money is needed.
        # sorting by (cost - cashback) may seen intuitive, however this means a transaction like
        # [100_000_000, 100_000_000] is performed first, though it would be least optimal to perform
        # it as the last negative value operation
        ls = sorted((t for t in transactions if t[0] > t[1]), key=lambda x: x[1])
        for cost, cash in ls:
            # if it costs more than current money availible, add cost - money to starting money
            if cost > money:
                starting += cost - money
                money = cost
            # subtract cost from current money
            money += cash - cost

        # calculate extra money needed for most expensive cost<=cashback transaction
        needed_for_positive = max(0, max((cost for cost, cash in transactions if cost <= cash), default=0) - money)
        return starting + needed_for_positive
