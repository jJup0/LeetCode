"""
You are given a sorted array nums of n non-negative integers and an integer
maximumBit. You want to perform the following query n times:
1. Find a non-negative integer k < 2maximumBit such that
   nums[0] XOR nums[1] XOR... XOR nums[nums.length-1] XOR k is maximized. k is the
   answer to the ith query.
2. Remove the last element from the current array nums.

Return an array answer, where answer[i] is the answer to the ith query.

Constraints:
- nums.length == n
- 1 <= n <= 10^5
- 1 <= maximumBit <= 20
- 0 <= nums[i] < 2maximumBit
- nums is sorted in ascending order.
"""


class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        # get XOR of whole array
        curr_xor = 0
        for num in nums:
            curr_xor ^= num

        # largest number smaller than 2**maximumBit = 2**maximumBit-1
        bit_mask = (1 << maximumBit) - 1

        res: list[int] = []
        for num in reversed(nums):
            # k which maximizes XOR is is current XOR of
            # emaining nums xor the bitmask
            res.append(bit_mask ^ curr_xor)
            # update remaining XOR by removing current number
            curr_xor ^= num
        return res
