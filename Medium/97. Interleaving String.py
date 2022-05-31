from typing import List, Set, Tuple


class Solution:
    """
    Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
    An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:
        s = s1 + s2 + ... + sn
        t = t1 + t2 + ... + tm
        |n - m| <= 1
        The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
        Note: a + b is the concatenation of strings a and b
    Constraints:
        0 <= s1.length, s2.length <= 100
        0 <= s3.length <= 200
        s1, s2, and s3 consist of lowercase English letters.
    """

    def isInterleave(self, s1, s2, s3):
        n1, n2, n3 = len(s1), len(s2), len(s3)
        # if lengths differ, can not be interleave
        if n1 + n2 != n3:
            return False
        # stack of states where entry (i, j) means s1[:i] and s2[:j] can successfully interleave to make s3[:i+j]
        # i.e s1[i] and s2[j] next letters to be used
        stack: List[Tuple[int, int]] = [(0, 0)]

        # set of states where entry (i, j) s1[:i] and s2[:j] interleaving has been visited
        visited: Set[Tuple[int, int]] = set(stack)

        while stack:
            # pop i, j from stack
            i, j = stack.pop()
            # calculate next index in s3
            k = i + j
            # if equal to length, return true
            if k == n3:
                return True

            # if letters left in s1, and next letter in s1 matches s3
            if i < n1 and s1[i] == s3[k]:
                # for next_state increase i by one
                next_state = (i + 1, j)
                # if state has not been visited, add it to the stack and visited set
                if not (next_state in visited):
                    stack.append(next_state)
                    visited.add(next_state)

            # identical procedure for s2
            if j < n2 and s2[j] == s3[k]:
                next_state = (i, j + 1)
                if not (next_state in visited):
                    stack.append(next_state)
                    visited.add(next_state)

        # if interleaving not found by DFS, return false
        return False

    def isInterleave1(self, s1, s2, s3):
        n1, n2, n3 = len(s1), len(s2), len(s3)
        # if lengths differ return false
        if n1+n2 != n3:
            return False

        # dp[i][j] to track whether s1[:i] and s2[:j] make an interleaving for s3[:i+j]
        dp = [[True] * (n2+1) for _ in range(n1+1)]

        # initialize first row and column, values remain true if s1[i]==s3[i] and s2[j]==s3[j] respectively
        for i in range(1, n1+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, n2+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        # dp[i][j] can be reached if any direct predecessor can be reach and next letter matches
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                # dp[i][j] =    (s3_interleavable_with_s1[:i-1]_and_s[:j] and s1[i]_matches_s3[i+j]) or
                #               (s3_interleavable_with_s1[:i]_and_s[:j-1] and s2[j]_matches_s3[i+j])
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or (dp[i][j-1] and s2[j-1] == s3[i-1+j])
        return dp[-1][-1]
