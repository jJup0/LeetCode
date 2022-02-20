class Solution:
    def numTrees(self, n: int) -> int:
        count = [1] + [0] * n

        for i in range(1, n + 1):
            for j in range(0, i):
                count[i] += count[j] * count[i - j - 1]

        return count[n]
