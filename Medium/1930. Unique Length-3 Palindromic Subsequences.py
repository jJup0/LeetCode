"""
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

Constraints:
- 3 <= s.length <= 10%5
- s consists of only lowercase English letters.
"""


import bisect
from collections import defaultdict


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        return self.countPalindromicSubsequence_faster(s)

    def countPalindromicSubsequence_og(self, s: str) -> int:
        """
        O(len(set(s)) * len(s))
        """
        chars_to_idxs: defaultdict[str, list[int]] = defaultdict(list)
        for i, c in enumerate(s):
            chars_to_idxs[c].append(i)

        res = 0
        for c, idxs in chars_to_idxs.items():
            start = idxs[0] + 1
            end = idxs[-1]
            res += len(set(s[start:end]))
        return res

    def countPalindromicSubsequence_faster(self, s: str) -> int:
        """
        O(len(s) + len(set(s))^2 * log(len(s)))
        """
        chars_to_idxs: defaultdict[str, list[int]] = defaultdict(list)
        for curr_idxs, char in enumerate(s):
            chars_to_idxs[char].append(curr_idxs)

        res = 0
        for char, curr_idxs in chars_to_idxs.items():
            if len(curr_idxs) < 2:
                continue
            if len(curr_idxs) > 2:
                res += 1
            for other_char, other_idxs in chars_to_idxs.items():
                if char == other_char:
                    continue
                if bisect.bisect(other_idxs, curr_idxs[0]) < bisect.bisect(
                    other_idxs, curr_idxs[-1]
                ):
                    res += 1
        return res
