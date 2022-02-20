class Solution:
    def findJudge(self, N: int, trust: [[int]]) -> int:
        trustFactor = [0] * (N+1)
        for elem in trust:
            trustFactor[elem[0]] -= 1  # will cause people who trust other people to not be identified as judge
            trustFactor[elem[1]] += 1
        for i in range(1, N+1):
            if trustFactor[i] == N-1:
                return i
        return -1
