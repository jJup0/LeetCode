class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        m, n = len(nums1), len(nums2)
        l1, r1, l2, r2 = 0, m, 0, n
        mid1, mid2 = (l1 + r1)//2, (l2 + r2)//2
        if nums1[mid1] > nums2[mid2]:
            pass
