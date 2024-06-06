"""
Alice has some number of cards and she wants to rearrange the cards into groups
so that each group is of size groupSize, and consists of groupSize consecutive
cards.

Given an integer array hand where hand[i] is the value written on the ith card
and an integer groupSize, return true if she can rearrange the cards, or false
otherwise.

Constraints:
- 1 <= hand.length <= 10^4
- 0 <= hand[i] <= 10^9
- 1 <= groupSize <= hand.length
"""

from collections import Counter


class Solution:
    def isNStraightHand(self, hand: list[int], group_size: int) -> bool:
        """
        Greedily form groups with smallest unused card as the lowest card in the group.
        O(n * log(n)) / O(n)    time / space complexity
        """
        if len(hand) % group_size:
            return False

        c = Counter(hand)
        for val in sorted(c.keys()):
            count = c[val]
            if not count:
                # skip value, all cards used up by previous groups
                continue
            # form groups with this card's value as the lowest card
            for group_val in range(val + 1, val + group_size):
                if c[group_val] < count:
                    # no matching cards
                    return False
                # virtually add cards to group by removing them from the counter
                c[group_val] -= count
        # all cards formed groups
        return True
