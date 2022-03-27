from typing import List
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # binary search to get position of last 1
        def powerOfRow(row: List[int]) -> int:
            lo = 0
            hi = n
            while lo < hi:
                mid = (lo + hi) >> 1
                if row[mid]:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        
        n = len(mat[0])
        mod = max(len(mat), n)
        # calculate the power of each row, and then sort by power
        # using powerOfRow(row) * mod + i is equivalent to (powerOfRow(row), i), just more efficient
        # just have to take modulo mod when returning result, constraint m, n <= 100 means numbers will not get bigger than 10000
        powers = sorted(powerOfRow(row) * mod + i
                        for i, row in enumerate(mat))
        
        return list(power % mod for power in powers[:k])

        # equivalent to:
        # powers = sorted((powerOfRow(row), i)
        #             for i, row in enumerate(mat))
        # return (i for _, i in powers[:k])