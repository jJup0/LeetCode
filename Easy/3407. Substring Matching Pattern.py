"""
You are given a string s and a pattern string p, where p contains exactly
one'*' character.

The'*' in p can be replaced with any sequence of zero or more characters.

Return true if p can be made a substring of s, and false otherwise.

A substring is a contiguous non-empty sequence of characters within a string.

Constraints:
- 1 <= s.length <= 50
- 1 <= p.length <= 50
- s contains only lowercase English letters.
- p contains only lowercase English letters and exactly one'*'
"""


class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        """
        Complexity:
            Time: O(n + m)
            Space: O(m)
        """
        s1, s2 = p.split("*")
        idx1 = s.find(s1)
        if idx1 == -1:
            return False
        idx2 = s.find(s2, idx1 + len(s1))
        if idx2 == -1:
            return False
        return True
