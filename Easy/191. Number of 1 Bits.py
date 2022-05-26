class Solution:
    """
    Write a function that takes an unsigned integer and returns the
    number of '1' bits it has (also known as the Hamming weight).
    Constraints:
        The input must be a binary string of length 32.
    """

    def hammingWeight(self, n: int) -> int:
        # result variable
        count = 0
        # while 1's remaining in number
        while n:
            # increment count if lowest bit set
            count += n & 1
            # right-shift n by 1
            n >>= 1
        return count
