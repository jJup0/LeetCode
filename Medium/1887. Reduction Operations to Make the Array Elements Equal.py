"""
Given an integer array nums, your goal is to make all elements in nums equal.
To complete one operation, follow these steps:

1. Find the largest value in nums. Let its index be i (0-indexed) and its value
   be largest. If there are multiple elements with the largest value, pick the
   smallest i.
2. Find the next largest value in nums strictly smaller than largest. Let its
   value be nextLargest.
3. Reduce nums[i] to nextLargest.

Return the number of operations to make all elements in nums equal.

Constraints:
- 1 <= nums.length <= 5 * 10^4
- 1 <= nums[i] <= 5 * 10^4
"""
from typing import Counter


class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        c = Counter(nums)
        numbers = 0
        res = 0
        for _, count in sorted(c.items(), reverse=True):
            res += numbers
            numbers += count
        return res
