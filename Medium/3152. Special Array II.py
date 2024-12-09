"""
An array is considered special if every pair of its adjacent elements contains
two numbers with different parity.

You are given an array of integer nums and a 2D integer matrix queries, where
for queries[i] = [from_i, to_i] your task is to check that subarray
nums[from_i..to_i] is special or not.

Return an array of booleans answer such that answer[i] is true if
nums[from_i..to_i] is special.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
- 1 <= queries.length <= 10^5
- queries[i].length == 2
- 0 <= queries[i][0] <= queries[i][1] <= nums.length - 1
"""

import bisect
import itertools
from functools import cache


class Solution1:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        """
        Divide and conquer approach with memoization.
        Complexity:
            Time: O(n ^ 2 + m)
            Space: O(n ^ 2)
        """
        self.nums = nums
        return [self._query_special(i, j) for i, j in queries]

    @cache
    def _query_special(self, i: int, j: int) -> bool:
        if i == j:
            return True
        if i + 1 == j:
            return (self.nums[i] & 1) != (self.nums[j] & 1)
        half = (i + j) // 2
        return self._query_special(i, half) and self._query_special(half, j)


class Solution2:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        """
        Create list of indexes `i` where nums[i] % 2 == nums[i+1] % 2,
        then bisect this array for each query (a,b) and check if for
        both indexes the same bisection result is returned.

        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        bads = [
            i
            for i, (num1, num2) in enumerate(itertools.pairwise(nums))
            if (num1 & 1) == (num2 & 1)
        ]

        return [
            bisect.bisect_left(bads, a) == bisect.bisect_left(bads, b)
            for a, b in queries
        ]


class Solution3:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        """
        Create accumulated sums of bad pairs and simply look-up with index.
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        accumuated_bad_pairs = self._get_bad_pairs(nums)
        return [
            accumuated_bad_pairs[start] == accumuated_bad_pairs[end]
            for start, end in queries
        ]

    def _get_bad_pairs(self, nums: list[int]) -> list[int]:
        """
        Returns an array `arr` where arr[i] = the amount indexes j, 0 < j <= i,
        such that nums[j] % 2 == nums[j-1] % 2.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        running_bad_pairs = 0
        accumuated_bad_pairs: list[int] = []
        prev_parity = None
        for num in nums:
            curr_parity = num & 1
            running_bad_pairs += curr_parity == prev_parity
            accumuated_bad_pairs.append(running_bad_pairs)
            prev_parity = curr_parity
        return accumuated_bad_pairs


class Solution(Solution3):
    pass
