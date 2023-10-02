class Solution:
    """
    There are n pieces arranged in a line, and each piece is colored either by
    'A' or by 'B'. You are given a string colors of length n where colors[i] is
    the color of the ith piece.

    Alice and Bob are playing a game where they take alternating turns removing
    pieces from the line. In this game, Alice moves first.

    - Alice is only allowed to remove a piece colored 'A' if both its neighbors
      are also colored 'A'. She is not allowed to remove pieces that are colored
      'B'.
    - Bob is only allowed to remove a piece colored 'B' if both its neighbors are
      also colored 'B'. He is not allowed to remove pieces that are colored 'A'.
    - Alice and Bob cannot remove pieces from the edge of the line.
    - If a player cannot make a move on their turn, that player loses and the
      other player wins.

    Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.
    """

    def winnerOfGame(self, colors: str) -> bool:
        """
        There is not "optimal" way to play, just pick pieces as long as
        possible. Scores easily determined by finding streaks of letters
        longer than 2.
        O(n) / O(1)     time / space complexity
        """

        def evaluate_streak():
            nonlocal streak_count, prev_c, points_alice, points_bob
            if streak_count >= 3:
                points = streak_count - 2
                if prev_c == "A":
                    points_alice += points
                else:
                    points_bob += points
            prev_c = c
            streak_count = 1

        # initialize points of both players to zero
        points_alice = points_bob = 0
        # pseudo intialize previous piece color to color of first piece, but
        # set prev_count to 0
        prev_c = colors[0]
        streak_count = 0
        for c in colors:
            if c == prev_c:
                streak_count += 1
            else:
                evaluate_streak()
        evaluate_streak()

        # alice must have strictly more points to win, since she plays first,
        # and has "no more moves" left first if they have equal points
        return points_alice > points_bob
