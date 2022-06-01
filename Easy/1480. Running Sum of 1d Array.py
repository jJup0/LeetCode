from typing import List


class Solution:
    """
    Given an array nums. We define a running sum of an array as
    runningSum[i] = sum(nums[0]…nums[i]).
    Return the running sum of nums.
    Constraints:
        1 <= nums.length <= 1000
        -10^6 <= nums[i] <= 10^6
    """

    def runningSum(self, nums: List[int]) -> List[int]:
        rsum = 0
        for i, num in enumerate(nums):
            rsum += num
            nums[i] = rsum
        return nums
