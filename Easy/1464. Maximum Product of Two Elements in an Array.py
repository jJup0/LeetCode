"""
Given the array of integers nums, you will choose two different indices
i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

Constraints:
- 2 <= nums.length <= 500
- 1 <= nums[i] <= 10^3
"""


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """
        O(n) / O(1)     time / space complexity
        """
        highest = second_highest = 0
        for num in nums:
            if num > highest:
                second_highest = highest
                highest = num
            elif num > second_highest:
                second_highest = num
        return (highest - 1) * (second_highest - 1)
