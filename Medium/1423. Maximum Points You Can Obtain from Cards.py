from typing import List


class Solution:
    """
    There are several cards arranged in a row, and each card has an associated number of points.
    The points are given in the integer array cardPoints.
    In one step, you can take one card from the beginning or from the end of the row. You have
    to take exactly k cards.
    Your score is the sum of the points of the cards you have taken.
    Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
    Constraints:
        1 <= cardPoints.length <= 10^5
        1 <= cardPoints[i] <= 10^4
        1 <= k <= cardPoints.length
    """

    def maxScore(self, card_points: List[int], k: int) -> int:
        """
        Greedily take all cards from left, and then gradually replace with cards from the right.
        Time: O(k), Space: O(1)
        """

        # current sum of taking k cards from ends
        s = sum(card_points[i] for i in range(k))

        # result variable
        res = s

        # diff == cards to take from right
        for cards_to_take_from_right in range(1, k+1):
            # replace right most card from left side, with one further card from right side
            s += card_points[-cards_to_take_from_right] - card_points[k-cards_to_take_from_right]

            # update res if required
            if s > res:
                res = s

        return res
