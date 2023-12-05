"""
You are given an integer n, the number of teams in a tournament that has strange rules:
- If the current number of teams is even, each team gets paired with another
  team. A total of n / 2 matches are played, and n / 2 teams advance to the
  next round.
- If the current number of teams is odd, one team randomly advances in the
  tournament, and the rest gets paired. A total of (n - 1) / 2 matches are
  played, and (n - 1) / 2 + 1 teams advance to the next round.

Return the number of matches played in the tournament until a winner is decided.

Constraints:
- 1 <= n <= 200
"""


class Solution:
    def numberOfMatches(self, n: int) -> int:
        return self.numberOfMatches_math(n)

    def numberOfMatches_math(self, n: int) -> int:
        # n-1 teams need to be eliminated to find a winner, so n-1 matches must be played
        return n - 1

    def numberOfMatches_simulation(self, n: int) -> int:
        res = 0
        while n > 1:
            if n & 1:
                res += (n - 1) // 2
                n = (n - 1) // 2 + 1
            else:
                res += n // 2
                n = n // 2
        return res
