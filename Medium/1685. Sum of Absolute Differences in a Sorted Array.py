"""
You are given an integer array nums sorted in non-decreasing order.

Build and return an integer array result with the same length as nums such
that result[i] is equal to the summation of absolute differences between
nums[i] and all the other elements in the array.

In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where
0 <= j < nums.length and j != i (0-indexed).

Constraints:
- 2 <= nums.length <= 10^5
- 1 <= nums[i] <= nums[i + 1] <= 10^4
"""


class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        """
        Iterate through nums tracking difference to num before and num after.
        Since numbers are sorted, we can easily calculate the sum of absolute
        differences by using the result of the previous number.
        O(n) / O(n)     time / space complexity
        """
        before = 0
        after = sum(num - nums[0] for num in nums)
        res: list[int] = []
        prev = nums[0]
        for i, num in enumerate(nums):
            diff_to_prev = num - prev
            before += diff_to_prev * i
            after -= diff_to_prev * (len(nums) - i)
            res.append(before + after)
            prev = num
        return res
