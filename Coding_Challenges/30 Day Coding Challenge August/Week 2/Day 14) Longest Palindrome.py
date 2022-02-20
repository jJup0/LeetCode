from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        retVal = 0
        singleLetter = False
        for val in Counter(s).values():
            if val % 2:
                singleLetter = True
            retVal += (val//2)*2
        return retVal + singleLetter
