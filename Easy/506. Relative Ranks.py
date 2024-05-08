"""
You are given an integer array score of size n, where score[i] is the score of
the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has
the highest score, the 2nd place athlete has the 2nd highest score, and so on.
The placement of each athlete determines their rank:
- The 1st place athlete's rank is"Gold Medal".
- The 2nd place athlete's rank is"Silver Medal".
- The 3rd place athlete's rank is"Bronze Medal".
- For the 4th place to the nth place athlete, their rank is their placement
  number (i.e., the xth place athlete's rank is"x" ).

Return an array answer of size n where answer[i] is the rank of the ith athlete.

Constraints:
- n == score.length
- 1 <= n <= 10^4
- 0 <= score[i] <= 10^6
- All the values in score are unique.
"""


class Solution:
    def findRelativeRanks(self, scores: list[int]) -> list[str]:
        """
        O(n) / O(n * log(n))    time / space complexity
        """
        score_idxs = sorted((score, i) for i, score in enumerate(scores))
        player_count = len(scores)
        res = [""] * player_count
        for i, (_score, player_idx) in enumerate(score_idxs):
            res[player_idx] = str(player_count - i)

        if player_count >= 3:
            res[score_idxs[-3][1]] = "Bronze Medal"
        if player_count >= 2:
            res[score_idxs[-2][1]] = "Silver Medal"
        res[score_idxs[-1][1]] = "Gold Medal"
        return res
