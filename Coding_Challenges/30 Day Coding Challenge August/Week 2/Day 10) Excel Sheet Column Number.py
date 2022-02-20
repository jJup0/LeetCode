class Solution:
    def titleToNumber(self, s: str) -> int:
        retVal = 0
        for i, c in enumerate(s[::-1]):
            retVal += (ord(c) - 64) * 26**i
        return retVal
