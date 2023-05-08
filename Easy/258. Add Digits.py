class Solution:
    """
    Given an integer num, repeatedly add all its digits until the
    result has only one digit, and return it.

    Constraints:
        0 <= num <= 2^31 - 1
    """

    def addDigits(self, num: int) -> int:
        res = 0
        for digit in [int(c) for c in str(num)]:
            res += digit
            if res >= 10:
                res = res % 10 + 1
        return res

    def addDigitsMath(self, num: int) -> int:
        if num == 0:
            return 0

        rem = num % 9
        if rem == 0:
            return 9
        return rem
