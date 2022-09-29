import bisect
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # upper and lower boundary for i for result arr[i:i+k]
        lo = 0
        hi = len(arr)-k

        while lo < hi:
            # mid as new potential i for result arr[i:i+k]
            mid = (lo + hi) >> 1
            if x-arr[mid] <= arr[mid+k]-x:
                # if |x - arr[mid]| <= |x - arr[mid+k]| (i.e. is closer) then reduce upper boundary
                # not mid - 1 as mid may be the solution for i
                hi = mid
            else:
                # else increase lower boundary
                # mid is definitely not the solution for i, so do mid + 1
                lo = mid + 1

        return arr[lo:lo+k]

    def findClosestElements_O_of_k(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Binary search once and then expand.
        O(log(n) + k) / O(1)    time / space
        """
        n = len(arr)
        j = bisect.bisect_left(arr, x)
        i = j - 1
        for _ in range(k):
            if i < 0:
                j += 1
            elif j >= n:
                i -= 1
            else:
                if x-arr[i] <= arr[j]-x:
                    i -= 1
                else:
                    j += 1

        return arr[i+1:j]


S = Solution()
S.findClosestElements(

    [1, 2, 3, 4, 5],
    2,
    -1,

)
