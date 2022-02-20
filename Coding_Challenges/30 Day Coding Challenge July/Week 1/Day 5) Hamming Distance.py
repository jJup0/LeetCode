class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        maxlen = max(len(x), len(y))
        x, y = bin(x)[2:].zfill(maxlen), bin(y)[2:].zfill(maxlen)
        retVal = 0
        for xbit, ybit in zip(x, y):
            retVal += xbit != ybit
        return retVal
