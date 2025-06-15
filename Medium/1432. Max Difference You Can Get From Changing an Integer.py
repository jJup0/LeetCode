"""
You are given an integer num. You will apply the following steps to num two
separate times:
- Pick a digit x (0 <= x <= 9).
- Pick another digit y (0 <= y <= 9). Note y can be equal to x.
- Replace all the occurrences of x in the decimal representation of num by y.

Let a and b be the two results from applying the operation to num independently.

Return the max difference between a and b.

Note that neither a nor b may have any leading zeros, and must not be 0.

Constraints:
- 1 <= num <= 10^8
"""


class Solution:
    def maxDiff(self, num: int) -> int:
        str_num = str(num)
        max_num = self._replace_digits(str_num, "9", "9")
        min_num = self._replace_digits(str_num, "1", "0")
        return max_num - min_num

    def _replace_digits(
        self, str_num: str, replacement_first_only: str, standard_replacement: str
    ) -> int:
        for i, digit in enumerate(str_num):
            replacement = replacement_first_only if i == 0 else standard_replacement
            if digit == replacement:
                continue
            if str_num[0] == digit and replacement == "0":
                # do not cause leading 0
                assert str_num[0] == "1"
                continue
            str_num = str_num.replace(digit, replacement)
            break
        return int(str_num)


def test():
    sol = Solution()
    res = sol.maxDiff(123456)
    assert res == 820000, res


test()
