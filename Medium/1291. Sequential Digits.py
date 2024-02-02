"""
An integer has sequential digits if and only if each digit in the number is one
more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive
that have sequential digits.

Constraints:
- 10 <= low <= high <= 10^9
"""


class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        return self.sequentialDigits_simple(low, high)

    def sequentialDigits_simple(self, low: int, high: int) -> list[int]:
        """
        Brute force approach, but still technically O(1) time complexity since base 10.
        b := base of the number system, in our case 10
        O(b^2) / O(b^2)     time / space complexity
        """
        BASE = 10
        digits = "".join(str(i) for i in range(1, BASE))
        res: list[int] = []
        for i in range(BASE - 1):
            for j in range(i + 1, BASE):
                number = int(digits[i:j])
                if low <= number <= high:
                    res.append(number)

        return sorted(res)

    def sequentialDigits_mathy(self, low: int, high: int) -> list[int]:
        """
        Mathmatical approach, somewhat complex.
        """
        res: list[int] = []
        digits = 123456789
        ones = 111111111

        # amount of digits low has
        len_num = len(str(low))
        # amount of possible numbers with len_num digits
        rounds = 10 - len_num
        # amount of digits to chuck off of digits and ones to generate sequential digit numbers
        divf = 10 ** (rounds - 1)

        while divf:  # can reach 0, then finished
            # number to add to get next strictly increasing number
            curr_ones = ones // divf
            # lowest number with 10-rounds strictly increasing digits
            curr = digits // divf
            for _ in range(rounds):
                if curr > high:
                    return res
                if curr >= low:
                    # in first round, possible the generated number is less than low
                    res.append(curr)

                curr += curr_ones

            divf //= 10  # generate next order numbers
            rounds -= 1  # this takes one round less

        return res
