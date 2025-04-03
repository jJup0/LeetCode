"""
You are given an integer array nums of length n and a 2D array queries where
queries[i] = [l_i, r_i, val_i].

Each queries[i] represents the following action on nums:
- Decrement the value at each index in the range [l_i, r_i] in nums by at most
  val_i.
- The amount by which each value is decremented can be chosen independently for
  each index.

A Zero Array is an array with all its elements equal to 0.

Return the minimum possible non-negative value of k, such that after processing
the first k queries in sequence, nums becomes a Zero Array. If no such k
exists, return -1.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 5 * 10^5
- 1 <= queries.length <= 10^5
- queries[i].length == 3
- 0 <= l_i <= r_i < nums.length
- 1 <= val_i <= 5
"""


class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        """
        Binary search for value of k. Apply queries using a delta array.
        Avoid recalculating delta array by only applying queries delta in binary search.

        Complexity:
            Time: O(q + n * log(q))
            Space: O(q)
        """
        min_k = 0
        max_k = len(queries)
        prev_k = 0
        modify_arr = [0] * (len(nums) + 1)
        while min_k < max_k:
            guess_k = (min_k + max_k) // 2
            self.apply_queries(modify_arr, queries, guess_k, prev_k)
            # self.sanity_check_modify(modify_arr, queries, guess_k)
            if self.check_0(nums, modify_arr):
                max_k = guess_k
            else:
                min_k = guess_k + 1
            prev_k = guess_k

        if min_k < len(queries):
            return min_k

        self.apply_queries(modify_arr, queries, len(queries), prev_k)
        if self.check_0(nums, modify_arr):
            return len(queries)

        return -1

    def apply_queries(
        self, modify_arr: list[int], queries: list[list[int]], k: int, prev_k: int
    ):
        """Save time by only undoing or doing difference of queries."""
        if k > prev_k:
            modify = 1
        else:
            modify = -1
            prev_k -= 1
            k -= 1
        for i in range(prev_k, k, modify):
            l, r, val = queries[i]
            modify_arr[l] += val * modify
            modify_arr[r + 1] -= val * modify

    def check_0(self, nums: list[int], modify_arr: list[int]):
        current_diff = 0
        for num, mod in zip(nums, modify_arr):
            current_diff += mod
            if current_diff < num:
                return False
        return True

    def _sanity_check_modify(
        self, modify_arr: list[int], queries: list[list[int]], guess_k: int
    ):
        """Check if the time saving modify array is correct."""
        real_mod = [0] * len(modify_arr)
        for l, r, val in queries[:guess_k]:
            real_mod[l] += val
            real_mod[r + 1] -= val
        assert real_mod == modify_arr
