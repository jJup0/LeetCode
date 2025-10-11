"""
A magician has various spells.

You are given an array power, where each element represents the damage of a
spell. Multiple spells can have the same damage value.

It is a known fact that if a magician decides to cast a spell with a damage of
power[i], they cannot cast any spell with a damage of power[i] - 2,
power[i] - 1, power[i] + 1, or power[i] + 2.

Each spell can be cast only once.

Return the maximum possible total damage that a magician can cast.

Constraints:
- 1 <= power.length <= 10^5
- 1 <= power[i] <= 10^9
"""

from collections import Counter


class Solution:
    def maximumTotalDamage(self, powers: list[int]) -> int:
        """
        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        # spells of the same power can be used together, create a counter to
        # make this easier to handle and sort to easily get power-level neighbors
        spell_counter = sorted(Counter(powers).items())
        # dp[i] = highest possible total power for using the first i+1 spells
        dp = [0] * (len(spell_counter))
        for i, (power, count) in enumerate(spell_counter):
            total_power_for_spell = power * count
            # initial total power for i is previous total power, or only using this spell
            dp[i] = max(dp[i - 1], count * power)
            if i > 0 and spell_counter[i - 1][0] < power - 2:
                # previous spell is compatible
                dp[i] = dp[i - 1] + total_power_for_spell
            elif i > 1 and spell_counter[i - 2][0] < power - 2:
                # spell before previous is compatible
                dp[i] = max(dp[i], dp[i - 2] + total_power_for_spell)
            elif i > 2:
                # two previous spells levels are not compatible
                dp[i] = max(dp[i], dp[i - 3] + total_power_for_spell)
        return dp[-1]


def test():
    powers = [1, 1, 3, 4]
    res = Solution().maximumTotalDamage(powers)
    assert res == 6
