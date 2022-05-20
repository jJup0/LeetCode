class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        factorials = [1 for _ in range(m+n)]
        for i in range(1, len(factorials)):
            factorials[i] = factorials[i-1] * i
        return int(factorials[m+n-2]/(factorials[m-1]*factorials[n-1]))
