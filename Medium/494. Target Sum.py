"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols'+'
and'-' before each integer in nums and then concatenate all the integers.
- For example, if nums = [2, 1], you can add a'+' before 2 and a'-' before 1
  and concatenate them to build the expression"+2-1".

Return the number of different expressions that you can build, which evaluates
to target.

Constraints:
- 1 <= nums.length <= 20
- 0 <= nums[i] <= 1000
- 0 <= sum(nums[i]) <= 1000
- -1000 <= target <= 1000
"""

from collections import Counter


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        """
        Complexity:
            Time: O(2^n)
            Space: O(2^n)
        """
        curr_vals = Counter([0])
        for num in nums:
            next_vals: Counter[int] = Counter()
            for val, count in curr_vals.items():
                next_vals[val + num] += count
                next_vals[val - num] += count
            curr_vals = next_vals
        return curr_vals[target]
