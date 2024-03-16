"""
Given a binary array nums, return the maximum length of a contiguous subarray
with an equal number of 0 and 1.

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
"""


class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        """
        O(n) / O(n)     time / space complexity
        """
        # prev_sums as {count:index} tracks first occurance of an amount of 1s vs 0s
        prev_sums = {0: -1}
        result = 0
        balance = 0
        for i, num in enumerate(nums):
            # if num is 1 add 1, if num is 0 subtract 1
            balance += 1 if num else -1
            # if current sum has already occurred at index j, then nums[j:i+1] has same amount of 0s and 1s
            if balance in prev_sums:
                contiguous_length = i - prev_sums[balance]
                # if calculated length longer than previous, store it
                result = max(result, contiguous_length)
            else:
                # if current sum has never occurred then take note of current index
                prev_sums[balance] = i
        return result
