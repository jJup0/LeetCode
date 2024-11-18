"""
Given an integer array nums and an integer k, return the length of the shortest
non-empty subarray of nums with a sum of at least k. If there is no such
subarray, return -1.

A subarray is a contiguous part of an array.

Constraints:
- 1 <= nums.length <= 10^5
- -10^5 <= nums[i] <= 10^5
- 1 <= k <= 10^9
"""

from collections import deque


class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        res = len(nums) + 1
        # current prefix sum
        curr_sum = 0
        # m_deque[i] = (sum(nums[:j+1]), j), montonic increasing prefix sums
        m_deque: deque[tuple[int, int]] = deque()

        for i, num in enumerate(nums):
            curr_sum += num
            if curr_sum >= k:
                res = min(res, i + 1)

            # Make subarrays with previous indexes `end_idx` while the
            # sum is larger or equal to k, as this is the shortest
            # subarray starting with `end_idx` that creates a sum
            # greater/equal k.
            while m_deque and curr_sum - m_deque[0][0] >= k:
                _prefix, end_idx = m_deque.popleft()
                res = min(res, i - end_idx)

            # "validate" the monotonic deque; may happen when num <= 0.
            # Let j = m_deque[-1][1] then `nums[j:i+1] <= 0` so there is
            # no point trying to find a shortest subarray starting at j,
            # as nums[j:i+1] only contributes to the length, but
            # contributes nothing to a larger sum.
            while m_deque and m_deque[-1][0] > curr_sum:
                m_deque.pop()
            m_deque.append((curr_sum, i))

        if res == len(nums) + 1:
            return -1
        return res
