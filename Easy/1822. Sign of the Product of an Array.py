class Solution:
    """
    There is a function signFunc(x) that returns:
        1 if x is positive.
        -1 if x is negative.
        0 if x is equal to 0.

    You are given an integer array nums. Let product be the product of all
    values in the array nums.

    Return signFunc(product).

    Constraints:
        1 <= nums.length <= 1000
        -100 <= nums[i] <= 100
    """

    def arraySign(self, nums: list[int]) -> int:
        negative = False
        for num in nums:
            if num < 0:
                negative = not negative
            elif num == 0:
                return 0
        return -1 if negative else 1
