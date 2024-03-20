"""
Given an integer array nums, return an arrayanswersuch thatanswer[i]is equal to
the product of all the elements ofnumsexceptnums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
integer.

You must write an algorithm that runs in O(n) time and without using the
division operation.

Constraints:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
integer.
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        O(n) / O(1)     time / extra space complexity
        """
        output = [1] * len(nums)
        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]
        # output now contains product of all elements to the left

        multiplier = 1
        # go in reverse to include product of all elements to the right
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= multiplier
            multiplier *= nums[i]
        return output
