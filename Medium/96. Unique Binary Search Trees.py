class Solution:
    def numTrees(self, n: int) -> int:

        # # Brute Force:
        # if n <= 1:
        #     return 1
        # # choose i as node, find numTrees of left child * numTrees of right child.
        # # left contains nodes 1..i-1, right: i+1..n, note i+1..n has same numTrees as 1..n-i
        # return sum(self.numTrees(i-1) * self.numTrees(n-i) for i in range(1, n+1))

        # # Dynamic Programming
        # # same as Brute force, just remember results. numTrees(0) := 1
        # nTrees = [1] + [0] * n
        # for i in range(1, n + 1):   # i is number of nodes
        #     for j in range(i):   # j is idx of chosen root
        #         nTrees[i] += nTrees[j] * nTrees[i - j - 1]
        # return nTrees[n]

        # Catalan Numbers
        # numTrees produces a series known as the catalan numbers.
        # C_n = (1/(n+1)) * (2n choose n)  == (2n!)/((n+1)!n!)
        # Can compute directly, python has native bigint, speed is negligible
        fac = [1]*(2*n + 1)
        for i in range(2, len(fac)):
            fac[i] = i * fac[i-1]
        return fac[2*n] // (fac[n+1] * fac[n])
