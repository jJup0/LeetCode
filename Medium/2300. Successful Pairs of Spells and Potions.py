import bisect


class Solution:
    """
    You are given two positive integer arrays spells and potions, of length n and m
    respectively, where spells[i] represents the strength of the ith spell and
    potions[j] represents the strength of the jth potion.

    You are also given an integer success. A spell and potion pair is considered
    successful if the product of their strengths is at least success.

    Return an integer array pairs of length n where pairs[i] is the number of potions
    that will form a successful pair with the ith spell.

    Constraints:
        n == spells.length
        m == potions.length
        1 <= n, m <= 10^5
        1 <= spells[i], potions[i] <= 10^5
        1 <= success <= 10^10
    """

    def successfulPairs(
        self, spells: list[int], potions: list[int], success: int
    ) -> list[int]:
        """
        Sort potions in order to binary search the index of
        the weakest potion still compatible with the spell.
        O((m + n)*log(m)) / O(1)    time / (extra) space complexity
        """
        potions.sort()
        pairs = []
        for spell in spells:
            # potion needs to have power of at least success * spell
            potion_power_needed = success / spell

            # binary search power needed in potions
            idx = bisect.bisect_left(potions, potion_power_needed)

            # all potions up until idx can be paired with spell
            pairs.append(len(potions) - idx)

        return pairs
