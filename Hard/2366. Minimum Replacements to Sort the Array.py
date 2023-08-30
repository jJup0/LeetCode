import math


class Solution:
    """
    You are given a 0-indexed integer array nums. In one operation you can replace
    any element of the array with any two elements that sum to it.

    - For example, consider nums = [5,6,7]. In one operation, we can replace nums[1]
      with 2 and 4 and convert nums to [5,2,4,7].

    Return the minimum number of operations to make an array that is sorted in
    non-decreasing order.

    Constraints:
    - 1 <= nums.length <= 10^5
    - 1 <= nums[i] <= 10^9
    """

    def minimumReplacement(self, nums: list[int]) -> int:
        """
        Iterate in reverse order and greedily split into largest pieces
        possible when a larger number is encountered.
        O(n) / O(1)     time / space complexity
        """
        # previous array element after any splits
        prev = nums[-1]
        res = 0
        for num in reversed(nums):
            if num > prev:
                # number needs to be split
                divisions_needed = math.ceil((num - prev) / prev)
                res += divisions_needed
                # update prev to be the smallest number of the split
                prev = num // (divisions_needed + 1)
            else:
                # no need to split the current number
                prev = num
        return res
