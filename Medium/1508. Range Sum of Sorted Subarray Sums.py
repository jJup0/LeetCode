"""
You are given the array nums consisting of n positive integers. You computed
the sum of all non-empty continuous subarrays from the array and then sorted
them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

Return the sum of the numbers from index left to index right (indexed from 1),
inclusive, in the new array. Since the answer can be a huge number return it
modulo 10^9 + 7.

Constraints:
- n == nums.length
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 100
- 1 <= left <= right <= n * (n + 1) / 2
"""


class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        """
        Naive implementation.
        O(n^2 * log(n)) / O(n^2)     time / space complexity
        """
        sums: list[int] = []
        for start in range(n):
            curr_sum = 0
            for end in range(start, n):
                curr_sum += nums[end]
                sums.append(curr_sum)
        sums.sort()

        MOD = 10**9 + 7
        res = 0
        for i in range(left - 1, right):
            res = (res + sums[i]) % MOD
        return res


s = Solution()
print(s.rangeSum([1, 2, 3, 4], 4, 1, 10))
