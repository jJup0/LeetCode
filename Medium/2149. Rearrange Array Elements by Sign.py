"""
You are given a 0-indexed integer array nums of even length consisting of an
equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows
the given conditions:

1. Every consecutive pair of integers have opposite signs.
2. For all integers with the same sign, the order in which they were present in nums is preserved.
3. The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements to satisfy the
aforementioned conditions.

Constraints:
- 2 <= nums.length <= 2 * 10^5
- nums.length is even
- 1 <= |nums[i]| <= 10^5
- nums consists of equal number of positive and negative integers.
"""


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        """
        O(n) / O(n)     time / space complexity
        """
        all_pos = [num for num in nums if num > 0]
        all_neg = [num for num in nums if num < 0]
        res: list[int] = []
        for pos, neg in zip(all_pos, all_neg):
            res.append(pos)
            res.append(neg)
        return res
