"""
You are given two integer arrays of equal length target and arr. In one step,
you can select any non-empty subarray of arr and reverse it. You are allowed to
make any number of steps.

Return true if you can make arr equal to target or false otherwise.

Constraints:
- target.length == arr.length
- 1 <= target.length <= 1000
- 1 <= target[i] <= 1000
- 1 <= arr[i] <= 1000
"""

from collections import Counter


class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        """
        At ith step, reverse arr[i:x+1] where x is the position of the ith smallest number.
        O(n) / O(n)     time / space complexity
        """
        return Counter(target) == Counter(arr)
