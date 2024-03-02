"""
Given an integer array nums sorted in non-decreasing order, return an array of
the squares of each number sorted in non-decreasing order.

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in non-decreasing order.
"""

import bisect


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        """
        Find index first positive number, then iterate using two pointers
        from that index, one going to the left to negative numbers, the
        other to the right to positive numbers.
        O(n) / O(n)     time / space complexity
        """
        p_idx = bisect.bisect(nums, 0)
        n_idx = p_idx - 1
        n = len(nums)
        res: list[int] = []
        while n_idx >= 0 and p_idx < n:
            p_num = nums[p_idx]
            n_num = nums[n_idx]
            if p_num < -n_num:
                res.append(p_num * p_num)
                p_idx += 1
            else:
                res.append(n_num * n_num)
                n_idx -= 1

        while n_idx >= 0:
            res.append(nums[n_idx] * nums[n_idx])
            n_idx -= 1
        while p_idx < n:
            res.append(nums[p_idx] * nums[p_idx])
            p_idx += 1

        return res
