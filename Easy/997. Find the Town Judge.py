"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of
these people is secretly the town judge.

If the town judge exists, then:

You are given an array trust where trust[i] = [a_i, b_i] representing that the
person labeled a_i trusts the person labeled b_i. If a trust relationship does
not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be
identified, or return -1 otherwise.

Constraints:
- 1 <= n <= 1000
- 0 <= trust.length <= 10^4
- trust[i].length == 2
- All the pairs of trust are unique.
- a_i != b_i
- 1 <= a_i, b_i <= n
"""


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        """
        Everybody trusts town judge, town judge trusts nobody =>
        only the judge is trusted by n-1 more people than they trust.

        O(len(trust)) / O(n)    time / space complexity
        """
        if n == 1:
            # edge case needs to be handled separately
            return 1

        is_trusted_minus_trusts = [0] * (n + 1)
        for trusts, isTrusted in trust:
            is_trusted_minus_trusts[trusts] -= 1
            is_trusted_minus_trusts[isTrusted] += 1

        # people enumeration start at 1
        for i, trust_diff in enumerate(is_trusted_minus_trusts):
            if trust_diff == n - 1:
                return i
        return -1
