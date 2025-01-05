"""
You are given an array of integers nums.

Your task is to find the length of the longest subsequence seq of nums, such
that the absolute differences between consecutive elements form a
non-increasing sequence of integers. In other words, for a subsequence seq_0,
seq_1, seq_2,..., seq_m of nums,
|seq_1 - seq_0| >= |seq_2 - seq_1| >=... >= |seq_m - seq_m - 1|.

Return the length of such a subsequence.

A subsequence is an non-empty array that can be derived from another array by
deleting some or no elements without changing the order of the remaining elements.

Constraints:
- 2 <= nums.length <= 10^4
- 1 <= nums[i] <= 300
"""


class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        """
        Exploit the fact that 1 <= nums[i] <= 300 (small range)
        Complexity:
            Time: O(max(nums) * n)
            Space: O(max(nums) * n)
        """
        smallest_num = min(nums)
        largest_num = max(nums)
        max_possible_diff = largest_num - smallest_num
        # dp[num][diff] = longest streak possible for maximum difference
        # of `diff` for subsequence starting with `num`
        dp = [[0] * (max_possible_diff + 1) for _ in range(largest_num + 1)]
        for num in reversed(nums):
            streaks_for_num = [0] * (max_possible_diff + 1)
            longest_streak = 1
            for diff in range(max(num - smallest_num, largest_num - num) + 1):
                if num >= diff:
                    longest_streak = max(longest_streak, dp[num - diff][diff] + 1)
                if num + diff <= largest_num:
                    longest_streak = max(longest_streak, dp[num + diff][diff] + 1)
                streaks_for_num[diff] = longest_streak

            # update dp[nums[i]] with maximum of its current values and values in `curr`
            dp[num] = [
                max(prev_streak, now_streak)
                for prev_streak, now_streak in zip(dp[num], streaks_for_num)
            ]
        return max(max(streaks_for_val) for streaks_for_val in dp)
