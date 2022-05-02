from typing import List


class Solution:
    """
    Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
    Return any array that satisfies this condition.
    """

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: x & 1)
        return nums
