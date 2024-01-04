"""
You are given a 0-indexed array nums consisting of positive integers.

There are two types of operations that you can apply on the array any number of
times:
- Choose two elements with equal values and delete them from the array.
- Choose three elements with equal values and delete them from the array.

Return the minimum number of operations required to make the array empty, or -1
if it is not possible.

Constraints:
- 2 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
"""
from collections import Counter


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        O(n) / O(n)     time / space complexity
        """
        res = 0
        for count in Counter(nums).values():
            if count == 1:
                return -1
            div, rest = divmod(count, 3)
            res += div + bool(rest)
        return res
