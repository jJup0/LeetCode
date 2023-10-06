class Solution:
    """
    Given an integer n, break it into the sum of k positive integers, where k >= 2,
    and maximize the product of those integers.

    Return the maximum product you can get.

    Constraints:
    - 2 <= n <= 58
    """

    def integerBreak(self, n: int) -> int:
        """3 is the most effective summand to use to maximize product, only when
        there would be a remainder of 1 would it be better to use 2*2 instead of 1*3.
        Note breaking down into 4 is equivalent to two 2's.
        Some examples:
        5 < 2*3
        6 < 2*2*2 < 3*3
        7 < 2*2*2*1 < 3*2*2
        8 < 4*4 == 2*2*2*2 < 3*3*2
        O(log(n)) / O(1)     time / space complexity
        """
        # n <= 3 is a special case, as n cannot be
        # broken down into factors of 2 and three
        if n <= 3:
            return n - 1

        threes, mod = divmod(n, 3)
        if mod == 0:
            # n divisible by 3, use all threes
            return 3**threes
        if mod == 1:
            # remainder of 1, use 4 or 2*2
            return 3 ** (threes - 1) * 4
        # remainder of 2, use 2
        return 3 ** (threes) * 2
