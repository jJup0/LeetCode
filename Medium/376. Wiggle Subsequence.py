from typing import List


class Solution:
    """
    A wiggle sequence is a sequence where the differences between successive numbers strictly
    alternate between positive and negative. The first difference (if one exists) may be either
    positive or negative. A sequence with one element and a sequence with two non-equal elements
    are trivially wiggle sequences.
        For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences
        (6, -3, 5, -7, 3) alternate between positive and negative.
        In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. The first is
        not because its first two differences are positive, and the second is not because its
        last difference is zero.
    A subsequence is obtained by deleting some elements (possibly zero) from the original sequence,
    leaving the remaining elements in their original order.
    Given an integer array nums, return the length of the longest wiggle subsequence of nums.

    Constraints:
        1 <= nums.length <= 1000
        0 <= nums[i] <= 1000
    """

    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
        Subsequence with maximum wiggles is found by ignoring subsequent
        non-increasing and non-decreasing contiguous sequences.
        O(n) / O(1)     Time/Space complexity
        """
        n = len(nums)

        # current and previous value
        curr = prev = nums[0]

        # find first unequal number
        i = 1   # bind i for type check (not needed)
        for i in range(1, n):
            if nums[i] != prev:
                break
        curr = nums[i]

        # special case, if all numbers in list are equal
        if curr == prev:
            return 1

        # increasing is true if previous "wiggle" was up/increasing, else false
        increasing = prev < curr

        # result variable
        res = 2

        for i in range(i, n):
            curr = nums[i]
            # if current "wiggle" is opposite of previous, then increase res and change wiggle
            if (prev != curr) and ((prev < curr) != increasing):
                res += 1
                increasing = not increasing
            prev = curr

        return res
