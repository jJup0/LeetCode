"""
Given an array of integers nums, sort the array in increasing order based on
the frequency of the values. If multiple values have the same frequency, sort
them in decreasing order.

Return the sorted array.

Constraints:
- 1 <= nums.length <= 100
- -100 <= nums[i] <= 100
"""

from collections import Counter


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        """
        O(n) / O(n)     time / space complexity
        """
        c = Counter(nums)
        nums.sort(key=lambda num: (c[num], -num))
        return nums
