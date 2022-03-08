from typing import List
import statistics
import random


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        n, m = len(nums1), len(nums2)
        half_len = (n + m) >> 1
        lo1, hi1 = half_len - m + 1, half_len - 1

        while lo1 < hi1:
            mid1 = (lo1 + hi1) >> 1
            mid2 = half_len - mid1
            try:
                v1, v2 = nums1[mid1], nums2[mid2]
            except:
                print(f"\n\nm1, m2 - l1, l2: {(mid1, mid2)}{(n, m)}\n")
                return -1
            if v1 <= v2:
                lo1 = mid1 + 1
            else:
                hi1 = mid1 - 1

        mid1 = (lo1 + hi1) >> 1
        mid2 = half_len - mid1
        try:
            return (nums1[mid1] + nums2[mid2]) / 2
        except:
            print(f"\n\nm1, m2 - l1, l2: {(mid1, mid2)}{(n, m)}\n")
            return -1


# S = Solution()

# # random.seed(1)
# nsize = 20000
# for _ in range(100):
#     s1, s2 = tuple(random.randint(1, 1000) for _ in range(2))

#     n1, n2 = tuple(sorted(random.randint(1, nsize) for _ in range(s1)) for _ in range(2))

#     total = sorted(n1 + n2)

#     x = S.findMedianSortedArrays(n1, n2)
#     real = statistics.median(total)
#     print(abs(x - real), end = "\t")
