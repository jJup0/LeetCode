class Solution:
    def titleToNumber(self, s: str) -> int:
        a_dec = ord('A') - 1
        retVal = 0
        for i, c in enumerate(s):
            retVal = retVal * 26 + (ord(c) - a_dec)
        return retVal