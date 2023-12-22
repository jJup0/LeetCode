"""
Given a string s of zeros and ones, return the maximum score after splitting
the string into two non-empty substrings (i.e. left substring and right
substring).

The score after splitting a string is the number of zeros in the left substring
plus the number of ones in the right substring.

Constraints:
- 2 <= s.length <= 500
- The string s consists of characters '0' and '1' only.
"""


class Solution:
    def maxScore(self, s: str) -> int:
        """
        O(n) / O(1)     time / space complexity
        """
        score = s.count("1")
        res = score - 1
        for i in range(len(s) - 1):
            if s[i] == "1":
                score -= 1
            else:
                score += 1
                res = max(res, score)
        return res
