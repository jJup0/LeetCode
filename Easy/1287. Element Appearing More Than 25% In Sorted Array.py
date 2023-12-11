"""
Given an integer array sorted in non-decreasing order, there is exactly one
integer in the array that occurs more than 25% of the time, return that integer.

Constraints:
- 1 <= arr.length <= 10^4
- 0 <= arr[i] <= 10^5
"""
import bisect


class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        """
        Check number at each 12.5% index. A number appearing more than 25%
        of the time in a sorted array will be seen at least twice. To confirm
        that it indeed appears more than 25% or the time, use binary search to
        find the first and last occurance of the number.

        O(log(n)) / O(1)    time / space complexity
        """
        quarter_n = len(arr) / 4
        prev = arr[-1]
        for eight_nr in range(8):
            i = (len(arr) * eight_nr) // 8
            num = arr[i]
            if num == prev:
                first_occ = bisect.bisect_left(arr, num)
                last_occ = bisect.bisect_right(arr, num)
                if last_occ - first_occ > quarter_n:
                    return num
            prev = num
        raise ValueError(r"No number occurs more than 25% of the time")
