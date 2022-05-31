class Solution:
    """
    Given two integers dividend and divisor, divide two integers without using multiplication,
    division, and mod operator. The integer division should truncate toward zero, which means
    losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would
    be truncated to -2.
    Return the quotient after dividing dividend by divisor.
    Note: Assume we are dealing with an environment that could only store integers within the
    32-bit signed integer range: [-2^31, 2^31 - 1]. For this problem, if the quotient is strictly
    greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly less than -2^31,
    then return -2^31.
    Constraints:
        -231 <= dividend, divisor <= 231 - 1
        divisor != 0
    """

    def divide(self, dividend: int, divisor: int) -> int:
        # make both numbers positive, and note if result is positive or negative
        negative = False
        if dividend < 0:
            dividend = -dividend
            negative = True
        if divisor < 0:
            divisor = -divisor
            negative = not negative

        # left shift divisor while it is smaller than dividend
        lshifts = 0
        while dividend >= divisor:
            lshifts += 1
            divisor <<= 1

        # result variable
        res = 0
        # go through possible 2^n multiples of divisor, checking if the fit into the remaining divisor
        mutliple = 1 << lshifts
        while mutliple:
            # if divisor is bigger, substract it from dividend, and add current multiple to result
            if dividend >= divisor:
                dividend -= divisor
                res += mutliple
            # right shift both multiple and divisor
            mutliple >>= 1
            divisor >>= 1

        # if result should be negative, negate it
        if negative:
            res = -res

        # res can not be smaller than INT_MIN
        # result only greater than INT_MAX when division is: INT_MIN / -1
        return min(res, (1 << 31) - 1)
