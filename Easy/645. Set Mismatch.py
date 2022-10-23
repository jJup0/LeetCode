from collections import Counter
from typing import List


class Solution:
    """
    You have a set of integers s, which originally contains all the numbers from 1 to n.
    Unfortunately, due to some error, one of the numbers in s got duplicated to another number in
    the set, which results in repetition of one number and loss of another number.

    You are given an integer array nums representing the data status of this set after the error.

    Find the number that occurs twice and the number that is missing and return them in the form of
    an array.

    Constraints:
        2 <= nums.length <= 10^4
        1 <= nums[i] <= 10^4
    """

    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        O(n) / O(n)     time / space complexity
        """

        # result variable
        res = [0, 0]

        counter = Counter(nums)
        # go through all the numbers that should be in nums
        for num in range(1, len(nums) + 1):
            # if the number does not occur once, set entry in the result as appropriate
            count = counter[num]
            if count == 2:
                res[0] = num
            elif count == 0:
                res[1] = num

        return res
