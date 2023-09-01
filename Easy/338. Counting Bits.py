class Solution:
    """
    Given an integer n, return an array ans of length n + 1 such that for each i
    (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

    Constraints:
    - 0 <= n <= 10^5

    Follow up:
    - It is very easy to come up with a solution with a runtime of O(n log n).
      Can you do it in linear time O(n) and possibly in a single pass?
    - Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
    """

    def countBits(self, num: int) -> list[int]:
        return self.countBits2(num)

    def countBits1(self, num: int) -> list[int]:
        """
        O(n) / O(1)     time / space complexity
        """
        # base case, 0 has 0 1's
        result = [0]
        final_len = num + 1
        # build result until length reached
        while len(result) < final_len:
            # invariant: length of result is a power of two: result contains
            # the bit counts for numbers up to 2**x

            # calculate remaining bit counts needed for result
            remaining = min(len(result), final_len - len(result))

            # the bit counts of numbers from (2**x)+1 to 2**(x+1) are identical
            # to the bit counts of numbers from 0 to 2**x, except they have one
            # extra 1 as the highest set bit
            result.extend(1 + result[i] for i in range(remaining))

        return result

    def countBits2(self, n: int) -> list[int]:
        """
        O(n) / O(1)     time / space complexity
        """
        res = [0]
        for i in range(1, n + 1):
            # even numbers are have the same bit count as the number half their
            # value, as they are simply lefted (extra 0 in the units digit)
            # odd numbers are the same as left shifting, but adding a 1 in the units digit
            res.append(res[i >> 1] + (i & 1))
        return res
