"""
There are several consecutive houses along a street, each of which has some
money inside. There is also a robber, who wants to steal money from the homes,
but he refuses to steal from adjacent homes.

The capability of the robber is the maximum amount of money he steals from one
house of all the houses he robbed.

You are given an integer array nums representing how much money is stashed in
each house. More formally, the ith house from the left has nums[i] dollars.

You are also given an integer k, representing the minimum number of houses the
robber will steal from. It is always possible to steal at least k houses.

Return the minimum capability of the robber out of all the possible ways to
steal at least k houses.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= (nums.length + 1)/2
"""


class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        """Binary search for minimum capacity.

        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        nums_sorted = sorted(nums)
        l = 0
        r = len(nums)
        while l < r:
            mid = (l + r) // 2
            capacity = nums_sorted[mid]
            if self._can_steal_capacity(nums, capacity, k):
                r = mid
            else:
                l = mid + 1
        return nums_sorted[l]

    def _can_steal_capacity(self, nums: list[int], capacity: int, k: int):
        steals = 0
        stole_prev = False
        for num in nums:
            if num > capacity or stole_prev:
                stole_prev = False
                continue

            steals += 1
            stole_prev = True
            if steals == k:
                return True
        return False
