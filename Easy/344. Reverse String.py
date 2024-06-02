"""
Write a function that reverses a string. The input string is given as an array
of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Constraints:
- 1 <= s.length <= 10^5
- s[i] is a printable ascii character.
"""


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        O(n) / O(1)     time / space complexity
        """
        # s.reverse() in long form:
        for i in range(len(s) // 2):
            temp = s[i]
            s[i] = s[-(i + 1)]
            s[-(i + 1)] = temp
