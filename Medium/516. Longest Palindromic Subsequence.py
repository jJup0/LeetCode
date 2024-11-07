"""
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by
deleting some or no elements without changing the order of the remaining elements.

Constraints:
- 1 <= s.length <= 1000
- s consists only of lowercase English letters.
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        Returns the length of the longest palindrome in a subsequence of s[i:j+1]
        Complexity:
            Time: O(n^2)
            Space: O(n^2)
        """
        self.s = s
        self.dp = [[-1] * len(s) for _ in range(len(s))]
        return self._longest_palindrome(0, len(s) - 1)

    def _longest_palindrome(self, i: int, j: int) -> int:
        """
        Returns the length of the longest palindrome in a subsequence of s[i:j+1]
        """
        if i == j:
            # single character (palindrome of length 1)
            return 1
        if i > j:
            # empty string
            return 0

        if self.dp[i][j] == -1:
            if self.s[i] == self.s[j]:
                # use two s[i] and s[j] as outside characters for palindrome
                self.dp[i][j] = 2 + self._longest_palindrome(i + 1, j - 1)
            else:
                # get maximum of skipping first or last letter in
                # constructing subsequence palindrome
                self.dp[i][j] = max(
                    self._longest_palindrome(i + 1, j),
                    self._longest_palindrome(i, j - 1),
                )
        return self.dp[i][j]
