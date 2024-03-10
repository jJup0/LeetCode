"""
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

Constraints:
- 1 <= nums1.length, nums2.length <= 105
- 1 <= nums1[i], nums2[j] <= 109
- Both nums1 and nums2 are sorted in non-decreasing order.
"""


class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        """
        O(n) / O(1)     time / space complexity
        """
        i2 = 0
        for num in nums1:
            while i2 < len(nums2) and nums2[i2] < num:
                i2 += 1
            if i2 == len(nums2):
                break
            if nums2[i2] == num:
                return num
        return -1
