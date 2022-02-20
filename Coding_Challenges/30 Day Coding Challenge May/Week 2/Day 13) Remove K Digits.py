class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        i, largestD = 0, ['0']
        while i < len(num) and k > 0:
            if int(num[i]) >= int(largestD[-1]):
                largestD.append(num[i])
                i += 1
            else:
                x = largestD.pop(-1)
                num = num.replace(x, '', 1)
                i -= 1
                k -= 1
        num = num.lstrip('0')
        if k:
            if not(num[:-k]):
                return '0'
            return num[:-k]
        else:
            if not(num):
                return '0'
            return num
