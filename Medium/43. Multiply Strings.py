class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        res = [0]*(len(num1) + len(num2))
        n1 = list(map(int, num1))
        n2 = list(map(int, num2))
        for i, d1 in enumerate(reversed(n1), start=1):
            pos = len(res) - i
            carry = 0
            for d2 in reversed(n2):
                carry, digit = divmod(d1*d2 + res[pos] + carry, 10)
                res[pos] = digit
                pos -= 1
            res[pos] = carry

        return ''.join(map(str, res[res[0] == 0:]))


#         # oops violates built in bigInt
#         if num1 == '0' or num2 == '0':
#             return '0'
#         val1 = val2 = 0
#         for c in num1:
#             val1 = val1*10 + ord(c) - ord('0')
#         for c in num2:
#             val2 = val2*10 + ord(c) - ord('0')

#         res = val1 * val2
#         resStr = []
#         while res:
#             digit = res % 10
#             resStr.append(chr(ord('0') + digit))
#             res = (res - digit) //10
#         return ''.join(reversed(resStr))

        # # fug the rules
        # return str(int(num1) * int(num2))
