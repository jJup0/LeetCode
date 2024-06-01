"""
You are given a string s. The score of a string is defined as the sum of the
absolute difference between the ASCII values of adjacent characters.

Return the score of s.

Constraints:
- 2 <= s.length <= 100
- s consists only of lowercase English letters.
"""


class Solution:
    def scoreOfString(self, s: str) -> int:
        """
        O(n) / O(1)     time / space complexity
        """
        # make iterator which is one character ahead
        iter_curr = iter(s)
        next(iter_curr)
        # sum of absolute differences of neighboring letters
        return sum(abs(ord(prev) - ord(curr)) for prev, curr in zip(s, iter_curr))
