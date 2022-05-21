from typing import List


class Solution:
    """
    You are given an integer array coins representing coins of different denominations and an
    integer amount representing a total amount of money.
    Return the fewest number of coins that you need to make up that amount. If that amount of
    money cannot be made up by any combination of the coins, return -1.
    You may assume that you have an infinite number of each kind of coin.
    Constraints:
        1 <= coins.length <= 12
        1 <= coins[i] <= 2^31 - 1
        0 <= amount <= 10^4
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        # bitmap of amounts reachable by subtracting coins, at start only amount is reachable
        reachable = 1 << amount

        for res in range(amount + 1):
            # 1 is the same as 1 << 0, so if 1 << 0 is set in bitmap, it means 0 can be reached
            # by subtracting coins from the original amount so return steps taken
            if reachable & 1:
                return res

            # calculate all new reachable positions from current reachable
            next_reachable = reachable
            for coin in coins:
                next_reachable |= (reachable >> coin)

            # if new reachable is same as before, and 0 has not been reached, will not be able to reach 0
            if next_reachable == reachable:
                break

            # update reachable
            reachable = next_reachable

        return -1


# class SlowerSolutions:
#     def coinChangeSlowest(self, coins: List[int], amount: int) -> int:
#         coins = sorted(set(coins))
#         largest_coin = coins[-1]
#         front = set([0])
#         rounds = 0

#         while front:
#             if amount in front:
#                 return rounds
#             else:
#                 front = set(prev + c for prev in front for c in coins if prev + c <= amount)
#             rounds += 1
#         return -1

#     def coinChangeSlower(self, coins: List[int], amount: int) -> int:

#         coins = sorted(set(coins))
#         largest_coin = coins[-1]
#         front: List[Tuple[int, int, int]] = [(amount, 0, 0)]

#         dp = [amount + 1] * (amount + 1)

#         def key(coins_used, total):
#             return coins_used + (amount - total)//largest_coin

#         while front:
#             _, coins_used, total = heapq.heappop(front)

#             if coins_used >= dp[total]:
#                 continue

#             dp[total] = coins_used

#             if total == amount:
#                 return coins_used

#             coins_used_inc = coins_used + 1
#             for c in coins:
#                 new_total = c + total
#                 if new_total > amount:
#                     break
#                 heapq.heappush(front, (key(coins_used_inc, new_total), coins_used_inc, new_total))

#         return -1

#     def coinChangeSlow(self, coins: List[int], amount: int) -> int:

#         dp = [amount + 1] * (amount + 1)
#         coins = sorted(set(coins), reverse=True)

#         def helper(total, coins_used, coins_start_idx):
#             if coins_used >= dp[total] or coins_used >= dp[-1]:
#                 return

#             dp[total] = coins_used
#             for c in coins[coins_start_idx:]:
#                 new_total = c + total
#                 if new_total <= amount:
#                     helper(new_total, coins_used + 1, coins_start_idx)
#                 else:
#                     coins_start_idx += 1

#         helper(0, 0, 0)

#         if dp[-1] == amount + 1:
#             return -1
#         else:
#             return dp[-1]
