from typing import List


class Solution:
    """
    Given an array of positive integers nums and a positive integer target, return the minimal
    length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is
    greater than or equal to target. If there is no such subarray, return 0 instead.
    Constraints:
        1 <= target <= 10^9
        1 <= nums.length <= 10^5
        1 <= nums[i] <= 10^4
    """

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # start index of current sub array
        start = 0
        
        # current running sum
        total = 0

        # result variable
        res = len(nums) + 1

        for end, num in enumerate(nums):
            # add current value to total
            total += num
            # shrink sub array while total is greater equal to target
            while total >= target:
                # update res if smaller than previous
                res = min(end - start + 1, res)
                total -= nums[start]
                start += 1

        # if res has default value return 0, else res
        return 0 if res == len(nums) + 1 else res
