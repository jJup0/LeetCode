class Solution:
    """
    Given an integer num, return the number of steps to reduce it to zero.
    In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
    Constraints:
        0 <= num <= 10^6
    """

    def numberOfSteps(self, num: int) -> int:
        # special case, not a single bit is set, need zero steps to get from 0 to 0
        if not num:
            return 0

        # start with result variable = -1, as res will be incremented one time to often when num == 1
        res = -1
        while num:
            # if lowest bit is set, need to subtract 1 first, and then divide by two (2 steps)
            # otherwise just divide by two
            res += 1 + (num & 1)

            # divide num by two
            num >>= 1
        return res
