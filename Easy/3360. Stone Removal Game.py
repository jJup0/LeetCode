"""
Alice and Bob are playing a game where they take turns removing stones from a
pile, with Alice going first.
- Alice starts by removing exactly 10 stones on her first turn.
- For each subsequent turn, each player removes exactly 1 fewerstonethan the
  previous opponent.

The player who cannot make a move loses the game.

Given a positive integer n, return true if Alice wins the game and false otherwise.

Constraints:
- 1 <= n <= 50
"""


class Solution:
    def canAliceWin(self, n: int) -> bool:
        """
        Complexity:
            Time: O(1)
            Space: O(1)
        """
        alices_turn = True
        rem = n
        for i in range(10, 1, -1):
            if rem >= i:
                rem -= i
            else:
                return not alices_turn
            alices_turn = not alices_turn
        raise Exception(f"n must be smaller than 54, got {n}")
