"""
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including
multiplicity.
- For example,"wrr" is a subset of"warrior" but is not a subset of"world".

A string a from words1 is universal if for every string b in words2, b is a
subset of a.

Return an array of all the universal strings in words1. You may return the
answer in any order.

Constraints:
- 1 <= words1.length, words2.length <= 10^4
- 1 <= words1[i].length, words2[i].length <= 10
- words1[i] and words2[i] consist only of lowercase English letters.
- All the strings of words1 are unique.
"""

from collections import Counter


class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        """
        Complexity:
            n := len(word1), m := len(word2), l := max(len(word) for word in words1 + words2)
            Time: O((n + m) * l)
            Space: O((n + m) * l)
        """
        word_2_universals: Counter[str] = Counter()
        for word in words2:
            for c, count in Counter(word).items():
                word_2_universals[c] = max(word_2_universals[c], count)

        # could be optimized, but easily passes tests
        return [word for word in words1 if Counter(word) >= word_2_universals]
