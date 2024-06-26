"""
Given an integer array nums and an integer k, return true if nums has a good
subarray or false otherwise.

A good subarray is a subarray where:
- its length is at least two, and
- the sum of the elements of the subarray is a multiple of k.

Note that:
- A subarray is a contiguous part of the array.
- An integer x is a multiple of k if there exists an integer n such that
  x = n * k. 0 is always a multiple of k.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
- 0 <= sum(nums[i]) <= 2^31 - 1
- 1 <= k <= 2^31 - 1
"""


class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        """
        Calculate running sums of nums modulo k, if there is a duplicate running sum at
        index i and j, then the subarray with a summing to a multiple of k will be
        nums[i+1:j+1].
        O(n) / O(n)     time / space complexity
        """
        # set first seen of running sum 0 to 0, since if the running sum ever comes to zero after
        # the first index, then sum(nums[:i+1]) is a multiple of k
        first_seen = {0: 0}

        # running sum of nums[:i+1] modulo k
        running_sum = 0
        for i, num in enumerate(nums):
            running_sum = (num + running_sum) % k

            if running_sum not in first_seen:
                # if current running sum has never been seen before, update first seen to
                # NEXT index, to avoid wrong truthy return value in case next value is a
                # multiple of k
                first_seen[running_sum] = i + 1

            elif first_seen[running_sum] < i:
                # else if the running sum has been encountered, and it was not at the
                # previous index (can only happen if num%k == 0) return True
                return True

        # no duplicate running sum found, return false
        return False


s = Solution()
s.checkSubarraySum([23, 2, 4, 6, 7], 6)
