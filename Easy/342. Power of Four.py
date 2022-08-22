class Solution:
    """
    Given an integer n, return true if it is a power of four. Otherwise, return false.
    An integer n is a power of four, if there exists an integer x such that n == 4^x.
    Constraints:
        -2^31 <= n <= 2^31 - 1
    """

    def isPowerOfFour(self, num: int) -> bool:
        num_bin = bin(num)[2:]
        # numbers that are a power of four only have the highest bit set, and an even number of zeros
        # for negative numbers will num_bin[0] = 'b', so rfind('1') never returns 0
        return num_bin.rfind('1') == 0 and len(num_bin) % 2 == 1
