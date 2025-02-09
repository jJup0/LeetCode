"""
You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad
pair if i < j and j - i!= nums[j] - nums[i].

Return the total number of bad pairs in nums.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

from collections import defaultdict


class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        # prev_occurances[i] = number of previous numbers that would be
        # part of no bad pairs if the array were of the form list(range(i, INF))
        prev_occurances: defaultdict[int, int] = defaultdict(int)
        res = 0
        for i, num in enumerate(nums):
            # forms a bad pair with all previuos numbers
            # except those that match up with `num`'s numberline
            res += i - prev_occurances[num - i]
            # increment count of
            prev_occurances[num - i] += 1
        return res
