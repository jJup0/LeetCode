"""
You are given two strings of the same length s and t. In one step you can
choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a
different (or the same) ordering.

Constraints:
- 1 <= s.length <= 5 * 10^4
- s.length == t.length
- s and t consist of lowercase English letters only.
"""
from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return self.minSteps_oneline(s, t)

    def minSteps1(self, s: str, t: str) -> int:
        """
        Intuition: surplus characters in t, i.e. characters of which there are
        higher counts in t than in s, do not need to be counted, as they can be
        removed and replaced with missing/needed characters in one step.
        O(n) / O(n)     time / space complexity
        """
        cs = Counter(s)
        ct = Counter(t)
        return sum(
            max(0, count - ct[character])  # only sum up missing characters
            for character, count in cs.items()
        )

    # taking either difference works
    # in the "normal" logic sum up all characters that are not needed in t, and convert them
    # in the "reverse" logic, sum up all characters in s which do not exist in t
    #   since we do not have to find out which characters to convert in t, the reverse logic also works
    def minSteps_oneline(self, s: str, t: str) -> int:
        # "-" only keeps positive values
        return sum((Counter(s) - Counter(t)).values())

    def minSteps_reverse_logic_oneline(self, s: str, t: str) -> int:
        # "-" only keeps positive values
        return sum((Counter(t) - Counter(s)).values())
