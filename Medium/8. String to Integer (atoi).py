class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        # ignore starting white space
        while i < len(s) and s[i] == ' ':
            i += 1

        # return 0 in case empty
        if i == len(s):
            return 0

        # check if negative
        negative = s[i] == '-'

        # "ignore" starting positive/negative sign
        if s[i] == '+' or s[i] == '-':
            i += 1

        # store ord of 0 for performance
        zero_ord = ord('0')
        res = 0
        # go through string while current char is a digit
        for char in s[i:]:
            if char < '0' or char > '9':
                break
            res = res * 10 + (ord(char) - zero_ord)

        # cap the result
        if negative:
            res = -res
            if res < -(1 << 31):
                res = -(1 << 31)
        else:
            if res > (1 << 31) - 1:
                res = (1 << 31) - 1

        return res
