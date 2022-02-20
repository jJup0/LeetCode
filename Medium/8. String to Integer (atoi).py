class OldSolution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        nums = '0123456789'
        negative = False
        if s[0] == '+' or s[0] == '-':
            if s[0] == '-':
                negative = True
            s = s[1:]
        elif not(s[0] in nums):
            return 0

        retVal = 0
        for char in s:
            nums_i = nums.find(char)
            if nums_i == -1:
                break
            else:
                retVal *= 10
                retVal += nums_i
        if negative:
            retVal = -retVal
        if retVal > 2**31 - 1:
            retVal = 2**31-1
        if retVal < -(2**31):
            retVal = -(2**31)
        return retVal

class Solution:
    def myAtoi(self, s: str) -> int:
        s = list(s)
        s.append('$')
        i = 0
        while s[i] == ' ':
            i += 1

        negative = s[i] == '-'
        if s[i] == '+' or s[i] == '-':
            i += 1
    
        zero_ord = ord('0')
        nine_ord = ord('9')
        res = 0
        digit_ord = ord(s[i])
        while digit_ord >= zero_ord and digit_ord <= nine_ord:
            res *= 10
            res += digit_ord - zero_ord
            i += 1
            digit_ord = ord(s[i])

        if negative:
            res = -res
            if res < -(1<<31):
                res = -(1<<31)
        else:
            if res > (1<<31) - 1:
                res = (1<<31) - 1
                
        return res