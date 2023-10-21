"""
Given an integer array nums and an integer k, return the maximum sum of a non-empty
subsequence of that array such that for every two consecutive integers in the
subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can
be zero) from the array, leaving the remaining elements in their original order.

Constraints:
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""
from collections import deque


class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        return self._constrainedSubsetSum_no_queue(nums, k)

    def _constrainedSubsetSum_no_queue(self, nums: list[int], k: int) -> int:
        """
        This was my first implementation which somehow consistently beats 100%,
        I guess test cases are quite random, and include enough positive numbers,
        which this algorithm can take advantage of.

        It works almost identically to constrainedSubsetSum_queue, but only stores
        the largest previously calculated value.

        Worst case for this algorithm is when nums looks like [0, -1, -2, -3, -4, ...] and k ~= len(n) / 2.

        O(n * k) / O(n)     time / space complexity
        """
        dp = [0] * len(nums)
        prev_max = 0
        prev_max_i = -1
        for i, num in enumerate(nums):
            if i - k > prev_max_i:
                prev_max, prev_max_i = max((dp[j], j) for j in range(i - k, i))

            if prev_max >= 0:
                curr = num + prev_max
            else:
                curr = num

            dp[i] = curr
            if curr >= prev_max:
                prev_max = curr
                prev_max_i = i

        return max(dp)

    def _constrainedSubsetSum_queue(self, nums: list[int], k: int) -> int:
        """
        Store previous k results in queue in decreasing total sum.
        O(n) / O(n)     time / space complexity
        """
        # tracks index largest, postive previous results
        # indexes stored are in decreasing order of dp
        prev_largest_queue: deque[int] = deque()

        # dp[i] = maximum constrained subset sum for nums[:i+1] including nums[i] in the sum
        # only reserve space, initial value has no meaning
        dp = [0] * len(nums)
        for i, num in enumerate(nums):
            kick_out_until = i - k
            while prev_largest_queue and kick_out_until > prev_largest_queue[0]:
                prev_largest_queue.popleft()

            prev_largest = dp[prev_largest_queue[0]] if prev_largest_queue else 0

            curr = num + prev_largest
            dp[i] = curr
            if curr > 0:
                while prev_largest_queue and dp[prev_largest_queue[-1]] <= curr:
                    prev_largest_queue.pop()
                prev_largest_queue.append(i)

        return max(dp)
