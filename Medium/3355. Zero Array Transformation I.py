"""
You are given an integer array nums of length n and a 2D array queries, where
queries[i] = [l_i, r_i].

For each queries[i]:
- Select a subset of indices within the range [l_i, r_i] in nums.
- Decrement the values at the selected indices by 1.

A Zero Array is an array where all elements are equal to 0.

Return true if it is possible to transform nums into a Zero Array after
processing all the queries sequentially, otherwise return false.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^5
- 1 <= queries.length <= 10^5
- queries[i].length == 2
- 0 <= l_i <= r_i < nums.length
"""


class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        """Track cumulative decrements.

        Complexity:
            Time: O(n + q)
            Space: O(n)
        """
        # create subtraction diff array
        subtraction_diff = [0] * (len(nums) + 1)
        for start, stop in queries:
            subtraction_diff[start] += 1
            subtraction_diff[stop + 1] -= 1

        # keep track of current amount that can be subtracted and
        # return false if this is ever less than current nums
        curr_subtraction = 0
        for num, delta in zip(nums, subtraction_diff):
            curr_subtraction += delta
            if num > curr_subtraction:
                return False
        return True
