"""
Given two strings s and t, return the number of distinctsubsequences of s which
equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

Constraints:
- 1 <= s.length, t.length <= 1000
- s and t consist of English letters.
"""

from collections import defaultdict


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        Complexity:
            Time: O(s * t)
            Space: O(t)
        """
        # mapping from charact to indexes in t
        char_indexs_t: dict[str, list[int]] = defaultdict(list)
        for i, c_t in enumerate(t):
            char_indexs_t[c_t].append(i)

        # ways to construct t[:i]
        construct_ways = [0] * (len(t) + 1)
        construct_ways[0] = 1

        for char_in_s in s:
            # iterate through all occurances of character in t and sum up ways
            # iterate in reversed order to avoid bug where one character is used multiple times
            for idx in reversed(char_indexs_t[char_in_s]):
                construct_ways[idx + 1] += construct_ways[idx]
        return construct_ways[-1]
