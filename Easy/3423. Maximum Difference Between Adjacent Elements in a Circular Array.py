"""
Given a circular array nums, find the maximum absolute difference between
adjacent elements.

Note: In a circular array, the first and last elements are adjacent.

Constraints:
- 2 <= nums.length <= 100
- -100 <= nums[i] <= 100
"""

import itertools


class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        circular_diff = abs(nums[0] - nums[-1])
        regular_diff = max(abs(n1 - n2) for n1, n2 in itertools.pairwise(nums))
        return max(circular_diff, regular_diff)
