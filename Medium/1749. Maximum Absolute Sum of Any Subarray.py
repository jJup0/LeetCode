"""
You are given an integer array nums. The absolute sum of a subarray
[nums_l, nums_l+1,..., nums_r-1, nums_r] is
abs(nums_l + nums_l+1 +... + nums_r-1 + nums_r).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:
- If x is a negative integer, then abs(x) = -x.
- If x is a non-negative integer, then abs(x) = x.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

import itertools


class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        """
        Keep track of the largest and smallest value of sum(nums[:i]),
        when encountering negative numbers the maxixmum absolute subarray
        sum will be `nums[largest_idx:i+1]`, else `nums[smallest_idx:i+1]`.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        largest = smallest = 0
        res = 0
        for accu in itertools.accumulate(nums):
            if accu < 0:
                res = max(res, -(accu - largest))
                if accu < smallest:
                    smallest = accu
            else:
                res = max(res, accu - smallest)
                if accu > largest:
                    largest = accu
        return res
