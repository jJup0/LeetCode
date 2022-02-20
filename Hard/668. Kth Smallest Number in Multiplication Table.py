class Solution:
    # idea hella stolen, really optimized though from 580ms to 232ms
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # iterates over the length of one side, faster if smaller side
        if m > n:
            m, n = n, m
        lo, hi = 1, m*n
        while lo < hi:
            mid = (lo+hi) >> 1

            # sum of numbers in column i that are smaller than mid
            # simplified from: for i in range(1, m+1): count += n if n < mid//i else mid//i
            midDivN = (mid//n)
            count = (n * midDivN) + sum(mid//i for i in range(midDivN + 1, m + 1))

            if count >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
