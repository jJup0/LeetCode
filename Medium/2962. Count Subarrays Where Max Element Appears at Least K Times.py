"""
You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at
least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
- 1 <= k <= 10^5
"""


class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        """
        O(n) / O(1)
        """
        max_val = max(nums)
        # current count of maximum value
        max_val_count = 0
        # sliding window start
        i = 0
        # result subarray count
        res = 0
        for j, num in enumerate(nums):
            if num == max_val:
                max_val_count += 1
                if max_val_count >= k:
                    # move the sliding window index to the next occurance of max_val
                    i = nums.index(num, i, j + 1) + 1
            if max_val_count >= k:
                # any of the first `max_val_last_pos` indices can be used as the
                # starting index for the subarray containing at least k occurances
                res += i
        return res
