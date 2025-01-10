"""
You are given a 0-indexed string array words.

Let's define a boolean function isPrefixAndSuffix that takes two strings, str1
and str2:
- isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a
  suffix of str2, and false otherwise.

For example, isPrefixAndSuffix("aba","ababa") is true because"aba" is a prefix
of"ababa" and also a suffix, but isPrefixAndSuffix("abc","abcd") is false.

Return an integer denoting the number of index pairs (i, j) such that i < j,
and isPrefixAndSuffix(words[i], words[j]) is true.

Constraints:
- 1 <= words.length <= 50
- 1 <= words[i].length <= 10
- words[i] consists only of lowercase English letters.
"""


class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        """
        High complexity, but test instances are really small.
        See "3045. Count Prefix and Suffix Pairs II.py" for faster implementations.
        m := max(len(word) for word in words)
        Complexity:
            Time: O(n^2 * m)
            Space: O(1)
        """
        res = 0
        for j, word2 in enumerate(words):
            for i in range(j):
                word1 = words[i]
                res += word2.startswith(word1) and word2.endswith(word1)
        return res
