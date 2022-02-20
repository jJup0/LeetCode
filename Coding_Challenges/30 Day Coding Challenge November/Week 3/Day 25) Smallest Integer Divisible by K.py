class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if not (K % 2 and K % 5):
            return -1
        currMod = 0
        for l in range(1, K+1):
            currMod = (currMod*10+1) % K
            if not currMod:
                return l
