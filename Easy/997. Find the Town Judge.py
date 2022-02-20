from typing import List
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        isTrustedMoreThanTrusts = [0]*(N+1)
        for trusts, isTrusted in trust:
            isTrustedMoreThanTrusts[trusts] -= 1
            isTrustedMoreThanTrusts[isTrusted] += 1
        for i in range(1, N+1):
            if isTrustedMoreThanTrusts[i] == N-1:
                return i
        return -1