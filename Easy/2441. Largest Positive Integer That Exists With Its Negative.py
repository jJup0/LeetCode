"""
Given an integer array nums that does not contain any zeros, find the largest
positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.

Constraints:
- 1 <= nums.length <= 1000
- -1000 <= nums[i] <= 1000
- nums[i]!= 0
"""


class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        """
        O(n) / O(n)     time / space complexity
        """
        nums_set = frozenset(nums)
        res = 0
        for num in nums:
            if num > 0 and num > res and -num in nums_set:
                res = num
        return res
