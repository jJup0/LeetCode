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

from typing import TypeAlias

Len_T: TypeAlias = int
PrevFactor_T: TypeAlias = int | None
Node_T: TypeAlias = tuple[Len_T, PrevFactor_T]


class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        return self.largestDivisibleSubset_regular(nums)

    def largestDivisibleSubset_regular(self, nums: list[int]) -> list[int]:
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
            # add num to largest compatible divisible set
            factor_subsets.append(longest_compatible_factor_set + [num])

        # return the largest divisible subset
        return max(factor_subsets, key=len)

    def largestDivisibleSubset_space_efficient(self, nums: list[int]) -> list[int]:
        """
        Only store length and previous largest factor in the dp array.
        Much less understandable than the original implementation.
        O(n*n) / O(n)     time / space complexity
        """
        nums.sort()

        # factor_subsets[i] contains a tuple (l, p) where l is the size of the
        # largest divisible subset, and p is the next largest number (or None
        # if it is the smallest number) for divisible subsets where nums[i] is
        # the largest number in the divisible subset
        factor_subsets: list[Node_T] = []

        for i, num in enumerate(nums):
            # get all factor sets of numbers
            compatible_factor_sets: list[Node_T] = [
                (factor_subsets[j][0], j) for j in range(i) if num % nums[j] == 0
            ]

            if not compatible_factor_sets:
                factor_subsets.append((1, None))
                continue

            # get longest compatible set, increase its length by
            length, prev_index = max(compatible_factor_sets)
            factor_subsets.append((length + 1, prev_index))

        # reconstruct largest divisible subset
        _, prev_index, last_index = max(
            (l, prev_idx, idx) for idx, (l, prev_idx) in enumerate(factor_subsets)
        )
        res = [nums[last_index]]
        while prev_index != None:
            res.append(nums[prev_index])
            prev_index = factor_subsets[prev_index][1]
        return res
