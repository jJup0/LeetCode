"""
The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the
largest pair sum in a list of pairs.
- For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair
  sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.

Given an array nums of even length n, pair up the elements of nums into
n / 2 pairs such that:
- Each element of nums is in exactly one pair, and
- The maximum pair sum is minimized.

Return the minimized maximum pair sum after optimally pairing up the elements.

Constraints:
- n == nums.length
- 2 <= n <= 10^5
- n is even.
- 1 <= nums[i] <= 10^5
"""


class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        l = len(nums) - 1
        return max(nums[i] + nums[l - i] for i in range((l + 1) // 2))
