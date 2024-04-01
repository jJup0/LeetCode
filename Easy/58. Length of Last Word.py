"""
Given a string s consisting of words and spaces, return the length of the last
word in the string.

A word is a maximal substring consisting of non-space characters only.

Constraints:
- 1 <= s.length <= 10^4
- s consists of only English letters and spaces ' '.
- There will be at least one word in s.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        O(n) / O(1)     time / space complexity
        """
        i = len(s) - 1
        while s[i] == " ":
            i -= 1
        word_end = i
        while i >= 0 and s[i] != " ":
            i -= 1
        return word_end - i
