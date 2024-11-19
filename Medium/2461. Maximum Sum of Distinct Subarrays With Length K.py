"""
You are given an integer array nums and an integer k. Find the maximum subarray
sum of all the subarrays of nums that meet the following conditions:
- The length of the subarray is k, and
- All the elements of the subarray are distinct.

Return the maximum subarray sum of all the subarrays that meet the conditions.
If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
- 1 <= k <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""

import itertools


class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        accu = [0]
        accu.extend(itertools.accumulate(nums))
        # set of numbers in current sliding window
        curr_nums: set[int] = set()
        # starting index of current sliding window
        subarr_start_idx = 0
        res = 0
        for i, num in enumerate(nums):
            if num in curr_nums:
                # duplicate number in current sliding window
                while nums[subarr_start_idx] != num:
                    curr_nums.remove(nums[subarr_start_idx])
                    subarr_start_idx += 1
                subarr_start_idx += 1

            subarr_length = i - subarr_start_idx + 1
            if subarr_length > k:
                # unique numbers are longer than k, move left pointer
                # of sliding window one to the right
                curr_nums.remove(nums[subarr_start_idx])
                subarr_start_idx += 1

            if subarr_length >= k:
                # found subarray with unique numbers of length n
                res = max(res, accu[i + 1] - accu[subarr_start_idx])

            curr_nums.add(num)
        return res
