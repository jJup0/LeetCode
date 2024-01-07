"""
Given an integer array nums, return the number of all the arithmetic
subsequences ofnums.

A sequence of numbers is called arithmetic if it consists of at least three
elements and if the difference between any two consecutive elements is the
same.
- For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are
arithmetic sequences.
- For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.

A subsequence of an array is a sequence that can be formed by removing some
elements (possibly none) of the array.
- For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].

The test cases are generated so that the answer fits in 32-bit integer.

Constraints:
- 1 <= nums.length <= 1000
- -2^31 <= nums[i] <= 2^31 - 1
"""


from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        # dp[i][diff] = number of arithmetic subsequences of at least length 2
        # ending with nums[i], with a difference of "diff" between numbers
        dp: list[dict[int, int]] = [defaultdict(int) for _ in range(len(nums))]
        # result variable
        res = 0
        for i, curr_num in enumerate(nums):
            for j in range(i):
                diff = nums[j] - curr_num

                prev_ways = dp[j][diff]

                # there are `prev_ways + 1` new ways of making sequences of at least length 2
                # e.g. nums = [2, 2, 4, 6], i = 3, j = 2, then:
                # prev_subseqs := [[2, 4], [2, 4]]
                # prev_ways     = len(prev_subseqs) = 2
                # new_subseqs  := [seq + [nums[i]] for seq in prev_seq] + [nums[j], nums[i]]
                #               = [[2, 4, 6], [2, 4, 6], [4, 6]]
                # new_ways      = len(new_subseqs)      (= prev_ways + 1)
                new_ways = prev_ways + 1
                dp[i][diff] += new_ways

                # add prev_ways and not new_ways, because `dp` stores subsequences
                # of at least length 2, but we want the sum of subsequences of length 3
                # there are new_ways - 1 == prev_ways, new sequences of length 3
                res += prev_ways

        return res
