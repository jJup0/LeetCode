"""
There are 3n piles of coins of varying size, you and your friends
will take piles of coins as follows:
- In each step, you will choose any 3 piles of coins
  (not necessarily consecutive).
- Of your choice, Alice will pick the pile with the maximum number of coins.
- You will pick the next pile with the maximum number of coins.
- Your friend Bob will pick the last pile.
- Repeat until there are no more piles of coins.

Given an array of integers piles where piles[i] is the number of coins
in the ith pile.

Return the maximum number of coins that you can have.

Constraints:
- 3 <= piles.length <= 10^5
- piles.length % 3 == 0
- 1 <= piles[i] <= 10^4
"""


class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        """
        Pick two the two largest and the smallest remaining pile to maximize total coins.
        O(n*log(n)) / O(1)      time / space
        """
        n = len(piles)
        piles.sort()
        return sum(piles[i] for i in range(n // 3, n, 2))
