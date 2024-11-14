"""
Given a 0-indexed integer array nums of size n and two integers lower and
upper, return the number of fair pairs.

A pair (i, j) is fair if:
- 0 <= i < j < n, and
- lower <= nums[i] + nums[j] <= upper

Constraints:
- 1 <= nums.length <= 10^5
- nums.length == n
- -10^9 <= nums[i] <= 10^9
- -10^9 <= lower <= upper <= 10^9
"""

from sortedcontainers.sortedlist import SortedList


class OriginalSolution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        """
        Question phrasing made it seem like order matters but it really does not.
        Time complexity is optimal (apart from radix-sort) but overhead is large.
        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        prev_nums = SortedList()
        res = 0
        for num in nums:
            too_small = prev_nums.bisect_left(lower - num)
            too_large = prev_nums.bisect_right(upper - num)
            res += too_large - too_small
            prev_nums.add(num)
        return res


class Solution2:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        """
        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        nums.sort()
        return self.lower_bound(nums, upper + 1) - self.lower_bound(nums, lower)

    def lower_bound(self, nums: list[int], value: int) -> int:
        # Calculate the number of pairs with sum less than `value`.
        # O(n) time complexity
        left = 0
        right = len(nums) - 1
        result = 0
        while left < right:
            sum = nums[left] + nums[right]
            # If sum is less than value, add the size of window to result and move to the
            # next index.
            if sum < value:
                result += right - left
                left += 1
            else:
                # Otherwise, shift the right pointer backwards, until we get a valid window.
                right -= 1
        return result
