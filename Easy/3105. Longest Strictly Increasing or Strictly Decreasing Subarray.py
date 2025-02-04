"""
You are given an array of integers nums. Return the length of the
longestsubarray of nums which is either strictly increasing or strictly decreasing.

Constraints:
- 1 <= nums.length <= 50
- 1 <= nums[i] <= 50
"""

from typing import Iterable


class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        """
        Complexity:
            Time: O(n)
            Space: O(1)
        """
        return max(
            self._longest_strictly_increase(nums),
            self._longest_strictly_increase(reversed(nums)),
        )

    def _longest_strictly_increase(self, nums: Iterable[int]):
        prev = -1
        res = streak = 0
        for num in nums:
            if num <= prev:
                res = max(res, streak)
                streak = 0
            streak += 1
            prev = num
        return max(res, streak)
