"""
You are given an integer array nums where the ith bag contains nums[i] balls.
You are also given an integer maxOperations.

You can perform the following operation at most maxOperations times:
- Take any bag of balls and divide it into two new bags with a positive number
  of balls.
  - For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or
    two new bags of 2 and 3 balls.

Your penalty is the maximum number of balls in a bag. You want to minimize your
penalty after the operations.

Return the minimum possible penalty after performing the operations.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= maxOperations, nums[i] <= 10^9
"""


class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        """
        Binary search for a number that we can split all numbers to.
        Complexity:
            Time: O(n * log(n))
            Space: O(1)
        """
        lo = 1
        hi = max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if self._can_split(nums, mid, maxOperations):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def _can_split(self, nums: list[int], target: int, maxOperations: int):
        ops = 0
        for num in nums:
            ops += (num - 1) // target
            if ops > maxOperations:
                break
        return ops <= maxOperations
