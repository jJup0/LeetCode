"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

Constraints:
- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 1000
"""


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        O(n) / O(n)     time / space complexity
        """
        return list(set(nums1).intersection(nums2))
