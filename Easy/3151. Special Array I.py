"""
An array is considered special if every pair of its adjacent elements contains
two numbers with different parity.

You are given an array of integers nums. Return true if nums is a special
array, otherwise, return false.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
"""


class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        """
        Complexity:
            Time: O(n)
            Space: O(1)
        """

        # initialize to opposite parity of first number
        prev_parity = 1 - (nums[0] & 1)
        for num in nums:
            parity = num & 1
            if parity == prev_parity:
                return False
            prev_parity = parity
        return True

    def is_array_special_two_liner(self, nums: list[int]) -> bool:
        first_parity = nums[0] & 1
        return all((i + first_parity) & 1 == num & 1 for i, num in enumerate(nums))
