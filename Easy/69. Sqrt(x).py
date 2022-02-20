class Solution:
    def mySqrt(self, x: int) -> int:
        # lo = 0
        # hi = x + 1
        if x < 2:
            return x
        halfbits = (int.bit_length(x)//2)   # 1 << halfbit is approximately sqrt
        hi = 1 << (halfbits + 1)
        lo = 1 << (halfbits - 1)
        while lo < hi - 1:  # for lo = 0, hi = x + 1 use lo < hi, idk why tbh lol
            mid = (lo + hi) >> 1
            sq = mid * mid
            if sq > x:
                hi = mid
            elif sq < x:
                lo = mid
            else:
                return mid
        return lo

        # Newtons method, stolen
        # ans = x
        # while ans * ans > x:
        #     ans = int(ans + x/ans)//2
        # return ans
