class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 100:
            return num in (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
        result, divisor = 0, 2  # 10**((len(str(num))-1)/2)
        while abs(result - divisor) > 1:
            result = num/divisor
            divisor = (result+divisor+0.1)/2
        return num % round((result+divisor)/2) == 0
