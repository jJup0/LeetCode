from functools import cache


class Solution:
    """
    You are given an integer array coins representing coins of different
    denominations and an integer amount representing a total amount of money.

    Return the number of combinations that make up that amount. If that amount
    of money cannot be made up by any combination of the coins, return 0.

    You may assume that you have an infinite number of each kind of coin.

    The answer is guaranteed to fit into a signed 32-bit integer.

    Constraints:
    - 1 <= coins.length <= 300
    - 1 <= coins[i] <= 5000
    - All the values of coins are unique.
    - 0 <= amount <= 5000
    """

    def change(self, amount: int, coins: list[int]) -> int:
        """
        Dynamic programming approach.
        O(amount * len(coins)) / O(amount * len(coins))
        """

        @cache
        def helper(amount: int, coins_idx: int) -> int:
            if amount == 0:
                return 1

            curr_coin = self.coins[coins_idx]
            if coins_idx == 0:
                return int(amount % curr_coin == 0)

            return sum(
                helper(prev_amount, coins_idx - 1)
                for prev_amount in range(amount, -1, -curr_coin)
            )

        self.coins = sorted(coins)
        return helper(amount, len(coins) - 1)
