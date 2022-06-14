class Solution:
    """
    Given two strings word1 and word2, return the minimum number of steps
    required to make word1 and word2 the same.
    In one step, you can delete exactly one character in either string.
    Constraints:
        1 <= word1.length, word2.length <= 500
        word1 and word2 consist of only lowercase English letters.
    """

    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        # dp[i][j] stores minimum deletions needed to make word1[:i] and word2[:j] equal
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        # iterate through all substrings
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                # if either i == 0 or j == 0, then one of the substrings is equal to "", so
                # deletions necessary is length of other substring
                if (not i) or (not j):
                    dp[i][j] = i + j
                else:
                    # if characters are equal, no need to delete, so take value from dp[i-1][j-1]
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        # if characters are unequal, take smallest value from either previous step
                        # and add 1 for 1 more deletion
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

        # return dp for word1[:n1] and word2[:n2]
        return dp[n1][n2]
