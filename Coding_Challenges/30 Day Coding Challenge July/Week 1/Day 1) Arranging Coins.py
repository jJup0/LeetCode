class Solution:
    def arrangeCoins(self, n: int) -> int:
        # inverse of triangle rule n(n+1)/2
        return int((2*n+0.25)**0.5-0.5)
