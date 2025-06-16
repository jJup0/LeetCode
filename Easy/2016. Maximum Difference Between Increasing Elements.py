"""
Given a 0-indexed integer array nums of size n, find the maximum difference
between nums[i] and nums[j] (i.e., nums[j] - nums[i] ), such that
0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.

Constraints:
- n == nums.length
- 2 <= n <= 1000
- 1 <= nums[i] <= 10^9
"""


class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        smallest = nums[0]
        res = 0
        for num in nums:
            if num < smallest:
                smallest = num
            else:
                res = max(res, num - smallest)
        if res == 0:
            return -1
        return res
