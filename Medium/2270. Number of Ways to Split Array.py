"""
You are given a 0-indexed integer array nums of length n.

 nums contains a valid split at index i if the following are true:
- The sum of the first i + 1 elements is greater than or equal to the sum of
  the last n - i - 1 elements.
- There is at least one element to the right of i. That is, 0 <= i < n - 1.

Return the number of valid splits in nums.

Constraints:
- 2 <= nums.length <= 10^5
- -10^5 <= nums[i] <= 10^5
"""

import itertools


class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        sum_left = 0
        sum_right = sum(nums)
        res = 0
        for num in itertools.islice(nums, len(nums) - 1):
            sum_right -= num
            sum_left += num
            res += sum_left >= sum_right
        return res
