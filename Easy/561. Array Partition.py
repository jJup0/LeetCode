"""
Given an integer array nums of 2n integers, group these integers into n pairs
(a_1, b_1), (a_2, b_2),..., (a_n, b_n) such that the sum of min(a_i, b_i) for
all i is maximized. Return the maximized sum.

Constraints:
- 1 <= n <= 10^4
- nums.length == 2 * n
- -10^4 <= nums[i] <= 10^4
"""


class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        return sum(nums[::2])
