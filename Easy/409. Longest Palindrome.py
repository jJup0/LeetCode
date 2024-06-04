"""
Given a string s which consists of lowercase or uppercase letters, return the
length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example,"Aa" is not considered a palindrome.

Constraints:
- 1 <= s.length <= 2000
- s consists of lowercase and/or uppercase English letters only.
"""

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        O(n) / O(n)     time / space complexity
        """
        counts = Counter(s).values()
        # sum up length of identical letters with a pair
        res = sum((count // 2) * 2 for count in counts)
        # if any letter appears an odd number of times it can be
        # use as the middle letter of the palindrome
        single_letter = any(c & 1 for c in counts)
        return res + single_letter
