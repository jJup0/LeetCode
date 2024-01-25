"""
Given two strings text1 and text2, return the length of their longest common
subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string
with some characters (can be none) deleted without changing the relative order
of the remaining characters.
- For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both
strings.

Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        O(n * m) / O(n + m)     time / space complexity
        """
        # prev[j] = max subsequence of text1[:i] and text2[:j]
        prev = [0] * (len(text2) + 1)
        for char1 in text1:
            # curr[j] = max subsequence of text1[:i+1] and text2[:j]
            curr = [0] * (len(text2) + 1)
            for j, char2 in enumerate(text2):
                if char1 == char2:
                    # if the characters are the same, subsequence length is one more than for previous character
                    curr[j + 1] = prev[j] + 1
                else:
                    # store max subsequence of (text1[:i], text2[:j+1]) and (text1[:i+1], text2[:j])
                    curr[j + 1] = max(prev[j + 1], curr[j])
            prev = curr

        return prev[-1]
