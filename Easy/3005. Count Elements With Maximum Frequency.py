"""
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
"""

from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        """
        O(n) / O(n)     time / space complexity
        """
        c = Counter(nums)
        max_occ = max(c.values())
        return sum(count == max_occ for count in c.values()) * max_occ
