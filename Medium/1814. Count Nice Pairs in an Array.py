"""
You are given an array nums that consists of non-negative integers. Let us
define rev(x) as the reverse of the non-negative integer x. For example,
rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it
satisfies all of the following conditions:
- 0 <= i < j < nums.length
- nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])

Return the number of nice pairs of indices. Since that number can be too
large, return it modulo 109 + 7.

Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
"""


from typing import Counter


class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        """
        Pairs of numbers are nice if the difference to their reversed number is equal.
        For lists of numbers with equal differences, there are n-choose-2 ways to form nice pairs.
        O(n) / O()
        """
        diffs = Counter(n - int(str(n)[::-1]) for n in nums)
        MOD = 10**9 + 7
        return sum((count * (count - 1)) // 2 for count in diffs.values()) % MOD
