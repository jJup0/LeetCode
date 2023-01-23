class Solution:
    """
    In a town, there are n people labeled from 1 to n. There is a rumor that one of these people
    is secretly the town judge.

    If the town judge exists, then:

    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.
    You are given an array trust where trust[i] = [ai, bi] representing that the person labeled
    ai trusts the person labeled bi.

    Return the label of the town judge if the town judge exists and can be identified, or return
    -1 otherwise.
    """

    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        """
        Everybody trusts town judge, town judge trusts nobody =>
        only the judge is trusted by n-1 more people than they trust.

        O(len(trust)) / O(n)    time / space complexity
        """

        is_trusted_minus_trusts = [0]*(n+1)
        for trusts, isTrusted in trust:
            is_trusted_minus_trusts[trusts] -= 1
            is_trusted_minus_trusts[isTrusted] += 1

        # people enumeration start at 1
        for i in range(1, n+1):
            if is_trusted_minus_trusts[i] == n-1:
                return i
        return -1
