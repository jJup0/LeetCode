class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        r = dividend / divisor
        if r < -2 << 30:
            return -2 << 31
        if r > (2 << 30) - 1:
            return (2 << 30) - 1
        if r > 0:
            return int(r)
        if r < 0:
            return int(r)
        return 0
