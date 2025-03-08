"""
Given two strings str1 and str2, return the shortest string that has both str1
and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters
from t (possibly 0 ) results in the string s.

Constraints:
- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of lowercase English letters.
"""


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        shortest_dp = self._find_shortest_supersequence(str1, str2)
        return self._backtrack(str1, str2, shortest_dp)

    def _find_shortest_supersequence(self, str1: str, str2: str) -> list[list[int]]:
        """Returns a 2D array `shortest_dp` where shortest_dp[i][j] = len(shortestCommonSuperSequence(str1[:i], str2[:j])).

        Complexity:
            Time: O(n * m)
            Space: O(n * m)
        """
        shortest_dp = [[1_000_000] * (len(str2) + 1) for _ in range(len(str1) + 1)]
        shortest_dp[0] = list(range(len(shortest_dp[0])))
        for i in range(len(str1) + 1):
            shortest_dp[i][0] = i

        for i1, char1 in enumerate(str1, start=1):
            for i2, char2 in enumerate(str2, start=1):
                if char1 == char2:
                    # character is the same, can use it for both strings
                    shortest_dp[i1][i2] = shortest_dp[i1 - 1][i2 - 1] + 1
                else:
                    # do whatever is cheapest:
                    # construct superstring for str1[:i1] and str2[:i2-1], and add str2[i2] or
                    # construct superstring for str1[:i1-1] and str2[:i2], and add str1[i1]
                    shortest_dp[i1][i2] = (
                        min(shortest_dp[i1][i2 - 1], shortest_dp[i1 - 1][i2]) + 1
                    )

        return shortest_dp

    def _backtrack(self, str1: str, str2: str, shortest: list[list[int]]) -> str:
        """Backtrack through the dynamic programming array to construct the shortest supersequence.

        Complexity:
            Time: O(n + m)
            Space: O(n + m)
        """
        i1 = len(str1)
        i2 = len(str2)
        reverse_result: list[str] = []
        while i1 > 0 and i2 > 0:
            char1 = str1[i1 - 1]
            char2 = str2[i2 - 1]
            if char1 == char2:
                reverse_result.append(char1)
                i1 -= 1
                i2 -= 1
            elif shortest[i1][i2 - 1] < shortest[i1 - 1][i2]:
                reverse_result.append(char2)
                i2 -= 1
            else:
                reverse_result.append(char1)
                i1 -= 1

        # append reamining characters like in merge sort
        for i1 in range(i1 - 1, -1, -1):
            reverse_result.append(str1[i1])
        for i2 in range(i2 - 1, -1, -1):
            reverse_result.append(str2[i2])
        return "".join(reversed(reverse_result))
