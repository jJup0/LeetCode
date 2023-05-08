class Solution:
    """
        In the world of Dota2, there are two parties: the Radiant and the Dire.

    The Dota2 senate consists of senators coming from two parties. Now the Senate wants to
    decide on a change in the Dota2 game. The voting for this change is a round-based
    procedure. In each round, each senator can exercise one of the two rights:

        Ban one senator's right: A senator can make another senator lose all his rights
          in this and all the following rounds.
        Announce the victory: If this senator found the senators who still have rights to
          vote are all from the same party, he can announce the victory and decide on the
          change in the game.

    Given a string senate representing each senator's party belonging. The character 'R'
    and 'D' represent the Radiant party and the Dire party. Then if there are n senators,
    the size of the given string will be n.

    The round-based procedure starts from the first senator to the last senator in the
    given order. This procedure will last until the end of voting. All the senators who
    have lost their rights will be skipped during the procedure.

    Suppose every senator is smart enough and will play the best strategy for his own
    party. Predict which party will finally announce the victory and change the Dota2
    game. The output should be "Radiant" or "Dire".

    Constraints:
        n == senate.length
        1 <= n <= 104
        senate[i] is either 'R' or 'D'.
    """

    def predictPartyVictory(self, senate: str) -> str:
        """
        O(n * log(n)) / O(n)    time / space complexity
        """
        senate_l = list(senate)
        remaining_radiant_count = senate.count("R")
        remaining_dire_count = len(senate) - remaining_radiant_count

        # count of radiant senators yet to lose their rights when its their turn
        lrr_rem = 0
        # count of dire senators yet to lose their rights when its their turn
        lrd_rem = 0
        while True:
            for i, c in enumerate(senate_l):
                if c == "R":
                    if lrr_rem > 0:
                        # optimally, this radiant would have his
                        # rights excluded by previous vote of a dire
                        lrr_rem -= 1
                        senate_l[i] = " "
                    else:
                        # ban the next dire senator's rights
                        lrd_rem += 1
                        remaining_dire_count -= 1
                elif c == "D":
                    # analogous to radiant case
                    if lrd_rem > 0:
                        lrd_rem -= 1
                        senate_l[i] = " "
                    else:
                        lrr_rem += 1
                        remaining_radiant_count -= 1
                # else: voted out senator, has no effect
            # if one of the two parties has been completely banned, the other wins
            if remaining_dire_count < 0:
                return "Radiant"
            if remaining_radiant_count < 0:
                return "Dire"
