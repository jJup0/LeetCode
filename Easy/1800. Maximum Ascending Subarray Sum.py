"""
Given an array of positive integers nums, return the maximum possible sum of an
ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [nums_l, nums_l+1,..., nums_r-1, nums_r] is ascending if for all i
where l <= i < r, nums_i < nums_i+1. Note that a subarray of size 1 is ascending.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
"""


class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        """
        Complexity:
            Time: O(n)
            Space: O(1)
        """
        prev = nums[0] - 1
        res = curr_sum = 0
        for num in nums:
            if num > prev:
                curr_sum += num
            else:
                res = max(res, curr_sum)
                curr_sum = num
            prev = num
        return max(res, curr_sum)
