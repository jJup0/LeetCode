"""
Given a set of distinct positive integers nums, return the largest subset answer
such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
- answer[i] % answer[j] == 0, or
- answer[j] % answer[i] == 0

If there are multiple solutions, return any of them.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 2 * 109
- All the integers in nums are unique.
"""


class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        """
        O(n*n) / O(n*n)     time / space complexity
        """
        nums.sort()
        # factor_subsets[i] contains a list of the largest divisible subset where nums[i] is the largest number
        factor_subsets: list[list[int]] = []

        for i, num in enumerate(nums):
            # get all factor sets of numbers
            compatible_factor_sets: list[list[int]] = [
                factor_subsets[j] for j in range(i) if num % nums[j] == 0
            ]

            # get longest compatible set
            longest_compatible_factor_set = max(
                compatible_factor_sets,
                key=len,
                default=[],  # type: ignore # strict type checking does not like unknown list type
            )
            # add n
            factor_subsets.append(longest_compatible_factor_set + [num])

        return max(factor_subsets, key=len)
