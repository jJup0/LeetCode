"""
Given an array of integers arr, find the sum of min(b), where b ranges over
every (contiguous) subarray of arr. Since the answer may be large, return the
answer modulo10^9 + 7.

Constraints:
- 1 <= arr.length <= 3 * 10^4
- 1 <= arr[i] <= 3 * 10^4
"""


class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        """
        Dynamic programming and monotone stack.
        O(n) / O(n)     time / space complexity
        """
        MOD = 10**9 + 7
        # dp[i] = sum of subarray minimums for all subarrays ending with arr[i]
        dp = [0] * len(arr)
        # stack is contains indexes for arr, whose values are monotone increasing
        stack: list[int] = []

        for i, num in enumerate(arr):
            while stack and num <= arr[stack[-1]]:
                # remove all indexes from the stack which are larger than num
                # these are not important as the do not influence min(arr[j:i])
                stack.pop()
            if stack:
                # arr[j] is last value that is smaller than num
                j = stack[-1]
                # num * (i - j): for subbarrays arr[j+1:i+1] num is the smallest value
                # dp[j]        : for k <= j arr[k:i+1] is the same as sum minimums of subarrays [l:j], l < k
                # and for subarrays between i and j, arr[i] is the smallest,
                dp[i] = dp[j] + num * (i - j)
            else:
                # num is smallest so far
                dp[i] = num * (i + 1)
            stack.append(i)
        return sum(dp) % MOD
