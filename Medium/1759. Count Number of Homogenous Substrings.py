"""
Given a string s, return the number of homogenous substrings of s. Since the
answer may be too large, return it modulo 10^9 + 7.

A string is homogenous if all the characters of the string are the same.

A substring is a contiguous sequence of characters within a string.

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase letters.
"""


class Solution:
    def countHomogenous(self, s: str) -> int:
        """
        O(n) / O(1)     time / space complexity
        """
        MOD = 10**9 + 7
        prev_char = s[0]
        streak = 0
        res = 0
        for c in s:
            if c == prev_char:
                streak += 1
            else:
                res = (res + (streak * (streak + 1)) // 2) % MOD
                prev_char = c
                streak = 1
        return (res + (streak * (streak + 1)) // 2) % MOD
