"""
Given an array nums containing n distinct numbers in the range [0, n], return
the only number in the range that is missing from the array.

Constraints:
- n == nums.length
- 1 <= n <= 10^4
- 0 <= nums[i] <= n
- All the numbers of nums are unique.
"""


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """
        O(n) / O(1)     time / space complexity
        """
        # this sum of all numbers from 1 to n equals n*(n+1)//2
        n = len(nums)
        gauss_sum = n * (n + 1) // 2
        # subtract actual sum from theoretical sum to find missing number
        return gauss_sum - sum(nums)
