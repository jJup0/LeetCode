"""
Given an integer array nums and an integer k, find three non-overlapping
subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of
each interval (0-indexed). If there are multiple answers, return the
lexicographically smallest one.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- 1 <= nums[i] < 2^16
- 1 <= k <= floor(nums.length / 3)
"""


class Solution:
    SUBARRAY_COUNT = 3

    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        self.k = k
        self.nums = nums
        self.k_sums = self._get_k_rolling_sums(nums, k)

        best_for = [[(k_sum, -1) for k_sum in self.k_sums]]
        for i in range(1, self.SUBARRAY_COUNT):
            best_for.append(self._get_next_k_sub_dp(i, best_for[-1]))

        return self._backtrack_result(best_for)

    def _get_k_rolling_sums(self, nums: list[int], k: int) -> list[int]:
        curr_k_rolling = sum(nums[:k])
        k_sums: list[int] = [curr_k_rolling]
        for i in range(1, len(nums) - k + 1):
            curr_k_rolling += nums[i + k - 1] - nums[i - 1]
            k_sums.append(curr_k_rolling)
        return k_sums

    def _get_next_k_sub_dp(
        self, iteration_nr: int, prev_dp: list[tuple[int, int]]
    ) -> list[tuple[int, int]]:
        """
        Returns a list `next_best_for` where `next_best_for[i]` = (best_total_score, previous_idx)
        where best_total_score the is the best score possible using the
        subarray nums[i:i+k] as the `iteration_nr`th subarray (0-indexed),
        for which `previous_idx` was used as the `iteration_nr-1`th subarray.

        If `i` is too small to be used as the start of the `iteration_nr`th
        subarray, `next_best_for[i]` = [-1, -1].
        If `i` is too large to be used as the start of the `iteration_nr`th
        subarray, is is not included in `next_best_for` i.e. `len(next_best_for)` =
        `len(self.nums) - (self.SUBARRAY_COUNT - iteration_nr) * self.k + 1`

        Args:
            iteration_nr (int): Iteration index.
            prev_dp (list[tuple[int, int]]): Result of the previous iteration.

        Returns:
            list[tuple[int, int]]: ...

        Complexity:
            Time: O(n)
            Spacce: O(n)
        """
        next_best_for: list[tuple[int, int]] = [(-1, -1)] * iteration_nr * self.k
        best_for_one = 0
        best_for_one_idx = 0
        for i in range(
            iteration_nr * self.k,
            len(self.nums) - (self.SUBARRAY_COUNT - iteration_nr) * self.k + 1,
        ):
            prev_idx = i - self.k
            if prev_dp[prev_idx][0] > best_for_one:
                best_for_one = prev_dp[prev_idx][0]
                best_for_one_idx = prev_idx
            next_best_for.append((self.k_sums[i] + best_for_one, best_for_one_idx))
        return next_best_for

    def _backtrack_result(self, best_for: list[list[tuple[int, int]]]) -> list[int]:
        """Using the best_for dynamic programming array, construct the result by backtracking."""
        res_reverse: list[int] = []
        best_score = 0
        best_i3 = 0
        for i3, (score, _i2) in enumerate(best_for[-1]):
            if score > best_score:
                best_score = score
                best_i3 = i3
        res_reverse.append(best_i3)
        for i in range(self.SUBARRAY_COUNT - 1, 0, -1):
            next_i = best_for[i][res_reverse[-1]][1]
            res_reverse.append(next_i)
        return res_reverse[::-1]
