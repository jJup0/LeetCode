class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        curMax = 0
        r = 0
        rN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for c in s[::-1]:
            print(c)
            cur = rN[c]
            if cur >= curMax:
                r += cur
                curMax = cur
            else:
                r -= cur
        return r
