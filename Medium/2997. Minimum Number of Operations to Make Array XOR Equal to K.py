"""
You are given a 0-indexed integer array nums and a positive integer k.

You can apply the following operation on the array any number of times:
- Choose any element of the array and flip a bit in its binary representation.
  Flipping a bit means changing a 0 to 1 or vice versa.

Return the minimum number of operations required to make the bitwise XOR of all
elements of the final array equal to k.

Note that you can flip leading zero bits in the binary representation of
elements. For example, for the number (101)_2 you can flip the fourth bit and
obtain (1101)_2.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^6
- 0 <= k <= 10^6
"""


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        """
        O(n) / O(1)     time / space complexity
        """
        xor = 0
        for num in nums:
            xor ^= num

        res = 0
        while xor or k:
            res += (xor & 1) != (k & 1)
            k >>= 1
            xor >>= 1
        return res
