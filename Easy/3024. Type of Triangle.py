"""
You are given a 0-indexed integer array nums of size 3 which can form the sides
of a triangle.
- A triangle is called equilateral if it has all sides of equal length.
- A triangle is called isosceles if it has exactly two sides of equal length.
- A triangle is called scalene if all its sides are of different lengths.

Return a string representing the type of triangle that can be formed or "none" if
it cannot form a triangle.

Constraints:
- nums.length == 3
- 1 <= nums[i] <= 100
"""


class Solution:
    def triangleType(self, nums: list[int]) -> str:
        """
        Complexity:
            Time: O(1)
            Space: O(1)
        """
        if max(nums) >= sum(nums) - max(nums):
            return "none"

        unique_lens = len(set(nums))
        if unique_lens == 1:
            return "equilateral"
        if unique_lens == 2:
            return "isosceles"
        return "scalene"
