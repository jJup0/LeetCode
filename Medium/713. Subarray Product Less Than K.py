"""
Given an array of integers nums and an integer k, return the number of
contiguous subarrays where the product of all the elements in the subarray is
strictly less than k.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- 1 <= nums[i] <= 1000
- 0 <= k <= 10^6
"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        """
        Iterate through nums, keeping track of the current sliding window with
        a product less than k. For each number `num` add the length of the current
        sliding window to the result, as all subarrays ending with `num` have a
        total product less than k.
        O(n) / O(1)     time / space complexity
        """
        res = 0
        prod = 1
        i = j = 0
        for j, num in enumerate(nums):
            prod *= num
            while prod >= k and i <= j:
                prod = prod // nums[i]
                i += 1
            res += j - i + 1
        return res
