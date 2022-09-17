from typing import List


class Solution:
    """
    You are given a 0-indexed integer array players, where players[i] represents the ability of the
    ith player. You are also given a 0-indexed integer array trainers, where trainers[j] represents
    the training capacity of the jth trainer.
    The ith player can match with the jth trainer if the player's ability is less than or equal to
    the trainer's training capacity. Additionally, the ith player can be matched with at most one
    trainer, and the jth trainer can be matched with at most one player.
    Return the maximum number of matchings between players and trainers that satisfy these 
    conditions.
    Constraints:
        1 <= players.length, trainers.length <= 10^5
        1 <= players[i], trainers[j] <= 10^9
    """

    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        """
        Original from contest. Sort player and trainers, greedily match players with lowest trainers.
        O(n * log(n) + m * log(m)) / O(1)   time / space complexity
        """

        # sort player and trainer values
        players.sort()
        trainers.sort()

        # result variable
        res = 0

        # trainer index
        ti = 0

        # go through players in order of lowest ability
        for p in players:
            # match with next highest trainer
            while ti < len(trainers) and trainers[ti] < p:
                ti += 1
            # if no trainer is capable, break
            if ti == len(trainers):
                break
            res += 1
            ti += 1

        return res
