"""
You are given a 0-indexed integer array nums.

Return the maximum value over all triplets of indices (i, j, k) such that
i < j < k. If all such triplets have a negative value, return 0.

The value of a triplet of indices (i, j, k) is equal to
(nums[i] - nums[j]) * nums[k].

Constraints:
- 3 <= nums.length <= 100
- 1 <= nums[i] <= 10^6
"""


class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        """Track highest value and biggest difference so far while iterating through nums.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        highest_value = 0
        biggest_delta = 0
        res = 0
        for x in nums:
            res = max(res, biggest_delta * x)
            biggest_delta = max(highest_value - x, biggest_delta)
            highest_value = max(highest_value, x)
        return res

    def maximumTripletValue_naive(self, nums: list[int]) -> int:
        """
        Complexity:
            Time: O(n^3)
            Space: O(1)
        """
        res = 0
        for i in range(len(nums)):
            num1 = nums[i]
            for j in range(i + 1, len(nums)):
                num2 = nums[j]
                for k in range(j + 1, len(nums)):
                    res = max(res, (num1 - num2) * nums[k])
        return res
