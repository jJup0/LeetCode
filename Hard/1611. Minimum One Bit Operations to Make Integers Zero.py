"""
Given an integer n, you must transform it into 0 using the following operations
any number of times:
- Change the rightmost (0th) bit in the binary representation of n.
- Change the ith bit in the binary representation of n if the (i-1)th
  bit is set to 1 and the (i-2)th through 0th bits are set to 0.
- Return the minimum number of operations to transform n into 0.

Constraints:
- 0 <= n <= 10^9
"""


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        """
        O(log(n)) / O(log(n))   time / space complexity
        """
        # base case, 0 needs zero operations, 1 needs one opertion
        if n <= 1:
            return n

        # get the value of the highest set bit
        value_highest_bit = 1
        while value_highest_bit <= n:
            value_highest_bit <<= 1
        value_highest_bit >>= 1

        # for a number x which is a power of two, say x = 2^m,
        # we need 2^(m+1) - 1 operations to make it 0.
        # this is because we need 2^m operations to clear bit `m`,
        # after which bit `m-1` is set, so we need 2^(m-1) operations
        # to clear it, and so on.
        # so e.g. for 0b1000 we need 0b1111 operations to set it to 0 which is 2^(3+1) - 1 operations
        operations_needed_for_highest_bit = (value_highest_bit << 1) - 1

        # note that the amount of operations to set a number n to 0
        # is the same amount as getting 0 to n
        # when trying to get a number with other bits also set, we have to
        # subtract the amount of operations needed to get to that number
        # (n-value_highest_bit) from our result

        # e.g.                      we have 0b10000
        # we need 2^5-1 = 31 operations to make it 0
        # if instead we have                0b10011
        #               ... to clear this bit ^  ^^
        # we can use the progress of these bits  ||
        # and subtract the operations needed to get to 0b11 from our result
        operations_skipped = self.minimumOneBitOperations(n - value_highest_bit)
        return operations_needed_for_highest_bit - operations_skipped
