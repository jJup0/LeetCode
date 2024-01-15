"""
You are given an integer array matches where matches[i] = [winner_i, loser_i]
indicates that the player winner_i defeated player loser_i in a match.

Return a list answer of size 2 where:
- answer[0] is a list of all players that have not lost any matches.
- answer[1] is a list of all players that have lost exactly one match.

The values in the two lists should be returned in increasing order.

Note:
- You should only consider the players that have played at least one match.
- The testcases will be generated such that no two matches will have the same
outcome.

Constraints:
- 1 <= matches.length <= 10^5
- matches[i].length == 2
- 1 <= winner_i, loser_i <= 10^5
- winner_i != loser_i
- All matches[i] are unique.
"""


from collections import defaultdict


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        """
        O(n * log(n)) / O(n)    time / space complexity
        """
        # mapping from player to matches lost
        loss_count: dict[int, int] = defaultdict(int)

        for winner, loser in matches:
            # add 0 to winner to ensure winner is in dict
            loss_count[winner] += 0
            loss_count[loser] += 1

        one_loss: list[int] = []
        zero_loss: list[int] = []
        for loser, count in loss_count.items():
            if count == 0:
                zero_loss.append(loser)
            elif count == 1:
                one_loss.append(loser)
        one_loss.sort()
        zero_loss.sort()

        return [zero_loss, one_loss]
