from typing import List


class Solution:
    """
    Given an integer array nums of size n, return the minimum number of moves
    required to make all array elements equal.
    In one move, you can increment or decrement an element of the array by 1.
    Test cases are designed so that the answer will fit in a 32-bit integer.
    Constraints:
        n == nums.length
        1 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9
    """

    def minMoves2(self, nums: List[int]) -> int:
        """
        To get minimum moves, sort nums. The target value to increase/decrease to must
        be in between nums[0] and nums[-1]. It must then also be between nums[1] and
        nums[-2]. Keep going unti nums[n//2] which is the median. In case of even n,
        target can be any number in interval [nums[n//2] - 1, nums[n//2]]
        """

        # sort nums to find median easier
        nums.sort()

        median = nums[len(nums)//2]

        # sum distance from each num to median
        return sum(abs(median - num) for num in nums)
