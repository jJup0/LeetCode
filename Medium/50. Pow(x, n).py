class Solution:
    """
    Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

    Constraints:
    - -100.0 < x < 100.0
    - -2^31 <= n <= 2^31-1
    - n is an integer.
    - Either x is not zero or n > 0.
    - -10^4 <= xn <= 10^4
    """

    def myPow(self, x: float, n: int) -> float:
        """
        Square and multiply algorithm.
        Note that this implementation makes use of the "either x is not zero
        or n > 0" constraint.
        O(log(n)) / O(1)    time / space complexity
        """
        if n < 0:
            exponent_is_negative = True
            # if exponent is negative, use absolute value
            n = -n
        else:
            exponent_is_negative = False

        result = 1
        # square and multply
        current_square = x
        bit_mask = 1
        while bit_mask <= n:
            # if n has bit set at current bitmask bit, then multiply result with current square
            if bit_mask & n:
                result *= current_square
            # move on to next bit
            bit_mask <<= 1
            # square the current square value
            current_square *= current_square

        # if exponent is negative, return inverse of result
        if exponent_is_negative:
            return 1 / result
        return result
