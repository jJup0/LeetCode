"""
Write a function that takes the binary representation of an unsigned integer
and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

- Note that in some languages, such as Java, there is no unsigned integer
  type. In this case, the input will be given as a signed integer type. It
  should not affect your implementation, as the integer's internal binary
  representation is the same, whether it is signed or unsigned.
- In Java, the compiler represents the signed integers using 2's complement
  notation. Therefore, in Example 3, the input represents the signed integer -3.

Constraints:
- The input must be a binary string of length 32.
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        return self.hammingWeight_manual(n)

    def hammingWeight_manual(self, n: int) -> int:
        # result variable
        count = 0
        # while 1's remaining in number
        while n:
            # increment count if lowest bit set
            count += n & 1
            # right-shift n by 1
            n >>= 1
        return count

    def hammingWeight_builtin(self, n: int) -> int:
        return bin(n).count("1")
