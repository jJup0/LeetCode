from typing import List


class Solution:
    """
    Given an integer array nums and an integer k, return true if there are two distinct indices
    i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

    Constraints:
        1 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9
        0 <= k <= 10^5
    """

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # last occurance index of a value
        last_seen = {}
        for i, num in enumerate(nums):
            # if the number has previously occured and the difference in indexes is less than k
            # return true
            if num in last_seen and i - last_seen[num] <= k:
                return True
            # else update last seen index of current number
            last_seen[num] = i

        # if no such number is found return false
        return False
