"""
Given a string s, return the length of the longest substring between two equal
characters, excluding the two characters. If there is no such substring return
-1.

A substring is a contiguous sequence of characters within a string.

Constraints:
- 1 <= s.length <= 300
- s contains only lowercase English letters.
"""
from collections import defaultdict


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """
        O(n) / O(n)     time / space complexity
        """
        positions: defaultdict[str, list[int]] = defaultdict(list)
        for i, c in enumerate(s):
            positions[c].append(i)

        if len(positions) == len(s):
            return -1

        return max(poss[-1] - poss[0] for poss in positions.values()) - 1
