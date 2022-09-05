
from collections import deque
from typing import Deque, List


class Solution:
    """
    Return all non-negative integers of length n such that the absolute difference between every
    two consecutive digits is k.
    Note that every number in the answer must not have leading zeros. For example, 01 has one
    leading zero and is invalid.
    You may return the answer in any order.
    Constraints:
        2 <= n <= 9
        0 <= k <= 9
    """

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # special case to avoid using set in lsit comprehension
        if k == 0:
            all_ones = int("1" * n)
            return [all_ones * digit for digit in range(1, 10)]

        # start with all digits
        result = list(range(1, 10))

        for _ in range(n-1):
            # add digits to previous numbers in each iteration, if adding/subtracting k is a valid digit
            result = [x*10 + y
                      for x in result
                      for y in (x % 10 + k, x % 10 - k) if 0 <= y <= 9]
        return result

    def numsSameConsecDiff_first(self, n: int, k: int) -> Deque[int]:
        # if k is 0 then only have to add 0 to last digit when constructing, otherwise add/subtract k
        deltas = (-k, k) if k > 0 else (k, )

        # result variable
        result = deque(range(1, 10))

        # lowest number with n digits
        threshold = 10**(n-1)

        # keep constructing numbers until smallest number already has n digits
        while result[0] < threshold:
            # get number from queue
            num = result.popleft()
            # get last digit of the number
            digit = num % 10
            # add new digit at the end of the number
            for delta in deltas:
                next_digit = digit + delta
                # if next digit is possible, add to queue
                if 0 <= next_digit <= 9:
                    result.append(num*10 + next_digit)

        return result
