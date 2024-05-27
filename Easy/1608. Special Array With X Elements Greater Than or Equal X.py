"""
You are given an array nums of non-negative integers. nums is considered
special if there exists a number x such that there are exactly x numbers in
nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that
if nums is special, the value for x is unique.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000
"""


class Solution:
    def specialArray(self, nums: list[int]) -> int:
        """
        O(n * log(n)) / O(sort())   time / space complexity
        """
        nums.sort(reverse=True)
        if nums[-1] >= len(nums):
            # special case, all nums are bigger than len(nums)
            return len(nums)

        for i in range(1, len(nums)):
            if nums[i - 1] >= i and nums[i] < i:
                # all previous numbers are bigger and current number is smaller, we found "x"
                return i
        # no "x" for special array found
        return -1
