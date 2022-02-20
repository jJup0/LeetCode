class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # factors = [x for x in range(1, len(s)//2 + 1) if not len(s) % x]
        # for sublen in factors:
        #     if s[:sublen] * int(len(s) / sublen) == s:
        #         return True
        # return False
        return s in (s + s)[1: -1]
