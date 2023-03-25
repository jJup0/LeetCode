class Solution:
    """
    Given an integer array nums, return the number of subarrays filled with 0.

    A subarray is a contiguous non-empty sequence of elements within an array.

    Constraints:
        1 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9
    """

    def zeroFilledSubarray(self, nums: list[int]) -> int:
        """Counts zero filled subarrays using simple subarray combinatorics.
        O(n) / O(1)     time / space complexity
        """
        res = 0
        zero_streak = 0
        for num in nums:
            if num == 0:
                zero_streak += 1
                # add count of all subarrays that can be made that
                # have the current 0 as the last 0 of the subarray
                res += zero_streak
            else:
                # reset 0 streak if non-zero encountered
                zero_streak = 0

        return res
