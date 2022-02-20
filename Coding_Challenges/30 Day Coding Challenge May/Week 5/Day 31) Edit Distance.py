class copiedSolution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)  # switch word1 and word2 if m < n to ensure n ≤ m
        curr = list(range(n+1))
        for i in range(m):
            prev, curr = curr, [i+1] + [0] * n
            for j in range(n):
                curr[j+1] = prev[j] if word1[i] == word2[j] else min(curr[j], prev[j], prev[j+1]) + 1
        return curr[n]
