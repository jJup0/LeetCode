"""
A fancy string is a string where no threeconsecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to
make it fancy.

Return the final string after the deletion. It can be shown that the answer
will always be unique.

Constraints:
- 1 <= s.length <= 10^5
- s consists only of lowercase English letters.
"""


class Solution:
    def makeFancyString(self, s: str) -> str:
        """
        O(n) / O(n)     time / space
        """
        prev = s[0]
        streak = 0
        res: list[str] = []
        for c in s:
            if c == prev:
                streak += 1
            else:
                streak = 1
            if streak < 3:
                res.append(c)
            prev = c
        return "".join(res)
