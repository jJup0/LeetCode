"""
You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed, the only constraint stopping you from
robbing each of them is that adjacent houses have security systems connected
and it will automatically contact the police if two adjacent houses were broken
into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the
police.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        O(n) / O(1)     time / space complexity
        """
        max_rob = 0
        no_rob_prev = 0
        for num in nums:
            prev_max_rob = max_rob
            # maximum profit is largest between max profit of previous house,
            # and robbing this house and not robbing the previous house
            max_rob = max(no_rob_prev + num, max_rob)
            no_rob_prev = prev_max_rob
        return max_rob
