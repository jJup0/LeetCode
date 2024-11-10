"""
You are given an array nums of non-negative integers and an integer k.

An array is called special if the bitwise OR of all of its elements is at least k.

Return the length of the shortestspecialnon-emptysubarray of nums, or return -1
if no special subarray exists.

Constraints:
- 1 <= nums.length <= 2 * 10^5
- 0 <= nums[i] <= 10^9
- 0 <= k <= 10^9
"""

from typing import Literal


class SolutionComplex:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        """
        Original convoluted solution, for some reason I thought the simple
        approach would be too slow (it is faster for leetcode testcases),
        despite this one having the same time complexity.

        Complexity:
            Time: O(n^2)
            Space: O(n^2)
        """
        if any(num >= k for num in nums):
            # early return for performance and edge case of k == 0
            return 1
        self.nums = nums
        self.k = k
        self._build_bit_count()

        if self._bit_count_to_num() < k:
            # OR of full array is smaller than k
            return -1

        # self.dp[i,j] = smallest subarray length within nums[i:j+1]
        self.dp: dict[tuple[int, int], int] = {}
        return self._find_smallest(0, len(nums) - 1)

    def _build_bit_count(self):
        self.bit_count = [0] * 32
        for num in self.nums:
            self._add_sub_num_to_bit_count(num, 1)
        # shrink bit count down to largest number (only for performance)
        while not self.bit_count[-1]:
            self.bit_count.pop()

    def _add_sub_num_to_bit_count(self, num: int, add_sub: Literal[1, -1]):
        mask = 1
        i = 0
        while mask <= num:
            num_masked = num & mask
            self.bit_count[i] += bool(num_masked) * add_sub
            mask <<= 1
            i += 1

    def _bit_count_to_num(self) -> int:
        res = 0
        for i, val in enumerate(self.bit_count):
            if val:
                res += 1 << i
        return res

    def _find_smallest(self, i: int, j: int) -> int:
        # assert OR(self.nums[i:j+1]) >= k
        if (i, j) in self.dp:
            return self.dp[i, j]

        res = j - i + 1
        for index_to_remove, next_i, next_j in [(i, i + 1, j), (j, i, j - 1)]:
            # remove number from subarray
            num = self.nums[index_to_remove]
            self._add_sub_num_to_bit_count(num, -1)
            if self._bit_count_to_num() >= self.k:
                # subarray or is larger than k, continue shrinking subarray
                res = min(res, self._find_smallest(next_i, next_j))
            # add number back
            self._add_sub_num_to_bit_count(num, 1)

        self.dp[(i, j)] = res
        return res


class SolutionSimple:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        """
        Complexity:
            Time: O(n^2)
            Space: O(n)
        """
        n = len(nums)
        res = n + 1
        # dp[val] = largest index i such that OR(nums[i:j+1]) == val,
        # for current j in iteration
        dp: dict[int, int] = {}
        for j, num in enumerate(nums):
            # OR num with every previous subarray
            dp = {num | sub_arr_or: i for sub_arr_or, i in dp.items()}
            # set/override index for num
            dp[num] = j
            # update res if any subarray with an OR value larger than k
            # and shorter than previous subarrays exists
            smallest_with_j = min(
                ((j - i + 1) for sub_arr_or, i in dp.items() if sub_arr_or >= k),
                default=res,
            )
            res = min(res, smallest_with_j)
        return res if res <= n else -1


class Solution(SolutionSimple):
    pass
