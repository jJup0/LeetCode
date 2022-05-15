from typing import List


class Solution:
    """
    An n-bit gray code sequence is a sequence of 2n integers where:
        Every integer is in the inclusive range [0, 2n - 1],
        The first integer is 0,
        An integer appears no more than once in the sequence,
        The binary representation of every pair of adjacent integers differs by exactly one bit, and
        The binary representation of the first and last integers differs by exactly one bit.
    Given an integer n, return any valid n-bit gray code sequence.
    Constraints:
        1 <= n <= 16
    """

    def grayCode(self, n: int) -> List[int]:
        # start of with a base return list
        # virually prepend a '0' to all the values in res so far, maintaining invariant of start with 0 and
        # only changing 1 bit per number, then take the reverse of that list and prepend a '1' and add it to
        # the list, this way the last value in res so far will be one bit off the new part, and list that is
        # extended by also follows the 1 bit change rule and ends with 2**n, which has a leading one and
        # the res '0's, following the rule of the last number differing by one bit
        res = [0, 1]
        for i in range(n-1):
            add = 2 << i
            res.extend(num + add for num in reversed(res))
        return res
