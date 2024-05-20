"""
The XOR total of an array is defined as the bitwise XOR of all its elements, or
0 if the array is empty.
- For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.

Given an array nums, return the sum of all XOR totals for every subset of nums.

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting
some (possibly zero) elements of b.

Constraints:
- 1 <= nums.length <= 12
- 1 <= nums[i] <= 20
"""

import functools
import operator


class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        """
        Each number appears in half of all subsets. Intuitive reason: we can represent
        each subset as a series of bits, where the bit is 1 if the number is included
        and 0 if it is excluded.

        Claim: each set bit will be inluded in half of all subsets.

        Consider an array where two different members x and y share some arbitrary
        amount of set bits. When both of them are included in a subset, some of
        their bits will cancel each other out.

        A quarter of subsets will only contain x, a quarter will only contain y,
        a quarter will contain both, and a quarter will contain neither.

        In the subsets where only one of the two is present (half of the subsets), they
        contribute their bits without problem. In a quarter of subsets they will cancel
        each other out.

        So we still have each bit of each number represented in half of all subsets.
        This logic can be extended from 2 numbers, to an arbitrary amount of numbers.

        O(n) / O(1)     time / space complexity
        """
        all_or = 0
        for num in nums:
            all_or |= num

        half_of_subsets_count = 1 << (len(nums) - 1)
        # since each bit in in half of all subsets, multiply each bit by half the count of all subsets.
        return all_or * half_of_subsets_count

    def subsetXORSum_naive(self, nums: list[int]) -> int:
        """
        Naive approach
        O(2^n) / O(2^n)     time / space complexity
        """
        sub_sets: list[list[int]] = [[]]
        for num in nums:
            num_as_list = [num]
            sub_sets.extend(sub_sets[i] + num_as_list for i in range(len(sub_sets)))
        return sum(functools.reduce(operator.xor, sub_set, 0) for sub_set in sub_sets)
