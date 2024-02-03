"""
Given an integer array arr, partition the array into (contiguous) subarrays of
length at mostk. After partitioning, each subarray has their values changed to
become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are
generated so that the answer fits in a 32-bit integer.

Constraints:
- 1 <= arr.length <= 500
- 0 <= arr[i] <= 10^9
- 1 <= k <= arr.length
"""

from collections import deque


class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        return self.maxSumAfterPartitioning_fast(arr, k)

    def maxSumAfterPartitioning_fast(self, arr: list[int], k: int) -> int:
        """
        O(n * k) / O(n)     time / space complexity
        """
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(n):
            curr_max = best_partition_sum = 0
            for j in range(i, max(-1, i - k), -1):
                curr_max = max(curr_max, arr[j])
                curr_partition_sum = curr_max * (i - j + 1) + dp[j]
                best_partition_sum = max(best_partition_sum, curr_partition_sum)

            dp[i + 1] = best_partition_sum

        return dp[-1]

    def maxSumAfterPartitioning_queue(self, arr: list[int], k: int) -> int:
        """
        Inefficient use of dp: not use as partial result, but as termination condition
        i.e. do not bfs if result is not best so far.
        O(n * k) / O(n)   time / space complexity
        """
        n = len(arr)
        dp = [-1] * (n + 1)
        queue: deque[tuple[int, int]] = deque([(0, 0)])
        while queue:
            pos, running_sum = queue.popleft()
            if dp[pos] >= running_sum:
                continue
            dp[pos] = running_sum
            if pos == n:
                continue

            max_num = arr[pos]
            for i in range(pos, min(pos + k, n)):
                num = arr[i]
                if num > max_num:
                    max_num = num
                queue.append((i + 1, running_sum + max_num * (i - pos + 1)))
        return dp[-1]
