"""
We define a harmonious array as an array where the difference between its
maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious
subsequence among all its possible subsequences.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -10^9 <= nums[i] <= 10^9
"""

from collections import Counter


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        res = 0
        counter = Counter(nums)
        for num, count in counter.items():
            if num - 1 in counter:
                res = max(res, count + counter[num - 1])
        return res
