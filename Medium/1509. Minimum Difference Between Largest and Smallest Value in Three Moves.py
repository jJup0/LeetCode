"""
You are given an integer array nums.

In one move, you can choose one element of nums and change it to any value.

Return the minimum difference between the largest and smallest value of nums
after performing at most three moves.

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

import heapq


class Solution:
    def minDifference(self, nums: list[int]) -> int:
        """
        If 4 or fewer elements, change them all to the same value.
        Otherwise find combinatorical minimum of changing the first i numbers
        and the last 3-i numbers to some arbitrary number in between.
        O(n) / O(1)    time / space complexity
        """
        if len(nums) <= 4:
            return 0
        smallest = heapq.nsmallest(4, nums)
        largest = heapq.nlargest(4, nums)
        return min(large - small for large, small in zip(largest, smallest[::-1]))

    def minDifference_sort(self, nums: list[int]) -> int:
        """
        Same as above but using sort, might be more intuitive.
        O(n * log(n)) / O(timsort)    time / space complexity
        """
        if len(nums) <= 4:
            return 0
        nums.sort()
        return min(nums[i - 4] - nums[i] for i in range(4))
