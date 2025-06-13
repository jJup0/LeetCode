"""
You are given a 0-indexed integer array nums and an integer p. Find p pairs of
indices of nums such that the maximum difference amongst all the pairs is
minimized. Also, ensure no index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j, the difference of this
pair is |nums[i] - nums[j]|, where |x| represents the absolutevalue of x.

Return the minimummaximum difference among all p pairs. We define the maximum
of an empty set to be zero.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
- 0 <= p <= (nums.length)/2
"""


class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        """
        Binary search + greedy pairs strategy.
        Complexity:
            Time: O(n * log(n))
            Space: O(1)
        """
        if p == 0:
            return 0

        # sort nums to be able to pair up greedily.
        nums.sort()

        # lower and upper bound for maximum allowed difference between pairs
        lo = 0
        hi = nums[-1] - nums[0]

        # binary search
        while lo < hi:
            mid = (lo + hi) >> 1
            if self._can_form_pairs(nums, p, mid):
                # p pairs can be formed, result could be mid
                hi = mid
            else:
                # p pairs can not be formed, result needs to be greater than mid
                lo = mid + 1

        return lo

    def _can_form_pairs(self, nums: list[int], p: int, max_diff: int):
        """
        Checks greedily if neighboring numbers in nums can be paired up to
        have a difference of at most max_diff.
        O(n) / O(1)     time / space complexity
        """
        pair_count = 0
        i = 0
        while i < len(nums) - 1:
            if nums[i + 1] - nums[i] <= max_diff:
                # current num and next highest num can pair up
                pair_count += 1
                if pair_count >= p:
                    return True
                # skip next highest num, since already paired up
                i += 2
            else:
                # current num cannot be paired up, go to next
                i += 1
        return False
