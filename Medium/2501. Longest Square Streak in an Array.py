"""
You are given an integer array nums. A subsequence of nums is called a square
streak if:
- The length of the subsequence is at least 2, and
- after sorting the subsequence, each element (except the first element) is the
  square of the previous number.

Return the length of the longest square streak in nums, or return -1 if there
is no square streak.

A subsequence is an array that can be derived from another array by deleting
some or no elements without changing the order of the remaining elements.

Constraints:
- 2 <= nums.length <= 10^5
- 2 <= nums[i] <= 10^5
"""


class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        """
        Linear is also possible, but sorting is a much simpler solution.
        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        nums.sort(reverse=True)
        streaks: dict[int, int] = {}
        for num in nums:
            prev_streak = streaks.get(num * num, 0)
            streaks[num] = prev_streak + 1
        res = max(streaks.values())
        if res == 1:
            return -1
        return res
