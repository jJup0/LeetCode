class Solution:
    """
    Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
        answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
        answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
        Note that the integers in the lists may be returned in any order.

    Constraints:
        1 <= nums1.length, nums2.length <= 1000
        -1000 <= nums1[i], nums2[i] <= 1000
    """

    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        n1 = set(nums1)
        n2 = set(nums2)
        r1 = list(n1.difference(n2))
        r2 = list(n2.difference(n1))
        return [r1, r2]
