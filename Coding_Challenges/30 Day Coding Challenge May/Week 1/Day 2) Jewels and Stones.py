class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        retVal = 0
        for c in S:
            if c in J:
                retVal += 1
        return retVal
