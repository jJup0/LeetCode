"""
Given an integer array nums, in which exactly two elements appear only once and
all the other elements appear exactly twice. Find the two elements that appear
only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses
only constant extra space.

Constraints:
- 2 <= nums.length <= 3 * 10^4
- -2^31 <= nums[i] <= 2^31 - 1
- Each integer in nums will appear twice, only two integers will appear once.
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        """
        O(n) / O(1)     time / space complexity
        """
        xor = 0
        for num in nums:
            xor ^= num
        # xor contains the two single numbers xor'ed together
        # means if a bit in xor is set, only one of the two numbers will have it set at that position

        # this bit hack get the lowest set bit, any will set bit will suffice though
        bit = xor & ~(xor - 1)

        # repeat xor process, but this time, separate numbers out by this set bit
        # xor the numbers with the set bit with one another, and the numbers with it cleared with one another
        # the two single numbers CANNOT have this bit both set, so they will be xor'ed separately
        ret1 = ret2 = 0
        for num in nums:
            if num & bit:
                ret1 ^= num
            else:
                ret2 ^= num
        return [ret1, ret2]
