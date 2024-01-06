"""
Given an integer array nums, return the length of the longest strictly
increasing subsequence.

Constraints:
- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4
"""


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        """
        O(n * log(n)) / O(n)    time/space complexity
        """

        lis_builder: list[int] = []

        for num in nums:
            # binary search, find closest val bigger than num and overwrite
            lo, hi = 0, len(lis_builder)
            while lo < hi:
                mid = (lo + hi) >> 1
                if lis_builder[mid] < num:
                    lo = mid + 1
                else:
                    hi = mid

            if lo == len(lis_builder):
                lis_builder.append(num)
            else:
                lis_builder[lo] = num

        return len(lis_builder)
