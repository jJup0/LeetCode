"""
You are given two strings s and t consisting of only lowercase English letters.

Return the minimum number of characters that need to be appended to the end of
s so that t becomes a subsequence of s.

A subsequence is a string that can be derived from another string by deleting
some or no characters without changing the order of the remaining characters.

Constraints:
- 1 <= s.length, t.length <= 10^5
- s and t consist only of lowercase English letters.
"""


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """
        O(n) / O(1)     time / space complexity
        """
        t_i = 0
        for c in s:
            if c == t[t_i]:
                t_i += 1
                if t_i == len(t):
                    break
        return len(t) - t_i
